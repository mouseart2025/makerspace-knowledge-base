---
title: "AI 辅助动线规划：方法、工具与开源资源调研"
type: 调研
scope: 通用
source: "GitHub/arXiv/Sage/UCL Space Syntax/OpenReview 等全球检索"
date: 2026-08
tags: [动线规划, 空间句法, 人流模拟, 寻路, 疏散, 开源工具, AI, 可达性]
---

# AI 辅助动线规划：方法、工具与开源资源调研

> 调研时间：2026-08-30 ｜ 目的：补齐知识库"AI 动线规划专业技能"缺口
> 动线（circulation / pathfinding / wayfinding）是创客空间规划中相对专业的环节；现有 `AI辅助创客空间规划-方法与工具库.md` 已把"动线效率"列为 AI 邻接优化目标之一，但缺**量化评估与验证动线**的专业方法与工具。
> 本文给出三大方法体系 + 开源仓库清单 + 商业工具 + 学术文献 + 创客空间落地建议。

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
| **[depthmapX](https://github.com/SpaceGroupUCL/depthmapX)** | 空间句法可视化空间网络分析：连接度/整合度/选择度；Agent 识路分析 | 创客空间平面图的空间可达性评估 | UCL Bartlett 官方开源，**空间句法标准工具** |
| **[Space Syntax Toolkit](https://plugins.qgis.org/plugins/esstoolkit/)** | QGIS 插件，depthmapX 前端：GIS+空间网络分析+行人流分析 | 结合地图/场地数据做区域级动线 | UCL 开发，免费 |
| **[SpaceSyntaxNova](https://github.com/catsyntax/SpaceSyntaxNova/)** | 空间句法 + AI 集成：可见性/连接性/结构效率 | 平面图级分析，含 AI 集成 | 学术用途免费 |
| **[PlanX](https://github.com/YusufEminoglu/PlanX)** | 无需 axial map 的中心性分析：度/紧密度/介数，OD 可达性矩阵 | 需要精确可达性计算时 | 纯 Python |
| **[SS_Jgraph](https://github.com/HdMiii/SS_Jgraph)** | QGIS 空间句法 J-Graph 分析（拓扑深度） | 从某点（如入口）到各区的拓扑距离 | 轻量 |

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

## 七、风险与边界

1. **空间句法指标≠结论**：整合度高不代表"好用"，需结合功能与人的需求解读，避免唯指标论。
2. **ABM 校准困难**：社交力模型参数（期望速度/行人密度）需实测校准，否则结果仅供参考。
3. **LLM 动线仍处前沿**：TravelAgent/LLM-Powered 未产品化，当前实用价值主要在"生成建议+解释"，不替代确定性模拟。
4. **商业工具门槛**：MassMotion/Pathfinder 需正版授权与学习成本，仅在正式疏散合规/大型项目才值得投入。

## 相关文档

- [../02-空间搭建/AI辅助创客空间规划-方法与工具库.md](../02-空间搭建/AI辅助创客空间规划-方法与工具库.md)（AI 邻接优化中的"动线效率"目标）
- [../02-空间搭建/AI规划方法论-实战验证与提示词模板.md](../02-空间搭建/AI规划方法论-实战验证与提示词模板.md)
- [../04-运营与管理/实训室安全与应急预案专项.md](../04-运营与管理/实训室安全与应急预案专项.md)（动线与疏散的对接）
- [../06-资源索引/AI辅助建筑规划设计-全球调研与知识库适配.md](../06-资源索引/AI辅助建筑规划设计-全球调研与知识库适配.md)

## 主要来源

- UCL Space Syntax：[spacesyntax.online](https://www.spacesyntax.online/zh-hans/applying-space-syntax/building-methods/zh-hans-spatial-form-analysis/)、[depthmapX 官网](https://www.ucl.ac.uk/bartlett/depthmapx-visual-and-spatial-network-analysis-software)、[Space Syntax Toolkit QGIS](https://plugins.qgis.org/plugins/esstoolkit/)
- 开源仓库：[desire-paths](https://github.com/AbelVM/desire-paths)、[JuPedSim](https://github.com/PedestrianDynamics/jupedsim-web-community/wiki)、[T.R.A.G.I.C](https://github.com/sankhya007/T.R.A.G.I.C)、[depthmapX](https://github.com/SpaceGroupUCL/depthmapX)、[SpaceSyntaxNova](https://github.com/catsyntax/SpaceSyntaxNova/)、[PlanX](https://github.com/YusufEminoglu/PlanX)
- 商业工具：[MassMotion](https://www.oasys-software.com/products/pedestrian-simulation-software/massmotion/)、[AnyLogic](https://www.anylogic.kr/features/libraries/pedestrian-library/)、[疏散工具综述（IIETA）](https://www.iieta.org/journals/ijsse/paper/10.18280/ijsse.160310)
- 学术：[TravelAgent（SAGE）](https://journals.sagepub.com/doi/10.1177/23998083251360458)、[LLM-Powered 车站人流（OpenReview）](https://openreview.net/forum?id=KFUY3bhsuU)、[CAMS（arXiv）](https://arxiv.org/pdf/2506.13599v1.pdf)、[火灾疏散寻路（系统仿真学报）](https://www.china-simulation.com/EN/abstract/abstract3856.shtml)、[Nature Sci Rep 空间优化](https://www.nature.com/articles/s41598-026-56501-w_reference.pdf)
