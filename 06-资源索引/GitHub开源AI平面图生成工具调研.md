---
title: "GitHub开源AI平面图生成工具调研"
type: 资源索引
scope: 通用
source: "GitHub AI平面图工具调研"
date: 2026-08
tags: [AI平面图, 开源工具, Buildify, LLM+JSON, 调研]
---

# GitHub开源AI平面图生成工具调研

> 深度调研 GitHub 上 AI 平面图/空间布局生成的开源项目，评估技术路线可靠性，对标某职业院校创客空间项目给出可行路径
> 调研时间：2026-08 ｜ 调研范围：GitHub 开源项目 + 相关学术论文（House-GAN/HouseDiffusion/RLVR等）
> 定位：本文回答"AI 绘制规划图哪个方向更靠谱"——结论是**纯生成式图像模型（Seedream/Midjourney）不适合画精确平面图，LLM+结构化JSON+规则校验+确定性求解器的混合管线才是靠谱方向**。

---

## 一、核心结论

### 1.1 为什么纯生成式图像模型不靠谱

| 问题 | 原因 |
|------|------|
| 不理解真实平面图 | 纯文生图（T2I）没有输入真实平面图，L型是"想象"的而非真实的 |
| 几何幻觉 | 生成式模型基于概率出图，墙体/尺寸/门窗是"看起来像"而非精确计算 |
| 无法校验 | 出图后无法自动检查面积是否超标、房间是否重叠、通道是否够宽 |
| 文字乱码 | 区域标注/尺寸数字会生成乱码或错误文字 |
| 不可迭代 | 无法"把这个房间往左移0.5米"——只能重新生成一张全新的图 |

> **Seedream/Midjourney 的正确定位是"空间氛围渲染图/鸟瞰效果图"，不是"平面图"。**

### 1.2 靠谱的技术路线：混合管线

GitHub 上成熟项目的共同架构是**三段式混合管线**：

```
① LLM/神经网络生成结构化布局（JSON：房间类型/面积/坐标/邻接）
        ↓
② 规则引擎校验（面积/重叠/通道/规范/邻接）→ 失败自动修正
        ↓
③ 确定性求解器渲染（网格对齐/零间隙/精确几何 → SVG/3D/DXF）
```

关键洞察：**AI 负责"推理和发散"，确定性代码负责"精确和校验"**——这正是 OpenAI Cookbook "grounded spatial reasoning" 方法论的开源实现。

---

## 二、三大代表项目深度解析

### 2.1 Buildify —— 最成熟的混合管线（住宅）

**GitHub**: https://github.com/sarvanithin/Buildify ｜ MIT 协议 ｜ 2026年活跃

**核心定位**：端到端 AI 住宅建筑设计平台，输入卧室数/浴室数/面积/风格，数秒输出多个可审查的建筑平面图。

**5阶段混合生成管线**（这是全文最有价值的架构）：

| 阶段 | 方法 | 作用 |
|------|------|------|
| **Stage 1 — BUILD** | 确定性 | 从 IRC 规范和约束推导房间列表（车库/门厅/客厅/餐厅/厨房/走廊/卧室/浴室） |
| **Stage 2 — SIZE** | MOE 神经网络（8专家） | 混合专家模型输出8个专家权重，按总面积和风格缩放每个房间的宽×高 |
| **Stage 3 — PLACE** | HouseGAN++ 或 区域求解器 | 图拓扑布局（房间图→XY坐标）；HouseGAN++不可用时回退到确定性区域求解器（入口带/社交带/走廊脊柱/私密带/户外带） |
| **Stage 4 — VALIDATE** | IRC 规范校验 | 强制执行房间最小面积（居住≥70sqft、卧室≥10×10ft、走廊≥36in），裁剪到建筑轮廓内 |
| **Stage 5 — REFINE** | 确定性 | 对齐2英尺施工网格、消除房间间隙、强制精确轮廓宽度、解决重叠→**零间隙保证** |

**关键创新**：
- **零间隙保证**：房间在2英尺施工网格上边到边紧密排列，没有缝隙
- **规范合规**：每个方案都通过美国 IRC 住宅规范校验
- **生成式+确定性混合**：MOE+HouseGAN++负责智能，区域求解器+规范校验+网格对齐负责精确
- **DXF 导出**：可直接导入 AutoCAD
- **成本估算**：按面积和房间配置做区域成本估算

