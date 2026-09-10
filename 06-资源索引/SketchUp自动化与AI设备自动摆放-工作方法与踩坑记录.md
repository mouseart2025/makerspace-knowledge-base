---
title: "SketchUp 自动化与 AI 设备自动摆放：工作方法与踩坑记录"
type: 方法论
scope: 通用
source: "实战验证(职业院校L型创客空间项目)"
date: 2026-09
tags: [SketchUp, Ruby API, 自动化建模, 3D方案, 设备自动摆放, MCP, 踩坑记录]
---

# SketchUp 自动化与 AI 设备自动摆放 — 工作方法与踩坑记录

> 本文档记录某职业院校创客空间二期项目中，通过 SketchUp 2026 实现 L 型空间 3D 建模与设备自动摆放的完整技术路线、工作流程和踩坑经验。适用于需要批量生成多方案 3D 布局的创客空间规划场景。

---

## 一、技术路线概述

### 1.1 为什么选择 SketchUp 自动化

| 方案 | 优点 | 缺点 | 结论 |
|------|------|------|------|
| Seedream 5.0 Pro 绘制规划图 | 快速出图 | AI 无法正确理解平面图几何，尺寸不可控 | ❌ 否决 |
| 手动操作 SketchUp GUI | 精确可控 | 三方案重复操作耗时，易出错 | ⚠️ 仅用于调试 |
| SketchUp Ruby API 脚本 | 参数化、可复现、批量生成 | 需解决脚本自动执行问题 | ✅ 最终方案 |
| openskp (Python) | 无需启动 SketchUp | 功能有限，不支持复杂建模 | ⚠️ 可用于读取 .skp |

### 1.2 最终技术栈

- **建模工具**：SketchUp 2026（macOS）
- **自动化方式**：Plugins 自动加载 + 轮询定时器
- **脚本语言**：Ruby（SketchUp Ruby API）
- **坐标系统**：CAD 精确尺寸（mm），原点在 A 区西南角，X 向东，Y 向南，Z 向上
- **设备表示**：彩色 3D 盒子（按专业分类配色），后续可替换为精细模型

---

## 二、完整工作流程

### 2.1 阶段一：建筑基础模型生成

```
CAD 精确尺寸 → 参数化 Ruby 脚本 (generate_l_shape.rb) → 手动在 Ruby Console 运行 → 生成 .skp
```

**脚本生成内容**：
- 6 区域分色地坪（A/B/C 横向臂，D/E/F 纵向臂）
- 外墙（避开门洞分段）
- 内部隔墙 + 9 根结构柱（500×500mm）
- 5 扇门（门 1/3 防火门，门 2/4/5 玻璃门）
- 约 21 扇窗
- 天花板（层高 3370mm）
- 大梁（下皮 2600mm，梁厚 400mm）
- 区域标签（面积标注）

### 2.2 阶段二：设备自动摆放

```
设备清单 → 参数化设备定义 (name/x/y/z/w/d/h/color) → Plugins 自动加载脚本 → 
SketchUp 启动 → 轮询检测模型 → 自动摆放 → 隐藏天花板 → 设置顶视图 → 截图
```

**Plugins 自动加载机制**：
1. 注册文件 `makerspace_autoload.rb`（标准 SketchupExtension 格式）
2. 主逻辑 `makerspace_autoload/main.rb`
3. SketchUp 启动时自动加载插件
4. `UI.start_timer(2, true)` 每 2 秒轮询检测 `active_model.entities.count > 0`
5. 检测到模型后执行 `do_layout`，摆放所有设备
6. 摆放完成后 `UI.stop_timer` 停止轮询
7. 延迟 1 秒后执行：隐藏天花板 + 设置顶视图 + 缩放范围

### 2.3 阶段三：多方案批量生成

```
方案1设备列表 → main.rb (Plan 1) → 重启 SketchUp → 自动生成 → 保存 .skp + 截图
方案2设备列表 → main.rb (Plan 2) → 重启 SketchUp → 自动生成 → 保存 .skp + 截图
方案3设备列表 → main.rb (Plan 3) → 重启 SketchUp → 自动生成 → 保存 .skp + 截图
```

