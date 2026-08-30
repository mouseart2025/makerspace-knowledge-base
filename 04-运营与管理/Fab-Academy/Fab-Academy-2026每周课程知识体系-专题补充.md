---
title: "Fab Academy 2026 每周课程知识体系 · 专题补充"
type: 专题补充
scope: 通用
source: "Fab Academy官网2026"
date: 2026-08
tags: [Fab Academy, 2026, 每周课程, 知识体系]
---

# Fab Academy 2026 每周课程知识体系 · 专题补充

> 逐周深挖 19 个课程内容页（fabacademy.org/2026/classes/*/index.html）的完整知识体系：核心概念、知识要点、工具链、作业要求
> 调研时间：2026-08 ｜ 来源：官方日程页每周课程链接逐页抓取
> 定位：本文是 Fab Academy 系列的**第四篇**——在「学员（实战全解）/ 机构（平台与运营机制）/ 课程日历（2026 日程专题）」三视角之后，深入**每周课程内容本体**。前篇见 [Fab-Academy-2026课程日程-专题补充.md](Fab-Academy-2026课程日程-专题补充.md)。

---

## 〇、课程页面的通用结构（先看懂"怎么读"）

Fab Academy 每周课程页（`classes/<主题>/index.html`）不是讲义正文，而是 Neil Gershenfeld 式的**大纲 + 资源索引**：

| 要素 | 说明 |
|------|------|
| **大纲树** | 用缩进文本列出全部知识点（本周"教什么"的完整地图）|
| **hello board 生态** | 几乎每个知识点配一块可直接制造的参考电路板：board 图 + 元件清单 + 走线图 + 内廓图（PCB 铣削用）+ 三语言代码（C/Arduino/MicroPython）+ 演示视频 |
| **inventory 联动** | 页头链接 inventory.fabcloud.io 按本周 purpose 筛选设备/元件 |
| **assignment** | 页尾两段式作业：**小组作业**（表征实验，测机器/测器件）+ **个人作业**（设计-制造-编程闭环）+ extra credit |
| **学生案例** | 大量往届学生页面作为教学案例（"用学生作品教学生"传统）|

**三视角闭环的作业设计**贯穿全程：
1. 小组作业 = **科学表征**（测 kerf / 测功耗 / 测设计规则 → 建立机器参数基线）
2. 个人作业 = **工程闭环**（自己设计 + 自己制造 + 自己编程 + 文档化）
3. 附加分 = **边界突破**（换工艺 / 换语言 / 加难度）

---

## 一、逐周知识体系（W1–W19）

### W1 · Principles and Practices + Project Management（理念与项目管理）

- **核心**：数字制造（digital fabrication）总览；权利与责任（charter 章程：学术诚信、安全、协作）
- **知识点**：数字制造历史与原理、Fab Lab 起源、期末项目规划方法
- **讲义**：`ng.cba.mit.edu/show/script/26.01.fab.html`（快捷键 `i` 看索引，配视频）
- **作业**：plan and sketch a potential final project（规划并草图一个潜在期末项目）；"plan" 内嵌**往届项目 Google CSE 检索引擎**，"final project" 内嵌项目开发方法论页
- **资源**：FAQ、章程、往届项目检索（cse.google.com）、Project Development 页

### W2 · Computer-Aided Design（计算机辅助设计）★工具全景最全

- **核心概念对**：光栅 vs 矢量｜2D vs 3D｜**BRep/FRep/VRep**（边界/函数/体积三大 3D 表示法）｜GUI/脚本/HDL 三种交互方式｜命令式/声明式/生成式/优化/MDO/AI 设计范式
- **FreeCAD 教学体系**（26 个视频）：工作台/捕捉/坐标 → 拉伸/旋转/放样/扫掠 → CSG → 圆角倒角 → 约束/构造几何 → 投影/剖切 → 装配 → **参数化/编程化/算法化建模** → 制图/渲染/动画/CAM
- **工具矩阵**（约 100+）：2D（GIMP/Inkscape/Photoshop/QCAD）→ 3D 入门（SketchUp/Tinkercad/Blender）→ NURBS 参数化（Rhino+Grasshopper/Solvespace/FreeCAD）→ 商业 CAD（Fusion 360/SolidWorks/Onshape）→ 高端工业（Catia/NX）→ **脚本建模系**（OpenSCAD/CadQuery/Antimony/libfive，MIT CBA 一脉）→ 仿真（FEA：FreeCAD FEM/CalculiX、物理：PyBullet）→ 游戏引擎/VRAR → 音视频（ffmpeg/OBS）→ **AI**（LLM/文生图/文生 3D/Text-to-CAD）
- **作业**：对潜在期末项目做多模态建模（光栅/矢量/2D/3D/渲染/动画/仿真）+ 压缩图片视频 + 连同设计文件发布到课程页
- **必读**：**Matt Keeter 论文**（3D 表示类型学 + ASDF，本页理论核心）

### W3 · Computer-Controlled Cutting（计算机控制切割）★激光知识最全

- **切割工艺谱系**：刀具（Cricut/Roland/Zund）→ 激光（Epilog/Trotec/xTool/OLSK）→ 等离子 → 水刀（OMAX/WAZER）→ 热丝 → 线切割 EDM
- **激光物理**：受激辐射原理、增益介质与波长对照表（CO₂ 10.6μm / 光纤 1-2μm / Nd:YAG 1064nm / UV 355nm…）、四种切割机理（燃烧/熔化/蒸发/烧蚀）
- **工艺参数**：焦点/功率/速度/切割次数/坐标系/kerf 补偿/矢量 vs 光栅模式
- **材料学**：纸板（ECT 44）/胶合板/亚克力（粘接热弯）/POM/织物/**PVC 禁切**/玻璃需涂层/金属需 kW 光纤
- **应用**：press-fit 压合结构（接头类型/间隙/应力集中/参数化）、活动铰链、柔性结构、丝网印刷半调、3D 雕刻
- **乙烯基切割**：标牌/热转印/铜箔柔性电路/喷砂模板；参数（压力/速度/深度）；weeding 去废料技巧
- **安全**：激光等级、通风排烟、镜片清洁、全程看护、灭火毯
- **作业**：小组=安全培训+表征激光机（焦距/功率/速度/kerf/接头间隙）；个人=乙烯基切割一件 + 设计激光切割**参数化构造套件**（含 kerf 补偿）；加分=多种组装方式/非平面元素/雕切结合