**输出能力**：2D建筑平面图（带尺寸/标签/门开向）、3D外观模型、方案对比板（A/B/C变体）、DXF CAD导出、成本估算、AI设计咨询聊天

**技术栈**：React+Vite+TypeScript（前端）、FastAPI+Python（后端）、PyTorch MOE模型、HouseGAN++、Three.js（3D）、ezdxf（CAD导出）

**局限**：
- 住宅导向（bedrooms/bathrooms），不是商业/创客空间/实验室
- 单楼层
- 门窗放置仍在路线图中
- 与 Revit/SketchUp 直接集成仍在路线图中

**对标本项目的可复用点**：
- ✅ 5阶段混合管线架构可直接复用（把"IRC住宅规范"换成"职业院校实训室规范+安全规范"）
- ✅ 区域求解器的"带式布局"思路（入口带/社交带/私密带）可映射为"入口带/教学带/制造带/高风险带"
- ✅ 零间隙+网格对齐+规范校验的确定性后处理可复用
- ✅ DXF导出+成本估算能力可复用

---

### 2.2 Rosa Miniporto —— 最清晰的 LLM+校验架构

**GitHub**: https://github.com/inconquested/rosa-miniporto ｜ 18 commits ｜ 2026年活跃

**核心定位**：文本→3D平面图生成器，带交互式可视化和预算估算。把自然语言描述（如"3卧室公寓，120㎡，2浴室，开放厨房客厅"）转成结构化JSON布局，校验建筑规则，渲染为可交互3D模型。

**核心架构**（最简洁清晰的靠谱方案）：

```
自然语言描述
    ↓
Claude Opus 4.8（Azure AI Foundry）
  → 基于"走廊脊柱"系统提示词
  → 输出严格 JSON floor-plan schema
    （rooms数组：type/area/width/height/x/y）
    ↓
Zod schema 校验 + 自定义建筑规则引擎
  检查：无重叠、无悬浮房间、走廊/邻接连通性
    ↓
  失败？→ 第二次 Claude Opus "修正" pass 重新生成 rooms 数组
    ↓
Three.js 3D 可视化（彩色地板/真实墙厚/尺寸线/轨道控制）
    ↓
预算计算器（按房间材料/人工/家具 + 15%应急费）
```

**关键设计**：
- **严格 JSON schema**：LLM 输出的不是图片，是结构化数据（房间类型/面积/宽高/坐标），这是可校验、可修正、可渲染的基础
- **Validate→Correct 管线**：规则引擎检查失败后，自动触发第二次 LLM 修正，而非直接返回错误结果
- **"走廊脊柱"系统提示词**：强制 LLM 以走廊为结构脊柱组织布局，保证连通性
- **0.5m 网格坐标**：布局坐标使用0.5m网格增量，墙高2.4m，墙厚~0.125m
- **API 返回元数据**：success/usedProvider/corrected/attempts/rateLimit，可追溯是哪次pass产出的最终结果

**支持的房间类型**：bedroom/kitchen/bathroom/living_room/office/hallway/garage/carport/laundry/foyer

**尺寸约束**（系统提示词强制）：
- 客厅 20-42㎡（最大公共空间）
- 厨房 7-28㎡（邻接客厅）
- 卧室 7-23㎡（邻接走廊）
- 浴室 3-9㎡（邻接卧室）
- 走廊 4-14㎡（结构脊柱）

**已知局限**：
- 布局重叠（修正pass能修大部分但非全部）
- 仅矩形房间（无弧形/斜角）
- 单楼层
- 无家具渲染
- 单用户（无实时协作）

**对标本项目的可复用点**：
- ✅ **这是最容易复现的架构**——不需要训练模型，只需一个 LLM API + 规则引擎 + Three.js
- ✅ Validate→Correct 管线可直接复用（把建筑规则换成实训室安全规则）
- ✅ 严格 JSON schema + 0.5m网格的设计可复用
- ✅ 可把本项目真实L型平面图作为边界约束输入系统提示词
- ✅ 3D可视化+预算估算可直接用于方案汇报

---

### 2.3 LLM-Floor-plan —— Rhino/Grasshopper 集成（能引用真实平面图）