---

## 三、关键技术实现

### 3.1 Plugins 标准注册格式

**必须使用标准格式**，简单 .rb 文件放在 Plugins 根目录会被 SketchUp 拒绝（"无法将此文件标识为扩展程序"）。

```ruby
# makerspace_autoload.rb（注册文件，放在 Plugins 根目录）
require 'sketchup.rb'
require 'extensions.rb'

module MakerspaceAutoLayout
  path = File.dirname(__FILE__)
  loader = File.join(path, "makerspace_autoload/main")
  extension = SketchupExtension.new("创客空间自动摆放", loader)
  extension.description = "自动摆放设备"
  extension.version = "1.0"
  extension.creator = "Chaihuo"
  extension.copyright = "2026"
  Sketchup.register_extension(extension, true)
end
```

### 3.2 轮询定时器（关键！）

**一次性定时器会失败**：`UI.start_timer(5, false)` 在模型未加载完时触发，检测不到模型。

**正确做法**：使用重复定时器轮询，检测到模型后停止。

```ruby
module MakerspaceAutoLayout
  @@timer_id = nil
  @@attempts = 0

  def self.start
    @@timer_id = UI.start_timer(2, true) { self.poll }
  end

  def self.poll
    @@attempts += 1
    model = Sketchup.active_model
    if model && model.entities.count > 0
      log("Poll ##{@@attempts}: Model ready")
      do_layout
      UI.stop_timer(@@timer_id) if @@timer_id
    end
  end
end

MakerspaceAutoLayout.start
```

### 3.3 参数化设备定义

```ruby
EQUIPMENT = [
  # A区 - 新能源（红色）
  { name: "动力电池装调平台1", x: 1000, y: 1000, w: 2000, d: 1200, h: 800, color: "DC2626" },
  { name: "动力电池装调平台2", x: 4000, y: 1000, w: 2000, d: 1200, h: 800, color: "DC2626" },
  # ... 更多设备
]
```

### 3.4 创建设备（3D 盒子）

```ruby
def self.create_equipment(entities, model, eq)
  model.start_operation("Add #{eq[:name]}", true)
  pts = [
    Geom::Point3d.new(eq[:x], eq[:y], eq[:z] || 0),
    Geom::Point3d.new(eq[:x] + eq[:w], eq[:y], eq[:z] || 0),
    Geom::Point3d.new(eq[:x] + eq[:w], eq[:y] + eq[:d], eq[:z] || 0),
    Geom::Point3d.new(eq[:x], eq[:y] + eq[:d], eq[:z] || 0),
  ]
  face = entities.add_face(pts)
  face.pushpull(eq[:h])
  # 设置材质颜色
  material = model.materials.add(eq[:name])
  material.color = eq[:color]
  face.material = material
  face.back_material = material
  model.commit_operation
  true
rescue => e
  log("Error #{eq[:name]}: #{e.message}")
  false
end
```

### 3.5 自动隐藏天花板 + 设置顶视图

```ruby
UI.start_timer(1, false) do
  # 递归隐藏天花板（z > 3000mm 的面，包括 Group 内）
  hidden = [0]
  MakerspaceAutoLayout.hide_ceiling_recursive(model.entities, hidden)

  # 设置顶视图 + 平行投影
  view = model.active_view
  camera = view.camera
  camera.perspective = false
  camera.set([0, 0, 100000], [0, 0, 0], [0, 1, 0])
  view.zoom_extents
end
```

**注意**：
- 隐藏天花板必须**递归遍历** Group 和 ComponentInstance 内部的 Face
- 方法必须定义在 module 级别，**不能定义在 block 内部**（会报 `undefined method`）
- `camera.set(eye, target, up)` 中 up 向量用 `[0, 1, 0]`（Y 轴向上，对应顶视图）

---

## 四、踩坑记录（详细）

### 4.1 SketchUp 版本相关

