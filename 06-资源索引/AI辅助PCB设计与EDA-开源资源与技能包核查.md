---
title: "AI 辅助 PCB 设计与 EDA：2026-10 前沿进展、开源资源与技能包可用性核查"
type: 资源
scope: 通用
source: "GitHub 实证检索（2026-10-15 经 gh api 定点核查星标/许可/最近推送）+ aklofas/kicad-happy 仓库 README 与 SKILL 参考件原文抽取 + 四类商业 AI-PCB 工具的公开面核查"
date: 2026-10-15
tags: [PCB设计, EDA, KiCad, 开源工具, AI辅助设计, agent skill, MCP, Gerber, EMC, 资源核查]
---

# AI 辅助 PCB 设计与 EDA：2026-10 前沿进展、开源资源与技能包可用性核查

> **缘起**：用户问「AI 辅助 PCB 领域当前有哪些成果与进展、有无可补充进知识库的内容」。
> **本文做四件事**：① 先给结论：**本库在「AI 辅助 PCB / EDA」上确为空白**（不是没查，是查过没有）；② 把 2026-10 的技术进展收敛成**四条路线**并逐条给出实证仓库；③ 对头号候选 **`aklofas/kicad-happy`** 做**原文级抽取**（它的**流程骨架与判据纪律**比仓库本身更值钱）；④ 给出 A/B/C 三档实证清单、许可纪律、「★ 不纳入清单」与落地建议。
> **数据口径**：全文星标 / 许可 / 最近推送均为 **2026-10-15 经 `gh api` 定点核查**所得，**非记忆估计**；许可栏为 GitHub 许可证 API 的返回值原文。
> **与谁配对**：本文是「工具与资源」层；落地的工艺/耗材口径见 [开源软件工具链清单](../03-设备与工具/开源软件工具链清单.md) §1.4 与 [数字制造工艺全景-专题补充](../03-设备与工具/数字制造工艺全景-专题补充.md)。

---

## 一、结论先行

| # | 判断 | 依据 |
|---|---|---|
| 1 | **「AI 辅助 PCB / EDA」在本库确为空白，不是重复议题** | 全库含 PCB / EDA / KiCad / Gerber / 布线 / DRC / SMT 关键词的 21 个文件中，**唯一实质内容**只有《开源软件工具链清单》§1.4 的**一行**「KiCad｜GPL｜开源 EDA，原理图+PCB 全流程」；其余 20 处全是建筑规划、竞赛、课程、Fab 大会等场景的**顺带提及**，无专篇 |
| 2 | 2026-10 的进展可收敛为**四条互不替代的路线** | AI 审图（kicad-happy）/ Code-first 电路设计（atopile·tscircuit·SKiDL）/ MCP 直连 EDA（KiCAD-MCP-Server）/ 布线求解与出板件（freerouting·tracespace·gerbolyze）。四者补的是同一条链的不同环，**不可互相替换** |
| 3 | ★ **头号可用件是 `aklofas/kicad-happy`**（1,394★ / **MIT** / 2026-10-15），且**原生声明支持 OpenAI Codex** | 可用本机 `$skill-installer` 直接从 GitHub 装入；覆盖原理图分析→布局审查→EMC 预合规→SPICE 仿真→器件选型→出板准备全链；其「**确定性脚本做数据抽取、AI 只做数据之上的推理**」分工与本库已确立的「判定式而非生成式」纪律**同源**（详见 §五） |
| 4 | **既有那一行 KiCad 记录需要补许可口径** | 《开源软件工具链清单》§1.4 只写了「开源 EDA，原理图+PCB 全流程」，未写 EDA 的现实许可生态：**KiCad 本体 GPL-3.0，LibrePCB / Horizon 亦 GPL-3.0，gerbolyze 为 AGPL-3.0** —— GPL 家族**只能作独立进程调用**，设计件（原理图/布局/Gerber）**不可并入自有闭源工程** |
| 5 | **商业 AI-PCB 工具（Quilter / Celus / Backflip 一类）在本仓不可核** | 对其候选 `owner/repo` 定点核查 `gh api` 均返回 **404**（无对应公开仓库）；判定为**闭源商业 SaaS**。本库**只登记其存在与定位，不引用其功能细节**，避免把市场宣传写成事实 |
| 6 | **「技能包」与「设计件」必须分开对待** | 技能（审图 / 选型 / 出板）可装、可复用到任意 KiCad 工程；**设计件（原理图 / 布局 / Gerber）是不可移植的产物**，只能作为「写法范本 + 踩坑清单」借鉴，不能当作可复用资产入库 |

