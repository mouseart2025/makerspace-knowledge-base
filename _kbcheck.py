#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
知识库自检工具（合并原 _linkcheck.py + _check_links.py，并扩展为「守门」检查）

用法：
    python3 _kbcheck.py              # 人读报告（默认）
    python3 _kbcheck.py --stats-md   # 输出可直接粘进治理文档的 markdown 统计片段
    python3 _kbcheck.py --json       # 机器可读结果
    python3 _kbcheck.py --quiet      # 只在有问题时输出
    python3 _kbcheck.py --review-due # 按 §6.3 复核清单 + git 历史，列出到期该复核的文档

退出码：0 = 全部通过；1 = 有 WARN（登记/孤岛/粒度）；2 = 有 ERROR（断链/缺 frontmatter/表格列数）

十类检查：
  [E] 0 编码            —— .md 无法按 UTF-8 解码（GBK / UTF-16 / 误存二进制）；跳过内容并报错，不崩溃
  [E] 1 断链            —— 内部链接指向不存在的文件
  [W] 2 库外引用        —— 链接指向知识库之外（开源后对方点不开）
  [I] 2b 目录链接       —— 链接指向库内目录（可渲染，但 AI 检索不友好，建议指向具体文档）
  [W] 3 孤岛文档        —— 没有任何其他文档链向它
  [W] 4 README 未登记   —— 文件名未出现在 README.md（含结构导航树）
  [W] 5 GLOSSARY 未登记 —— 未被 GLOSSARY检索索引.md 以链接形式收录
  [E] 6 frontmatter     —— 缺失，或必备字段不全；type / scope 取值必须落在受控词表内（TYPE_VOCAB / SCOPE_VOCAB）
  [I] 7 date 粒度       —— date 只写到月（无法做时效排序，不阻塞）
  [E] 8 脱敏            —— 命中本地词表 _local_secrets.txt（真实委托方名/本地路径等），公开前必须清
                            覆盖面 = 「会被发布的文件集」中的**全部文本载体**（不止 .md/.py），
                            按扩展名黑名单排除二进制；--stats-md 输出实际扫描文件数以便复核（A-15）
  [E] 9 表格列数        —— markdown 表格「表头列数 = 分隔行列数 = 每个数据行列数」不成立（渲染即错位）
另附：README 结构导航树排版检查（一行挤了两个 .md 条目）+ 全库统计。