| 问题 | 现象 | 解决方案 |
|------|------|----------|
| SketchUp 2024 自动化全部失败 | `-RubyStartup` / `STARTUP_RUBY` 参数不生效；Plugins 自动加载器未触发；AppleScript 需要辅助功能权限 | 升级到 SketchUp 2026 |
| SketchUp 2026 欢迎界面按钮点击无效 | 普通 `cu.click` 对 web 视图中的模板按钮不生效 | 用 `cu.drag(from=to 同一点)` 模拟真实鼠标按下释放 |
| Ruby Console 输入不执行 | 通过 AX `type_text` 输入命令后按 return，输出区域空白 | 放弃 Ruby Console 方式，改用 Plugins 自动加载 |

### 4.2 Plugins 加载相关

| 问题 | 现象 | 解决方案 |
|------|------|----------|
| 简单 .rb 被拒绝 | "无法将此文件标识为扩展程序" | 使用标准 `SketchupExtension.new` + `register_extension` 格式 + 子目录结构 |
| 插件不加载（无日志） | 日志文件为空，插件未执行 | 检查文件权限（需 755，不能是 600）；检查恢复版本对话框是否阻止模型加载 |
| 一次性定时器失败 | `UI.start_timer(5, false)` 触发时模型未加载 | 改用 `UI.start_timer(2, true)` 重复轮询 |
| class variable 错误 | `class variable access from toplevel` | 定时器启动和变量访问必须在 module 内部方法中 |
| `empty?` 方法不存在 | `NoMethodError: undefined method 'empty?' for Sketchup::Entities` | 用 `count == 0` 代替 |

### 4.3 模型操作相关

| 问题 | 现象 | 解决方案 |
|------|------|----------|
| `write_image` 参数错误 | `no implicit conversion of Hash into Integer` | SketchUp 2026 用位置参数 `(filename, width, height, antialias)`，不用 hash |
| 恢复版本对话框反复弹出 | 每次打开 .skp 都问"是否转为打开恢复的版本？" | 删除 `~/Library/Application Support/SketchUp 2026/SketchUp/working/` 下的恢复文件 |
| 保存时弹出"清除未使用资源" | 保存前询问是否清理组件/材质/样式 | 点击"不要清除"（保留设备材质） |
| 天花板挡住内部设备 | 顶视图看不到设备 | 递归隐藏所有 z > 3000mm 的 Face |
| 隐藏天花板 0 个面 | 只遍历了顶层 entities，没遍历 Group 内 | 递归遍历 Group 和 ComponentInstance |
| 方法定义在 block 内 | `undefined method 'hide_ceiling_recursive'` | 方法定义在 module 级别，block 中调用 |

### 4.4 GUI 操作相关（mac_computer_use_tool）

| 问题 | 现象 | 解决方案 |
|------|------|----------|
| `press_key` 参数错误 | `too many positional arguments` / `Invalid element_index` | 查阅 cu API，用正确的参数格式 |
| element_index 过期 | 每次操作后 AX 树变化，index 失效 | 操作前重新 `get_app_state` 获取最新 index |
| 菜单子菜单点击失败 | 直接 click 子菜单项不生效 | 用键盘导航（down/right/return）比直接 click 更可靠 |
| 环绕观察拖动无效 | `cu.drag` 旋转视角不生效 | 改用 Ruby API 设置相机，或用菜单"相机→标准视图→顶视图" |
| 保存对话框文件名输入无效 | 输入相对路径不生效 | 直接用默认文件名保存，然后用 `mv` 重命名 |

### 4.5 坐标与尺寸相关

| 问题 | 现象 | 解决方案 |
|------|------|----------|
| 区域边界错误（v1-v3） | 把尺寸标注线当做了隔墙 | CAD 中隔墙是双线表示，尺寸标注线不是隔墙 |
| A/B 区宽度错误 | 标注为 7.25m，实际 7.35m | 按 CAD 标注：横向臂南北宽 7350mm |
| D/E/F 区宽度错误 | 标注为 8.11m，实际 7.65m | 纵向臂东西宽 7650mm |
| E 区长度错误 | 标注为 9.90m，实际 10.40m | 含柱子：9900 + 500mm |
| 门宽度不对 | 5 个门都窄了 | 门宽应为 900mm，检查坐标计算 |