**GitHub**: https://github.com/vencecai/LLM-Floor-plan ｜ 18 commits ｜ 2025年

**核心定位**：基于自然语言的平面图生成与操作系统，提供 Rhino/Grasshopper 与 Web 界面之间的无缝工作流。

**核心方法：层次空间划分 + 拓扑图生成**

```
① 边界定义
   - Rhino截图作为视觉参考
   - Web界面(tldraw)绘制边界
   - 或默认矩形边界
        ↓
② LLM递归空间划分
   - LLM决定沿X或Y轴划分（基于规则：二分划分/最小房间尺寸/功能需求）
   - 每个子矩形判断是否终止（最小尺寸/房间数/功能标签）
   - 未终止则继续递归
   - 每次划分创建两个子节点+邻接边
        ↓
③ 拓扑图生成
   - 树形划分结构→标准图（节点=房间类型+中心点，边=共享墙/门洞）
   - 计算节点中心性，提取主要通行动线
        ↓
④ 物理平面图生成
   - 生成最终几何，Web可视化或回传Rhino
        ↓
⑤（可选）Spatial OS 集成
   - 2D平面图→公寓对象
```

**关键创新**：
- **能引用真实平面图轮廓**——从 Rhino 截图作为参考，在 Web 界面绘制边界，这解决了"AI不理解真实平面图"的问题
- **双向 Grasshopper 连接**——生成的 JSON 布局可转回 Rhino 几何（创建图层/房间轮廓/面积标签）
- **递归二分划分**——LLM 决定划分方向，确定性算法执行几何，保证可计算
- **拓扑图+中心性分析**——从布局提取通行动线

**技术栈**：React+tldraw+Tailwind+Vite（前端）、Flask+Python+OpenRouter API（后端）、Rhino 8+Grasshopper（建筑设计端）

**局限**：
- 项目较早期（18 commits，最后更新2025年5月）
- 住宅/公寓导向
- 依赖 Spatial OS（可能不可用）
- 文档较简单

**对标本项目的可复用点**：
- ✅ **引用真实平面图轮廓的思路最关键**——把本项目L型平面图截图作为边界输入
- ✅ 递归二分划分+拓扑图的方法可复用
- ✅ Rhino/Grasshopper 双向连接——如果本项目用 Rhino，可直接对接
- ✅ tldraw 绘制边界的交互方式可复用

---

## 三、其他值得关注的项目

| 项目 | GitHub | 核心能力 | 亮点 | 局限 |
|------|--------|---------|------|------|
| **FloorGen AI** | github.com/Asadyousaf03/floorgen | 自然语言→CAD平面图 | FLUX.1-dev微调 + 栅格转矢量自动化 → 输出DXF/JSON/PNG，30秒出图，可导入AutoCAD/Revit/Blender/Unreal | 较新项目，住宅导向 |
| **RoomForge** | github.com/danyanovichp/roomforge | 自然语言brief→AI布局+2D规划器 | 粘贴OpenAI API key即用，2D米网格规划+拖拽+实时布局校验（重叠检测/房间跳转）+3D模式 | 需自备API key |
| **Aedifex** | （CSDN介绍）浏览器3D建筑编辑器+LLM助手 | 自然语言驱动建墙/开窗/摆家具，不需要专业建模工具 | 3D实时编辑+AI对话驱动 | 较新项目 |
| **Hogar Studio** | github.com/PanoramicRum/hogar-studio | 上传平面图→AI提取墙体/房间/门窗 | AI矢量化平面图+3D漫游+VR+AI渲染8+风格 | 偏室内设计，非布局生成 |
| **ArchiGen** | github.com/Dropio12/archigen | 自然语言/已有图纸→合规平面图 | 微调加拿大住宅规范，矢量布局+尺寸+墙对齐，可编辑可导出 | 加拿大住宅导向 |
| **Arch-Ai-Tex** | github.com/Aravkataria/Arch-Ai-Tex | GAN生成户型图+优化布局生成器 | 256×256分辨率，可选去噪器，基于尺寸/房间数的优化布局 | 分辨率低，研究向 |
| **floor-plan-rlvr** | github.com/ludolara/floor-plan-rlvr | LLM+强化学习可验证奖励(RVLR)生成平面图 | JSON多边形结构表示，RPLAN数据集，监督微调+RLVR训练+vLLM批量推理 | 学术向，需训练 |
| **awesome-nano-banana-spatial-design** | github.com/qzh3722/awesome-nano-banana-spatial-design | AI空间设计提示词仓库（中英文） | 场景化提示词实践，非"魔法提示词"集合 | 仅提示词，非工具 |
| **OpenLayout** | （findmydesignai提及）开源布局生成 | GitHub超100万下载 | 社区驱动的开源布局工具 | 需进一步核实 |