### W4 · Embedded Programming（嵌入式编程）

- **架构基础**：冯·诺依曼 vs 哈佛｜RISC vs CISC｜微处理器 vs 微控制器｜字长
- **存储器体系**：寄存器/SRAM/DRAM/EEPFLASH/Flash/熔丝位；外设（GPIO/ADC/PWM/USART/USB）
- **处理器家族谱**：**AVR**（ATtiny412/1614/3216、AVR128DB32）→ **ARM**（SAMD11/21/51、STM32）→ **RP2040**（双核 133MHz、PIO 可编程 IO）→ **Xtensa**（ESP8266/32）→ **RISC-V 开放架构**（ESP32-C3/C6）；教学彩蛋：Megaprocessor、MOnSter 6502 巨型复刻
- **语言层级**：汇编 → C/C++（GCC/make）→ **Rust**（内存安全）→ MicroPython/CircuitPython → **AI 辅助编程**（ChatGPT/Copilot/Cursor + 嵌入式 AI：TinyML/LiteRT/ESP-DL，2026 新增）
- **烧录三体系**：JTAG/SWD（OpenOCD/EDBG）｜UPDI（pyupdi，新 AVR）｜ISP（avrdude，自制 FabISP）
- **时钟/串口/调试/仿真**：RC/陶瓷/石英晶振精度对比；串口工具链；调试（LED/打印/gdb）；仿真（Wokwi/Falstad）
- **作业**：小组=对比不同架构工具链；个人=**通读一款 MCU 完整数据手册** + 写程序实现交互（I/O）与通信（有线/无线）；加分=不同语言/环境

### W5 · 3D Scanning and Printing（3D 扫描与打印）