---

## 五、验证清单

每次生成方案后，按以下清单验证：

- [ ] **日志检查**：`/tmp/makerspace_autolayout.log` 显示 "Layout complete! Success: N, Failed: M"
- [ ] **设备数量**：Success 数量与设备清单一致（允许少量与实体重叠的失败）
- [ ] **天花板隐藏**：日志显示 "Hidden N ceiling faces"（N > 0）
- [ ] **顶视图**：日志显示 "Set top view and zoom extents"
- [ ] **视觉检查**：截图中 6 个区域清晰可见，设备颜色与专业分类一致
- [ ] **区域完整性**：A/B/C 横向臂 + D/E/F 纵向臂，L 型结构正确
- [ ] **设备分布**：各区域设备数量与方案文档一致
- [ ] **无越界**：设备全部在区域边界内，不超出外墙
- [ ] **文件保存**：.skp 文件大小增加（含设备），修改时间更新
- [ ] **截图保存**：顶视图 PNG 清晰，无对话框遮挡

---

## 六、已知限制与后续优化

### 6.1 当前限制

1. **设备模型简单**：所有设备用彩色盒子表示，无真实 3D 模型
2. **2 个设备偶发失败**：与现有墙柱实体重叠的设备可能放置失败（"reference to deleted DrawingElement"）
3. **设备标签缺失**：3D 模型中没有设备名称标签，需对照清单
4. **无动线可视化**：当前只摆放设备，未绘制人流动线
5. **无尺寸标注**：3D 模型中没有设备间距、通道宽度等标注
6. **SketchUp 必须重启**：每次修改脚本后需重启 SketchUp 才能生效
7. **macOS 专用**：Plugins 路径和 GUI 操作基于 macOS，Windows 需调整

### 6.2 后续优化方向

1. **精细设备模型**：从 3D Warehouse 下载或用 AI 生成（TRELLIS/Hunyuan3D）真实设备模型，替换彩色盒子
2. **设备标签**：用 `entities.add_text` 添加 3D 文字标签
3. **动线绘制**：用 `entities.add_cline` 或彩色路径绘制人流动线
4. **多方案对比**：自动生成三方案并排对比图
5. **导出 GLB/OBJ**：用 `model.export` 导出为通用 3D 格式，可在 Blender/Unity 中渲染
6. **参数化配置文件**：设备列表从 JSON/YAML 读取，不硬编码在 Ruby 脚本中
7. **碰撞检测**：自动检测设备之间、设备与墙柱之间的碰撞
8. **Windows 适配**：调整 Plugins 路径和 GUI 操作方式

---

## 七、文件结构参考

```
项目根目录/
├── 3D模型/
│   ├── generate_l_shape.rb          # 建筑基础模型生成脚本
│   ├── 项目名_L型空间_v1.skp   # 基础模型（含建筑）
│   ├── 方案1_设备落位_顶视图.png     # 方案1顶视图
│   └── ...
└── 规划方案/
    ├── 方案1_L型布局_v2.svg          # 2D 方案图
    └── ...

SketchUp Plugins 目录（macOS）:
~/Library/Application Support/SketchUp 2026/SketchUp/Plugins/
├── makerspace_autoload.rb             # 插件注册文件
└── makerspace_autoload/
    └── main.rb                      # 主逻辑（设备列表 + 摆放 + 视角设置）
```

---

## 八、相关知识库文档

- [AI 空间规划方案图绘制-确定性方法与校验清单](../06-资源索引/AI空间规划方案图绘制-确定性方法与校验清单.md)
- [AI 平面图理解与矢量提取方法论](../06-资源索引/AI平面图理解与矢量提取方法论.md)
- [AI 规划方法论-实战验证与提示词模板](../02-空间搭建/AI规划方法论-实战验证与提示词模板.md)
- [无人机测绘实训区设计](../02-空间搭建/无人机测绘实训区设计.md)