---

## 二、核查口径

### 2.1 三分类判据（同本库一贯口径）

| 判定 | 含义 | 处置 |
|---|---|---|
| ✅ 已有 | 本库有等价或更强的文档 | 引用即可，**不新建** |
| ➕ 增量 | 本库确无，且能直接用于本项目 | 列入补充候选，排优先级 |
| ❌ 不可用 | 与项目范围界定冲突 / 数值错误 / 来源过时 | 记入本文并标注正确口径 |

### 2.2 ★ 本库的收录门槛（决定「进不进库」）

> 本库对「通用工具清单」的收录门槛是：**它必须能回答本项目的一个具体判断**。
> 「PCB/EDA 工具大全」本身不构成收录理由；**能回答「哪一件现在就能装、许可能不能用、它替我省掉哪一步人工」的，才进库。**

### 2.3 与相邻文档的边界（防重复）

| 相邻文档 | 与本文的分工 |
|---|---|
| [开源软件工具链清单](../03-设备与工具/开源软件工具链清单.md) | 该篇是「数字制造全链软件的**选型表**」（CAD/CAM/切片/EDA 各一行）；本文是「**AI 辅助 PCB 这一子域**的进展与可用件核查」，不重复其全链选型 |
| [开源硬件与AI开发套件选型](../03-设备与工具/开源硬件与AI开发套件选型.md) | 该篇选的是**开发板/套件**（Jetson/树莓派/Arduino）；本文选的是**画板子用的软件与技能** |
| [数字制造工艺全景-专题补充](../03-设备与工具/数字制造工艺全景-专题补充.md) | 该篇讲**工艺链**（加法/减法/模切）；本文讲**设计端**（从原理图到出板件） |
| [AI操控Blender工具生态-MCP与插件资源调研](AI操控Blender工具生态-MCP与插件资源调研.md) | 同属「AI 操控专业软件的 MCP / 技能生态」形态，可对照阅读（那篇是 3D 建模，本文是电子设计） |

---

## 三、技术进展：四条路线

| 路线 | 原理 | 代表件（本文实证） | 适合场景 | 本库缺口 |
|---|---|---|---|---|
| **AI 审图 / 设计审查** | 确定性脚本把 KiCad/PCB/Gerber **解析成结构化 JSON**，AI 在这份数据上做推理，输出**分级问题清单** | `aklofas/kicad-happy` | 已有工程的质量门禁、PR 自动评审、下单前把关 | ➕ 确有 |
| **Code-first 电路设计** | 用**代码/声明式语言**描述电路，天然可版本控制、可复用、可自动校验 | `atopile/atopile`、`tscircuit/tscircuit`、`devbisme/skidl` | 需要版本管理与设计复用；参数化改板 | ➕ 确有 |
| **MCP 直连 EDA** | EDA 侧起 MCP 服务，AI 客户端**直接读写工程文件**、调用命令 | `mixelpixx/KiCAD-MCP-Server` | 对话式改板、批量脚本化操作 | ➕ 确有 |
| **布线求解与出板件** | 自动布线器、Gerber 生成/渲染/叠加、BOM 出图 | `freerouting/freerouting`、`tracespace/tracespace`、`jaseg/gerbolyze`、`yaqwsx/PcbDraw` | 布线自动化、出图与合规件制作 | 部分（本库仅在工具链清单一笔带过） |

