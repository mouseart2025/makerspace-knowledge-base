---
title: "Fab Lab / MIT 开源资源专题补充（设备与工具清单/选型）"
type: 资源索引
scope: 通用
source: "Fab官方+MIT开源调研+cba.mit.edu全站"
date: 2026-08
tags: [Fab Lab, MIT, 开源资源, CAM工具链, 清单模板, CBA]
---

# Fab Lab / MIT 开源资源专题补充（设备与工具清单/选型）

> 定位：补充《设备清单与选型》的**开源资源层**——官方标准清单入口、MIT 开源软件工具链、Fab Academy 教学资源、开源管理软件、真实实验室清单实例。
> 调研时间：2026-08-26
> 覆盖缺口：CAM 软件层、设备管理软件、低成本打包方案、可复制的真实选型模板

---

## 一、Fab 官方标准清单（权威源头）

| 资源 | 链接 | 内容 | 可用性 | 建议 |
|------|------|------|--------|------|
| **Fab Foundation Getting Started** | fabfoundation.org/getting-started | Fab Lab 定义四标准（公共开放/遵守宪章/共享工具集/参与全球网络）+ 5 类核心设备 + **Fab Charter 宪章全文** | ✅ 在线 | 建空间前必读，Charter 可直接翻译作为空间公约 |
| **官方全量清单（设备+工具+耗材）** | http://inventory.fabcloud.io/ | research 级 Fab Lab 全量库存；源码在 GitLab：`gitlab.fabcloud.org/inventory/inventory.fabcloud.io`（数据文件 `public/inv.toml`，另有 `inv.json` / `inv.xlsx` 成品） | ⚠️ 502：整台 FabCloud GitLab 服务器重启中（诊断见文末附录） | 恢复后运行「一键存档脚本」抓取 3 种格式离线备份 |
| **MIT CBA 历史清单页** | fab.cba.mit.edu/about/fab/inv.html | 官方清单历史版 | ❌ 已 404 | 用下方「真实实验室实例」替代 |
| **Fab Foundation 软硬件页** | fabfoundation.org/index.php/the-hardware-and-software/ | Fab 官方开源/免费软件清单（2D/3D/仿真全栈） | ✅ 在线 | 与知识库「软件环境」章节互补 |
| **Fab-in-a-Box 官方打包套件** | fabfoundation.org/fiab | 低成本入门套件（详见下文 1.1） | ✅ 在线 | 低成本方案首选参考 |

### 1.1 Fab-in-a-Box（2024 年发布，Fab Foundation × MIT CBA × Dassault Systèmes）

面向教育/社区的低成本**打包式微型 Fab Lab**，总价 **< $10,000 USD**：

| 组成 | 型号/说明 |
|------|----------|
| 激光切割机 | xTool（40W 二极管，带空气辅助+蜂窝板） |
| 3D 打印机 | Bambu Lab P1S（教育级，稳定可靠） |
| 乙烯基切割机 | Brother Scan n' Cut（贴纸/标识/软材料） |
| 净化 | 烟雾净化器（保障教室环境） |
| 电脑 | 预装全部软件的教师控制电脑 |
| 软件 | xDesign（SOLIDWORKS 3DEXPERIENCE 云 CAD） |
| 课程 | 10 个分级活动（exposure → exploration → deep dive），含教师指南/视频/评估工具，对齐 Common Core/NGSS/ITEEA 标准 |
| 载体 | 一体化推车（可运输+展开为工作台） |

> ⭐ **重要**：官方声明**正在开源 Fab-in-a-Box 设计**（硬件文件、构建说明、示例课程），仓库即将发布——这是"抄作业"级资源，适合低成本改造方案直接参照。
> 参考：《低成本入门方案.md》可与此联动。

---

## 二、MIT 开源软件工具链（设备配套软件，现有知识库缺口）

Fab 生态的设备控制/CAM 层全部开源，由 MIT Center for Bits and Atoms 维护：

| 工具 | 链接 | 说明 |
|------|------|------|
| **Fab Modules**（老版） | fabmodules.org · GitHub: `FabModules/fabmodules-html5` | 浏览器端 CAM 系统，生成激光切割机/CNC 铣床/水刀/乙烯基切割机的**刀具路径与 G-code**；支持 Roland MDX-15/20/40、ShopBot、Epilog、Trotec、GCC、Universal 等主流机型；自定义 MIT-like 开源协议 |
| **mods**（新版） | mods.cba.mit.edu · GitLab: `gitlab.cba.mit.edu/pub/mods` | Fab Modules 的下一代，工作流可在客户端保存/分享，算法持续更新，支持"制造机器的机器"（MTM） |
| kokopelli | GitHub（CBA 维护） | 配套设计/参数化建模 UI |

