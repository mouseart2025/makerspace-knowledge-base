---
title: "AI 辅助机械结构设计与参数化 CAD：2026-10 工具生态、可用性与 PCB↔结构桥接核查"
type: 资源
scope: 通用
source: "GitHub 实证检索（2026-10-15 经 gh api 定点核查星标/许可/最近推送）+ FreeCAD / OpenSCAD / CadQuery / build123d 官方仓库与 freecad-mcp 原文核查"
date: 2026-10-15
tags: [机械结构设计, 参数化CAD, Code-CAD, FreeCAD, OpenSCAD, CadQuery, build123d, MCP, text-to-CAD, 有限元, 资源核查]
---

# AI 辅助机械结构设计与参数化 CAD：2026-10 工具生态、可用性与 PCB↔结构桥接核查

> **缘起**：用户问「AI 辅助**结构设计**领域当前有哪些成果与进展、有无可补充进知识库的内容」。
> **★ 先分清两个「结构」**：本库既有 38 篇「**建筑 / 空间结构**」（空间动线、SLP、SketchUp、平面图）；本文只谈**机械结构设计**（零件 / 装配 / 公差 / 壳体）——这一支**本库确为空白**。
> **本文做四件事**：① 给结论并**证明是空白**；② 把 2026-10 的进展收敛成**三条路线**并逐条实证；③ ★ 补上本库此前缺的 **PCB ↔ 结构桥接件**；④ 给出 A/B/C 清单、许可纪律、「★ 不纳入清单」与落地建议。
> **数据口径**：全文星标 / 许可 / 最近推送均为 **2026-10-15 经 `gh api` 定点核查**所得，**非记忆估计**。
> **与谁配对**：本文是**结构侧**；板子那一侧见姊妹篇 [AI辅助PCB设计与EDA-开源资源与技能包核查](AI辅助PCB设计与EDA-开源资源与技能包核查.md)；软件全链选型见 [开源软件工具链清单](../03-设备与工具/开源软件工具链清单.md)。

---

## 一、结论先行

| # | 判断 | 依据 |
|---|---|---|
| 1 | **「机械结构设计」在本库确为空白，且极易与「建筑结构」混淆** | 全库命中 SolidWorks / CAD / 参数化 / 铝型材 / 公差 / 有限元 / 仿真 的**近百个文件**中，**绝大多数是建筑与空间结构**（空间动线、SLP、SketchUp、Blender、平面图，属 02-空间搭建）；**机械零件 / 装配 / 公差 / 壳体**方向**无专篇**，仅《开源软件工具链清单》§1.1 有 FreeCAD / SolveSpace / CadQuery **三行工具名** |
| 2 | ★ **「结构」在下游是两个不同对象，必须分开选址** | ① **建筑 / 空间结构** → 已属 [02-空间搭建](../02-空间搭建/)；② **机械结构设计** → 本库空白，**本文落点**。混用会导致「拿建筑规范去校机械公差」这类错配 |
| 3 | 2026-10 的机械结构设计 AI 化落在**三条路线** | **Code-CAD**（用代码写几何，可版本控制）/ **AI 自然语言建模**（text-to-CAD）/ **MCP 直连 CAD**（AI 客户端操作 CAD 宿主） |
| 4 | ★ **头号可用件是 `gumyr/build123d`（Apache-2.0）与 `neka-nat/freecad-mcp`（MIT）** | build123d 3,423★ 是 Python 参数化建模库，**许可宽松、可移植**；freecad-mcp 2,869★ 让 AI 客户端直连 FreeCAD。两者分别补「写」与「改」 |
| 5 | **FreeCAD 是这一侧的「主宿主」，但许可为 LGPL-2.1** | FreeCAD 本体 34,306★ / **LGPL-2.1** → **只作独立进程调用**；其 AI 扩展 `freecad-ai`（LGPL-2.1）、CFD 扩展 `CfdOF`（LGPL-3.0）同族，边界一致 |
| 6 | ★ **本库此前缺的「PCB ↔ 结构」那一段，现在有件了** | `easyw/kicadStepUpMod`（693★）把 KiCad 板子几何搬进 FreeCAD（**ECAD→MCAD**），配合 `earthtojake/step.parts`（12,000+ 开源 **STEP** 元件）——**这正是「板子 + 外壳」一体项目的刚需**（详见 §五） |
| 7 | **`CadQuery` 的许可在 GitHub API 上为 `NOASSERTION`，与本库既有记录（Apache-2.0）并不矛盾但需注意** | 仓库根 `LICENSE` 为 **Apache-2.0 全文**（含自定义前言，故 GitHub 未自动识别）；**引用时以「许可 API 未识别 → 移植前复核」为准**，不因「本库早前记过 Apache-2.0」就免核 |

