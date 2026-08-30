---
title: "GitHub开源资源索引（本项目专项）"
type: 资源索引
scope: 本项目专项
source: "GitHub开源项目调研"
date: 2026-08
tags: [GitHub, 开源项目, 实训基地, 机器人, CNC]
---

# GitHub开源资源索引（本项目专项）

> 某职业院校创客空间（三专业共享）项目相关的GitHub开源项目与资源汇总：空间布局、机器人、新能源汽车、CNC、安全规范、模块化家具、四足机器狗
> 调研时间：2026-08 ｜ 收集方式：GitHub站内搜索 + site:github.com限定搜索
> 定位：本文是 [资源总索引.md](资源总索引.md) 的专项补充，聚焦本项目7个需求差距主题对应的开源资源。

---

## 一、创客空间布局与设计

| 项目 | 链接 | 核心价值 | 适用主题 |
|------|------|---------|---------|
| **MuMaLab Space Layout** | [munichmakerlab/space-layout](https://github.com/munichmakerlab/space-layout) | 慕尼黑创客空间的历史/当前/未来布局DXF文件，可直接参考空间规划思路 | 空间布局、L型规划 |
| **Tinker's Lab Layout** | [agarwal-dev/Tinkers-Lab-Layout](https://github.com/agarwal-dev/Tinkers-Lab-Layout) | AutoCAD 2D平面图，含设备定位和动线规划，实验室搭建阶段的参考模板 | 平面布局、设备定位 |
| **Waukesha Makerspace Floor Plan Tool** | [masterprompt/waukesha-makerspace-floor-layout-tool](https://github.com/masterprompt/waukesha-makerspace-floor-layout-tool) | 交互式平面图创建工具（React），可拖拽布局，有在线Demo | 布局验证、方案比选 |
| **Past-Lives Makerspace plfog** | [Past-Lives-Makerspace/plfog](https://github.com/Past-Lives-Makerspace/plfog) | 交互式矢量地图应用，按房间颜色编码状态（可用/占用/维护），含尺寸和价格 | 空间管理、状态可视化 |
| **makerspace-gt/interieur** | [makerspace-gt/interieur](https://github.com/makerspace-gt/interieur) | 德国亚琛工大创客空间的家具/工具/设备完整清单（德语），含3工作台、1木工台、2工具柜等 | 设备清单、家具配置 |
| **Maker-Ed Makerspace Playbook** | [Maker-Ed/Makerspace-Playbook](https://github.com/Maker-Ed/Makerspace-Playbook) | 创客空间手册开源版，含工具材料、安全考虑、维护、纺织品等章节 | 运营手册、工具材料 |

---

## 二、机器人实训与安全

| 项目 | 链接 | 核心价值 | 适用主题 |
|------|------|---------|---------|
| **Industrial Robotics GP7 Safety Simulation** | [djb222/industrial-robotics-gp7-safety-simulation](https://github.com/djb222/industrial-robotics-gp7-safety-simulation) | 安川GP7机器人的Python安全仿真，含安全围栏/屏障建模、碰撞检测、多机器人协同 | 安全围栏设计、碰撞验证 |
| **RoboMaster Simulator** | [alvinliu97/RoboMaster-Simulator](https://github.com/alvinliu97/RoboMaster-Simulator) | 上海科技大学的RoboMaster AI挑战赛Gazebo仿真器，含多智能体导航、裁判系统、射击功能 | 竞赛场地、仿真训练 |
| **rmoss_gazebo** | [liukong1220/rmoss_gazebo](https://github.com/liukong1220/rmoss_gazebo) | RoboMaster开源软件栈的Gazebo仿真，支持算法原型研究和比赛应用开发 | 竞赛训练、算法开发 |
| **RoboMaster战队培训课程** | [lvxin1024/2026-AIM-Courses](https://github.com/lvxin1024/2026-AIM-Courses) | 2025-2026年度RoboMaster新成员培训课程，算法/电控/机械双方向 | 课程体系、培训资源 |
| **VEX Push Back 2025-2026** | [anthonychen752/vex-push-back-2](https://github.com/anthonychen752/vex-push-back-2) | VEX 2025-2026赛季"狭路相逢"赛题的AI方案，含Jetson Nano+RealSense+YOLO | 竞赛方案、视觉识别 |
| **VEX V5 Competition Knowledge** | [ISB-Dragon-Robotics/knowledge_base](https://github.com/ISB-Dragon-Robotics/knowledge_base) | 国际学校VEX机器人竞赛知识库，含12ft×12ft场地说明、2v2赛制 | 竞赛规则、场地标准 |
| **Engineering Innovation Robot Control** | [TianBingzhuo/engineering-innovation-robot-control](https://github.com/TianBingzhuo/engineering-innovation-robot-control) | 2400×2400mm竞赛场地规则，含起始区、安全区、三角截面围栏设计 | 场地设计、安全围栏 |
| **ChipuRobo Challenge Arena** | [kevinekitabu/Afrobotics](https://github.com/kevinekitabu/Afrobotics) | 模块化竞赛场地设计：1×1m起始区+2m障碍区+1.2m门区+1×1m交付区 | 小型竞赛场地、模块化 |

---

## 三、四足机器狗（教育/开源）

| 项目 | 链接 | 核心价值 | 适用主题 |
|------|------|---------|---------|
| **go2-quadruped-sim** | [AOShei/go2-quadruped-sim](https://github.com/AOShei/go2-quadruped-sim) | Unitree Go2的ROS2 Jazzy完整仿真包，含自主导航、SLAM建图、CHAMP运动控制器，专为教育设计 | 四足仿真、教学平台 |
| **quadruped-dog-rl** | [darshmenon/quadruped-dog-rl](https://github.com/darshmenon/quadruped-dog-rl) | Go2/Spot/Mini Cheetah/ANYmal的RL运动训练工作区，MuJoCo+Gazebo+PPO策略+多地形 | 运动控制、强化学习 |
| **Unitree Go2 EDU ROS2** | [is-buiquocdoanh/unitree_go2_edu](https://github.com/is-buiquocdoanh/unitree_go2_edu) | Go2 EDU版的ROS2 Humble工作区，含bringup、URDF、Nav2导航、SLAM建图 | 教育版开发、导航 |
| **go2_ros2_sdk** | [targabor/go2_ros2_sdk](https://github.com/targabor/go2_ros2_sdk) | Go2 AIR/PRO/EDU的ROS2 SDK，支持WebRTC(WiFi)和CycloneDDS(以太网)双协议 | 软件开发、二次开发 |
| **Awesome Quadruped Locomotion** | [Xbotics-Embodied-AI-club/Xbotics-QuadPlatform](https://github.com/Xbotics-Embodied-AI-club/Xbotics-QuadPlatform) | 四足机器人运动控制资源汇总，含Unitree官方RL环境、Isaac Lab仿真、Sim→Real迁移 | 资源汇总、技术路线 |
| **Unitree Go2W AI-Agent SDK** | [grasp-lyrl/unitree_go2w_agent_sdk](https://github.com/grasp-lyrl/unitree_go2w_agent_sdk) | UPenn开发的Go2W+AgileX Piper臂的AI-Agent SDK，支持LLM自主智能体 | 具身智能、AI应用 |
| **Go2 Guide Dog** | [SooratiLab/go2-guide-dog-tutorial](https://github.com/SooratiLab/go2-guide-dog-tutorial) | Go2改造成导盲犬的ROS2项目，含LiDAR避障、YOLOv8目标检测 | 应用案例、感知开发 |

---

## 四、新能源汽车与电池

| 项目 | 链接 | 核心价值 | 适用主题 |
|------|------|---------|---------|
| **MathWorks Battery Systems** | [MathWorks-Teaching-Resources/Battery-Systems](https://github.com/MathWorks-Teaching-Resources/Battery-Systems) | MathWorks官方电池系统教学资源，含电池包设计、单体建模（电/热）、BMS基础、SoC估算，MATLAB/Simulink/Simscape | 电池教学、BMS实训 |
| **EV with MATLAB and Simulink** | [mathworks/EV-with-MATLAB-and-Simulink](https://github.com/mathworks/EV-with-MATLAB-and-Simulink) | 电动车建模资源合集：电池系统建模、电池包建模、热管理、电驱动仿真 | 整车仿真、教学演示 |
| **Simscape Automotive Student Teams** | [mathworks/Simscape-Essentials-for-Automotive-Student-Teams](https://github.com/mathworks/Simscape-Essentials-for-Automotive-Student-Teams) | 学生车队用Simscape模型，含电动动力总成仿真（电机+电池+SOC/SOH估算） | 电驱动教学、参数匹配 |
| **MiniBMS** | [ks-santosh/MiniBMS](https://github.com/ks-santosh/MiniBMS) | 开源迷你BMS：库仑计数SoC、电压/温度监控、电池容量计算，适合教学理解BMS原理 | BMS原理、开源硬件 |
| **LabVIEW EV and BMS** | [Krishna-Pai/LabVIEW-Electrical-Vehicle-and-Battery-Management-System](https://github.com/Krishna-Pai/LabVIEW-Electrical-Vehicle-and-Battery-Management-System) | NI LabVIEW的电动车与BMS课程，含PXI高速数据采集、电池包模块测试 | 数据采集、测试实训 |
| **Lithium Battery Charge-Discharge Animation** | [edutechtammy/lithium-battery-charge-discharge](https://github.com/edutechtammy/lithium-battery-charge-discharge) | 交互式锂电池充放电动画教学，纯HTML单文件，可直接用于课堂演示 | 教学演示、原理可视化 |
| **Automotive Embedded Systems Portfolio** | [keshwapanthula/automotive-embedded-systems-portfolio](https://github.com/keshwapanthula/automotive-embedded-systems-portfolio) | 汽车嵌入式系统面试/学习项目，含EV动力总成、AUTOSAR、ISO 26262功能安全 | 功能安全、嵌入式开发 |

---

## 五、桌面CNC与粉尘控制

| 项目 | 链接 | 核心价值 | 适用主题 |
|------|------|---------|---------|
| **Hübel Home Friendly CNC Mill** | [fellesverkstedet/fabricatable-machines](https://github.com/fellesverkstedet/fabricatable-machines/tree/master/hubel-home-friendly-cnc-mill) | ⭐ **最相关**：开源"家庭友好型"CNC，粉尘/噪音/烟气全封闭内置，吸尘器藏在柜内，透明门安全联锁，匹配IKEA PAX衣柜尺寸（100×58×200cm），加工区800×1220×55mm | 全封闭CNC、粉尘噪音控制、宿舍场景 |
| **TseNC-Pro CNC** | [Hinkleaj/TseNC-Pro_CNC_Machine](https://github.com/Hinkleaj/TseNC-Pro_CNC_Machine) | 开源全封闭CNC，600×370×145mm加工区，铝板+钢框架，T型槽铝台面，带冷却系统和全封闭罩，可无人值守切铝 | 全封闭CNC、金属加工 |
| **Sienci LongMill Dust Shoe** | [Sienci-Labs/Resources](https://github.com/Sienci-Labs/Resources/blob/main/longmill/lm-assembly/lm-assembling-add-ons.md) | LongMill CNC的磁吸式集尘罩设计，支持1.5"/2"/2-1/8"吸尘管，Z轴独立式，含安装教程 | 集尘罩设计、粉尘控制 |
| **3018 Mill Knowledge Base** | [doug-harriman/3018-Mill](https://github.com/doug-harriman/3018-Mill) | Genmitsu 3018 Pro CNC的知识库，含封闭罩改造（降噪+防尘+激光烟雾）、电源/USB穿线孔设计 | 低成本CNC改造、封闭罩DIY |
| **DIY CNC Machine** | [Arcustomzs556/DIY-CNC-machine](https://github.com/Arcustomzs556/DIY-CNC-machine) | 自制CNC完整方案，含3D打印吸尘漏斗STL/OBJ文件、铝型材框架、集尘罩设计 | DIY方案、集尘配件 |
| **Home-Made CNC Milling Machine** | [pratanczuk/cnc_mill](https://github.com/pratanczuk/cnc_mill) | 自制CNC铣床的完整BOM和成本明细（金属外壳DIN导轨、电脑、电气件等），含价格参考 | 成本估算、BOM参考 |
| **Big Yellow Proxxon MF70 CNC** | [dheera/big-yellow-proxxon-mf70-conversion](https://github.com/dheera/big-yellow-proxxon-mf70-conversion/) | Proxxon MF70小型铣床的CNC改造方案，作者强烈推荐加封闭罩，适合黄铜等小件精密加工 | 小型CNC、封闭罩建议 |

---

## 六、安全规范与SOP

| 项目 | 链接 | 核心价值 | 适用主题 |
|------|------|---------|---------|
| **CODE Makerspace** | [codeuniversity/makerspace](https://github.com/codeuniversity/makerspace) | ⭐ 柏林CODE大学创客空间的完整文档：设备准入制度、PPE规范（护目镜/面罩/手套/耳罩）、铣床/激光/3D打印/缝纫机/切纸机各设备SOP | 安全SOP、PPE规范、设备准入 |
| **CODE Milling Machine SOP** | [codeuniversity/makerspace/milling-machine.md](https://github.com/codeuniversity/makerspace/blob/main/milling-machine.md) | 铣床安全操作规范：实操能力测试制度、PPE要求、教师授权制 | 铣床安全、培训考核 |
| **CODE Basic Access** | [codeuniversity/makerspace/basic-access.md](https://github.com/codeuniversity/makerspace/blob/main/basic-access.md) | 创客空间基础准入：行为准则、PPE选择指南、电动工具安全 | 准入制度、PPE选择 |
| **Contemporary Physics Lab Safety** | [Contemporary-Physicslab/Labsafety](https://github.com/Contemporary-Physicslab/Labsafety) | 物理实验室安全导论：实验前安全检查清单、风险评估、 supervisor审核制度 | 安全检查清单、风险评估 |
| **Setting Up Physics and Electronics R&D Lab** | [Gist: nup002](https://gist.github.com/nup002/912383615b12dc1ec44ae9004c40b11f) | 物理/电子研发实验室搭建指南：ESD防护（防静电地板/腕带/离子风机）、元件库管理、耗材清单 | ESD防护、实验室搭建 |
| **UoA DTRG Safety Guidelines** | [UoA-DTRG/docs/wiki](https://github.com/UoA-DTRG/docs/wiki/Safety-Guidelines) | 无人机/机器人团队安全指南：最小安全距离（人30m/建筑50m/机场100m）、天气限制、紧急停机 | 机器人安全、飞行安全 |
| **SmallHall Makerspace Rules** | [SmallHallMakerspace/meta/wiki](https://github.com/SmallHallMakerspace/meta/wiki/Makerspace-Rules-of-Conduct) | William & Mary大学创客空间行为准则：设备操作前阅读说明书、事故报告制度、材料管理 | 行为准则、运营管理 |
| **Noisebridge Rules** | [Gist: brennanMKE](https://gist.github.com/brennanMKE/327c6e8b853380cc919182fd22db5a60) | Noisebridge黑客空间规则：电气安全（电路过载）、通风要求、社区环境考量 | 电气安全、通风要求 |

---

## 七、铝型材模块化家具与工作台

| 项目 | 链接 | 核心价值 | 适用主题 |
|------|------|---------|---------|
| **OpenBench** | [overgodev/openbench](https://github.com/overgodev/openbench) | ⭐ 2020铝型材+木质台面的模块化工作台和置物架系统，轻量、可扩展、易组装 | 模块化工作台、铝型材家具 |
| **Aluminum Furniture（中文）** | [649472774/aluminum-furniture](https://github.com/649472774/aluminum-furniture) | ⭐ 参数化2020欧标铝型材家具设计，OpenSCAD+NopSCADlib+Python流水线：改一个数→自动出渲染图/BOM/切割单/受力分析 | 参数化设计、BOM自动生成、受力分析 |
| **AluExt** | [ben-gineering/aluext](https://github.com/ben-gineering/aluext) | 铝型材配件的参数化3D模型，可定制3D打印的安装座/连接件，快速迭代 | 3D打印连接件、配件 |
| **FrameForgeMod** | [q921057310-byte/FrameForgeMod](https://github.com/q921057310-byte/FrameForgeMod) | FreeCAD的铝型材框架工作台模组，含国标/欧标多种槽宽（20/30/60系列），自动BOM | FreeCAD设计、型材框架 |
| **extrusionBench** | [rgon/extrusionBench](https://github.com/rgon/extrusionBench) | FreeCAD的参数化铝型材库，含DOLD Mechatronik的CAD数据提取脚本 | CAD库、型材模型 |
| **OpenSCAD Aluminum Extrusion Library** | [ServerNinja/OpenSCAD_AluminumExtrusionProfile_Library](https://github.com/ServerNinja/OpenSCAD_AluminumExtrusionProfile_Library) | OpenSCAD的铝型材截面库，可生成任意长度的型材3D模型 | 开源CAD、参数化建模 |
| **16Motion Carriage** | [mosomate/16motion](https://github.com/mosomate/16motion) | 3D打印的铝型材滑台小车，适配≤40mm宽型材，含684轴承+M3/M4螺丝，8个安装点 | 滑动机构、DIY配件 |

---

## 八、开源制造设备与Fab Lab

| 项目 | 链接 | 核心价值 | 适用主题 |
|------|------|---------|---------|
| **Awesome FOSS Manufacturing** | [bruno-dogancic/awesome-foss-manufacturing](https://github.com/bruno-dogancic/awesome-foss-manufacturing) | 去中心化制造的开源硬件/软件精选列表，含激光切割、3D打印、CNC、多工具平台等 | 开源设备资源汇总 |
| **BigFDM** | [fab-machines/BigFDM](https://github.com/fab-machines/BigFDM) | 开源大尺寸3D打印机，Fab Lab UAE开发，使用标准Fab Lab设备和技术制造 | 开源设备、Fab Lab |
| **Jubilee** | (Machine Agency UW) | 开源多工具运动平台，支持3D打印、液体处理、探测等，在awesome-foss列表中 | 多工具平台、研究设备 |
| **Seattle Makers Tools Wiki** | [seattlemakers/docs/wiki](https://github.com/seattlemakers/docs/wiki/Tools-And-Equipment) | 西雅图创客空间的工具设备清单，含Shapeoko CNC（30×30英寸）、材料适配范围等 | 设备清单、参数参考 |
| **Awesome FabAcademy** | [MichaelMartinez/awesome-fabacademy](https://github.com/MichaelMartinez/awesome-fabacademy) | Fab Academy资源汇总：开源软件、3D模型库、教程等 | Fab Academy、教学资源 |
| **FabLab Chengdu** | [fablab-chengdu](https://github.com/orgs/fablab-chengdu/repositories) | 成都Fab Lab的开源项目集合，含OpenPCR、OpenCT等开源科学仪器 | 开源仪器、国内Fab Lab |

---

## 九、高价值项目深度推荐

### 9.1 最值得参考的Top 5

1. **Hübel Home Friendly CNC Mill** — 完美匹配"宿舍场景下的全封闭CNC"需求，内置吸尘+噪音控制+安全联锁，IKEA衣柜尺寸可直接参考
2. **CODE Makerspace** — 完整的大学创客空间安全文档体系，PPE/准入/SOP可直接借鉴改写
3. **Aluminum Furniture（中文项目）** — 参数化铝型材家具，自动出BOM和切割单，非常适合硬装后轻量化改造的工作台/隔断设计
4. **go2-quadruped-sim** — Unitree Go2教育版的ROS2仿真，四足机器狗教学的软件基础
5. **MathWorks Battery Systems** — 官方电池系统教学资源，新能源汽车专业的理论教学配套

### 9.2 可直接复用的模板

| 模板 | 来源 | 用途 |
|------|------|------|
| 设备SOP模板 | CODE Makerspace | 铣床/激光/3D打印等设备操作规范 |
| 安全检查清单 | Contemporary Physics Lab | 实验前风险评估checklist |
| BOM自动生成 | aluminum-furniture | 铝型材家具的物料清单和切割单 |
| 集尘罩STL | DIY-CNC-machine | 3D打印吸尘漏斗模型 |
| 平面图模板 | Tinker's Lab Layout | AutoCAD布局参考 |

---

## 十、使用建议

1. **先看文档再看代码**：多数项目的README和Wiki比代码更有参考价值
2. **关注教育版（EDU）**：Unitree Go2 EDU、MathWorks Teaching Resources等专为教育设计
3. **开源协议注意**：商用/教学使用前检查LICENSE（MIT/Apache最宽松，GPL需开源衍生）
4. **Issue区有宝藏**：很多项目的Issue区有用户实际搭建经验和问题解答
5. **国内镜像**：GitHub访问慢时可用ghproxy.com等镜像加速下载

---

## 与现有知识库的衔接

- **资源总索引**：[资源总索引.md](资源总索引.md)（全资源导航）
- **工具设备资源**：[工具设备与摆放管理-资源汇总.md](工具设备与摆放管理-资源汇总.md)
- **空间搭建文档**：../02-空间搭建/（7篇本项目专项文档）
- **新能源实训**：[../02-空间搭建/新能源汽车部件实训区设计.md](../02-空间搭建/新能源汽车部件实训区设计.md)
- **机器人实训**：[../02-空间搭建/机器人实训区设计.md](../02-空间搭建/机器人实训区设计.md)
- **桌面CNC**：[../02-空间搭建/带盖桌面CNC选型与摆放规范.md](../02-空间搭建/带盖桌面CNC选型与摆放规范.md)
- **轻量化改造**：[../02-空间搭建/硬装已完成空间轻量化改造方案.md](../02-空间搭建/硬装已完成空间轻量化改造方案.md)
