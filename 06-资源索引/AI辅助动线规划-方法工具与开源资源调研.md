---
title: "AI 辅助动线规划：方法、工具与开源资源调研"
type: 调研
scope: 通用
source: "GitHub/arXiv/Sage/UCL Space Syntax/OpenReview 等全球检索"
date: 2026-09-20
tags: [动线规划, 空间句法, 人流模拟, 寻路, 疏散, 开源工具, AI, 可达性]
---

# AI 辅助动线规划：方法、工具与开源资源调研

> 调研时间：2026-08-30 ｜ 目的：补齐知识库"AI 动线规划专业技能"缺口
> 动线（circulation / pathfinding / wayfinding）是创客空间规划中相对专业的环节；现有 `AI辅助创客空间规划-方法与工具库.md` 已把"动线效率"列为 AI 邻接优化目标之一，但缺**量化评估与验证动线**的专业方法与工具。
> 本文给出三大方法体系 + 开源仓库清单 + 商业工具 + 学术文献 + 创客空间落地建议。
> **更新 v1.1（2026-09-20）**：补 depthmapX 落地要点（版本 / 许可 / macOS 安装 / 命令行，见 §3.1.1）、图型与尺度的选用纪律（见 §2.1）、**「方案模型 → DXF → VGA」接入路径**（见 §6.1）；文末新增变更记录。

---

## 一、动线规划问题定位

创客空间动线规划要回答三个问题：

| 追问 | 含义 | 对应指标/方法 |
|------|------|--------------|
| **可达性** | 各功能区是否方便到达、是否高效连通 | 空间句法：整合度/连接度/选择度 |
| **可理解性** | 初次到访者是否容易"识路"、直觉走到正确功能区 | 空间句法：可理解度；ABM 智能体识别行为 |
| **安全性** | 高峰/疏散时是否顺畅、有无瓶颈 | 人流模拟：拥堵热力图、疏散时间、瓶颈定位 |

---

## 二、三大方法体系

### 2.1 空间句法 Space Syntax（量化分析）

- **原理**：Bill Hillier（UCL Bartlett，1970s）用图论数学描述空间关系，揭示"空间布局如何影响人类行为"。["https://www.spacesyntax.online/zh-hans/applying-space-syntax/building-methods/zh-hans-spatial-form-analysis/"]
- **核心指标**：连接度 Connectivity、整合度 Integration（越整合越易到达）、选择度 Choice（路径被选择的概率）、平均深度 Mean Depth、可理解度 Intelligibility。
- **Agent 分析**：释放虚拟"识路代理"，依据视线分析图选择下一目的地，模拟人流模式——直接用于检验动线是否"自然"。
- **适用**：评估创客空间布局是否让人"自然走到"该去的功能区（教学区→实训区→储物区→出口），发现"死区/孤岛功能区"。

**★ 六种图，指标归属不同——不能混用**（这是空间句法最容易被误用的一处）：

| 图型 | 适用尺度 | 主要指标 | 对本类空间（单层 400㎡ 级）的适用性 |
|---|---|---|---|
| **轴线图 Axial** | 城市 / 街区尺度（街道网络） | 整合度 Integration、连接度 Connectivity、选择度 Choice、平均深度 Mean Depth | ❌ 单层房间内**意义有限**，其阈值不可套用 |
| **线段图 Segment** | 城市 / 街区尺度 | 角度选择度 NACh、角度整合度 NAIn（Hillier et al. 2012） | ❌ 同上 |
| **凸空间图 Convex** | 建筑 / 小尺度 | 空间连接与拓扑深度 | ⚠️ 可用于房间级邻接，但表达力弱于 VGA |
| **★ 视域图 VGA** | **建筑 / 房间尺度（主用）** | 可视域面积与周长、视觉整合度、视觉平均深度、**可理解度 Intelligibility** | ✅ **单层空间应用此图** |
| **等视域 Isovist / 视域路径** | 建筑尺度 | 单点可视域多边形、移动中的视域变化 | ✅ 定点诊断遮挡与视线通廊 |
| **智能体 Agent** | 建筑尺度 | 门流量、路径分布 | ✅ 检验"人会不会这样走" |

