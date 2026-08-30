---
title: "AI 辅助建筑规划设计：全球调研与知识库适配"
type: 调研
scope: 通用
source: "全球检索（RIBA/AIA/Autodesk/Chaos&Architizer/Parametric Architecture/PAACADEMY/小库/上海院/arXiv 等）"
date: 2026-08
tags: [AI建筑, 生成式设计, 全球调研, 工具生态, 采用率, 空间规划, 学术前沿]
---

# AI 辅助建筑规划设计：全球调研与知识库适配

> 调研时间：2026-08-30 ｜ 范围：全球（欧美主流工具 + 国内垂直生态 + 学术前沿）｜ 目的：判断有哪些 AI 辅助建筑规划设计的成果适合纳入创客空间知识库
> 与既有文档关系：本文是**现状全景**（回答"全球发展到哪一步"）；方法/工具可操作清单见 `02-空间搭建/AI辅助创客空间规划-方法与工具库.md`；行业案例见 `AI应用现状全景-创客空间各领域调研.md` 第九章

---

## 一、全球采用率与市场（2025-2026 关键数据）

| 数据 | 数值 | 来源 |
|------|------|------|
| 英国事务所 AI 使用率 | **59%**（同比 +18 个百分点），大型事务所 >80%，小型 48%；"大多数项目用 AI"从 4%→9% | RIBA AI Report 2025（n≈500） |
| 建筑师尝试过 AI 工具 | 64%，其中 74% 计划 12 个月内增加使用 | Chaos × Architizer（n≈800） |
| 建筑师已在项目中使用 AI | 46%（另有 24% 计划开始） | Architizer × Chaos（n=1,227） |
| 美国事务所使用 AI | 33%（大型事务所 61%）| AIA（2025-03） |
| AEC 决策者使用 AI | 27%，其中 94% 计划增加 | Bluebeam（n=1,000+，美英法德澳） |
| 行业对 AI 的定位 | 69% 认为"增强而非替代"人类 | Autodesk State of Design and Make（n=5,594） |
| 生成式 AI 建筑市场规模 | $1.47B（2025）→ $2.07B（2026） | Business Research Company |

**结论**：AI 在建筑设计已过"要不要用"的临界点，进入"用什么、用在哪"阶段；但最成熟、最普及的场景集中在**早期概念/方案阶段**（概念设计是 48% 受访者报告的最大时间节省点）。

---

## 二、全球工具生态图谱（按工作阶段分类，2026）

### 2.1 概念与可行性分析（早期方案——最成熟）

| 工具 | 核心能力 | 定价 | 备注 |
|------|---------|------|------|
| **Autodesk Forma**（前 Spacemaker AI）| AECO 行业首个端到端 AI 原生平台：实时日照/风/噪声/隐含碳分析；AI 生成室内布局（输入建筑类型+结构材料→**秒级生成完整布局**，如 36 户→改边界→56 户）；Forma Building Design beta | ~$185/月 或 ~$1,500/年 | 2025 AU 发布；Revit 为首个 Connected Client |
| **TestFit** | 实时生成式设计：输入场地边界/限高/户型组合/停车比→秒级生成体量、停车、户型与经济测算（Pro Forma）| $195/月 或 $15,000/年 | 拿地可行性分析标杆，多户住宅/学生公寓/停车 |
| **Architechures** | 生成式布局优化（住宅），多方案迭代 | €41/月 | 面向住宅建筑的布局优化 |
| **Finch3D** | AI 生成设计 copilot：把事务所设计系统编码进生成流程，实时数据探索成千方案权衡 | 订阅制 | "AI 协同 + 实时数据" |

### 2.2 平面/布局生成（AI 布局）

| 工具 | 核心能力 | 备注 |
|------|---------|------|
| **Maket.ai** | 自然语言描述（房间数/形状/面积）→可编辑平面图，带法规合规检查 | 住宅为主 |
| **Planner 5D / GetFloorPlan / Floor-Plan.ai / Blueprints AI** | 草图/照片/文字→2D/3D 平面图 | 见工具库文档 |
| **HouseCrafter**（ICCV'25 开源研究）| 平面图→3D 场景（2D 扩散模型生成多视角 RGB-D）| 研究→产品过渡 |

### 2.3 参数化/生成式 CAD（算法驱动）

| 工具 | 核心能力 | 备注 |
|------|---------|------|
| **Snaptrude** | 部门级空间规划：泡泡图→BIM，AI 邻接打包四目标优化 | 见工具库文档（方法论核心）|
| **Hypar** | 参数化生成式设计平台，有免费层 | — |
| **ArchiLabs Studio Mode** | 网页端 code-first 参数化 CAD：自然语言描述→AI 生成"Recipes"设计工作流，免装免改代码 | 2026 新锐 |