- **增材 vs 减材**范式；历史（1940s 墙体打印机 → 1984 Hull → 2008 RepRap）
- **工艺类型 10+**：SLA/FDM/SLS/DED-WAAM/Binder Jetting/HP MJF/PolyJet/生物打印/双光子聚合/体积式打印/装配机器人
- **FFF 材料学**：PLA（60℃ 玻璃化、易打）/PETG（80℃、韧）/PHA（可降解）/ABS/TPU/PEEK + 吸湿存储/回收
- **四大动机**：complexity（复杂性免费）/access/net-shape/减废；**六大约束**：失败/分辨率/时间/成本/排放通风/材料
- **设计规则测试体系**（全带 FreeCAD/STL 测试文件）：悬垂/间隙/角度/桥接/壁厚/尺寸精度/**各向异性与打印方向**/填充率/支撑/翘曲/附着力；进阶技巧：arc overhangs 免支撑、brick layers 强化
- **扫描技术 8 大类**：CT 断层/显微探针/**摄影测量**（Meshroom/Polycam）/结构光（POP3）/激光（Artec）/深度相机/LIDAR/牛奶扫描法等
- **格式体系**：STL→3MF/STEP/glTF；FRep；Marching Cubes
- **作业**：小组=测试打印机设计规则；个人=设计打印一个**无法减材制造**的小物体 + 3D 扫描一件

### W6 · Electronics Design（电子设计）

- **元件物理**：电阻（I=V/R）/电容（C=Q/V）/电感/二极管族（PN/Schottky/Zener/LED）/晶体管（BJT 变电流 vs MOSFET 变电阻）/运放（差分放大/负反馈/四种组态）/稳压器与 DC-DC
- **电路定律**：基尔霍夫电流/电压定律、功率 P=I²R、水位类比
- **EDA 全流程**：原理图录入 → 元件布局 → 布线 → DRC/ERC 检查 → 仿真 → 制造；层/过孔/电源平面/铺铜
- **EDA 工具梯队**：入门（Fritzing）→ 开源主力（**KiCad**/LibrePCB/EasyEDA/gEDA）→ 商业（Eagle→Fusion 360/Altium）→ 高端（OrCAD/Cadence）→ 脚本化（**pcb.py/SVG-PCB**，CBA 系）→ 硬件描述语言（Verilog/VHDL）
- **仿真**：数字（Wokwi）/模拟（SPICE/LTspice）/混合信号（Falstad）
- **测试仪器**：可调电源/万用表/示波器/逻辑分析仪
- **作业**：小组=用仪器观测 MCU 运行；个人=用 EDA 工具设计一个基于库存元件的 MCU 系统 + DRC 检查；加分=仿真/另一工作流/设计外壳

### W7 · Computer-Controlled Machining（大型 CNC 铣削）★米级制造

- **切削参数**：切屑负荷 0.001–0.010 英寸；feed rate = RPM × 刃数 × 切屑负荷；切深≈刀径、步距≈刀径/2；**chatter 颤振**
- **刀具学**：钻头 vs 铣刀、刃数/涂层/上切下切/平底球头/V 刀/锥度刀
- **装夹**：台钳/F 夹/气钉/真空吸附/牺牲层找正
- **刀路**：顺铣 vs 逆铣、粗精加工、自适应清角/摆线铣、多轴（2/2.5/3/4/3+2/5 轴）、**T-bone/Dog-bone 内角清角**、**tabs 留料**、**onion skinning**、嵌套排料（Deepnest）、双面加工定位
- **连接与成型**：数字接头图鉴（50 种）、互承框架、张拉整体、kerf 折叠、蒸汽弯曲
- **机床生态**：手持（Shaper Origin）/桌面（Shapeoko/Maslow）/大型（ShopBot/Avid）/金属（Tormach/Haas）；CAM 11 种（mods/VCarvePro/Fusion 360/Mastercam…）
- **材料**：瓦楞纸/MDF/OSB/HDPE/聚碳酸酯/铝/Hylite 复合板
- **安全**（专设板块）：木刺/割伤/烫伤/火灾/刀具断裂；**"你的手不是工具"**；看听闻三觉监控
- **作业**：小组=安全培训+表征机器（跳动/对齐/装夹/转速进给/材料/刀路）；个人=**设计+铣削+装配一件米级物品**；加分=无紧固件无胶/曲面/三轴刀路

### W8 · Electronics Production（电子生产）