**定位**：这是"设计文件 → 机器指令"的关键开源层，Fab Academy 全程用它铣 PCB、切板材。知识库「软件环境」表目前只有设计类软件，**应把 CAM 层补进去**。

---

## 三、Fab Academy 开源教学资源（选型参照 + 培训资源）

| 资源 | 链接 | 内容 | 用途 |
|------|------|------|------|
| **Fab Academy 官网** | fabacademy.org | 19 周课程体系：CAD、激光切割、电子产品生产（PCB 铣）、3D 扫描打印、电子设计、嵌入式编程、CNC 加工、成型铸造、复合材料、机器设计、I/O 设备、网络通信、系统集成等 | 员工/讲师培训大纲参考 |
| **历年学员文档档案** | archive.fabacademy.org | 全球历届学员逐周项目文档（含设备操作细节、PCB 制作流程、机器构建教程） | **当操作手册/教程库用**，比厂商文档更贴近创客场景 |
| **课程软件清单** | academy.cba.mit.edu/classes/ | Fab 官方使用的开源软件/免费软件列表 | 软件选型核对 |
| 中文教学点 | 同济 Fablab O（上海）、深圳开放创新实验室 SZOIL | 中国认证节点，可咨询落地经验与设备配置 | 实地对标 |

> 价值：Fab Academy 的**周课程主题本身就定义了设备能力矩阵**——对照它可反推"要开齐这些课，我需要哪些设备"。

---

## 四、开源管理软件：Fab Manager（设备管理数字化，现有知识库缺口）

**Fab Manager**（fab-manager.com · GitHub: `sleede/fab-manager`）——100% 开源，100+ Fab Lab 使用，持续维护（2026-05 仍发布 v6.5.9）：

| 模块 | 能力 |
|------|------|
| 资源管理 | 机器/工作坊/培训/空间统一管理，机器可按时段预约 |
| 日历 | 预约槽创建/移动/删除，iCal 同步，重复事件 |
| 会员 | CSV 导入、会员空间、家庭账户、权限标签（如"专家"可解锁特定机器）、资料上传核验 |
| 计费 | 订阅方案、在线支付（卡）、电子钱包、现场收款、发票 PDF、GDPR/法国反欺诈合规 |
| 库存 | 库存管理模块 + **RFID 连接器**（刷卡开门/借用） |
| 社区 | 项目画廊、讨论帖、协作邀请、Open Labs 网络互通 |
| 统计 | 预约率、订阅变化、项目跟踪 |

**与上一轮发现的轻量方案对比**：

| 方案 | 定位 | 适用 |
|------|------|------|
| **Fab Manager**（本轮新增） | 完整版 Fab Lab 管理套件，自托管（Docker）/云版 | 会员+预约+计费+库存全要的中大型空间 |
| MakerMatrix（上轮） | 轻量借用/维护记录/校准提醒，MIT 协议 | 只想管工具借用与维保的小空间 |
| myTurn（上轮） | 托管 SaaS，300+ 工具图书馆 | 不想自建服务器 |

> 建议：Fab Manager 完全开源可私有化部署，符合项目隐私偏好，可作为设备管理数字化首选。

---

## 五、真实 Fab Lab 设备清单实例（选型模板，比官方清单更落地）

官方清单 502 期间的**替代参照**，均为在运营实验室的真实配置（含具体型号）：