第 9 类实现要点（两条都是踩过坑的）：
  · 单元格内的转义竖线 `\|` 不算列分隔符，否则会把正确表格误报为超列；
  · 代码围栏（``` / ~~~）内的行一律跳过，否则示例代码里的竖线会被当成表格。
选附：--review-due 复核到期检查——时效敏感清单直接从治理文档 §6.3 的表格解析（不硬编码，
      清单改了脚本自动跟随），文档年龄取自 git 最后一次提交日，无 git 时优雅跳过。

设计约束：BASE 由 __file__ 推导，脚本内不含任何本地绝对路径，可安全提交到公开仓库。
"""
import os
import re
import sys
import json
import datetime
import collections
import subprocess

BASE = os.path.dirname(os.path.abspath(__file__))
README = "README.md"
GLOSSARY = "06-资源索引/GLOSSARY检索索引.md"
# 豁免集：README 是导航根，自身不需要被登记/被链接
README_EXEMPT = {README}
# GLOSSARY 需要被 README 登记（否则它就是孤岛），但它自己不收录导航根
GLOSSARY_EXEMPT = {README, GLOSSARY}
REQUIRED_FIELDS = ["title", "type", "scope", "source", "date", "tags"]
# type 的受控词表（与 CONTRIBUTING.md §2.1 保持一致）。
# 教训：此前规范只写 7 类、脚本只验证「字段存在」，实际长出 13 类且无人察觉 —— 规范形同虚设。
TYPE_VOCAB = ["入口", "治理", "方法论", "规范", "方案", "案例", "资源", "索引", "专题补充"]
SCOPE_VOCAB = ["通用", "本项目专项"]
LONG_DOC_THRESHOLD = 30000  # 字，超过则提示考虑拆分
GOVERNANCE = "00-知识库治理/知识库覆盖度分析与补充路线图.md"
REVIEW_MONTHS_SENSITIVE = 6   # §6.3：时效敏感内容每 6 个月核验
REVIEW_MONTHS_NORMAL = 24     # 方法论/理念类无强时效，2 年提示一次
# 本地脱敏词表：含真实委托方名称，必须被 .gitignore 排除。
# 本脚本自身不写死任何敏感词，因此可安全提交到公开仓库。
SECRETS_FILE = "_local_secrets.txt"
# 第 8 类脱敏扫描的覆盖面：**默认为全部可发布文本载体**，只按扩展名黑名单排除二进制。
# 教训 A-15：此处曾写死为 (".md", ".py")，与《公开前安全核查与历史遗留对象处置规程》§三 1a
# 声称的「会被发布的文件集」口径不符 —— NOTICE / CITATION.cff / LICENSE 这类根级合规文件
# 恰恰是最容易被人手改、又最需要脱敏复核的载体，却被整类漏扫。
SECRETS_BINARY_EXT = (
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp", ".ico", ".tif", ".tiff",
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".key", ".pages", ".numbers",
    ".zip", ".rar", ".7z", ".gz", ".tar", ".bundle",
    ".dwg", ".dxf", ".skp", ".stl", ".obj", ".3dm", ".step", ".stp",
    ".mp3", ".mp4", ".mov", ".avi", ".wav",
    ".ttf", ".otf", ".woff", ".woff2", ".eot",
    ".ai", ".psd", ".sketch", ".fig",
)
SECRETS_MAX_BYTES = 2 * 1024 * 1024   # 单文件解码上限（正常文档远小于此），超过则跳过

LINK_RE = re.compile(r'\]\((?!http|#|mailto:)([^)#\s]+)(#[^)]*)?\)')


def rel(p):
    return os.path.relpath(p, BASE).replace(os.sep, "/")


def all_md():
    out = []
    for root, dirs, files in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in (".git", "存档")]
        for f in sorted(files):
            if f.endswith(".md"):
                out.append(os.path.join(root, f))
    return sorted(out)


def load_secret_words():
    """读取本地脱敏词表；文件不存在则返回空列表（开源使用者没有该文件，检查自动跳过）。"""
    path = os.path.join(BASE, SECRETS_FILE)
    if not os.path.isfile(path):
        return []
    words = []
    for line in read(path).split("\n"):
        line = line.strip()
        if line and not line.startswith("#"):
            words.append(line)
    return words


def publishable_files():
    """git 真正会发布的文件集 = 已跟踪 ∪ 未跟踪但未被 ignore。
    没有 git 时退化为「全量减去 .gitignore 里按文件名列出的条目」。"""
    try:
        out = set()
        for cmd in (["git", "ls-files"], ["git", "ls-files", "--others", "--exclude-standard"]):
            r = subprocess.run(cmd, cwd=BASE, capture_output=True, text=True, timeout=30)
            if r.returncode == 0:
                out |= {l for l in r.stdout.split("\n") if l}
        if out:
            return out
    except Exception:
        pass
    ignored = set()
    gi = os.path.join(BASE, ".gitignore")
    if os.path.isfile(gi):
        for line in read(gi).split("\n"):
            line = line.strip()
            if line and not line.startswith("#") and "/" not in line and "*" not in line:
                ignored.add(line)
    out = set()
    for root, dirs, names in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in (".git", "存档")]
        for n in names:
            r = os.path.relpath(os.path.join(root, n), BASE).replace(os.sep, "/")
            if n not in ignored:
                out.add(r)
    return out


# 单元格内的转义竖线（\|）不是列分隔符
CELL_SPLIT_RE = re.compile(r"(?<!\\)\|")   # 未转义的竖线才是列分隔符
FENCE_RE = re.compile(r"^\s*(```|~~~)")


def table_ncols(line):
    """按未转义竖线切分，返回该行的列数；首尾空段（行以 | 开头/结尾）不计。"""
    parts = CELL_SPLIT_RE.split(line.strip())
    if parts and parts[0].strip() == "":
        parts = parts[1:]
    if parts and parts[-1].strip() == "":
        parts = parts[:-1]
    return len(parts)