---

## 二、核查口径

### 2.1 三分类判据

| 判定 | 含义 | 处置 |
|---|---|---|
| ✅ 已有 | 本库有等价或更强的文档 | 引用即可，**不新建** |
| ➕ 增量 | 本库确无，且能直接用于本项目 | 列入补充候选，排优先级 |
| ❌ 不可用 | 与项目范围界定冲突 / 数值错误 / 来源过时 | 记入本文并标注正确口径 |

### 2.2 ★ 收录门槛与边界（防重复、防错配）

> **收录门槛**：清单本身不构成收录理由；**能回答「哪一件现在就能装 / 许可能不能用 / 它替我省掉哪一步人工」的，才进库。**

| 相邻文档 | 与本文的分工 |
|---|---|
| [02-空间搭建](../02-空间搭建/)（38 篇） | 全部是**建筑 / 空间结构**；本文**不涉**，避免与空间规划混淆 |
| [开源软件工具链清单](../03-设备与工具/开源软件工具链清单.md) | 该篇是「全链软件**选型表**」（CAD/CAM/切片/EDA 各一行）；本文是「**机械结构设计这一支**的 AI 化进展与可用件核查」 |
| [免费3D素材源清单-开源库与授权判据](免费3D素材源清单-开源库与授权判据.md) | 该篇管**素材从哪来、能不能商用**（含工程 CAD 库 GrabCAD/TraceParts 等）；本文管**建模工具与技能** |
| 姊妹篇 [AI辅助PCB设计与EDA](AI辅助PCB设计与EDA-开源资源与技能包核查.md) | 板子那侧；两篇在 §五「桥接」处合龙 |

---

## 三、技术进展：三条路线

| 路线 | 原理 | 代表件（本文实证） | 适合场景 |
|---|---|---|---|
| **Code-CAD（代码写几何）** | 用 **Python / 声明式语言**描述实体，天然可版本控制、可参数化改型、可批量生成 | `gumyr/build123d`、`CadQuery/cadquery`、`openscad/openscad`、`Fluid-CAD/FluidCAD` | 参数化零件、系列化改型、可复现的建模脚本 |
| **AI 自然语言建模（text-to-CAD）** | 自然语言 / 图片 → CAD 实体；或 Agent 装「CAD 技能」后建模 | `earthtojake/text-to-cad`、`Adam-CAD/CADAM`、`KittyCAD/modeling-app`、`Pan-Chera/Multi-Agent-CAD`、`ghbalf/freecad-ai` | 概念阶段快速起形体；把「说需求」变成「出模型」 |
| **MCP 直连 CAD** | CAD 侧起 MCP 服务，AI 客户端**直接读写模型/装配**、执行脚本 | `neka-nat/freecad-mcp`（FreeCAD） | 对话式改模型、批量脚本化操作 |

> ★ 与 PCB 侧的对照：**PCB 侧的「审图」是读已完成的工程并挑错；结构侧的「text-to-CAD」是直接生成几何** —— 后者风险更高（几何错了看不出来），因此**「生成几何」之后必须接一段「确定性的几何/公差校验」**（本库在 PCB 篇把这段叫「判定式而非生成式」，此处同理）。

---

## 四、★ 实证清单（2026-10-15 `gh api` 定点核查）

### 4.1 A 档 —— 可直接用（MIT / Apache-2.0）