| 实验室 | 激光 | 3D 打印 | CNC/铣 | 电子 | 特色 |
|--------|------|---------|--------|------|------|
| **Fab Lab Vancouver** | Trotec Speed 80W CO₂ | Bambu P1S / Ender 3 S1 / UP300 | ShopBot PR（96"×60"）+ X-Carve | 焊台/热风/万用表/可调电源/示波器/防静电垫 | 陶瓷打印（Clay Kit）、缝纫刺绣、真空成型 |
| **Fab Lab Tulsa** | Epilog Fusion 60W ×4 | Ultimaker S5 + Formlabs Form 3 | ShopBot PRSalpha 8'×4' | 标准电子站 | 三区制（Studio/Wood/Metal）：水刀 ProtoMAX、注塑机、等离子切割、焊机 |
| **Charlotte Super Fab Lab** | CO₂ + Fiber 双激光 | Formlabs Fuse 1 / Prusa MK4S / Markforged / SLS | Haas Mini Mill + 水刀 | Roland SRM-20 PCB 铣 + 信号发生器/示波器 | 纺织区（Zünd 数字切割、10 针刺绣）、完整机器车间 |
| **Fab Lab Reykjavik**（Fab Academy 节点） | Epilog Mini 40 ×2 + Fusion M2 | Prusa MK3S+ ×3 / MK4 / Ultimaker 3 | Roland Modela MDX-20 + ShopBot | 标准电子站 | 真空成型、Delta Wasp 粘土打印、兄弟刺绣机——**标准 Fab 学院配置参考** |
| **UCLA DMA Fab Lab** | Universal ILS12.150D + PLS6.60 | Ultimaker 3 ×2 | Shopbot PRS Alpha + Desktop | Bantam PCB 铣 + Siglent 电源 | **10 房间分区**（机器间/电子/工具间/激光室/喷漆室/除尘室/存储室）——可参考到「设备摆放」主题 |

**用法**：
1. 与科普场馆需求表（`设备清单与选型.md`）逐项对照，验证参数是否合理
2. 选一个体量接近的实例（如 Reykjavik 学院节点 或 Vancouver 社区型）作为完整配置基准
3. UCLA 的分区清单可平移进「设备摆放与布局」规范

---

## 六、成本基线参考（Fab 官方口径）

| 规模 | 设备投入 | 耗材/年 |
|------|----------|---------|
| 完整 Fab Lab（research 级） | $25,000 – $65,000 | $15,000 – $40,000 |
| Fab-in-a-Box（教育微型） | < $10,000（打包价） | 含起步材料 |
| 社区/学校入门 | $10,000 – $25,000 | — |

> 与上轮《工具设备与摆放管理-资源汇总》及《创客空间搭建及运营指南》第 195-197 页中文化三段采购清单可交叉验证。

---

## 七、与现有知识库的衔接建议

1. **《设备清单与选型.md》**：在「软件环境」表补入 **Fab Modules / mods（CAM 层）**；在采购策略中补 **Fab-in-a-Box 低成本打包方案**；新增「真实实验室清单实例」小节
2. **《工具设备与摆放管理-资源汇总.md》**：管理软件对比表补入 **Fab Manager**；UCLA 10 房间分区清单可引至设备摆放规范
3. **《低成本入门方案.md》**：Fab-in-a-Box 开源设计发布后直接引用
4. **下一步落库优先级**：① 设备摆放与布局规范（含 UCLA 分区）→ ② 设备维护保养规范 → ③ 设备管理系统选型（Fab Manager vs MakerMatrix vs myTurn）

## 八、MIT CBA 官网资源导航（2026-08 抓取）

> 来源：https://cba.mit.edu/ 全站（about / tools / classes / people / news / events / docs）。CBA = MIT 比特与原子中心，Fab Lab 网络的源头实验室，Neil Gershenfeld 任主任。

**定位**：CBA 是"数字制造研究级实验室"的黄金参照——从原子到建筑的制造与测量。普通创客空间无需达到该配置，但可作为**顶配知识边界**与设备演进方向参考：了解研究级在用什么设备、做什么研究，可反推哪些技术将在 5–10 年后下沉到教育级/社区级。

### 8.1 CBA 是什么

- 跨学科倡议，探索**计算机科学与物理科学之间的边界**："把数据变成东西（turn data into things），把东西变成数据"
- 2001 年由美国国家科学基金会（NSF）资助启动，创建跨学科、跨尺度（原子→建筑）的数字制造设施
- 四条主线：管理设施 / 运行研究项目 / 指导学生 / 与赞助商合作 + 创业 + 公众科普

### 8.2 研究方向（前沿技术雷达）

| 方向 | 说明 |
|------|------|
| 量子计算 | 分子核自旋实现最早期的完整量子计算之一 |
| 物理单向加密 | 介观光散射实现物理单向加密函数 |
| 微流体气泡逻辑 | 用气泡做逻辑门——"比特"同时传输材料与信息 |
| 异步逻辑自动机 | 让硬件与软件对齐的异步逻辑 |
| 智能基础设施 | 面向能效的智能基础设施 |
| 合成生命 | 重新编码基因组、创造合成生命 |
| 编码折叠（coded folding）| "编程物质"——由折叠规则决定全局结构的材料 |
| 数字材料加法组装 | 用离散"数字材料"（类乐高：有限构件+可逆连接）自组装成功能结构（官网首页四格图即数字材料受力演变示意）|