---

## 九、MCP 方案（推荐进阶路线）

> 2026-09-05 新增：通过 `zinin/sketchup-mcp2` 实现 AI 与 SketchUp 的实时交互，比 Plugins 自动加载方案更灵活，支持动态执行 Ruby 代码、查询模型状态、自动截图验证，无需重启 SketchUp。

### 9.1 方案对比

| 维度 | Plugins 自动加载（v1.0） | MCP 方案（v2.0 推荐） |
|------|--------------------------|----------------------|
| **交互方式** | 脚本写死，重启执行 | AI 动态调用工具，实时交互 |
| **修改脚本** | 改 .rb → 重启 SketchUp | 直接发 Ruby 代码执行，无需重启 |
| **结果验证** | 靠日志 + 手动截图 | 内置截图工具，可自动迭代 |
| **工具集** | 只有自己写的摆放函数 | 几何体/材质/布尔/倒角/导出/内省等预制工具 |
| **模型查询** | 无 | get_model_info / list_components / find_components |
| **撤销支持** | 无 | 每次操作原子化，可 undo |
| **配置成本** | 低（复制 2 个文件） | 中（Python MCP server + Ruby plugin） |
| **适用场景** | 一次性批量生成 | 迭代优化、多方案对比、AI 自动调整 |

### 9.2 安装步骤

#### 1. 安装 Ruby Plugin（SketchUp 端）

```bash
# 克隆仓库
git clone https://github.com/zinin/sketchup-mcp2.git

# 直接复制到 Plugins 目录（无需构建 .rbz）
PLUGINS_DIR="$HOME/Library/Application Support/SketchUp 2026/SketchUp/Plugins"
cp -r sketchup-mcp2/mcp_for_sketchup/mcp_for_sketchup.rb "$PLUGINS_DIR/"
cp -r sketchup-mcp2/mcp_for_sketchup/mcp_for_sketchup "$PLUGINS_DIR/"
```

> 注意：系统 Ruby 2.6 无法安装最新 rubyzip 构建 .rbz，直接复制文件即可。

#### 2. 启动 MCP Server

在 SketchUp 中：`扩展 → MCP Server → Start Server`

默认监听 `127.0.0.1:9876`，可在 `Settings...` 中修改。

#### 3. 验证端口

```bash
lsof -i :9876
# 应显示 SketchUp 进程在 LISTEN
```

### 9.3 TCP 协议格式

MCP server 使用自定义 TCP 协议（非标准 MCP stdio）：

**帧格式**：`4字节大端长度前缀 + JSON-RPC 2.0 消息体`

```python
import struct, json

def encode_frame(body: dict) -> bytes:
    data = json.dumps(body).encode("utf-8")
    return struct.pack(">I", len(data)) + data

def decode_frame(sock) -> dict:
    header = sock.recv(4)
    length = struct.unpack(">I", header)[0]
    body = b""
    while len(body) < length:
        body += sock.recv(length - len(body))
    return json.loads(body.decode("utf-8"))
```

**握手**（必须第一个发送）：
```json
{"jsonrpc": "2.0", "method": "hello", "params": {"client_version": "0.3.1"}, "id": 1}
```
响应：
```json
{"jsonrpc": "2.0", "result": {"server_version": "0.3.1", "client_id": 0}, "id": 1}
```

**工具调用**：
```json
{"jsonrpc": "2.0", "method": "tools/call", "params": {"name": "工具名", "arguments": {...}}, "id": 2}
```

### 9.4 可用工具列表