> ★ **尺度纪律**：本库面向 400㎡ 级单层空间，**只用 VGA / Isovist / Agent**。轴线图与线段图是城市与街区尺度的工具——在单一房间内既难自动生成、指标的统计意义也会退化，**不可把城市尺度的"整合度"阈值搬来做布局结论**。

### 2.2 基于智能体的人流模拟 ABM（验证动线）

- **原理**：每个虚拟行人按简单规则行动（社交力模型 Social Force / 势场 / A* 寻路），个体简单规则涌现出整体人流模式。["https://abelvm.github.io/desire-paths/docs/faq.html"]
- **适用**：验证高峰时段拥堵点、疏散瓶颈、布局改动前后对比（如"把储物区移到门口后疏散时间变化"）。
- **成熟开源实现**：社交力模型（Helbing）系——libpedsim / JuPedSim；ABM 涌现路线——Desire Paths。

### 2.3 AI 生成式动线（LLM + 寻路算法）

- **原理**：LLM/生成式 Agent 做宏观需求理解与决策 + A*/Dijkstra 等确定性算法做几何寻路 + 生成式模型做可视化。
- **代表**：TravelAgent（生成式 Agent 在建成环境导航）、LLM-Powered 车站密集人流路径规划、CityGPT 城市人流模拟。
- **适用**：自动生成建议动线、解释"为什么这样走"、把动线约束（噪声区/危险区隔离）融入 LLM 规划提示词。

---

## 三、开源仓库清单（可直接选用）

### 3.1 空间句法分析（量化动线）