| 仓库 | ★ | 许可 | 最近推送 | 为什么是它 |
|---|---|---|---|---|
| **[gumyr/build123d](https://github.com/gumyr/build123d)** | 3,423 | **Apache-2.0** | 2026-10-15 | ★ 头号候选：**Python 参数化 CAD 库**（Code-CAD 主力），比 CadQuery 更现代的 API；许可宽松，可移植实现 |
| **[neka-nat/freecad-mcp](https://github.com/neka-nat/freecad-mcp)** | 2,869 | **MIT** | 2026-10-13 | ★ FreeCAD 的 **MCP 服务端**，让 AI 客户端直连 FreeCAD 建模/改模型（「改」这一环） |
| **[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)** | 20,505 | MIT | 2026-10-15 | **agent 技能库**（不是软件）：`cad` / `dxf` / `step-parts` / **`dfam-check`** / `gcode` / `sdf` / `urdf` 等。★ 本库《空间动线与摆放规划》已收录，此处明确其**结构设计侧**可直接复用 |
| **[earthtojake/step.parts](https://github.com/earthtojake/step.parts)** | 382 | MIT | 2026-06-13 | **12,000+ 开源 STEP 元件**模型，结构与装配的现成零件源 |
| **[partcad/partcad](https://github.com/partcad/partcad)** | 505 | **Apache-2.0** | 2026-10-14 | 硬件的「**包管理器 + 数字线程**」：把零件/装配当可版本化的产物管理（对应「变更追溯」需求） |
| **[KittyCAD/modeling-app](https://github.com/KittyCAD/modeling-app)** | 1,316 | MIT | 2026-10-15 | Zoo Design Studio 应用（text-to-CAD 路线的商业开源 app），可观摩其**交互式 text-to-CAD** 产品形态 |
| **[Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD)** | 1,034 | MIT | 2026-09-24 | 多智能体 text-to-CAD 框架（研究前沿，**读思路**用） |
| **[Fluid-CAD/FluidCAD](https://github.com/Fluid-CAD/FluidCAD)** | 631 | MIT | 2026-10-14 | JavaScript 参数化建模，浏览器可用（轻量参数化入口） |
| **[JWock82/Pynite](https://github.com/JWock82/Pynite)** | 758 | MIT | 2026-10-15 | ★ 3D 有限元库（Python）。**注意口径**：它是**土木/框架结构工程**FEM，**不是机械零件 FEM** —— 归 A 档但**用错了对象就是错配** |

### 4.2 B 档 —— 条件可用（许可或依赖需限定）

| 仓库 | ★ | 许可 | 最近推送 | 用途与限定 |
|---|---|---|---|---|
| [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD) | 34,306 | **LGPL-2.1** | 2026-10-15 | ★ 这一侧的**主宿主**（参数化 3D CAD + FEM/BIM/CAM 工作台）。**LGPL → 只作独立进程调用**；本库《开源软件工具链清单》§1.1 已收录 |
| [openscad/openscad](https://github.com/openscad/openscad) | 10,447 | **`NOASSERTION`**（实际为 GPL-2.0+） | 2026-10-15 | 「程序员的实体建模器」，脚本化实体最直观。**仓库级许可未被 API 识别 → 只读思路**，不复制其素材 |
| [LibreCAD/LibreCAD](https://github.com/LibreCAD/LibreCAD) | 6,484 | **`NOASSERTION`**（实际为 GPL-2.0） | 2026-10-15 | 2D CAD（可读写 DXF/DWG），出 2D 工程图的免费件。同上只读 |
| [CadQuery/cadquery](https://github.com/CadQuery/cadquery) | 5,938 | **`NOASSERTION`**（LICENSE 为 Apache-2.0 全文 + 自定义前言） | 2026-10-10 | Python 参数化 CAD（基于 OCCT）。★ **本库《开源软件工具链清单》§1.1 记其为 Apache-2.0，与 GitHub API 的 `NOASSERTION` 不一致** —— 二者不矛盾（文件确为 Apache-2.0），但**移植前须复核** |
| [Adam-CAD/CADAM](https://github.com/Adam-CAD/CADAM) | 5,267 | GPL-3.0 | 2026-10-15 | 开源 **text-to-CAD web 应用**。**GPL → 只作独立进程 / 独立服务使用**，不可并入自有闭源代码 |
| [solvespace/solvespace](https://github.com/solvespace/solvespace) | 4,197 | GPL-3.0 | 2026-10-15 | 轻量参数化 2D/3D CAD。**GPL → 独立进程**；本库《开源软件工具链清单》§1.1 已收录 |
| [ghbalf/freecad-ai](https://github.com/ghbalf/freecad-ai) | 566 | LGPL-2.1 | 2026-10-14 | FreeCAD 的**自然语言建模工作台**（说需求 → 出 3D 模型）。**LGPL → 独立进程** |
| [jaheyns/CfdOF](https://github.com/jaheyns/CfdOF) | 731 | LGPL-3.0 | 2026-10-07 | FreeCAD 上的 **CFD** 工作台（基于 OpenFOAM），结构件的**流体/散热仿真**扩展。**LGPL → 独立进程** |
| [earthtojake/step.parts](https://github.com/earthtojake/step.parts) | 382 | MIT | 2026-06-13 | 见 A 档（重复列出于此便于许可表对齐，正文以 A 档为准） |

### 4.3 C 档 —— 仅作参照

| 仓库 | ★ | 许可 | 最近推送 | 说明 |
|---|---|---|---|---|
| [xiangechen/chili3d](https://github.com/xiangechen/chili3d) | 4,910 | **AGPL-3.0** | 2026-10-09 | 纯浏览器 3D CAD。★ **AGPL → 只可内部运行取结果**，不可作为对外网络服务 |
| [hannobraun/fornjot](https://github.com/hannobraun/fornjot) | 2,554 | `NOASSERTION` | 2026-06-19 | Rust 写的 B-rep 内核，**早期阶段**（README 自述），只读思路 |
| [CADmium-Co/CADmium](https://github.com/CADmium-Co/CADmium) | 1,637 | `NOASSERTION` | 2025-09-05 | 浏览器 CAD，**已近 13 个月未推送**，参照 |
| [realthunder/FreeCAD_assembly3](https://github.com/realthunder/FreeCAD_assembly3) | 907 | GPL-3.0 | 2025-11-08 | FreeCAD 下一代**装配**工作台（实验性）。**GPL → 独立进程**；装配是机械结构的关键环，值得跟踪 |
| [m2n037/awesome-mecheng](https://github.com/m2n037/awesome-mecheng) | 1,721 | GPL-3.0 | **2024-09-24** | 机械工程资源清单。★ **GPL → 只做外链，不搬内容**；且**已 2 年多未更新** |
| [FreeCAD/FreeCAD-library](https://github.com/FreeCAD/FreeCAD-library) | 2,010 | `NOASSERTION` | 2026-10-07 | FreeCAD 零件库（**极其庞大**，README 自警「下载慢、易卡」），按需取用、不作全量依赖 |

### 4.4 许可纪律（逐条对照）

| 许可类型 | 本库允许的动作 | 本文涉及 |
|---|---|---|
| MIT / Apache-2.0 | 可移植实现、可改写、可并入自有工程 | build123d、freecad-mcp、text-to-cad、step.parts、partcad、modeling-app、Multi-Agent-CAD、FluidCAD、Pynite |
| **LGPL-2.1 / LGPL-3.0** | **只作独立进程调用**；不得静态链接进自有代码 | FreeCAD、freecad-ai、CfdOF |
| GPL-3.0 | 同上，独立进程；自身代码不被传染 | CADAM、solvespace、FreeCAD_assembly3、awesome-mecheng |
| **AGPL-3.0** | **只可内部运行取结果**，不可作对外网络服务 | chili3d |
| `NOASSERTION` / 无 LICENSE | **只读思路**，不复制素材、不依赖 | OpenSCAD、LibreCAD、CadQuery、fornjot、CADmium、FreeCAD-library |

> ★ 本库为 **CC BY 4.0（含商用）**：含 `NC` / `SA` 的第三方材料**一律只做「原理借鉴 + 外链」，不复制素材**；第三方受版权材料只摘录、不整段转载。

---

## 五、★ PCB ↔ 结构 桥接（本文独有增量）

> 「板子 + 外壳」是硬件项目最常被两套工具链**撕成两半**的地方：EDA 里一块、CAD 里一块，改一处另一处不动。下面四件把这条缝焊上。

| 环节 | 件 | ★ | 许可 | 用途 |
|---|---|---|---|---|
| **板子几何 → 结构模型** | [easyw/kicadStepUpMod](https://github.com/easyw/kicadStepUpMod) | 693 | **无 LICENSE 文件** | ★ ECAD→MCAD：把 KiCad 板子与元件**几何**带进 FreeCAD，做干涉检查、画外壳。**因无许可文件 → 只作独立进程参照，不作依赖** |
| **标准件 / 元件 3D 模型** | [earthtojake/step.parts](https://github.com/earthtojake/step.parts)（12,000+ STEP）／ [FreeCAD/FreeCAD-library](https://github.com/FreeCAD/FreeCAD-library) | 382 / 2,010 | MIT / `NOASSERTION` | 结构件、连接件、对接件的现成模型源 |
| **可制造性校验** | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) 的 **`dfam-check`** 技能 | 20,505 | MIT | ★ 把「**输出校验结论而非输出图形**」封装成技能，正是本库「判定式」纪律在结构侧的落地范本 |
| **装配与版本（数字线程）** | [partcad/partcad](https://github.com/partcad/partcad) | 505 | Apache-2.0 | 把零件/装配当**可版本化产物**管理，对应「改了板子，外壳版本要跟着走」 |

> ★ **一条纪律**：**板子与外壳不允许各维护一套几何** —— 以 EDA 为单一几何来源，用 `kicadStepUp` 单向导入 CAD，改板后**重跑导入**（本库对应纪律：单一发布面 / 图与链接同批换）。

---

## 六、★ 技能市场检索（英文技术专名，2026-10-15）

> **纪律**：专业技能市场的检索是**描述文本的模糊匹配**，**中文职能词（「结构」「零件」「外壳」）会假阴性**；专业技能的描述里必然含**罗马字技术专名**。本轮一律用英文技术名检索。

| 检索词 | 命中 | 相关性 |
|---|---|---|
| `freecad skills` | 3 | 全部 ≤2★（`SalvatoreMastrangelo/freecad_skill` 1★「FreeCAD skill for Claude Code」等）—— **基本空白** |
| `cad skills agent` | **0** | **0 命中** |
| `step cad agent` | **0** | **0 命中** |
| `kicad skills` | 8 | 对照项：仅 `aklofas/kicad-happy`（1,394★）成规模，其余 1–23★（见 PCB 篇 §六） |

> **结论**：**机械结构 / CAD 方向技能市场尚无规模件** —— 只能走 **GitHub 仓库直装**（如 `neka-nat/freecad-mcp` 走 MCP 通道）**或自研**；`text-to-cad` 是唯一成规模的**agent 技能库**（20,505★），其 `dfam-check` 可直接借用。
> **一条限制（照实记）**：本机 `skill-installer` 的**策展列表接口本次返回 HTTP 403**（未取到官方 `.curated` 列表），故上表以 **GitHub 主题/关键词检索**为准，**策展市场一栏待补**。

---

## 七、Skill 适配结论（与本机既有技能对账）

| 本机既有技能（`~/.workbuddy/skills/`） | 与本文的关系 |
|---|---|
| `blender-headless-modeling`、`sketchup-mcp-modeling` | **AI 操控 3D 建模软件**的技能，与本文「几何」层部分重叠；但**它们是场景/建筑几何，不是参数化零件/公差/装配** |
| `render-texture-regularity-audit`、`visual-art-direction-audit` | 视觉呈现层，与结构**工程正确性**无关 |
| `mcp-registry-publish` | 若自研结构侧 MCP，可用它发布 |
| `external-knowledge-pack-audit` | 本文即按该技能方法产出 |

**真缺口（本机确无）**：**参数化结构设计 / 出工程图（2D 引用图）/ 公差链校核** 这一层，本机**无技能**。→ **建议**：优先装/接 `neka-nat/freecad-mcp`（MIT）走 MCP 通道；**不要**为「生成几何」自研技能，把力气花在**几何/公差的确定性校验**上（对应 `dfam-check` 的形态）。

---

## 八、★ 不纳入清单（逐项写明理由，防止日后被翻案）

| 不纳入项 | 理由 |
|---|---|
| **建筑 / 空间结构**相关任何内容 | 已属 [02-空间搭建](../02-空间搭建/)（38 篇）；放进本文会造成「拿建筑规范校机械公差」的错配 |
| **把 Pynite 当「机械结构 FEM」用** | 它是**土木/框架结构**有限元；对象不同，**不可错配**（本文只作 A 档参考件，附口径警告） |
| **`kicadStepUpMod` 作依赖** | **仓库无 LICENSE 文件**；只可作独立进程**参照**，不得并入自有工程分发 |
| **`awesome-mecheng` 正文搬录** | GPL-3.0 → **只外链**；且 2024-09 后未更新，时效已弱 |
| **AGPL 件（chili3d 等）作对外服务** | AGPL 意味着**只要对外提供网络服务就须开放全部源码**；本库只用其**内部取结果** |
| **把 OpenSCAD / LibreCAD / CadQuery 的 `NOASSERTION` 当 MIT 用** | 许可 API 未识别 ≠ 宽松；**移植前必须看仓库根 LICENSE 原文** |
| **`FreeCAD-library` 全量入库** | 库极大（README 自警会拖慢 addons manager）；**按需取用**，不作全量依赖 |
| **任何第三方受版权结构件图纸 / 整段文档转载** | 本库为 CC BY 4.0；第三方材料只摘录 + 外链 |

---

## 九、落地建议（P0 / P1 / P2）

| 优先级 | 动作 | 不要做什么 |
|---|---|---|
| **P0** | 做「板子 + 外壳」项目：**FreeCAD（LGPL，独立进程）为主宿主**，`kicadStepUp` 单向导入板子几何，`build123d`（Apache）写参数化结构脚本 | **不要**板子和外壳各维护一套几何（见 §五 纪律） |
| **P0** | 要让 AI 直连 CAD：装 **`neka-nat/freecad-mcp`（MIT）**走 MCP 通道 | **不要**为「生成几何」自研技能 |
| **P1** | 参数化零件 / 系列化改型：用 **build123d**（Apache-2.0，可移植）写脚本，纳入版本控制 | **不要**用 `NOASSERTION` 的 CadQuery 直接并入分发（先复核 LICENSE） |
| **P1** | 结构与装配的**版本追溯**：评估 **partcad**（Apache-2.0）管理零件/装配快照 | **不要**把设计件当「文档」散放（会丢失版本因果） |
| **P1** | 结构**仿真**：散热/流体用 FreeCAD 的 **CfdOF**（LGPL，独立进程） | ⚠️ **不要**用 Pynite 做机械零件强度校核（它是土木框架 FEM） |
| **P2** | 把 `text-to-cad` 的 **`dfam-check`** 思路抄成自研的**几何/公差确定性校验**清单 | **不要**只接「生成几何」而不接「校验几何」 |

---

## 相关文档

| 文档 | 关系 |
|---|---|
| [AI辅助PCB设计与EDA-开源资源与技能包核查.md](AI辅助PCB设计与EDA-开源资源与技能包核查.md) | ★ 姊妹篇：板子那侧；两篇在 §五「PCB↔结构桥接」合龙 |
| [开源软件工具链清单](../03-设备与工具/开源软件工具链清单.md) | 全链软件选型表；本文补其 CAD 一支的 **AI 化**延伸 |
| [免费3D素材源清单-开源库与授权判据.md](免费3D素材源清单-开源库与授权判据.md) | 素材/零件库的**授权判据**（工程 CAD 库 GrabCAD/TraceParts 等） |
| [数字制造工艺全景-专题补充](../03-设备与工具/数字制造工艺全景-专题补充.md) | 设计件之后的工艺链（3D 打印 / CNC / 激光） |
| [AI操控Blender工具生态-MCP与插件资源调研.md](AI操控Blender工具生态-MCP与插件资源调研.md) | 同形态对照：AI 操控专业建模软件的 MCP / 插件生态 |
| [空间动线与摆放规划-外部知识包核查与开源工具适配.md](空间动线与摆放规划-外部知识包核查与开源工具适配.md) | 建筑/空间结构侧（**勿与本文混用**）；其 §7 已收录 `text-to-cad` |

## 主要来源（均为 2026-10-15 经 `gh api` 定点核查）

- 仓库元数据（星标 / 许可 / 最近推送）：GitHub REST API `repos/<owner>/<repo>`
- 仓库检索：GitHub 主题检索（`cad` / `mechanical-engineering` / `ai-skills`）与关键词检索（`freecad` / `freecad skills` / `cad skills agent`）
- 许可原文核查：`CadQuery/cadquery` 仓库根 `LICENSE`（确认含 Apache-2.0 全文 + 自定义前言）；`openscad/openscad`、`LibreCAD/LibreCAD`、`FreeCAD/FreeCAD`、`easyw/kicadStepUpMod` 的 API 返回值
- 官方仓库自述：FreeCAD（参数化 3D CAD + FEM/BIM/CAM）、OpenSCAD（程序员实体建模）、CadQuery（OCCT 参数化脚本）、build123d（Python CAD 库）、freecad-mcp（MCP 服务端）

## 变更记录

| 版本 | 日期 | 变更 |
|---|---|---|
| v1 | 2026-10-15 | 首版：三条路线收敛 + A/B/C 实证清单（24 项）+ PCB↔结构桥接四件 + 技能市场英文专名检索 + 不纳入清单 + P0/P1/P2 |