| 分类 | 工具 | 说明 |
|------|------|------|
| **几何体** | `create_component` | 创建立方体/圆柱体/圆锥体/球体，参数：type, dimensions[w,d,h], position[x,y,z], name |
| | `delete_component` | 删除组件 |
| | `transform_component` | 变换组件 |
| **材质** | `set_material` | 设置材质，参数：id, material（颜色名或hex） |
| **布尔** | `boolean_operation` | 并集/差集/交集 |
| **边操作** | `chamfer_edge`, `fillet_edge` | 倒角/圆角 |
| **榫卯** | `create_mortise_tenon`, `create_dovetail`, `create_finger_joint` | 木工榫卯 |
| **导出** | `export_scene` | 导出 skp/obj/dae/stl/png/jpg |
| **内省** | `get_model_info` | 模型信息（路径/单位/边界盒/实体数/图层） |
| | `list_components` | 组件列表（含 bbox_mm） |
| | `get_component_info` | 组件详情 |
| | `find_components` | 按名称查找组件 |
| | `list_layers`, `create_layer` | 图层管理 |
| | `get_selection` | 当前选择 |
| | `get_version` | 版本信息 |
| **视图** | `get_viewport_screenshot` | 截图（需 SketchUp 2026+），参数：max_size, view_preset, style, zoom_extents |
| **生命周期** | `undo` | 撤销上一次操作 |
| **逃逸口** | `eval_ruby` | 执行任意 Ruby 代码（默认启用，可在 Settings 关闭） |

### 9.5 关键工具参数说明

#### get_viewport_screenshot（截图）

```python
# 参数
{
    "max_size": 1920,           # 必填，64-4096
    "view_preset": "top",       # 必填，current/front/back/left/right/top/bottom/iso
    "style": "shaded",          # 必填，default/shaded/hidden_line/wireframe
    "zoom_extents": True,       # 可选，缩放范围
    "restore_view": False       # 可选，是否恢复原视角（默认true）
}
# 返回：JSON文本 {"png_base64": "...", "width": ..., "height": ...}
```

#### create_component（创建设备）

```python
{
    "name": "动力电池装调平台",  # 可选
    "type": "cube",             # 必填，cube/cylinder/cone/sphere
    "dimensions": [2000, 1200, 900],  # 必填，[宽,深,高] mm
    "position": [2000, 2000, 0]       # 必填，[x,y,z] mm
}
# 返回：{"id": 19624, "name": "...", "type": "group", "bbox_mm": {...}}
```

#### eval_ruby（执行 Ruby）

```python
{"code": "Sketchup.active_model.entities.count.to_s"}
# 返回：执行结果的字符串
```

### 9.6 Python 完整示例

```python
import socket, json, struct, base64

HOST, PORT = "127.0.0.1", 9876

def encode_frame(body):
    data = json.dumps(body).encode()
    return struct.pack(">I", len(data)) + data

def decode_frame(sock):
    length = struct.unpack(">I", sock.recv(4))[0]
    body = b""
    while len(body) < length:
        body += sock.recv(length - len(body))
    return json.loads(body)

def call_tool(sock, name, args, req_id):
    sock.sendall(encode_frame({
        "jsonrpc": "2.0", "method": "tools/call",
        "params": {"name": name, "arguments": args}, "id": req_id
    }))
    return decode_frame(sock)

# 连接 + 握手
sock = socket.socket()
sock.connect((HOST, PORT))
sock.sendall(encode_frame({"jsonrpc": "2.0", "method": "hello",
    "params": {"client_version": "0.3.1"}, "id": 1}))
print("握手:", decode_frame(sock))

# 查询模型
resp = call_tool(sock, "get_model_info", {}, 2)
print("模型:", resp["result"]["content"][0]["text"][:200])

# 创建设备
resp = call_tool(sock, "create_component", {
    "name": "测试设备", "type": "cube",
    "dimensions": [2000, 1000, 800], "position": [3000, 3000, 0]
}, 3)
print("创建:", resp["result"]["content"][0]["text"])

# 截图
resp = call_tool(sock, "get_viewport_screenshot", {
    "max_size": 1920, "view_preset": "top",
    "style": "shaded", "zoom_extents": True
}, 4)
data = json.loads(resp["result"]["content"][0]["text"])
with open("top.png", "wb") as f:
    f.write(base64.b64decode(data["png_base64"]))

# 撤销
call_tool(sock, "undo", {}, 5)
sock.close()
```