| 仓库 | 能力 | 适用场景 | 备注 |
|------|------|---------|------|
| **[depthmapX](https://github.com/SpaceGroupUCL/depthmapX)** | 空间句法可视化空间网络分析：**VGA 视域图**、等视域、Agent 识路、轴向/线段图；另附**官方命令行 `depthmapXcli`**（官方明示可嵌入 R / Python，便于进自动化管线） | 平面图的空间可达性**与可视性**评估；可脚本化批量跑多个方案 | UCL Bartlett 官方开源，**空间句法标准工具**。⚠️ 引用其指标数字**必须标注版本号**（见 §3.1.1） |
| **[Space Syntax Toolkit](https://plugins.qgis.org/plugins/esstoolkit/)** | QGIS 插件，depthmapX 前端：GIS+空间网络分析+行人流分析 | 结合地图/场地数据做区域级动线 | UCL 开发，免费 |
| **[SpaceSyntaxNova](https://github.com/catsyntax/SpaceSyntaxNova/)** | 空间句法 + AI 集成：可见性/连接性/结构效率 | 平面图级分析，含 AI 集成 | 学术用途免费 |
| **[PlanX](https://github.com/YusufEminoglu/PlanX)** | 无需 axial map 的中心性分析：度/紧密度/介数，OD 可达性矩阵 | 需要精确可达性计算时 | 纯 Python |
| **[SS_Jgraph](https://github.com/HdMiii/SS_Jgraph)** | QGIS 空间句法 J-Graph 分析（拓扑深度） | 从某点（如入口）到各区的拓扑距离 | 轻量 |

#### 3.1.1 ★ depthmapX 落地要点（2026-09-20 核实）

| 项 | 事实 | 对使用的影响 |
|---|---|---|
| **许可** | **GPLv3**；且**仅 README 文本声明，仓库根没有 `LICENSE` 文件**（自动化许可识别工具读不到，会判为"无许可"） | 本库为 CC BY 4.0 公开仓 → **只写方法与指标定义，不搬运其源码或文档原文**；用它的分析结果出图、出结论**不触发 copyleft** |
| **维护状态** | 2012 年建仓；**v0.8.0（2020-11-08）之后停更近 6 年**，2026-07-27 发 v0.9.0、**2026-08-09 发 v0.9.1** | **已复活且接入 CI**；不要凭"看起来很久没更新"的印象把它排除 |
| **交付形态** | 四平台（Linux AppImage / macOS arm64 / macOS intel / Win64）**原生 GUI 与命令行分别发布** | **有 CLI → 可进自动化管线**：批量跑多方案不必开图形界面 |
| **★ 版本敏感** | v0.9.1 发布说明明确警告：`Integration [P-value]` 与部分 `RA [Penn]` **结果与早前版本不同**（旧版用 D-value 公式算 P-value、Penn 归一化取了错误的最大深度） | **引用任何指标数字都必须写明 depthmapX 版本号**；**跨版本的数字不可比** |
| **macOS 安装** | 应用**未做 Apple 开发者签名**（并非文件损坏），首次启动会被系统拦下；arm64 与 intel 是两个独立包，装错无法运行 | 首次放行：`xattr -dr com.apple.quarantine /Applications/depthmapX.app`，或「系统设置 → 隐私与安全性 → 仍要打开」 |
| **输入格式** | 可直接导入纯几何（平面图 / 道路中心线）再转成空间网络；支持 **DXF**（含深层级块）、MIF/MID；另有 SalaScript 脚本与属性表公式可做二次计算 | 关键是**先把方案导成 DXF**——见 §6.1 |

> ⚠️ **不要走「depthmapX + QGIS 插件」这条路**：Space Syntax Toolkit 这个 QGIS 插件依赖 **`depthmapXnet 0.35`** —— 一个独立的旧二进制，托管在个人站点而非官方发布页；插件本身最后更新于 **2023-09**，与当前 0.9.x 并非同一条线。**直接用 depthmapX 0.9.x 本体（GUI 或 CLI）即可。**

### 3.2 人流/疏散模拟（验证动线）

| 仓库 | 能力 | 适用场景 | 备注 |
|------|------|---------|------|
| **[Desire Paths](https://github.com/AbelVM/desire-paths)** | ABM 行人流模拟：放置起点/终点，涌现"踩出来的路"（摩擦场）| **直观理解动线**：哪些区域会被自然踩出路径、哪些是死角 | 交互式，基于 CEUS 2025 研究，**最易上手** |
| **[JuPedSim Web](https://github.com/PedestrianDynamics/jupedsim-web-community/wiki)** | 网页端行人拥挤模拟：DXF/**IFC(BIM) 导入**、5 种行人模型、逃生分析 | 从 CAD/BIM 直接建人流模型 | 浏览器运行，德国尤利希研究中心 |
| **[libpedsim / Pedestrian Simulator](https://github.com/srl-freiburg)** | 社交力模型（Helbing SFM）2D 行人模拟 | 机器人与行人共存的拥挤场景（机器人导航研究）| 弗莱堡大学 |
| **[T.R.A.G.I.C](https://github.com/sankhya007/T.R.A.G.I.C)** | 平面图→U-Net 提取可走空间→4 种算法疏散模拟→**分数+热力图+建议**（如"某走廊拥堵"）| 创客空间疏散/安全评估，**自动出建议** | 输入只需平面图图片 |
| **[Emergency Evacuation (NetLogo)](https://github.com/Sidharthkris/emergency-evacuation-simulation)** | 大学教室疏散 ABM：布局如何影响瓶颈、恐慌传染 | 教学型疏散分析 | NetLogo，易改 |
| **[Dynamic Crowd](https://github.com/Subhronilmukhopadhyay/Dynamic-Crowd-Simulation-with-Realistic-Behavior-Modeling)** | GNN+Transformer 预测行人轨迹 + PPO 智能体导航 | 密集人流下的 AI 导航研究 | 学术型 |

### 3.3 多智能体寻路（MAPF，扩展）

| 仓库 | 能力 | 备注 |
|------|------|------|
| **[SMART](https://github.com/smart-mapf/smart)** | 多智能体路径规划真实测试床（物理引擎+执行监控，千级机器人）| MAPF 算法对比；面向机器人/AGV |

---

## 四、商业工具（成熟度高，需购买）

| 工具 | 能力 | 适用 |
|------|------|------|
| **Autodesk MassMotion**（Oasys）| 3D 行人模拟：BIM 导入（.fbx/.ifc/.dwg）、疏散/高峰/运营场景评估 | 大型创客空间/公共空间正式评估 |
| **Thunderhead Pathfinder** | Agent-based 疏散模拟（消防工程师标准工具）| 疏散合规验证 |
| **AnyLogic（Pedestrian Library）** | 社交力模型行人库，2D/3D，密度热力图，可二次开发 | 需定制建模的场景 |
| **LEGION / BuildingEXODUS / Vissim 行人模块** | 行人流/疏散评估 | 交通枢纽级 |
| **SimWalk / FDS+Evac** | 行人/CFD 耦合疏散 | 火灾耦合 |

> 商业工具对比综述见 IIETA《State-of-the-Art Review of Evacuation Simulation Tools》。["https://www.iieta.org/journals/ijsse/paper/10.18280/ijsse.160310"]

---

## 五、学术文献（前沿与方法依据）

| 文献 | 方向 | 要点 |
|------|------|------|
| **TravelAgent**（Environment & Planning B, 2025）| 生成式 Agent 在建成环境导航 | 200 次模拟/3364 决策点/约 80% 任务完成率，覆盖目标导向导航到自由探索，可评估不同用户如何体验空间 ["https://journals.sagepub.com/doi/10.1177/23998083251360458"] |
| **LLM-Powered Agent for Dense Pedestrian Flow Path Planning**（OpenReview 2025）| LLM+人流路径规划 | 势场人群模拟 + LLM 宏观决策 + 车站知识图谱（StationKG）；北京西站高保真验证 ["https://openreview.net/forum?id=KFUY3bhsuU"] |
| **CAMS: CityGPT-Powered Agentic Framework**（arXiv 2506.13599）| 城市人流模拟 | 语言化城市基础模型 + 智能体框架模拟城市移动性 ["https://arxiv.org/pdf/2506.13599v1.pdf"] |
| **Space Syntax + NetLogo 集成**（SAGE 2025）| 空间句法与 ABM 结合 | 在 NetLogo 复现 depthmapX 分析，扩展空间认知分析 ["https://journals.sagepub.com/doi/10.1177/14780771251352967"] |
| **Agent-based Pathfinding for Indoor Fire Evacuation**（系统仿真学报）| 火灾疏散寻路 | 动态 A* + 热辐射/烟雾/CO 动态代价网络，实时重规划 ["https://www.china-simulation.com/EN/abstract/abstract3856.shtml"] |
| **Integrating AI for Sustainable Architectural Space Optimization**（Nature Sci Rep 2026）| CNN+GNN+RL 空间优化 | 人流/交通/环境实时数据驱动布局优化 ["https://www.nature.com/articles/s41598-026-56501-w_reference.pdf"] |
| **Spatial cognition and emotion simulation**（Taylor & Francis 2026）| 认知-情绪智能体 | 3D 体素编码（层高/色彩/节点），迭代寻路模拟空间认知 ["https://www.tandfonline.com/doi/full/10.1080/12265934.2026.2641648"] |

---

## 六、对创客空间的可操作建议

**推荐组合工作流（零成本起步 → 按需升级）**：

```
①空间句法评估 → ②ABM人流验证 → ③LLM动线优化 → ④（可选）商业疏散工具
depthmapX+QGIS  Desire Paths/JuPedSim  提示词工作流      MassMotion/Pathfinder
（免费）          （免费）              （免费）          （付费，正式报建/验收）
```

| 步骤 | 工具 | 成本 | 输出 |
|------|------|------|------|
| 1. 现状可达性评估 | depthmapX + QGIS | 免费 | 整合度/连接度热力图，发现"孤岛功能区" |
| 2. 自然动线模拟 | Desire Paths | 免费 | 涌现路径图：哪些区域自然通行、哪些死角 |
| 3. 高峰/疏散验证 | JuPedSim / T.R.A.G.I.C | 免费 | 拥堵热力图、疏散时间、瓶颈位置 |
| 4. AI 动线优化建议 | LLM（含本库提示词模板）| 免费 | 布局调整建议 + 理由（噪声/危险区隔离）|
| 5. 正式疏散合规（如需）| Pathfinder / MassMotion | 付费 | 合规报告 |

**要点**：
- **轻量起步首选 depthmapX + Desire Paths**：一个量化可达性、一个直观看自然动线，均免费且上手快。
- **疏散安全强相关**：创客空间含机器人/高压电池/激光等危险源，动线应天然"参观动线与操作区分离"——可用 ABM 验证是否做到。
- **LLM 的角色**：把动线约束（噪声区、危险区、参观动线分离、器材搬运路径）写进规划提示词，让 AI 生成方案时自带动线逻辑，再用 ABM 验证。

---

### 6.1 ★ 落地实例：把方案模型接进 depthmapX（VGA 路线）

空间句法落地的门槛**不在软件，而在"把方案变成它认的输入"**。若项目已做到"几何数据源与落位坐标数据源分离"（见本库 [AI空间方案工作流-九阶段端到端方法论.md](../02-空间搭建/AI空间方案工作流-九阶段端到端方法论.md) 的"单一数据源"纪律），这一步可以脚本化：

| 步 | 做什么 | 关键点 |
|---|---|---|
| 1 | **几何 → DXF**：把墙体、柱、门洞轮廓按**真实坐标**写成 DXF 图元（LINE / LWPOLYLINE） | 用几何数据源生成，**不要手描**；**门洞保持开敞**（不要画门扇），否则 VGA 会把门口当成墙 |
| 2 | **设备 → DXF**：把每个已落位设备的**本体外轮廓**按坐标写进**同一张 DXF** | ★ **这一步才是关键**：VGA 算的是"被遮挡之后的视野"。只画墙不画设备，结果毫无意义。设备须选**对应状态**的方案（常驻态 / 满载并发态分开跑） |
| 3 | 导入 depthmapX → 生成 **VGA 网格** | 网格间距决定精度与耗时，建议先粗后细；**参数必须记录** |
| 4 | 跑 **Visual Integration / Visual Mean Depth / Intelligibility**，以及定点 **Isovist** | 得到视觉整合度热力图与视线瓶颈 |
| 5 | 跑 **Agent 分析**，起点设在主入口 | 看门流量分布与路径，检验"人是不是这么走" |
| 6 | **把热力图叠回方案图**，作为设计文档附图 | 与"通道净宽"结论**并列呈现**，不替代 |

**★ 它能回答什么、不能回答什么**

| 手段 | 回答的问题 |
|---|---|
| 关系图（REL 关系图） | 谁**应该**挨着谁（关系） |
| 通道净宽探针 | 走**得过去、走得下**吗（几何） |
| **VGA / Isovist / Agent** | 走**得对不对、看不看得见**（拓扑与视觉） |

**输出怎么变成判据**：把方案里那些**用文字写死的连通性与公共性约束**——例如"主公共通道不得被设备阻断""入口前厅段必须保持公共性"——从形容词变成**沿通道的视觉整合度曲线**：被设备遮挡处曲线会掉，**掉几处、掉多少一眼可数**。这正是纯几何净宽查不出来的那一层。

**边界**：① 结论依赖 DXF 几何质量与网格精度，**发布结论时必须同时声明网格参数与 depthmapX 版本号**；② 指标只用于**同一项目不同方案之间的相对比较**，**不要跨项目套阈值**；③ 若 VGA 结论与通道净宽完全一致，它就是冗余的——**它的价值只在能推翻或补充既有判据时体现**。

## 七、风险与边界

1. **空间句法指标≠结论**：整合度高不代表"好用"，需结合功能与人的需求解读，避免唯指标论。
2. **ABM 校准困难**：社交力模型参数（期望速度/行人密度）需实测校准，否则结果仅供参考。
3. **LLM 动线仍处前沿**：TravelAgent/LLM-Powered 未产品化，当前实用价值主要在"生成建议+解释"，不替代确定性模拟。
4. **商业工具门槛**：MassMotion/Pathfinder 需正版授权与学习成本，仅在正式疏散合规/大型项目才值得投入。

5. **★ 指标版本敏感**：同一份数据在不同 depthmapX 版本下可能给出不同数字（v0.9.1 即修正了 P-value 与 Penn 归一化）。**引用指标必须同时给出软件版本号与网格参数**，否则结论不可复现。
6. **★ 尺度失配**：轴线图 / 线段图属城市与街区尺度。把城市尺度的"高整合度"阈值直接套到单层房间上，会得出看似精确、实则无意义的结论。单层空间**只用 VGA / Isovist / Agent**。

## 相关文档

- [../02-空间搭建/AI辅助创客空间规划-方法与工具库.md](../02-空间搭建/AI辅助创客空间规划-方法与工具库.md)（AI 邻接优化中的"动线效率"目标）
- [../02-空间搭建/AI规划方法论-实战验证与提示词模板.md](../02-空间搭建/AI规划方法论-实战验证与提示词模板.md)
- [../04-运营与管理/实训室安全与应急预案专项.md](../04-运营与管理/实训室安全与应急预案专项.md)（动线与疏散的对接）
- [../06-资源索引/AI辅助建筑规划设计-全球调研与知识库适配.md](../06-资源索引/AI辅助建筑规划设计-全球调研与知识库适配.md)

- [../02-空间搭建/SLP系统布置设计-专题补充.md](../02-空间搭建/SLP系统布置设计-专题补充.md)（关系导向的布局方法；与本文形成「关系 → 几何 → 视觉」三层互补）
- [AI空间规划方案图绘制-确定性方法与校验清单.md](AI空间规划方案图绘制-确定性方法与校验清单.md)（方案图坐标驱动绘制；VGA 热力图叠图的前置）
- [空间动线与摆放规划-外部知识包核查与开源工具适配.md](空间动线与摆放规划-外部知识包核查与开源工具适配.md)（**本文的"落地件"补充**：§6.1 第 1–2 步「几何/设备 → DXF」缺的那一件 = `ezdxf`；另含 4 处规范口径纠正与 30 项开源资源实证清单）

## 主要来源

- UCL Space Syntax：[spacesyntax.online](https://www.spacesyntax.online/zh-hans/applying-space-syntax/building-methods/zh-hans-spatial-form-analysis/)、[depthmapX 官网](https://www.ucl.ac.uk/bartlett/depthmapx-visual-and-spatial-network-analysis-software)、[Space Syntax Toolkit QGIS](https://plugins.qgis.org/plugins/esstoolkit/)
- 开源仓库：[desire-paths](https://github.com/AbelVM/desire-paths)、[JuPedSim](https://github.com/PedestrianDynamics/jupedsim-web-community/wiki)、[T.R.A.G.I.C](https://github.com/sankhya007/T.R.A.G.I.C)、[depthmapX](https://github.com/SpaceGroupUCL/depthmapX)、[SpaceSyntaxNova](https://github.com/catsyntax/SpaceSyntaxNova/)、[PlanX](https://github.com/YusufEminoglu/PlanX)
- 商业工具：[MassMotion](https://www.oasys-software.com/products/pedestrian-simulation-software/massmotion/)、[AnyLogic](https://www.anylogic.kr/features/libraries/pedestrian-library/)、[疏散工具综述（IIETA）](https://www.iieta.org/journals/ijsse/paper/10.18280/ijsse.160310)
- 学术：[TravelAgent（SAGE）](https://journals.sagepub.com/doi/10.1177/23998083251360458)、[LLM-Powered 车站人流（OpenReview）](https://openreview.net/forum?id=KFUY3bhsuU)、[CAMS（arXiv）](https://arxiv.org/pdf/2506.13599v1.pdf)、[火灾疏散寻路（系统仿真学报）](https://www.china-simulation.com/EN/abstract/abstract3856.shtml)、[Nature Sci Rep 空间优化](https://www.nature.com/articles/s41598-026-56501-w_reference.pdf)

---

## 变更记录

| 版本 | 日期 | 变更 |
|---|---|---|
| v1.1 | 2026-09-20 | 新增 §3.1.1「depthmapX 落地要点」（许可 / 维护状态与版本 / 交付形态与命令行 / **版本敏感** / macOS 安装 / 输入格式，并排除已被弃用的 QGIS 插件路线）；§2.1 新增「六种图与指标归属」表及**尺度纪律**；新增 §6.1「把方案模型接进 depthmapX（VGA 路线）」六步接入路径与判据转化说明；§七 风险补 2 条（指标版本敏感 / 尺度失配）；补相关文档与交叉链接 |
| v1.0 | 2026-08-30 | 首次成文：三大方法体系 + 开源仓库清单 + 商业工具 + 学术文献 + 创客空间落地建议 |