### 8.3 课程体系（Fab Academy 的"母本"课程谱系）

CBA 课程 = Fab Academy / Academany 的源头，多年持续迭代：

| 课程 | 首开 | 最近一期 | 说明 |
|------|------|----------|------|
| **How to Make (almost) Anything** | 2003 | 2026 | **Fab Academy 母本**，每年一届 |
| How to Make Something That Makes (almost) Anything | 2004 | 2024 | "制造制造机器的机器"（MTM）|
| The Nature of Mathematical Modeling | 2005 | 2026 | 数学建模方法论 |
| The Physics of Information Technology | 2006 | 2025 | 信息技术物理 |
| How to Grow (almost) Anything | 2019 | 2022 | 生物制造 / 合成生物学方向 |
| How to Design (almost) Anything | 2017 | 2017 | 设计方法论 |

### 8.4 设备配置（四尺度分组，研究级顶配）

CBA 工具按 **nano（纳米）/ micro（微米）/ meso（毫米–米）/ macro（米以上）** 四组，设备 24 小时开放给研究项目；另设 instrumentation / biology / computation / communication 四类能力。代表设备：

| 尺度 | 代表设备 | 用途 |
|------|----------|------|
| **Nano**（纳米级）| Hitachi FlexSEM 1000（SEM，4nm@20kV）、Keysight 5500 SPM（原子力显微镜）、EMS 150TES 镀膜机、TPT HB05 引线键合机 | 纳米成像/元素分析/EBL 光刻/封装互连 |
| **Micro**（微米级）| Light Conversion Pharos 15W（飞秒激光）、Oxford A 系列激光微加工、Rigaku CT Lab HX130（X 射线显微 CT，2.1 voxel 分辨率）、Zeiss LSM 500 共聚焦显微镜 | 飞秒加工/微切割/三维断层扫描/形貌与生物成像 |
| **Meso**（毫米–米）| BOY 35 注塑机、Neoden IN6C 回流焊、xTool F2 UV / F2 Ultra / F1 Ultra / P3（UV·二极管·光纤·CO₂ 激光）、Desktop Metal Shop/Studio（金属 3D 打印）、Stratasys J55（全彩）、Formlabs Fuse 1+（SLS）/ Form 3（SLA）、Markforged Mark Two（连续纤维复材）、Prusa Pro HT90（PEEK 等高温）/ XL（5 头多材料）/ i3 MK4S、Flashforge Creator Pro 2、Sodick SL400G 线切割、Roland MDX-540（4 轴 CNC）/ SRM-20 / GS-24 刻字机、Makera Carvera（自动换刀，铣 PCB）、Mechatronika M10V 贴片机、Buehler IsoMet 1000 精密切割、Orion PA 230 点焊机、Brother SE1800 刺绣缝纫机 | 注塑/回流焊/激光切割雕刻/金属3D打印/SLS/SLA/纤维复材/高温塑料/线切割/CNC/PCB铣削/贴片/焊接/纺织 |
| **Macro**（米以上）| DMG MORI NLX 2500 车铣复合加工中心（27.8" 车削长度，Y 轴 ±60mm）等 | 大型机加工 |

> **启示**：CBA 的 **meso 尺度清单**（激光/3D 打印/CNC/线切割/贴片/回流焊/焊接）与创客空间"金标准"设备栈高度同构，仅型号为工业级；nano/micro/macro 是研究级独有，提示未来设备演进方向（如显微 CT、金属打印、纤维复材、大型机加工）。

### 8.5 其他资源入口

- **people**：Neil Gershenfeld（主任）、Marissa Marcoux（运营）、Dan Gilbert（工坊/实验室）、Sherry Lassiter（外联/fab labs）；现任成员含 Alfonso Parra Rubio、Camron Blackburn、Jake Read 等（多位 FAB26 演讲者）
- **alumni 明星**：Nadya Peek（UW）、Saul Griffith（MacArthur 奖）、Max Lobovsky（Formlabs）、Manu Prakash（TED Fellow）、Jason Taylor（Facebook VP）、Ara Knaian（Project Ara）——CBA 堪称数字制造"创业黄埔军校"
- **sponsors（资助方，反映产业兴趣方向）**：Toyota、Google、Autodesk、Nike、P&G、Cisco、Microsoft、Airbus、Spirit AeroSystems、Dassault/SolidWorks、NIH、NIST、Philips 等
- **docs**：Papers + Theses（论文 / 学位论文库）
- **news**：CBA 季刊 Newsletter（2007–2026 全存档）
- **events**：FAB26/FAB25/历届 FABx 大会、Mel King Festschrift、Interspecies Internet Workshop 等