### 9.7 验证结果（2026-09-05）

| 测试项 | 结果 |
|--------|------|
| 握手（hello） | ✅ server_version=0.3.1, client_id 分配正常 |
| get_model_info | ✅ 返回路径/单位/边界盒/1697实体/9图层 |
| get_version | ✅ ruby_version=0.3.1 |
| eval_ruby | ✅ 执行任意 Ruby 代码正常 |
| create_component | ✅ 创建立方体，返回 id 和 bbox_mm |
| get_viewport_screenshot | ✅ 顶视图/鸟瞰图，1920x1040 PNG |
| undo | ✅ 原子化撤销正常 |
| 递归隐藏天花板 | ✅ 通过 eval_ruby 隐藏 8 个面 |

### 9.8 MCP 方案的典型工作流

```
AI 规划设备布局 → eval_ruby 清空旧设备 → create_component 批量创建设备 
→ set_material 设置颜色 → get_viewport_screenshot 截图验证 
→ AI 分析截图 → 调整坐标 → 重复迭代 → export_scene 导出最终方案
```

**优势**：
- AI 可以"看到"截图结果，自动调整布局
- 多方案切换只需执行不同代码，无需重启
- 每次操作可撤销，安全可控
- 支持碰撞检测（通过 eval_ruby 查询实体交集）

### 9.9 注意事项

1. **eval_ruby 默认启用**：有安全风险（任意 Ruby → 文件系统/网络/Shell 访问），生产环境可在 Settings 关闭
2. **set_material 参数**：用 `material` 不是 `color`，用 `id` 不是 `entity_id`
3. **截图 restore_view**：设为 false 可保持当前视角，避免反复切换
4. **版本兼容**：client_version 必须在 [0.3.0, 0.3.1] 范围内，否则握手被拒
5. **多客户端**：支持同时连接多个 MCP 客户端，但操作在 SketchUp UI 线程串行执行
6. **帧大小限制**：单帧最大 64 MiB，截图 base64 后约 43 MiB，max_size 建议 ≤ 1920

---

## 十、CAD 图理解与 3D 建模实战方法论（本项目 v2-v13 案例）

> 2026-09-05 新增：从 CAD 直接绘制空间 3D 基础模型的完整方法论。某项目经历 13 个版本迭代，核心教训是**AI 容易错误理解 CAD 图**，因此本章重点提炼通用方法论，项目特定事实单独标注。

### 10.1 通用方法论：CAD 图理解的正确流程

**核心原则：不要凭经验假设，一切以 CAD 原图为准。**

#### 第一步：建立坐标系映射（最关键）

CAD 与 SketchUp 的 Y 轴方向**可能不同**，必须先确认：

| 坐标系 | X 轴 | Y 轴 | 原点 |
|--------|------|------|------|
| 建筑 CAD（常见） | 向东（右） | **向南（下）** | 西北角 |
| SketchUp | 向东（右） | **向北（上）** | 模型原点 |

**映射公式**（需根据实际 CAD 方向调整）：
```ruby
# 若 CAD Y 向南，SketchUp Y 向北，则需反转
su_y = total_height - cad_y
# X 轴通常一致，不需反转
su_x = cad_x
```

**验证方法**：生成后立即看顶视图，确认空间朝向与 CAD 一致。

#### 第二步：识别 CAD 图例（避免误读）

AI 常见误读：
- ❌ 把**尺寸标注线**当成隔墙（尺寸线是细线，隔墙是双线）
- ❌ 把**柱子填充**当成墙体（柱子是实心方块，墙体是双线）
- ❌ 把**门窗符号**当成墙体开口（门有弧线符号，窗是四线表示）
- ❌ 假设区域之间有隔墙（实际可能是大通间，只有结构柱）

**正确做法**：
1. 先渲染 CAD 高分辨率图（≥300 DPI）
2. 逐区域放大观察墙体、柱子、门窗的表示方式
3. 对照尺寸标注确认每个元素的位置和尺寸
4. 不确定的元素标注为"待确认"，不要猜测