def scan_tables(text):
    """扫全文 markdown 表格，返回 (表格块数, [(起始行, 结束行, {列数: 行数})])。

    跳过代码围栏内的行；只统计「以 | 开头且至少 2 列」的连续行块，块内少于 2 行的不算表格。
    """
    def close(cur, blocks, bad):
        if len(cur) > 1:
            blocks += 1
            cnt = collections.Counter(n for _, n in cur)
            if len(cnt) > 1:
                bad.append((cur[0][0], cur[-1][0], dict(sorted(cnt.items()))))
        return blocks, []

    blocks, bad, cur = 0, [], []
    in_code = False
    for i, line in enumerate(text.split("\n"), 1):
        if FENCE_RE.match(line):
            in_code = not in_code
            blocks, cur = close(cur, blocks, bad)
            continue
        st = line.strip()
        if not in_code and st.startswith("|") and table_ncols(st) >= 2:
            cur.append((i, table_ncols(st)))
        else:
            blocks, cur = close(cur, blocks, bad)
    close(cur, blocks, bad)
    return blocks, bad


def scan_secrets(words):
    """扫描「会被发布的文件集」中的脱敏词。

    返回 (hits, scanned)：
      hits    = [(相对路径, 词表序号, 首个命中行号)]
      scanned = 实际成功解码并扫描的文件数 —— 覆盖面必须可复核（A-13 纪律），
                否则「0 命中」无法区分「真的干净」与「根本没扫到」。

    覆盖面口径：已跟踪 ∪ 未跟踪未忽略（见 publishable_files），排除二进制扩展名、
    超过 SECRETS_MAX_BYTES 的载体、词表自身；无法按 UTF-8 解码者自然跳过。
    只报词表序号而不报词本身，避免诊断输出被转贴时二次泄漏。"""
    hits = []
    scanned = 0
    for r in sorted(publishable_files()):
        if os.path.basename(r) == SECRETS_FILE:
            continue
        if os.path.splitext(r)[1].lower() in SECRETS_BINARY_EXT:
            continue
        fp = os.path.join(BASE, r)
        if not os.path.isfile(fp):
            continue
        try:
            if os.path.getsize(fp) > SECRETS_MAX_BYTES:
                continue
            txt = read(fp)
        except Exception:
            # 非法 UTF-8 / 二进制伪装成文本扩展名：不承载可检索文本，跳过
            continue
        scanned += 1
        for i, w in enumerate(words, 1):
            if w and w in txt:
                ln = next((k for k, l in enumerate(txt.split("\n"), 1) if w in l), 0)
                hits.append((r, i, ln))
    return hits, scanned


def git_last_dates(files):
    """返回 {绝对路径: date} —— 取每个文件最后一次 git 提交日；无 git/非仓库时返回 {}。"""
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
        subprocess.run(["git", "rev-parse", "--git-dir"], cwd=BASE,
                       capture_output=True, check=True)
    except Exception:
        return {}
    out = {}
    for f in files:
        try:
            r = subprocess.run(["git", "log", "-1", "--format=%ad", "--date=short",
                                "--", os.path.relpath(f, BASE)],
                               cwd=BASE, capture_output=True, text=True, timeout=20)
            d = r.stdout.strip()
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", d):
                out[f] = datetime.date.fromisoformat(d)
        except Exception:
            continue
    return out