### 2.4 中文垂直工具（教育/空间场景友好）

| 工具 | 核心能力 | 备注 |
|------|---------|------|
| **小库科技 XKool** | AI 设计引擎："数-模-规统一"（**设计即建模、建模即合规**），规划/户型/彩总智能生成 | 国内 AI 建筑设计头部，"合规自动检查"是其差异点 |
| **酷家乐**（群核科技）| AI 户型识别、5 分钟出全屋方案、3 小时完成全案设计（传统 3-7 天）、模袋云 AI 建筑创作（在线 SD 出图）| 教育空间/实验室专项模块见工具库文档 |
| **暗壳 AI（Ark.art）** | 空间设计垂类平台：传统空间设计一周→1 小时；线稿/文字/局部重绘；2025 年获政府基金近千万融资 | 亦庄 OPC 案例的设计方 |
| **ArchiNeur**（上海建筑设计研究院）| 建筑师一站式 AI 创意生成平台 | 上海"模塑申城"住建 AI 十佳案例 |
| **毕鲁斯 AI（Billus）** | 建筑 AI 设计方案（与基准方中深度合作）| 国内建筑 AI 落地代表 |

### 2.5 施工深化（从概念走向施工图）

| 工具/方案 | 核心能力 | 备注 |
|----------|---------|------|
| **DeepSeek+天正（施工图智能深化）** | 自然语言指令→规范解析→施工图生成；7 层病房楼设计周期 2 周→1 天（-70%）；规范符合性 100% 自动保障；工程量误差 ±8%→<0.5% | 自建工作流范例 |
| **华艺 AI CAD 插件** | 自动化地库排布：参数化车位布置（道路宽度/转弯半径/车位尺寸自动核算）| 专利级 CAD 插件 |
| **ZD-PLM**（中南建筑设计院 × 法国达索）| 全球首个工程全生命周期数字化管理平台，"造房子无需图纸" | 中法合资 |
| **中国二十二冶 AI 钢结构模块化设计** | 自研软件使设计效率提升 100%，用于唐山钢结构住宅/海港职业技术学院 | 设计院自研 |

---

## 三、学术研究前沿（生成式/LLM 方向）

| 研究 | 方向 | 进展状态 |
|------|------|---------|
| **FloorPlan-LLaMa**（清华，ACL'25）| 建筑专业知识驱动的平面图自动生成，解决"指标优秀但实际不可用"痛点 | 学术验证 |
| **DiffPlanner**（arXiv 2508）| 免光栅化：直接在矢量空间生成有边界约束的平面图（Transformer+扩散）| 学术验证 |
| **Text-to-Layout**（arXiv 2509）| 用 LLM 分步生成建筑平面草图工作流 | 学术验证 |
| **HouseCrafter**（ICCV'25）| 平面图→一致的多视角 3D 场景（2D 扩散模型）| 学术验证 |
| **注意力约束扩散模型**（ASCE, 2025）| 无障碍平面图生成：约束注意力机制保证合规与几何 | 学术验证 |
| **扩散模型日照性能评估**（Cambridge, 2025）| 用 ChatGPT/Copilot/LookX 生成住宅平面→AutoCAD 重建→日照模拟，31 稿中 8 稿有效 | 学术验证（提示词质量是关键瓶颈）|
| **MDPI《Shaping Architecture with Generative AI》** | GAN/VAE/扩散/Transformer 在建筑设计工作流的系统综述 | 综述 |

**结论**：学术研究处于"单点验证"阶段（扩散模型+LLM 双主线），**尚未产品化到普通用户可用**；对创客空间而言，当前应优先采用**已商用的 2.1-2.4 工具**，学术成果作为观察窗口即可。

---

## 四、对创客空间知识库的可迁移点

1. **早期"可行性分析"最成熟、最该用**：Forma/TestFit 的日照、噪声、隐含碳、经济测算实时分析——直接对应创客空间"楼上宿舍噪声敏感""面积紧张""预算核算"三大痛点（与本库 `AI规划方法论-实战验证` 的 H 系列硬约束吻合）。
2. **"数-模-规统一"是合规解法**：小库的"设计即合规"理念可迁移到创客空间消防/疏散/安全距离自动检查，补强本库"AI 可能幻觉规范条款"的短板。
3. **低门槛"文字→平面→3D"可用于教学**：Maket/HouseCrafter 类工具让学生参与规划成为可能，把 AI 规划做成创客教育项目（呼应 `AI+创客教育` 文档）。
4. **施工深化 AI 面向正式装修/报建**：创客空间如做正式装修图，DeepSeek+天正类工作流可将周期从周级压到天级（本库现多为概念方案，深化阶段是增量）。
5. **采用率数据支撑决策**：59%/46%/33% 等数据可作为"AI 规划已是主流"的立项依据，写入本库对外汇报材料。
6. **边界提醒**：学术前沿（矢量扩散、LLM 草图）尚不成熟，别追新；全球 2026 共识仍是"AI 出方案 + 人工把关节能、需校验"。