#### 第三步：结构化提取建筑元素

按以下顺序提取，避免遗漏：
1. **外墙轮廓**：确定空间边界和总面积
2. **内墙/隔墙**：注意区分"完整隔墙"和"半截墙"
3. **结构柱**：位置、截面尺寸、是否有并排柱/双柱
4. **门**：位置、宽度、开启方向、门类型（防火门/玻璃门）
5. **窗**：位置、宽度、窗台高度
6. **特殊结构**：T 型墙、设备基座、天井等

#### 第四步：生成后逐项验证（强制）

生成 3D 模型后，必须对照 CAD 原图逐项验证：
- [ ] 空间轮廓和朝向与 CAD 一致
- [ ] 每根柱子的位置与 CAD 一致
- [ ] 每扇门的位置和宽度与 CAD 一致
- [ ] 墙体（含半截墙、T 型墙）位置正确
- [ ] 区域之间是否有隔墙（不要凭经验假设）
- [ ] 边界盒尺寸与 CAD 标注总面积吻合

### 10.2 通用技术踩坑（SketchUp API）

#### 面法线必须检查

**问题**：`add_face` 创建的面法线方向不确定，若 `normal.z < 0`，`pushpull` 正数会向下延伸（z 负值）。

**解决方案**：
```ruby
def make_face(ents, pts)
  f = ents.add_face(pts)
  f.reverse! if f && f.normal.z < 0  # 确保法线向上
  f
end
```

**验证**：边界盒 z 范围应为 0~墙高，不应出现负值。

#### pushpull 后面对象被删除

**问题**：`face.pushpull(h)` 后，原 face 对象被删除，再访问 `face.material` 会报错。

**解决方案**：先设置材质再 pushpull，或用 group 包裹。

#### 单位转换

**问题**：`.mm` 被调用两次会导致尺寸放大 1000 倍。

**解决方案**：坐标数值统一用 mm，在创建几何体时统一调用一次 `.mm`。

### 10.3 本项目特定事实（某 L 型空间）

> ⚠️ 以下内容仅适用于本案例项目，其他项目需重新从 CAD 提取。

#### 空间结构
- L 型 434㎡，横向臂（A/B/C）+ 纵向臂（D/E/F）
- **大通间设计**：区域之间无隔墙，只有结构柱
- 横向臂南墙（朝向天井）有 3 个 T 型墙（竖杆向北伸入室内 2250mm）
- B-C 之间有一段半截墙（从北墙向南延伸 2000mm）

#### 柱子分布
- 纵向臂柱子在中间线 x=28825 和东墙 x=32225
- D/E/F 区内部无柱，只有 D-E、E-F 分界处有柱
- D-E 分界：中间双柱 + 东墙双柱（1100mm 间距）
- C 区内有 1 根独立柱，靠近南墙/C-D 连通口

#### 门
- 5 扇门，均为 1500mm 双开门（非对称）
- 门 1/3 为防火门（北墙），门 2/4/5 为玻璃门

### 10.4 版本迭代记录（案例参考）

| 版本 | 错误类型 | 根因 | 教训 |
|------|---------|------|------|
| v2 | Y 轴方向颠倒 | 未确认 CAD Y 轴方向 | 先建立坐标系映射再建模 |
| v4 | L 型方向错误 | 凭印象移动纵向臂 | 一切以 CAD 原图为准 |
| v5 | 面法线向下 | 未检查 normal.z | add_face 后必须检查法线 |
| v6 | 区域间加了隔墙 | 假设区域间有墙 | 不要假设，从 CAD 确认 |
| v7 | T 型墙方向反 | 未仔细看图例 | 放大 CAD 图确认结构方向 |
| v11 | 柱子位置错 | 假设柱子在墙边 | 柱子可能在中间线，逐根核对 |
| v13 | 区域内多加柱 | 假设每个区域都有柱 | 分界柱≠区域内柱，仔细区分 |

---

*文档版本：v1.3 | 更新日期：2026-09-05 | 重构第十章：区分通用方法论与项目特定事实*