def parse_review_list():
    """从治理文档 §6.3「时效敏感文档复核清单」表格解析时效敏感文档名（去掉 NN- 目录前缀）。
    不硬编码：清单变更后本函数自动跟随。"""
    txt = read(os.path.join(BASE, GOVERNANCE))
    if not txt:
        return []
    # 必须锚定到四级标题本身：§6.1 更新日志里也出现过这个短语（历史条目在引用它），
    # 不加锚点会抓到更新日志表，解析出一堆日期。
    m = re.search(r"^#{2,6}\s*时效敏感文档复核清单.*?\n(.*?)(?=^#{2,6}\s|\Z)",
                  txt, re.S | re.M)
    if not m:
        return []
    names = []
    for line in m.group(1).split("\n"):
        line = line.strip()
        if not line.startswith("|") or set(line) <= set("|-: "):
            continue
        cell = line.strip("|").split("|")[0].strip()
        if not cell or cell in ("文档", "时效敏感文档"):
            continue
        # 形如 "04-职业教育政策与实训基地标准汇编"，或一格多名 "03-A / B / C"，
        # 或带补充说明 "04-Fab-Academy平台与运营机制（及 2026 两篇）"
        for part in re.split(r"\s*/\s*", cell):
            part = re.sub(r"（.*?）", "", part).strip()
            part = re.sub(r"^\d\d-", "", part).strip()
            if part:
                names.append(part)
        # "（及 2026 两篇）"这类补充说明 -> 同目录下同词干的年度文档（如 Fab-Academy-2026*）
        for yr in re.findall(r"（及\s*(\d{4})\s*[^）]*）", cell):
            for part in re.split(r"\s*/\s*", re.sub(r"（.*?）", "", cell)):
                part = re.sub(r"^\d\d-", "", part).strip()
                stem = re.match(r"[A-Za-z0-9\-]+", part)
                if stem:
                    names.append(f"{stem.group(0)}-{yr}")
    return names


def review_due(files, today=None):
    """按 §6.3 约定判断复核到期。返回 [(相对路径, 最后提交日, 逾期天数, 是否时效敏感)]。"""
    today = today or datetime.date.today()
    dates = git_last_dates(files)
    if not dates:
        return None, None
    sensitive = parse_review_list()
    rows = []
    for f, d in dates.items():
        base = os.path.splitext(os.path.basename(f))[0]
        # 命中清单任一前缀即视为时效敏感
        hit = any(base.startswith(n) or n.startswith(base) for n in sensitive)
        limit = REVIEW_MONTHS_SENSITIVE if hit else REVIEW_MONTHS_NORMAL
        due = d + datetime.timedelta(days=limit * 30)
        if due <= today:
            rows.append((rel(f), d, (today - due).days, hit))
    rows.sort(key=lambda r: (not r[3], -r[2]))
    return rows, today


def read(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def read_md_safe(files):
    """批量读取 .md：遇到非 UTF-8 载体不崩溃，改为记入可报告的错误清单。

    返回 (texts, bad_enc)，bad_enc = [(相对路径, 异常类型名)]。
    动机（A-15 ②）：本脚本会在外部贡献者的机器上跑（fork / PR 场景），仓库里出现
    GBK、UTF-16 或误存二进制的 markdown 完全可能。直接抛 UnicodeDecodeError 会让
    使用者只看到一串 traceback、无法定位是哪个文件——**工具在不可信输入上必须给出
    可读诊断，而不是崩在读取阶段**。BOM 一并剥掉，否则 frontmatter 正则会误判"缺失"。
    """
    texts, bad_enc = {}, []
    for f in files:
        try:
            t = read(f)
        except (UnicodeDecodeError, OSError, ValueError) as e:
            bad_enc.append((rel(f), type(e).__name__))
            texts[f] = ""
            continue
        if t.startswith("\ufeff"):
            t = t[1:]
        texts[f] = t
    return texts, bad_enc


def parse_frontmatter(text):
    m = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.S)
    if not m:
        return None
    fm = {}
    for line in m.group(1).split("\n"):
        mm = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$", line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip()
    return fm