- **PCB 制造五路线**：dead bug / **化学蚀刻**（氯化铁/过硫酸盐）/ **铣削**（0.010"、1/64、1/32、V 刀）/乙烯基柔性连接/激光/导电墨水打印/电镀
- **板材**：FR1（酚醛纸，首选可铣）/FR4（环氧玻璃）/Kapton 柔性/高频板；铜厚 0.5/1/2 oz
- **制板厂**：JLCPCB/PCBWay/OSH Park；设计规则（线宽/间距 15/5 mil）；层数/阻焊/丝印/过孔工艺
- **装配工艺树**：**焊接**（有铅/无铅/低温铋基；烙铁/热风/回流焊：钢网+热台+红外；虚焊/连锡检查）→ 贴装顺序（底到顶、内到外）→ **拆焊**（编织带/吸锡器/热风）→ 断线补救/跳线
- **CAM**：Gerber/RS-274X、png 分辨率；**mods**（MIT 模块化 CAM，trace/interior 输出）；FlatCAM/pcb2gcode
- **调试五步**：查焊点 → 查元件方向数值 → 核数据手册 → 量供电 → 探 I/O 信号
- **作业**：小组=表征本实验室 PCB 工艺设计规则 + 向制板厂提交一份设计；个人=**制作并测试自己设计的 MCU 系统**；加分=另一种工艺制作

### W9 · Input Devices（输入设备）★"一物理量一板子"

- **接口四件套**：GPIO/比较器/ADC/**I2C**（NXP AN10216）
- **信号调理**：去抖动、平均滤波屏蔽、**同步检测与扩频**（抗环境光）、传感器融合
- **按物理量全覆盖**（每类配 hello board + 三语言代码）：
  - 开关/电位器（分压→ADC）
  - **磁场**：线性霍尔 A1324、3D 矢量 TLE493D
  - **编码器**：绝对/增量、光学/电容/磁式；MT6835 达 21 位精度
  - **⭐阶跃响应**（篇幅最大）：测时间常数变化 → 感知触摸/多点触摸/位置/压力/湿度/弯曲；自电容（1 引脚）/互电容（2 引脚）两大方案
  - **温度**：电桥/NTC/RTD 铂电阻/红外 MLX90614/热电偶
  - **光**：LED 反偏做光感/光电三极管/颜色 VEML6040/手势 APDS-9960
  - **运动**：多普勒雷达 RCWL-0516/热释电 PIR
  - **距离**：ToF VL53L0X~L5CX/超声 HC-SR04/LIDAR
  - **IMU**：3 轴 ADXL343 → 6 轴 MPU-6050/LSM6DSV16X（含融合）→ 9 轴 BNO085
  - **声音**：MEMS 数字 I2S/模拟驻极体+运放
  - GNSS 定位、RTC 时钟、脉搏 MAX30102、气压 DPS310、图像（ESP32-S3 CAM/Grove Vision AI）
- **作业**：小组=探测输入设备的模拟与数字信号；个人=**在自己设计的板上加传感器并读取数据**

### W10 · Output Devices（输出设备）★"从 mA 到 kA 功率谱系"

- **电气安全**（开篇）：1mA 安全/10mA 肌肉收缩/**100mA 心室纤颤**；人体内外电阻；反接保护/反电动势/连接器防呆
- **电源管理**：线径选择、USB PD 生态、超级电容/LiPo（安全储存）、无线供电
- **电流测量五法**（小组作业支撑）：电流表/电源特性/采样电阻/磁场/电感
- **器件驱动谱系**（全部配 hello board）：
  - **LED**：限流→PWM 调光→**Charlieplexing 查理复用**→可寻址 WS2812B→大功率+MOSFET 开关（SI2336DS/SUD50N03）
  - **显示**：LCD HD44780（并口/I2C PCF8574）→OLED SSD1306→TFT ILI9341（软/硬 SPI）→电子墨水→ATtiny44 直接生成视频信号
  - **音频**：MP3 模块 DFPlayer/I2S 功放 MAX98357A/PWM D 类放大
  - **直流电机**：H 桥 TB67H451（3.5A/44V）
  - **舵机**：50Hz PWM 脉宽 1–2ms
  - **无刷 BLDC**：三相六步换相/BEMF 反电动势传感/A4949/ESC 电调（开源固件 tgy）；电流参考：风扇 1A→无人机 10A→滑板 100A→汽车 1000A
  - **步进**：step/dir 专用驱动 DRV8428/双 H 桥/大功率 DRV8263（29A）；微步细分/FOC
  - **固态继电器**驱动市电 + **线色规范**（务必开关火线）
  - **前沿执行器**：形状记忆合金/压电/人工肌肉（钓鱼线自制）/软体气动液压
- **作业**：小组=测量输出设备功耗；个人=**在自己设计的板上加输出设备并编程实现功能**

### W11 · Networking and Communications（网络与通信）★协议大全

- **组网四目的**：location/parallelism/modularity/interference
- **OSI 七层主线** + 香农信道容量公式
- **有线**：异步串行（RS-232/422/485；**总线 bridge/node 寻址**、hop-count、D-Bus 破解洗衣机）→ **I2C**（Qwiic/STEMMA 连接器生态、I3C 前沿）→ **SPI**（SD 卡+FAT）→ USB（TinyUSB/HID/MIDI）→ 以太网 W5500 → CAN/LIN/MODBUS/DMX
- **无线**：**ESP32 全家桶**（WiFi/BLE/C6 加 Zigbee/Thread/Matter/ESP-NOW，2026 新增）→ 蓝牙（GATT/Mesh）→ **LoRa/LoRaWAN**（km 级、月面反射实验）→ **Meshtastic 网状网**（2026 新增）→ RFID MFRC522 → nRF24L01 → UWB 定位
- **理论层**：调制（FSK/QAM/OFDM/FHSS 跳频-Hedy Lamarr 典故）；多路访问（CSMA 家族/TDMA/CDMA）；差错控制（CRC/Hamming/Reed-Solomon/Turbo）
- **互联网栈**：TCP/UDP/HTTP/DNS/DHCP/NAT + socket 三语言示例 + **SLIP 让 MCU 直接入网** + Wireshark
- **射频硬件**：电台架构（振荡/混频/PA/LNA/IQ）、天线、GNU Radio 软件无线电、OpenWrt
- **作业**：小组=两个项目间发一条消息；个人=**设计制作带地址、带本地 I/O 的联网节点**

### W12 · Mechanical Design + Machine Design（机械/机器设计，团队周）

- **力学原理清单**：应力-应变/刚度强度硬度/**Maxwell 判据**（精确约束）/摩擦/迟滞/**backlash 背隙**/**force loops 力回路**/弹性平均 vs **运动学耦合**/准确度 vs 精密度
- **零件资源地图**（以 McMaster-Carr 为主）：材料 → 连接（热熔嵌件/埋入螺母/铆钉销钉）→ 框架（**T 型槽铝型材**/自对准卡扣）→ **传动**（渐开线齿轮 Mods 生成/摆线齿形/行星/谐波减速器学生自制/丝杠滚珠丝杠/绞盘传动 Urumbu）→ **导向**（光轴导轨/球轴承/直线轴承/预紧）→ 运动件（全向轮）
- **机构图鉴**：柔性铰链/OpenFlexure 显微镜/SEA 串联弹性驱动/连杆（Cornell KMODDL）/**507 种经典机构**/deltabot/**Stewart 六足平台**/CoreXY/Sarrus/Hangprinter/Strandbeest 仿生行走
- **作业**（团队项目 "Hanging Time"）：设计一台含**机构+驱动+自动化+功能+用户界面**的机器 → **先做机械部分手动操作验证** → 记录团队与个人贡献