---

## 四、学术前沿（技术路线参考）

| 研究 | 核心方法 | 对标价值 |
|------|---------|---------|
| **House-GAN / House-GAN++** | 关系GAN，从泡泡图生成户型图 | Buildify Stage 3 的基础 |
| **HouseDiffusion** | 扩散模型生成矢量平面图 | 更稳定的生成质量 |
| **HouseLLM** (arXiv 2411.12279) | LLM辅助两阶段文本→平面图 | Rosa Miniporto 的学术前身 |
| **RLVR平面图生成** (arXiv 2605.14117) | LLM+强化学习可验证奖励，JSON多边形结构 | floor-plan-rlvr 项目，用可验证奖励替代人工偏好 |
| **CasaGPT** (arXiv 2504.19478) | 自回归模型顺序排列长方体，生成物理合理的3D室内场景 | 3D家具布局生成 |
| **HomeWorld** (arXiv 2606.06390) | 30万真实户型数据集训练LLM，平面图→家具→小物件全流程 | 大规模可控全屋场景生成 |
| **空间句法后训练(SSPT)** | 把空间句法知识注入平面图生成，非微分oracle | 提升布局的空间合理性 |

---

## 五、技术路线对比

| 路线 | 代表 | 精确性 | 可校验 | 可迭代 | 实现难度 | 适合本项目？ |
|------|------|--------|--------|--------|---------|-----------|
| 纯生成式图像 | Seedream/Midjourney | ❌ 低 | ❌ 不可 | ❌ 不可 | 低 | ❌ 不适合平面图 |
| GAN/扩散生成 | House-GAN/HouseDiffusion | ⚠️ 中 | ⚠️ 部分 | ⚠️ 有限 | 高（需训练） | ⚠️ 需大量数据 |
| **LLM+JSON+规则校验** | **Rosa Miniporto** | ✅ 高 | ✅ 可校验 | ✅ 可修正 | **中（LLM API+规则引擎）** | ✅ **最推荐** |
| **混合管线（生成+确定性）** | **Buildify** | ✅✅ 很高 | ✅✅ 规范校验 | ✅ 可迭代 | 高（需MOE模型） | ✅ 架构可复用 |
| LLM+递归划分+Rhino | LLM-Floor-plan | ✅ 高 | ✅ 几何可算 | ✅ 可编辑 | 中 | ✅ 如有Rhino可用 |
| LLM+RLVR | floor-plan-rlvr | ✅ 高 | ✅ 可验证奖励 | ✅ 可训练 | 很高（需训练） | ⚠️ 学术向 |

---

## 六、对标本项目的可行路径建议

### 推荐方案：参考 Rosa Miniporto 架构，轻量自建

**为什么选这个**：不需要训练模型，不需要大量数据，只需 LLM API + 规则引擎 + 渲染器，1-2周可出原型。

**架构映射到本项目**：

```
本项目真实L型平面图（434㎡）
    ↓ 作为边界约束输入系统提示词
LLM（本对话AI / Claude / GPT）
  → 输出结构化 JSON：
    { zones: [
        {type:"数字设计区", area:50, x:0, y:0, w:10, h:5, adjacency:["公共教学区"]},
        {type:"创客制造区", area:60, ...},
        ...
      ],
      totalArea: 434, constraints: {...}
    }
        ↓
规则引擎校验（实训基地专项规则）：
  ✅ 总面积 ≤ 434㎡
  ✅ 无区域重叠
  ✅ 主通道 ≥ 1.5m
  ✅ 高噪音区（制造/机器人）远离宿舍方向
  ✅ 高压电池区独立隔离
  ✅ 工业机器人区含安全围栏面积
  ✅ 激光区靠墙+排烟
    ↓ 失败 → 自动触发第二次LLM修正
        ↓
SVG/Three.js 渲染（顶视平面图+3D鸟瞰）
    ↓
导出：SVG / PNG / DXF（可选）
```