## 五、结论与建议

- **值得纳入知识库的成果**：全球采用率数据（决策依据）、Forma/TestFit/Finch/Architechures（可行性分析工具）、小库"数-模-规统一"（合规理念）、DeepSeek+天正（深化阶段工作流）、FloorPlan-LLaMa/DiffPlanner（学术观察）。
- **下一步建议**：在 `AI辅助创客空间规划-方法与工具库.md` 中补入 Forma/Finch/小库/ArchiNeur 等工具条目（本文 2.1/2.4 已给出能力与定价），并新增"按阶段+预算+难度"的选型矩阵。
- **不纳入**：学术研究细节（对创客空间实操价值低）、商业报价浮动数据（以官方为准）。

## 主要来源

- RIBA AI Report 2025 / AIA 2025 / Bluebeam AEC Tech Outlook / Autodesk State of Design and Make 2025（采用率）：[creativetoolsai.com](https://www.creativetoolsai.com/state-of-ai-in-architecture-2026/)、[illustrarch](https://illustrarch.com/artificial-intelligence/75112-ai-architectural-design-tools.html)、[Chaos×Architizer 报告](https://blog.chaos.com/hubfs/2026/Architizer-report/How-is-AI-Reshaping-Architectural-Design-&-Visualization-in-2026-Chaos-&-Architizer-Report.pdf)、[ArchitectureLab](https://www.architecturelab.net/ai-site-analysis-tools/)
- Autodesk Forma：官方博客 [AU 2025](https://www.autodesk.com/blogs/construction/au-2025-top-autodesk-construction-announcements/)、[illustrarch 评测](https://illustrarch.com/articles/design-softwares/73363-autodesk-forma-review.html)
- TestFit：[官方 Site Solver](https://www.testfit.io/product/site-solver)、[MeltFlex 定价对比](https://www.meltflexai.com/blog/best-ai-space-planning-tools-architects)
- Finch：[finch3d.com](https://www.finch3d.com/)、[PAACADEMY Top 12](https://paacademy.com/blog/top-ai-tools-architectural-planning)、[Parametric Architecture](https://parametric-architecture.com/10-ai-tools-transforming-architecture/)
- 小库科技：[xkool.ai](https://www.xkool.ai/zh/XkoolDesignCloud)
- 暗壳 AI：[融资报道](https://m.aitntnews.com/newDetail.html?newId=18702)、[AI工具导航](https://ai.fly63.com/arkart)
- 酷家乐：[AI 产品页](https://www.kujiale.com/activities/AI-kujiale)、[全案设计指南](https://b.kujiale.com/article-detail/3FO4K4WEBWER)
- 提效录（TestFit 实战 + 选型）：[tixiaolu.com](https://www.tixiaolu.com/posts/ai-architect-design-2026/)
- 上海院 ArchiNeur：[澎湃新闻](https://m.thepaper.cn/newsDetail_forward_32042003)
- ZD-PLM：[长江网](http://news.cjn.cn/whpd/yw_19947/202510/t5222721.htm)
- DeepSeek+天正：[CSDN](https://blog.csdn.net/weixin_39815573/article/details/149395423)
- 二十二冶 AI 钢结构设计：[极目新闻](http://www.ctdsb.net/c1747_202512/2617717.html)
- 学术：FloorPlan-LLaMa [腾讯新闻](http://news.qq.com/rain/a/20250906A04B6H00)；DiffPlanner [arXiv:2508.13738](https://arxiv.org/html/2508.13738)；Text-to-Layout [arXiv:2509.00543](https://arxiv.org/html/2509.00543v1)；HouseCrafter [GitHub](https://github.com/AkihikoWatanabe/paper_notes/issues/3432)；ASCE [扩散模型无障碍平面](https://ascelibrary.com/doi/10.1061/JCCEE5.CPENG-6456)；MDPI [综述](https://mdpi-res.com/d_attachment/architecture/architecture-05-00094/article_deploy/architecture-05-00094.pdf)