### W13 · Break + Midterm Review（期中评审）

期中四项交付（挂在个人项目站上）：
1. 项目**系统框图**（system diagram）
2. 待完成任务清单
3. 任务进度时间表
4. 与讲师约一次**计分评审**（graded review，覆盖期中材料 + 每周作业）

> 期中不考新知识，考的是「项目是否已系统化地想清楚」。

### W14 · Molding and Casting（模塑与铸造）

- **模具类型学**：注射（主流道/分流道/浇口/排气/分型线/飞边）、嵌件包覆、真空成型（Formech FM660）、吹塑、旋模/离心、注浆、压铸/熔模、**柔性软模**
- **材料体系**：蜡/泡沫/藻酸盐/聚氨酯/硅胶（Mold-Star/Mold-Max 60/PDMS 微流控）/石膏（USG）/水泥（Hydro-Stone）/Jesmonite/**低熔点合金 Cerrotru**/食品级
- **工艺细节**：work time/demold time、**除泡七法**（振动/涂刷/真空腔/压力腔…）、固化机理（聚合/交联/水化/放热吸热）、**脱模斜度与脱模剂**（稀释洗洁精/凡士林/滑石粉）
- **数字制模**：CNC 粗精加工（球头刀/步距）+ FFF/SLA 打印模
- **软件**：VCarve Pro/Fusion 360+Moldflow/SolidWorks Plastics/FreeCAD CAM/mods
- **作业**：小组=读 SDS 后做材料对比测试铸件；个人=设计模具 → 制出**表面无刀痕**的模具 → 铸造零件；加分=多分模/自制材料