**关键改造点**（从住宅版→创客空间版）：
1. 房间类型替换：bedroom→"数字设计区"/"制造区"/"机器人区"/"新能源区"/"AI区"/"公共教学区"/"储物区"/"管理区"
2. 尺寸约束替换：卧室7-23㎡ → 各功能区按设备清单推导的面积
3. 规则引擎替换：IRC住宅规范 → 实训室安全规范+消防规范+降噪规范
4. 边界输入：默认矩形 → 本项目真实L型平面图轮廓
5. 邻接关系：卧室邻接走廊 → 制造区邻接储物区、机器人区邻接AI区、高风险区远离公共区

### 备选方案：直接部署 Buildify 并改造

- 优点：5阶段管线已实现，DXF导出+成本估算+3D可视化都有
- 缺点：需要部署MOE模型+HouseGAN++，改造工作量大，住宅导向深
- 适合：如果有Python/ML团队，可长期投入

### 不推荐：继续用 Seedream 画平面图

- Seedream 适合做**空间氛围渲染图/鸟瞰效果图**，作为方案汇报的视觉补充
- 不适合做**精确平面图**——这是工具能力边界，不是prompt能解决的

---

## 七、局限与风险

| 风险 | 说明 | 应对 |
|------|------|------|
| 所有项目都是住宅导向 | 没有专门针对创客空间/实验室/商业空间的开源项目 | 架构可复用，需替换房间类型/规则/约束 |
| LLM布局仍可能重叠 | Rosa Miniporto的修正pass能修大部分但非全部 | 多次生成+人工筛选+确定性后处理 |
| 非矩形空间支持弱 | L型/异形空间的划分比矩形复杂 | LLM-Floor-plan的递归划分可处理异形边界，或手动定义边界 |
| 家具/设备级布局缺失 | 现有项目只到房间级，不到设备级 | 房间级布局确定后，设备级用确定性算法（邻接打包）或人工CAD |
| 项目成熟度参差 | Buildify较成熟，Rosa/LLM-Floor-plan较早期 | 参考架构而非直接部署，轻量自建核心管线 |
| 规范适配 | 美国IRC规范≠中国职业院校实训室规范 | 规则引擎需按中国规范+实训基地专项安全要求重写 |

---

## 八、资源索引

### 核心项目
- Buildify: https://github.com/sarvanithin/Buildify
- Rosa Miniporto: https://github.com/inconquested/rosa-miniporto
- LLM-Floor-plan: https://github.com/vencecai/LLM-Floor-plan

### 其他项目
- FloorGen AI: https://github.com/Asadyousaf03/floorgen
- RoomForge: https://github.com/danyanovichp/roomforge
- ArchiGen: https://github.com/Dropio12/archigen
- Arch-Ai-Tex: https://github.com/Aravkataria/Arch-Ai-Tex
- Hogar Studio: https://github.com/PanoramicRum/hogar-studio
- floor-plan-rlvr: https://github.com/ludolara/floor-plan-rlvr
- awesome-nano-banana-spatial-design: https://github.com/qzh3722/awesome-nano-banana-spatial-design
- Aedifex（CSDN介绍）: https://blog.csdn.net/HashTang/article/details/160412090

### 学术论文
- House-GAN / House-GAN++ (Nauata et al. 2020/2021)
- HouseDiffusion
- HouseLLM: LLM-Assisted Two-Phase Text-to-Floorplan (arXiv 2411.12279)
- Generative Floor Plan Design with LLMs via RLVR (arXiv 2605.14117)
- CasaGPT: Cuboid Arrangement and Scene Assembly (arXiv 2504.19478)
- HomeWorld: Floorplan-to-Furnished Framework (arXiv 2606.06390)
- OpenAI Cookbook: Grounded Spatial Reasoning with GPT-5.5 (https://developers.openai.com/cookbook/examples/multimodal/grounded_spatial_reasoning_layouts)

### 方法论衔接
- 知识库《AI辅助创客空间规划-方法与工具库》——本文是其"工具选型"的深化
- 知识库《AI规划方法论-实战验证与提示词模板》——验证了LLM推理+人工校验的有效性，本文给出了可自动化的开源实现路径