def main():
    args = set(sys.argv[1:])
    quiet = "--quiet" in args

    files = all_md()
    norm = {os.path.normpath(p) for p in files}
    texts, bad_enc = read_md_safe(files)

    # ---------- 选做：复核到期检查 ----------
    if "--review-due" in args:
        rows, today = review_due(files)
        if rows is None:
            print("⚠️ 读不到 git 历史（非 git 仓库或未装 git），跳过复核到期检查。")
            return 0
        rl = parse_review_list()
        print(f"复核到期检查 · 基准日 {today}")
        print(f"约定（来自 {GOVERNANCE} §6.3）：时效敏感 {REVIEW_MONTHS_SENSITIVE} 个月 / 其他 {REVIEW_MONTHS_NORMAL} 个月")
        print(f"时效敏感清单：从 §6.3 表格解析到 {len(rl)} 项 -> {'、'.join(rl[:6])}"
              f"{'…' if len(rl) > 6 else ''}\n")
        if not rows:
            print("✅ 没有到期需复核的文档。")
            return 0
        sens = [r for r in rows if r[3]]
        other = [r for r in rows if not r[3]]
        if sens:
            print(f"=== 🔴 时效敏感·已到期（{len(sens)}）===")
            for r, d, over, _ in sens:
                print(f"  逾期 {over:>4} 天  最后提交 {d}  {r}")
        if other:
            print(f"\n=== 🟡 其他·超 {REVIEW_MONTHS_NORMAL} 个月未动（{len(other)}）===")
            for r, d, over, _ in other[:15]:
                print(f"  逾期 {over:>4} 天  最后提交 {d}  {r}")
            if len(other) > 15:
                print(f"  …另有 {len(other) - 15} 篇")
        print(f"\n结论：{'❌ 有时效敏感文档到期，请核验后更新 date 并登记 §6.1' if sens else '⚠️ 仅有长期未动的非时效文档'}")
        return 1 if sens else 0

    errors, warns = [], []

    # ---------- 0 文件编码 ----------
    for f, why in bad_enc:
        errors.append(("编码",
                       f"{f} 无法按 UTF-8 解码（{why}）—— 本库统一 UTF-8（无 BOM），"
                       f"请转码后重新提交；脚本已跳过其内容，不因此崩溃"))

    # ---------- 1/2 断链 + 库外引用 ----------
    broken, outside, dirlinks = [], [], []
    inbound = collections.Counter()
    for p in files:
        d = os.path.dirname(p)
        for m in LINK_RE.finditer(texts[p]):
            tgt = m.group(1).strip()
            if not tgt or tgt.startswith("/"):
                continue
            try:
                from urllib.parse import unquote
                tgt = unquote(tgt)
            except Exception:
                pass
            ap = os.path.normpath(os.path.join(d, tgt))
            if ap in norm and ap != os.path.normpath(p):
                inbound[ap] += 1
            elif os.path.isfile(ap):
                inbound[ap] += 1
            elif os.path.isdir(ap) and ap.startswith(BASE):
                dirlinks.append((rel(p), tgt))
            elif ap.startswith(BASE):
                broken.append((rel(p), tgt))
            else:
                outside.append((rel(p), tgt))

    for f, l in broken:
        errors.append(("断链", f"{f} → [{l}] 不存在"))
    for f, l in outside:
        warns.append(("库外引用", f"{f} → [{l}]（指向知识库外，开源后对方点不开）"))

    # ---------- 3 孤岛 ----------
    orphans = [rel(p) for p in files
               if inbound[os.path.normpath(p)] == 0 and rel(p) not in README_EXEMPT]
    for o in orphans:
        warns.append(("孤岛文档", f"{o} 没有任何入链"))

    # ---------- 4 README 登记 ----------
    readme_text = texts.get(os.path.join(BASE, README), "")
    for p in files:
        r = rel(p)
        if r in README_EXEMPT:
            continue
        if os.path.basename(r) not in readme_text:
            warns.append(("README未登记", r))

    # ---------- 5 GLOSSARY 登记 ----------
    gpath = os.path.join(BASE, GLOSSARY)
    gtext = texts.get(gpath, "")
    glossary_targets = set()
    for m in LINK_RE.finditer(gtext):
        ap = os.path.normpath(os.path.join(os.path.dirname(gpath), m.group(1).strip()))
        glossary_targets.add(ap)
    for p in files:
        r = rel(p)
        if r in GLOSSARY_EXEMPT:
            continue
        if os.path.normpath(p) not in glossary_targets:
            warns.append(("GLOSSARY未登记", r))

    # ---------- 6/7 frontmatter ----------
    coarse_date = []
    for p in files:
        fm = parse_frontmatter(texts[p])
        if fm is None:
            errors.append(("缺frontmatter", rel(p)))
            continue
        missing = [k for k in REQUIRED_FIELDS if k not in fm or not fm[k]]
        if missing:
            errors.append(("frontmatter字段不全", f"{rel(p)} 缺 {', '.join(missing)}"))
        # type 取值必须落在受控词表内（ERROR 级，与「字段不全」同级）
        tv = str(fm.get("type", "")).strip()
        if tv and tv not in TYPE_VOCAB:
            errors.append(("type越界", f"{rel(p)} type={tv} 不在受控词表内（{ ' / '.join(TYPE_VOCAB) }）"))
        # scope 取值同样受控（ERROR 级）
        sv = str(fm.get("scope", "")).strip()
        if sv and sv not in SCOPE_VOCAB:
            errors.append(("scope越界", f"{rel(p)} scope={sv} 不在受控词表内（{ ' / '.join(SCOPE_VOCAB) }）"))
        dv = str(fm.get("date", ""))
        if re.fullmatch(r"\d{4}-\d{2}", dv):
            coarse_date.append((rel(p), dv))
    infos = [("目录链接", f"{f} → [{l}]（指向库内目录，GitHub 可渲染但 AI 检索不友好，建议改为具体文档）")
             for f, l in dirlinks]
    infos += [("date粒度", f"{f} date={dv}（只到月，无法做时效排序）") for f, dv in coarse_date]

    # ---------- 8 脱敏 ----------
    secret_words = load_secret_words()
    secret_hits, secret_scanned = scan_secrets(secret_words)
    for f, wi, ln in secret_hits:
        errors.append(("脱敏", f"{f} 第 {ln} 行命中 {SECRETS_FILE} 第 {wi} 项，公开前必须改写为中性表述"))

    # ---------- 9 表格列数一致性 ----------
    table_blocks = 0
    table_bad = []
    for p in files:
        n, bad = scan_tables(texts[p])
        table_blocks += n
        for l0, l1, cnt in bad:
            cols = "、".join(f"{k} 列×{v} 行" for k, v in cnt.items())
            errors.append(("表格列数",
                           f"{rel(p)} 第 {l0}-{l1} 行表格列数不一致（{cols}）——"
                           f"权威口径：表头 = 分隔行 = 每个数据行；缺列的多为漏写单元格"))
    table_bad_total = len([e for e in errors if e[0] == "表格列数"])

    # ---------- README 结构导航树排版 ----------
    tree_bad = []
    for i, line in enumerate(readme_text.split("\n"), 1):
        if line.count(".md") >= 2 and ("├──" in line or "└──" in line):
            tree_bad.append((i, line.strip()[:60]))
    for i, s in tree_bad:
        warns.append(("README树排版", f"README.md 第 {i} 行挤了多个条目：{s}…"))

    # ---------- 统计 ----------
    per_dir = collections.Counter()
    for p in files:
        r = rel(p)
        per_dir[r.split("/")[0] if "/" in r else "(根目录)"] += 1
    chars = {rel(p): len(texts[p]) for p in files}
    body = [c for r, c in chars.items() if r not in {README, GLOSSARY}]
    long_docs = [(r, c) for r, c in chars.items() if c > LONG_DOC_THRESHOLD]

    stats = {
        "md总数": len(files),
        "正文篇数": len(body),
        "正文总字数": sum(body),
        "逐目录": dict(sorted(per_dir.items())),
        "入链最多": inbound.most_common(3) and [
            [rel(k) if k.startswith(BASE) else k, v] for k, v in inbound.most_common(3)],
        "超长文档": sorted(long_docs, key=lambda x: -x[1]),
        "date只到月": len(infos),
        "脱敏扫描覆盖面": secret_scanned,
        "脱敏词表条数": len(secret_words),
    }

    if "--stats-md" in args:
        print("<!-- 由 _kbcheck.py --stats-md 自动生成，请勿手抄 -->")
        print(f"| 指标 | 值 |\n|---|---|")
        print(f"| md 文件总数 | {stats['md总数']} |")
        print(f"| 正文篇数（不含 README / GLOSSARY） | {stats['正文篇数']} |")
        print(f"| 正文总字数 | {stats['正文总字数']:,} |")
        print(f"| 断链 | {len(broken)} |")
        print(f"| 孤岛文档 | {len(orphans)} |")
        print(f"| 库外引用 | {len(outside)} |")
        print(f"| 库内目录链接 | {len(dirlinks)} |")
        print(f"| README 未登记 | {len([w for w in warns if w[0] == 'README未登记'])} |")
        print(f"| GLOSSARY 未登记 | {len([w for w in warns if w[0] == 'GLOSSARY未登记'])} |")
        print(f"| 脱敏词表 | {'已加载 ' + str(len(secret_words)) + ' 词' if secret_words else '未配置（跳过）'} |")
        print(f"| 脱敏扫描覆盖面 / 命中 | {secret_scanned} 个可发布文本文件 / {len(secret_hits)} 命中 |")
        print(f"| 表格块 / 列数异常 | {table_blocks} / {table_bad_total} |")
        print(f"| frontmatter 完整 | {len(files) - len([e for e in errors if e[0] == '缺frontmatter'])}/{len(files)} |")
        print("\n| 目录 | 篇数 |\n|---|---|")
        for k, v in stats["逐目录"].items():
            print(f"| {k} | {v} |")
        if stats["超长文档"]:
            print(f"\n> 超过 {LONG_DOC_THRESHOLD:,} 字、建议拆分的文档：")
            for r, c in stats["超长文档"]:
                print(f"> - `{r}`（{c:,} 字）")
        return 0

    if "--json" in args:
        print(json.dumps({"errors": errors, "warnings": warns, "infos": infos, "stats": stats},
                         ensure_ascii=False, indent=2, default=str))
        return 2 if errors else (1 if warns else 0)

    if quiet and not errors and not warns:
        return 0

    print(f"知识库自检 · {rel(BASE) or '.'}")
    print(f"共 {len(files)} 个 md（正文 {len(body)} 篇，{sum(body):,} 字）\n")

    print(f"=== ERROR（{len(errors)}）===")
    if not errors:
        print("  无")
    grouped = collections.defaultdict(list)
    for kind, msg in errors:
        grouped[kind].append(msg)
    for kind, msgs in grouped.items():
        print(f"  [{kind}] {len(msgs)} 处")
        for m in msgs:
            print(f"      {m}")

    print(f"\n=== WARN（{len(warns)}）===")
    if not warns:
        print("  无")
    grouped = collections.defaultdict(list)
    for kind, msg in warns:
        grouped[kind].append(msg)
    for kind in ["README未登记", "GLOSSARY未登记", "孤岛文档", "README树排版",
                 "库外引用", "frontmatter字段不全", "type越界", "scope越界", "表格列数"]:
        if kind not in grouped:
            continue
        msgs = grouped.pop(kind)
        print(f"  [{kind}] {len(msgs)} 处")
        show = msgs if len(msgs) <= 12 else msgs[:12] + [f"…另有 {len(msgs)-12} 处（用 --json 查看全部）"]
        for m in show:
            print(f"      {m}")
    for kind, msgs in grouped.items():
        print(f"  [{kind}] {len(msgs)} 处")
        for m in msgs[:12]:
            print(f"      {m}")

    infos_by_kind = collections.defaultdict(list)
    for kind, msg in infos:
        infos_by_kind[kind].append(msg)
    if infos_by_kind:
        n = sum(len(v) for v in infos_by_kind.values())
        print(f"\n=== INFO（{n}，不阻塞）===")
        for kind in ["目录链接", "date粒度"]:
            if kind not in infos_by_kind:
                continue
            msgs = infos_by_kind.pop(kind)
            print(f"  [{kind}] {len(msgs)} 处")
            for m in (msgs if len(msgs) <= 5 else msgs[:5] + [f"…另有 {len(msgs)-5} 处（用 --json 查看全部）"]):
                print(f"      {m}")
        for kind, msgs in infos_by_kind.items():
            print(f"  [{kind}] {len(msgs)} 处")
            for m in msgs[:5]:
                print(f"      {m}")

    print("\n=== 逐目录篇数 ===")
    for k, v in stats["逐目录"].items():
        print(f"  {k:<22} {v}")
    if stats["超长文档"]:
        print(f"\n=== 超长文档（>{LONG_DOC_THRESHOLD:,} 字，建议拆分）===")
        for r, c in stats["超长文档"]:
            print(f"  {c:>8,}  {r}")

    print(f"\n结论：{'❌ 有 ERROR，必须修' if errors else ('⚠️ 有 WARN，建议修' if warns else '✅ 全部通过')}")
    return 2 if errors else (1 if warns else 0)


if __name__ == "__main__":
    sys.exit(main())