> ★ 一句话判别四条路线：**审图路线是「读」，code-first 是「写」，MCP 是「改」，求解器是「算」** —— 它们都能独立落地，选型时按「你要它替掉哪一步人工」来挑，而不是按星标高低挑。

---

## 四、★ 实证清单（2026-10-15 `gh api` 定点核查）

### 4.1 A 档 —— 可直接用（许可为 MIT / Apache-2.0，可移植实现）

| 仓库 | ★ | 许可 | 最近推送 | 为什么是它 |
|---|---|---|---|---|
| **[aklofas/kicad-happy](https://github.com/aklofas/kicad-happy)** | 1,394 | MIT | 2026-10-15 | ★ 头号候选：KiCad 的 **AI agent 技能包**（11 个 skill），原生支持 **OpenAI Codex**；做「读」这一环（详见 §五） |
| **[atopile/atopile](https://github.com/atopile/atopile)** | 3,989 | MIT | 2026-10-14 | 「用代码设计电路板」，声明式 `.ato` 语言 + 校验/复用/版本控制，做「写」这一环 |
| **[tscircuit/tscircuit](https://github.com/tscircuit/tscircuit)** | 2,838 | MIT | 2026-10-14 | 用 TypeScript/React 描述真实电路并浏览器渲染，做「写 + 看」这一环 |
| **[mixelpixx/KiCAD-MCP-Server](https://github.com/mixelpixx/KiCAD-MCP-Server)** | 2,697 | MIT | 2026-10-01 | KiCad 的 MCP 服务端，让 LLM 直接操作 KiCad，做「改」这一环 |
| **[yaqwsx/KiKit](https://github.com/yaqwsx/KiKit)** | 2,042 | MIT | 2026-10-09 | KiCad 自动化工具集（**Python API + 命令行**），是把审图/改板脚本化的底座 |
| **[devbisme/skidl](https://github.com/devbisme/skidl)** | 1,693 | MIT | 2026-09-24 | 最老牌的「Python 描述电路」库，做 code-first 的轻量入口 |
| **[openscopeproject/InteractiveHtmlBom](https://github.com/openscopeproject/InteractiveHtmlBom)** | 4,602 | MIT | 2026-10-14 | 交互式 HTML BOM 生成插件（KiCad/EasyEDA/Eagle 等通用），贴片/焊接阶段的实用件 |
| **[yaqwsx/PcbDraw](https://github.com/yaqwsx/PcbDraw)** | 1,438 | MIT | 2026-10-09 | 把 KiCad 板子转成**可读的 2D 图纸**（引脚图/装配图） |
| **[tracespace/tracespace](https://github.com/tracespace/tracespace)** | 955 | MIT | 2025-01-20 | Gerber → 精确 SVG 渲染，出图与视觉复核用（★ 已 21 个月未推送，**留作参照，不建议作主链**） |
| **[earthtojake/step.parts](https://github.com/earthtojake/step.parts)** | 382 | MIT | 2026-06-13 | 12,000+ 开源 **STEP** 元件模型，是 **PCB ↔ 结构设计**的桥（配合下方 `kicadStepUp` 用） |

### 4.2 B 档 —— 条件可用（许可或依赖需限定）

| 仓库 | ★ | 许可 | 最近推送 | 用途与限定 |
|---|---|---|---|---|
| [LibrePCB/LibrePCB](https://github.com/LibrePCB/LibrePCB) | 3,017 | GPL-3.0 | 2026-10-12 | 独立 EDA 套件。★ **GPL → 只可作独立进程使用**，不可链接进自有代码 |
| [freerouting/freerouting](https://github.com/freerouting/freerouting) | 2,105 | GPL-3.0 | 2026-10-14 | 先进自动布线器。**GPL → 独立进程调用**；输出（布线结果）可自用 |
| [horizon-eda/horizon](https://github.com/horizon-eda/horizon) | 1,323 | GPL-3.0 | 2026-10-04 | 独立 EDA 套件。同上 GPL 限定 |
| [jaseg/gerbolyze](https://github.com/jaseg/gerbolyze) | 417 | **AGPL-3.0** | 2026-04-25 | 把 SVG 覆盖层直接渲染进 Gerber/Excellon。★ **AGPL → 只可内部运行取结果，绝不可作为对外服务** |
| [michaelgale/pcbflow](https://github.com/michaelgale/pcbflow) | 199 | BSD-3-Clause | 2025-02-12 | Python 布线/设计包，**许可宽松可移植**，但活跃度低、生态小 |
| [Argmaster/pygerber](https://github.com/Argmaster/pygerber) | 123 | MIT | 2026-03-24 | Gerber X3/X2 标准的 Python 实现 + 2D 渲染，做**出板件自动核对**很合适 |
| [curtacircuitos/pcb-tools](https://github.com/curtacircuitos/pcb-tools) | 312 | Apache-2.0 | 2024-06-19 | PCB 数据（Gerber/Excellon/NC）工具。**停更 2 年+**，仅作参照 |
| [joanbono/awesome-kicad](https://github.com/joanbono/awesome-kicad) | 629 | GPL-3.0 | 2026-10-13 | KiCad 资源清单。**GPL → 只做外链，不搬内容** |

### 4.3 C 档 —— 仅作参照 / 名录

| 仓库 | ★ | 许可 | 最近推送 | 说明 |
|---|---|---|---|---|
| [kitspace/awesome-electronics](https://github.com/kitspace/awesome-electronics) | 8,227 | CC0-1.0 | 2026-10-12 | 电子工程资源大清单。**CC0 → 可摘编，但仍须标来源**（本库纪律：即便 CC0 也保留出处） |
| [KiCad/kicad-source-mirror](https://github.com/KiCad/kicad-source-mirror) | 3,034 | — | — | KiCad 官方开发分支**镜像**（上游在 GitLab）；查源码可读，**不作依赖** |
| KiCad 官方本体（GPL-3.0） | — | GPL-3.0 | — | 本库《开源软件工具链清单》§1.4 已收录；**GPL 家族 → 独立进程使用** |

### 4.4 许可纪律（本库硬规则，逐条对照）

| 许可类型 | 本库允许的动作 | 本文涉及 |
|---|---|---|
| MIT / Apache-2.0 / BSD-3 | 可移植实现、可改写、可并入自有工程 | kicad-happy、atopile、tscircuit、SKiDL、KiKit、KiCAD-MCP-Server、PcbDraw、pygerber、pcbflow |
| GPL-3.0（含 KiCad 本体 / LibrePCB / Horizon / freerouting） | **只作独立进程调用**；自身代码不可被其传染 | LibrePCB、freerouting、horizon、awesome-kicad |
| **AGPL-3.0** | **只可内部运行取结果**，不可作为对外网络服务 | gerbolyze |
| CC0-1.0 | 可摘编，**仍须标来源** | awesome-electronics |
| `NOASSERTION` / 无 LICENSE | **只读思路**，不复制素材、不依赖 | kicad-source-mirror 等 |

> ★ 本库自身为 **CC BY 4.0（含商用）**，因此**含 `NC`（禁商用）/ `SA`（同源）的第三方材料一律只做「原理借鉴 + 外链」，不复制素材**；第三方受版权材料只摘录、不整段转载。

---

## 五、★ `aklofas/kicad-happy` 原文抽取（本文最高价值段）

> 价值不在「它是个 KiCad 技能包」，而在它**把一条专业设计审查链，拆成了可审计的两段**。这两段的分工，比工具本身更值得写进本库。

### 5.1 它到底做什么

| 项 | 值 |
|---|---|
| 仓库 | [aklofas/kicad-happy](https://github.com/aklofas/kicad-happy)（1,394★ / MIT / 2026-10-15 推送）|
| 定位 | 「AI-powered design review for KiCad」——分析原理图、PCB 布局与 Gerber，**在下单前抓真 bug** |
| 兼容客户端 | Claude Code、★ **OpenAI Codex**、GitHub Copilot CLI、Google Antigravity、opencode；也可作 **GitHub Action** 做 PR 自动评审，或直接跑独立 Python 脚本 |
| 技能数 | **11 个 skill**：`kicad` / `bom` / `datasheets` / `emc` / `spice` / `digikey` / `mouser` / `lcsc` / `element14` / `jlcpcb` / `pcbway` |
| 安装（Codex） | 「用 `$skill-installer` 从 `https://github.com/aklofas/kicad-happy` 装 kicad-happy 的技能」——即**走本机 skill-installer 通道，不装任何 EXE** |
| 实测样例 | 一块 184 元件机器人控制板、一块 296 元件 GNSS 振荡器板（仓库内附完整报告） |

### 5.2 ★ 最值钱的一条分工纪律

> **「分析脚本是数据抽取工具，不是 AI」** —— 脚本是**确定性 Python**，把 KiCad 的 S 表达式文件解析成结构化 JSON（元件表、网络连通性、识别出的子电路、板框尺寸、DFM 测量）；**没有机器学习、没有逐次漂移的启发式、不调云**。**「AI 的部分，是在数据之上做推理——不是数据本身」。**

由此推出的三条可复用原则（**与本库既有纪律同源**）：

| 原则 | kicad-happy 的原话/做法 | 对应本库已立纪律 |
|---|---|---|
| **数据可审计** | 脚本自己跑一遍、读 JSON、任何结论都能复核 | 本库「判定式而非生成式」、坐标驱动 + 几何校验 |
| **推理可透明** | Agent 展示算式、引脚追踪、数据手册引用 | 本库「依据可核到条号/仓库」 |
| **无隐藏决策** | 脚本开放、方法有独档、JSON 人类可读 | 本库「登记 + 可追溯」 |

### 5.3 三（+一）步流程骨架

1. **解析文件** —— `analyze_schematic.py` / `analyze_pcb.py` / `analyze_gerbers.py`：把 S 表达式解析成通用树（**不写按 KiCad 版本分支的逻辑**，因此 KiCad 5→10 都能吃）、走层级子图、抽每个元件（位号/值/封装/MPN/数据手册 URL/引脚坐标，且**应用旋转与镜像变换**）、用**并查集按坐标建网络图**（0.01mm 内的点合并），再跑 **60+ 个检测器**（分压/RC-LC 滤波/电源反馈/运放/电流检测/保护器件/晶振负载电容/桥式电路/总线 I²C-SPI-CAN 及其上拉与终端校验/…），最后输出 60–220KB 结构化 JSON。
2. **取数据手册** —— 用 distributor skill（DigiKey/Mouser/LCSC/element14）下载每个有 MPN 的元件手册，本地缓存 + `manifest.json`，再由 `datasheets` skill 抽成按 MPN 的结构化规格（v1.4 起为 schema 驱动的**类型化抽取**，每个值带 `min/typ/max/unit/condition/evidence` 与三级质量评分）。
3. **交叉核对与评审** —— Agent 同时读分析 JSON 与数据手册：**核对分析数据**（与原始原理图的元件数抽查、关键网络逐脚追踪）、**与手册对照校验**（反馈分压算出的 Vout 对上稳压器真实 Vref…）、**原理图↔PCB 互校**（元件数是否一致、网络是否都布通、发热焊盘过孔够不够）、**出板件检查**（Gerber 层是否齐、钻孔文件在不在、坐标是否对齐、压缩包是否过期），最后写成分级报告。
4. **★ 第四步：你先审这份评审** —— 官方原话是「**You review the review**」：输出是**工程判断的起点，不是替代品**；每个算式都摊开、每处手册引用都标出、每条发现都带足够上下文供你**确认或驳回**。

### 5.4 ★ 一条可直接搬进本库的判据

> ★★ **没有数据手册，只能查「自洽」（原理图与自己一致）；有数据手册，才能查「正确」（元件值与厂商推荐值、绝对最大额定值、参考电路是否相符）。**

配套的**置信标签**做法也值得抄：每条发现都带 `deterministic` / `heuristic` / `datasheet-backed` 之一，v1.4 起还给每个值加**信任闸**（按证据置信度过滤，把「没抽到」「抽到了但低于闸」「可信值在」三态分开）——这正好是本库反复踩过的「**读数不能脱离口径单独比较**」的工程化版本。

### 5.5 非破坏性：只读层不可被改写

v2.0 的 **Deep Review** 通道做逐 IC 的手册比对，产出写在 `analysis/deep_review.json`；**该轮是「非破坏性」的** —— Layer 1 的确定性发现**永不被修改**，把 `llm_*` 字段剥掉即可回到确定性基线。★ 与本库「**新增文档不改既有文档正文，修订另起版本号**」是同一类保护。

### 5.6 ★ 它内嵌的规范口径（可直接引用的 EMC 限值）

该仓库的 `emc` 技能自带一份《EMC Standards Quick Reference》，**自述其限值「已对照官方法规文本与认可实验室文档核对（2026-04）」**，可作本库对外合规表述的二手来源（**正式引用前仍须以法规原文复核**）：

| 标准 | 适用 | 关键限值（示例） |
|---|---|---|
| **FCC Part 15 §15.109**（美） | Class B 住宅，**3 m 测** | 30–88 MHz **40.0 dBµV/m**；88–216 MHz 43.5；216–960 MHz 46.0；>960 MHz 54.0 |
| **FCC Part 15 §15.109** | Class A 商用/工业，**10 m 测** | 30–88 MHz 39.1；88–216 MHz 43.5；216–960 MHz 46.4；>960 MHz 49.5 |
| **CISPR 32 / EN 55032**（国际 / 欧盟 CE） | Class A / Class B，10 m 测 | 30–230 MHz：A **40** / B **30** dBµV/m；230–1000 MHz：A 47 / B 37 |
| **CISPR 25 Class 5**（车载，1 m 测） | ALSE 内测试，五级中**最严** | 见仓内表；用于汽车电子 |

> ★ **一条口径纠正**：**CISPR 32 已取代旧的 CISPR 22 / EN 55022** —— 若外部资料仍引 CISPR 22，属旧号。另：FCC Class B 与 CISPR 32 Class B 在按测距归一后**大致等价**（0–3 dB 内）。

### 5.7 它固化的踩坑（“别人用血换的”）

| 坑 | 事实 |
|---|---|
| **插件更新检测不到新版本** | Claude Code 的 `/plugin update` 不可靠（上游 issue #36317）；**正确做法是清缓存重装**（删 `~/.claude/plugins/cache/...` 与 `marketplaces/...` 后重新 add + install） |
| **技能发现期有 churn** | 2025 末–2026 初 skill-loader 连续有 bug（glob 不匹配、全局目录遍历、`skills.path` 配置命名）；**锁定 2025-12 之后的版本**可规避 |
| **数据手册这一步不能省** | 省掉它，审查只能停在「自洽」层（见 §5.4） |

---

## 六、★ 技能市场检索（英文技术专名，2026-10-15）

> **纪律**：专业技能市场的检索是**描述文本的模糊匹配**，**中文职能词（「电路」「画板」「结构」）会假阴性**；专业技能的描述里必然含**罗马字技术专名**。本轮一律用英文技术名检索。

| 检索词 | 命中 | 相关性 |
|---|---|---|
| `kicad skills` | 8 | ★★★ **`aklofas/kicad-happy`（1,394★）一支独大**；其余 7 个均为 1–23★ 的个人小仓（如 `Milind220/Ki-Stack` 23★、`mash/kicad-skills`「Codex skills」1★） |
| `pcb agent skills` | 1 | 仅 1 个 0★ 中文仓库（`yymqd/kicad-pcb-agent-skills`，描述含 kicad-cli / MCP-KiCad 三管线） |
| `freecad skills` | 3 | 全部 ≤2★（`SalvatoreMastrangelo/freecad_skill` 1★ 等）—— **FreeCAD 侧技能市场基本空白** |
| `cad skills agent` / `step cad agent` | 0 | **0 命中** |
| GitHub 主题 `ai-skills` 全量按星排行 | — | `aklofas/kicad-happy` 是其中**唯一的 PCB/EDA 条目**（1,394★） |

> **结论**：PCB / EDA 方向**规模化技能只有 kicad-happy 一支**（长尾都是个人小仓）；FreeCAD / CAD 方向**技能市场尚无规模件**，只能走 GitHub 仓库直装或自研。
> **一条限制（照实记）**：本机 `skill-installer` 的**策展列表接口本次返回 HTTP 403**（未能取到官方 `.curated` 列表），故上表以 **GitHub 主题/关键词检索**为准，**策展市场一栏待补**。

---

## 七、Skill 适配结论（与本机既有技能对账）

| 本机既有技能（`~/.workbuddy/skills/`） | 与本文的关系 |
|---|---|
| `external-knowledge-pack-audit` | 本文即按该技能方法产出（外部核查 → GitHub 实证 → 三档 → 落盘） |
| `open-knowledge-source-probe` / `external-api-service-review` | 与 kicad-happy 的 distributor skill（DigiKey/Mouser/LCSC/element14）属同类「外部服务核查」形态，可对照 |
| `llm-derived-field-extraction` | 与 kicad-happy `datasheets` skill 的「**类型化字段抽取 + 置信度闸**」同构，是本库已有能力的外部镜像 |
| `blender-headless-modeling` / `sketchup-mcp-modeling` | 同为「AI 操控专业软件」的技能，但作用于 3D 建模；**与 PCB 侧技能不重叠** |

**真缺口（本机确无）**：**没有**任何「电子设计 / 原理图 / PCB / Gerber / 出板件」方向的技能。→ **建议**：若本项目要开始做板子，**优先用 `$skill-installer` 装 kicad-happy**（MIT，可直接用），而不是自研审图技能。

---

## 八、★ 不纳入清单（逐项写明理由，防止日后被翻案）

| 不纳入项 | 理由 |
|---|---|
| **任何闭源商业 AI-PCB 工具的功能描述**（Quilter / Celus / Backflip 一类） | 本仓**不可核**（`gh api` 候选仓 404）；把市场宣传写进库会污染「可核查」基线。**只登记其存在** |
| **`kicad-source-mirror` 作依赖** | 它只是**镜像**（上游在 GitLab），且许可未在 GitHub 标注；**读源码可以，引用为依赖不行** |
| **`tracespace` 作主链** | 已 21 个月未推送（最近 2025-01-20）；**留作参照**，主链改走 `pygerber` |
| **`pcb-tools` 作依赖** | 停更 2 年+（2024-06）；仅作参照 |
| **awesome 清单的正文搬录** | `awesome-kicad` 为 GPL（**只外链**）；`awesome-electronics` 为 CC0（可摘编**但仍须标来源**）——两者都**不整段搬进本库** |
| **任何 KiCad/EDA 的**设计件**（原理图/布局/Gerber 文件）** | 设计件是**不可移植的产物**，且常带第三方版权；只作「写法范本 + 踩坑清单」借鉴 |
| **把 `kicad-happy` 的 SKILL 正文整篇复制进库** | 本库为 CC BY 4.0 含商用，kicad-happy 为 MIT；**本文只做「结构抽取 + 外链」**，不整篇转载其文档 |

---

## 九、落地建议（P0 / P1 / P2）

| 优先级 | 动作 | 不要做什么 |
|---|---|---|
| **P0** | 若要立刻做板子：用 `$skill-installer` 装 **kicad-happy**（MIT/Codex 原生），先把「审图」这一环补上 | **不要**自研审图技能；**不要**把它的文档整篇拷进库 |
| **P0** | 把本文第 4 行结论回填进《开源软件工具链清单》§1.4：EDA 许可为 **GPL 家族（KiCad GPL-3.0 / LibrePCB GPL-3.0 / gerbolyze AGPL）**，写明「独立进程调用」边界 | **不要**只写「GPL」两字就完事（边界不写清＝日后必踩） |
| **P1** | 需要参数化改板 / 版本控制电路时，评估 **atopile**（MIT）或 **tscircuit**（MIT）做 code-first 试点 | **不要**一上来就把既有工程全迁 code-first |
| **P1** | 出板件自动核对：接 **pygerber**（MIT）替代停更的 tracespace/pcb-tools | **不要**用 AGPL 的 gerbolyze 做对外服务 |
| **P2** | 若开始做「板子 + 外壳」一体的硬件项目：把 **PCB ↔ 结构**的桥接件（`step.parts` + `kicadStepUp`）纳入选型，见姊妹篇 [AI辅助机械结构设计](AI辅助机械结构设计与参数化CAD-工具生态与可用性核查.md) | **不要**把板子的 3D 模型与结构模型各维护一套 |

---

## 相关文档

| 文档 | 关系 |
|---|---|
| [开源软件工具链清单](../03-设备与工具/开源软件工具链清单.md) | ★ 本文回填其 §1.4 许可口径；该篇是全链软件选型表 |
| [AI辅助机械结构设计与参数化CAD-工具生态与可用性核查.md](AI辅助机械结构设计与参数化CAD-工具生态与可用性核查.md) | ★ 姊妹篇：PCB 设计完成后，**结构/外壳**这一侧的进展与可用件 |
| [数字制造工艺全景-专题补充](../03-设备与工具/数字制造工艺全景-专题补充.md) | 设计件之后的工艺链（打样/贴片/装配） |
| [AI操控Blender工具生态-MCP与插件资源调研.md](AI操控Blender工具生态-MCP与插件资源调研.md) | 同形态对照：AI 操控专业软件的 MCP / 技能生态 |
| [AI应用现状全景-创客空间各领域调研.md](AI应用现状全景-创客空间各领域调研.md) | AI 全领域背景地图 |
| [知识库覆盖度分析与补充路线图](../00-知识库治理/知识库覆盖度分析与补充路线图.md) | 本文回应其中「缺 CAD/CAM/EDA 软件对比与选型」一行的**设计端**延伸 |

## 主要来源（均为 2026-10-15 经 `gh api` 定点核查）

- 仓库元数据（星标 / 许可 / 最近推送）：GitHub REST API `repos/<owner>/<repo>`
- `aklofas/kicad-happy`：仓库 `README.md`、`how-it-works.md`、`install-guidance.md`、`skills/*/SKILL.md`（技能清单）、`skills/emc/references/emc-standards.md`（EMC 限值）
- 仓库检索：GitHub 主题检索（`pcb` / `gerber` / `eda` / `cad` / `ai-skills` / `claude-skills`）与关键词检索（`kicad skills` 等）
- EMC 限值原始出处（kicad-happy 所引）：47 CFR §15.109、IEC CISPR 32:2015+AMD1:2019、IEC CISPR 25:2021

## 变更记录

| 版本 | 日期 | 变更 |
|---|---|---|
| v1 | 2026-10-15 | 首版：四条路线收敛 + A/B/C 实证清单（19 项）+ kicad-happy 原文抽取（流程骨架/判据/踩坑/EMC 口径）+ 技能市场英文专名检索 + 不纳入清单 + P0/P1/P2 |