## 相关文档

- [../03-设备与工具/设备清单与选型.md](../03-设备与工具/设备清单与选型.md)
- [../06-资源索引/工具设备与摆放管理-资源汇总.md](../06-资源索引/工具设备与摆放管理-资源汇总.md)
- [../02-空间搭建/低成本入门方案.md](../02-空间搭建/低成本入门方案.md)
- [../01-创客文化与源流/Neil思想与数字制造革命.md](../01-创客文化与源流/Neil思想与数字制造革命.md)
- [../05-案例研究/全球Fab-Lab案例.md](../05-案例研究/全球Fab-Lab案例.md)

---

## 附录：inventory.fabcloud.io 502 故障诊断与离线替代（2026-08-26）

### 1. 诊断结论

| 项目 | 结果 |
|------|------|
| 现象 | `inventory.fabcloud.io` 返回 HTTP 502 |
| 真实原因 | **不是网络/不是单个站点**——502 页面标题为 "Waiting for GitLab to boot"：整台 **FabCloud GitLab 服务器（gitlab.fabcloud.org）正在重启/启动**，清单站点与源码仓库共用该基础设施，故同时不可用 |
| 验证方法 | `curl -I https://inventory.fabcloud.io/` → 502；`gitlab.fabcloud.org/inventory/inventory.fabcloud.io/-/raw/main/public/inv.toml` → 同一 502 |
| 恢复预期 | 官方页面提示 "up to a few minutes"；实测 6 次探测（间隔 20s，17:43–17:45）仍全 502，实际恢复时间可能 30 分钟–数小时，需周期性重试 |
| Wayback Machine | ⚠️ **该域名无任何历史存档**（CDX 查询为空），不可依赖存档恢复 |

### 2. 恢复后如何抓取全量数据（一键脚本）

已保存脚本：`存档/fetch-fab-inventory.sh`。服务恢复后运行一次即可：

```zsh
chmod +x "创客空间知识库/06-资源索引/存档/fetch-fab-inventory.sh"
"创客空间知识库/06-资源索引/存档/fetch-fab-inventory.sh"
```

将抓取三种格式到 `存档/` 目录：
- `inv.toml` —— 源数据（推荐，含每类设备的型号/描述/来源/价格/数量/关税编码/原产地，可用于逐项对照选型）
- `inv.json` —— 机器可读（后续可导入知识库自动化处理）
- `inv.xlsx` —— 表格版（适合直接分发核对）

> 抓取后建议：把 inv.toml 与《设备清单与选型.md》逐类对照，标注哪些条目适配科普场馆需求。

### 3. 离线替代：Fab Foundation 最低设备标准（文字版）

502 期间可用此标准核对选型，与真实实验室实例（本文件第五节）交叉验证。来源：Fab Foundation 标准 / Fab Academy 节点要求（经 Grokipedia 整理，2025 年更新）：

| 类别 | 最低标准 | 典型机型/规格 | 加工能力 |
|------|----------|--------------|----------|
| CNC 铣床（大格式） | 必备 | ShopBot 级大格式路由器，工作面积可达 **4'×8'** | 减材加工：木材/塑料/蜡/铝 3D 造型 |
| 激光切割机 | 必备 | Epilog 级 CO₂ | 2D 切割/雕刻，薄板材，精度公差可达 **0.1mm**（press-fit 装配） |
| 乙烯基切割机 | 必备 | Roland 级，大格式可达 4'×8' | 标牌/模板/软材料/可穿戴电子接口 |
| 3D 打印机 | 标配（非强制） | RepRap 风格 FDM | 增材：PLA/ABS 逐层沉积，复杂几何 |
| 电子工作台 | 必备 | Arduino 微控制器 + 焊台 + 示波器 + **PCB 铣削** | 铜箔基板直接铣 PCB，实验室自制电路 |
| 开源软件栈 | 必备 | FreeCAD（参数化3D）/ Inkscape（2D矢量SVG）/ GIMP（光栅）/ PyCAM（CAM生成G-code） | 设计→制造全流程免费工具链 |

> 注：截至 2025 年，Fab 网络已大量采用桌面级低价设备（紧凑 CNC + 消费级 3D 打印机），初始成本从数十万美元降至数万美元，与本文件第六节成本基线一致。