### W15 · Interface and Application Programming（界面与应用编程）

- **语言全景**（hello world 到 esoteric）：C/C++ → Go/Rust → Python（Flask）→ **Processing/Arduino/p5.js 一脉** → JS 全家（Node/WebAssembly/TypeScript/DeviceScript）→ 低代码/数据流（Node-RED/**mods**）
- **AI 专题**（2026 强化）：Claude Code/Codex/Copilot/Cursor + **vibe coding 的版权/幻觉/理解问题**
- **设备接口**：串口（pySerial/Web Serial）/I2C/FTDI/Firmata/USB/**MQTT**（Mosquitto + 浏览器端）
- **用户界面梯队**：ncurses → Tk/wxWidgets/Qt/GTK/Kivy → Web（jQuery/Bootstrap → **React**/Electron）
- **图形栈**：Canvas/SVG/WebGL/**Three.js**/WebGPU → OpenGL/X11/Java Swing → VTK/ParaView → Unity/Godot
- **音视频**：SDL/Pygame/openFrameworks/TouchDesigner/Web Audio/WebRTC
- **数学/科学**：NumPy/SciPy/matplotlib/Jupyter/R/Plotly/**D3**/Chart.js
- **性能**：Numba/Jax/OpenMP/MPI/CUDA/WebGPU（π 计算基准贯穿）
- **机器学习**：PyTorch/TF.js/Hugging Face/ONNX/**LLM + MCP + APIs**
- **部署**：REST/PWA/AWS/Docker/K8s；安全（攻击面/依赖补丁/加密）
- **作业**：小组=对比尽可能多的工具选项；个人=**写一个应用把用户与你自制的输入/输出设备连接起来**

### W16 · System Integration（系统集成）★可靠性工程

- **DFM 面向制造的设计**：标准件/净成型/柔性铰链 vs 紧固件 vs 胶/自对准特征/**最少零件数**
- **封装**：PCB 安装/走线/机构对准/表面处理
- **测试体系**：QA（防缺陷）vs QC（检缺陷）；shake/drop/burn-in/cycling/环境/**fuzzing**
- **失效模式清单**（工程经验浓缩）：机械（应力集中裂纹/紧固件松振/螺纹滑丝/失稳）→ 布线（**扯断走线/连接器拔线/应力消除/防呆极性/线束**）→ 元件（MOSFET 过压过流/反电动势/瞬态保护/EMI）→ 电源（预算/**48V 误接 24V 输入**/旁路电容/地环路）→ 软件（内存泄漏/缓冲区溢出/竞态）→ 复杂度相变 → 供应链
- **修复与生命周期**：模块化/**"Widlarize"**（暴力拆解重装）、右翼维修权、拆解回收
- **开发哲学**：fail fast、前馈 vs 反馈开发
- **作业**：为期末项目**设计并文档化系统集成方案**

### W17 · Wildcard Week（自选周）

- **规则**：用一个**其他作业未覆盖**的 CAD+CAM 数字化工艺做一件作品 + 完整可复现文档
- **13+ 自选方向菜单**：磨削/多轴/EDM/水刀/等离子/金属激光/激光微加工 → 焊接 → 真空/旋转成型 → **折叠数学**（Demaine 折纸/Kirigami 超强结构）→ **机器人**（UR10 机械臂/软体/气动充气）→ 贴片机/可编程逻辑 → 嵌入式 AI/机器视觉 → **食物打印**（Digital Gastronomy）→ **材料合成**（Materiom 开源配方库）→ **生物技术**（DIYbio/iGEM/HTGAA）→ **纺织**（机器针织/刺绣 PEmbroider/Ink-Stitch/Fabricademy）→ 复合材料
- **设备**：Hurco 5 轴/Sodick 线切割/Omax 水刀/Zund 裁切/Fablight 金属激光/Mechatronika 贴片机

### W18 · Applications and Implications + Project Development（立项 + 冲刺）

**上午课（Applications）——期末项目"立项评审"的 11 问**：
1. 项目做什么？ 2. 前人做过什么？ 3. 用什么信息源？ 4. 你设计什么？ 5. 用什么材料元件？ 6. 从哪来？ 7. 花多少钱？ 8. 哪些自制？ 9. 用什么工艺？ 10. 有何待解问题？ 11. **如何评估？**
- 技术底线：项目必须整合 2D/3D 设计 + 增/减材制造 + 电子设计生产 + 嵌入式编程 + 系统集成封装
- 文化原则：**Make, don't buy**；合作可以但须证明个人独立掌握、项目能独立运行
- 附 **34 个应用领域全景**（医疗假肢→卫星无人机→房屋城市→社区经济体），每领域有案例库可查先例

**下午课（Project Development）——"如何把项目做完"**：
- 项目管理概念：**墨菲定律**、**80/20 与 95/5**（最后 5% 收尾耗 95% 精力）、**triage 分诊取舍**、需求侧 vs 供给侧时间管理、**螺旋开发**（先端到端最小可运行再迭代）、串行 vs 并行任务、DevOps、完成质量
- 交付硬规格：`presentation.png`（1920×1080）+ `presentation.mp4`（1080p、≤1 分钟、≤25MB、HTML5 兼容）
- **往届百个项目范例库**（2010–2025）可作选题与演示参考

### W19 · Invention, Intellectual Property, and Income（发明/知识产权/收益）

- **发明**：R&D 传统（Endless Frontier）、**Ready-Fire-Aim** 迭代方法论（Neil TED 演讲）、创业生态、包容性
- **IP 三件套**：
  - **专利**（USPTO）：实用 20 年（自申请）/外观 15 年（自授权）；**公开披露的国际新颖性陷阱**（美国 1 年宽限期 vs 多数国家即刻丧失）；临时申请 1 年转正；三性审查；PCT 国际申请；防御性公开；成本量级 **$100→$1k→$10k→$100k**；专利流氓
  - **版权**：创作即自动保护，终身+70 年；**开源许可体系**（GPL/MIT/Apache/CC/OSHWA 开源硬件认证）；洁净室开发（Phoenix BIOS 案例）
  - **商标**：使用确立→注册 ®→保护
- **收益**：三动机（财务/影响/社会）；四原则（**推绳子**不硬推/痛点/护城河/MVP）；**八大收入来源**（产品 Formlabs/套件 Prusa/耗材剃刀刀片 Gillette/许可 ARM/广告 Google/平台 Apple/基础设施 AWS/服务 Fab Foundation+劳斯莱斯按小时付费）；企业类型（LLC/合作社/员工持股 ShopBot/B Corp/PBC）；融资（VC/天使/**众筹 Reekon**/自举）；企业生命周期失败点
- **制造生态**：加速器（HAX）/代工（PCH/Flex/**Seeed**）/认证（UL/CE/GDPR）
- **作业**：为最终项目制定**传播计划**（选开源/专利/混合策略）+ 五问进度追踪（完成了什么/什么在正常工作/还有什么问题/时间表/学到什么）

---

## 二、知识体系的设计规律（横向分析）

### 1. 四大主线交替推进

```
设计表示线：  W2 CAD ────────────────→ W15 界面编程（输入设计→输出呈现）
制造工艺线：  W3 切割 → W5 3D打印 → W7 CNC → W14 铸造 → W17 自选
电子系统线：  W4 嵌入式 → W6 设计 → W8 生产 → W9 输入 → W10 输出 → W11 联网
集成转化线：  W12 机器 → W16 系统集成 → W18 立项开发 → W19 商业化
```

每周只推一条主线的一个环节，但**作业要求横跨多线**（如 W9 作业 = 自己设计板[W6/W8 技能] + 传感器[本周] + 编程[W4 技能]）——**螺旋上升式复用**。

### 2. "表征实验"文化（小组作业的一致模式）

| 周 | 表征对象 | 产出 |
|----|---------|------|
| W3 | 激光机 kerf/功率/速度/接头间隙 | 机器参数基线表 |
| W5 | 3D 打印机设计规则 | 悬垂/壁厚/间隙极限表 |
| W7 | CNC 跳动/对齐/装夹/转速进给 | 切削参数基线 |
| W8 | PCB 铣削工艺设计规则 | 线宽/间距极限 |
| W9/W10 | 输入输出器件信号与功耗 | 信号特征/功耗档案 |

**启示：每台机器进实验室都应先做一次"表征实验"，建立参数基线**——这与本库《设备维护保养规范》的「设备档案卡」、《工具组织与现场管理》的「一机一码台账」直接呼应。

### 3. "hello board" 可复现生态

电子线每周的每个知识点都有**全套开源参考设计**：原理图 + PCB + 走线图 + 铣板文件 + 三语言代码 + 视频。教学单元 = 可直接制造的完整工件。**课程内容的载体本身就是数字制造产品**。

### 4. 安全与文档是"隐形第一课"

W3 激光安全 → W7 CNC 专设安全板块（"你的手不是工具"）→ W10 电气安全阈值 → W14 SDS 制度；文档化从 W1 贯穿到 W19（边做边记 → 期中框图 → 期末 1 分钟视频）。

### 5. 前沿内容的滚动更新机制

2026 版新增：AI 辅助编程/嵌入式 AI（W4/W15）、Meshtastic/ESP32-C6 Zigbee（W11）、I3C、流变学打印（W17）——核心骨架 20 年稳定，**边缘每年更新**。

---

## 三、对柴火的映射与启示

| Fab Academy 周 | 对应柴火资产 | 可直接借鉴 |
|----------------|-------------|-----------|
| W1 项目管理 + 文档文化 | 知识库本身 | 「边做边记」作为空间运营 SOP |
| W2 CAD 工具矩阵 | M0 课程积木 | 工具梯队表（入门→脚本→专业）可做 M0 进阶路线图 |
| W3 激光/切割 | 激光 STEAM 课程（语雀）+ 《设备摆放与布局规范》 | **kerf 表征实验**可直接做激光认证培训的实操关卡 |
| W5 3D 设计规则测试 | 3D 打印机维保 | 设计规则测试件 = 打印机**健康巡检标准件**（一石二鸟）|
| W7 CNC 表征 | CNC 维保 | 切屑负荷公式 + 参数基线表 |
| W8 mods PCB 流程 | 实验室能力建设 | 铣板 PCB 最低成本电子自制路线 |
| W9-W10 传感器/执行器 | M0 硬件积木（Wio Terminal + DHT20）| 「一物理量一板子」教学法；DHT20 = 温度周的现成教具 |
| W11 ESP32 全家桶 | XIAO ESP32 系（C 系列）| Wio/XIAO 生态在课程里的官方地位 |
| W12 团队造机器 | 中大训练营 | **先手动验证机构再自动化**的团队项目节奏 |
| W13 期中系统框图 | 训练营 checkpoint | 中途评审四件套：框图+任务清单+时间表+计分评审 |
| W16 失效模式清单 | 《设备维护保养规范》 | 失效模式表可直接并入维保文档的「故障诊断」章节 |
| W17 自选周 | 训练营展示环节 | 13 方向菜单 = 兴趣分流的选题池 |
| W18 十一问 + Make don't buy | 训练营项目化教学 | **立项 11 问**可浓缩为学员项目提案模板 |
| W19 开源许可 | 柴火开源传统 | GPL/MIT/CC 选择树 + 传播计划模板 |

---

## 四、资源入口汇总

| 入口 | URL |
|------|-----|
| 2026 日程总页 | https://fabacademy.org/2026/schedule.html |
| 每周课程页 | https://fabacademy.org/2026/classes/&lt;主题&gt;/index.html（如 computer_design、electronics_production）|
| Recitation 页 | https://fabacademy.org/2026/recitation/&lt;主题&gt;/index.html |
| 讲义脚本系统 | http://ng.cba.mit.edu/show/script/26.01.fab.html（`i` 看索引）|
| 历史讲义库 | http://academy.cba.mit.edu/classes/（MIT CBA 全量）|
| 往届项目检索 | Google CSE（fabacademy final projects）|
| 往届亮点 | https://fabacademy.org/2025/highlights.html（逐年类推）|
| 设备/元件库存 | http://inventory.fabcloud.io/?purpose=&lt;周主题&gt; |
| 开源 CAM | https://modsproject.org / gitlab.fabcloud.org/pub/project/mods |
| 往届课堂视频 | 每周日程页 Vimeo 链接（lecture + review 两段）|

---

*本文为 Fab Academy 系列第四篇。系列全览：[Fab-Academy实战全解.md](../Fab-Academy实战全解.md)（学员）→ [Fab-Academy平台与运营机制-专题补充.md](Fab-Academy平台与运营机制-专题补充.md)（机构）→ [Fab-Academy-2026课程日程-专题补充.md](Fab-Academy-2026课程日程-专题补充.md)（日历）→ 本文（每周知识体系）。*
