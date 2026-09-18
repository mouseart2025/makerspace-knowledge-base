---
title: "三维模型网页发布与分享工作流：Blender → GLB → model-viewer 单文件网页 / 飞书文档归档"
type: 资源索引
scope: 通用
source: "柴火团队实战复盘（2026-09，Blender 5.2 + @google/model-viewer 3.5 + 飞书云文档）"
date: 2026-09-18
tags: [Blender, GLB, glTF, model-viewer, 网页3D, 模型分享, 单文件HTML, 飞书文档, 无头Chrome, AR, 交付物]
---

# 三维模型网页发布与分享工作流

> 把 Blender 原生模型变成"发一个文件/链接就能旋转查看"的网页成果，并归档进飞书文档作为勘察/设计成果。
>
> 配套阅读：模型怎么建见 [实景三维重建-AI驱动Blender原生建模工作流.md](../02-空间搭建/实景三维重建-AI驱动Blender原生建模工作流.md)；模型怎么按实测核对修订见 [实景重建模型-实测标注核对与版本化修订工作流.md](../02-空间搭建/实景重建模型-实测标注核对与版本化修订工作流.md)。

---

## 一、三条发布路线与选型

| 路线 | 产物 | 查看方式 | 可见性 | 适用 |
|---|---|---|---|---|
| **A. 单文件 HTML**（推荐首选） | 1 个 .html（GLB 以 base64 内嵌，约 1MB/千构件量级） | 双击用浏览器打开；微信/邮件直接发文件 | 不公开，收件人范围即分享范围 | 内部评审、客户私发、不允许公开的实测数据 |
| **B. 静态托管公开链接** | index.html + .glb，挂 GitHub Pages / 任意静态空间 | 一个网址，可嵌公众号/文档 iframe | **全网可见、可下载** | 宣传展示、公开汇报、需要在飞书文档里"嵌入网页"块直接交互 |
| **C. 仅发 GLB** | .glb 单文件 | 对方需有 3D 软件或在线查看器 | 随发送范围 | 交给设计/施工方继续编辑（glTF 生态通用） |

关键判断：**飞书文档不能运行本地 HTML/JS**。想在文档里直接交互，只能走 B（公开 https URL + "嵌入网页"块）；不接受公开就走 A，文档内放渲染图 + HTML 附件（见 §六）。

## 二、从 Blender 导出 GLB

glTF/GLB 是网页 3D 的事实标准（OpenGL 系，Y-up、米制）。无头导出脚本要点：

```python
# export_web.py：blender --background --python export_web.py -- 模型.blend out.glb
import bpy, sys, os
src, out = sys.argv[sys.argv.index("--")+1:][0:2]
bpy.ops.wm.open_mainfile(filepath=src)

# 1) 隐藏参考层（导入的 OBJ/扫描底模，文件名前缀 REF_）
for o in bpy.data.objects:
    if o.name.startswith("REF_"):
        o.hide_set(True); o.hide_render = True; o.hide_viewport = True

# 2) 文字标注必须转网格：glTF 不导出 FONT 对象，中文标注否则全部丢失
texts = [o for o in bpy.data.objects if o.type == 'FONT']
bpy.ops.object.select_all(action='DESELECT')
for o in texts: o.select_set(True)
if texts:
    bpy.context.view_layer.objects.active = texts[0]
    bpy.ops.object.convert(target='MESH')

# 3) 仅导出可见网格
bpy.ops.object.select_all(action='DESELECT')
n = 0
for o in bpy.data.objects:
    if o.type == 'MESH' and not o.hide_get() and not o.hide_render:
        o.select_set(True); n += 1

bpy.ops.export_scene.gltf(filepath=out, export_format='GLB', use_selection=True,
                         export_apply=True, export_yup=True,
                         export_cameras=False, export_lights=False)
print("mesh count:", n)
```

注意：

- **修改器要应用**（`export_apply=True`），否则布尔/实体化结果不进 GLB；
- 灯光/相机关闭导出，网页端用 model-viewer 自带 IBL 照明；
- 材质用 Principled BSDF 最稳；自发光/节点特效可能降级，导出后必须回读验证；
- 实战参考：319 个可见网格、含中文面积标注的结构模型，GLB 约 730KB。

## 三、model-viewer 查看页

Google 的 [`<model-viewer>`](https://modelviewer.dev/) Web Component 是最省事的方案：一行标签带轨道控制、自动取景、阴影、移动端 AR（Scene Viewer/Quick Look）。

页面骨架（关键属性）：

```html
<script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer@3.5.0/dist/model-viewer.min.js"></script>
<model-viewer src="./asbuilt.glb" camera-controls touch-action="pan-y"
  auto-rotate auto-rotate-delay="2500" shadow-intensity="1"
  environment-image="neutral" camera-orbit="35deg 70deg auto"
  field-of-view="32deg" interaction-prompt="none" ar>
  <!-- 标注热点：坐标为 glTF 坐标系（米，Y 朝上） -->
  <button class="hotspot" slot="hotspot-1"
          data-position="28.8 1.5 -18.7" data-normal="0 0 1"></button>
  <div slot="hotspot-1"><b>双柱</b><br>中距 700 / 净距 200</div>
</model-viewer>
```

工程要点：

1. **坐标换算**：Blender（X 东、Y 北、Z 上，毫米）导出 Y-up 后为 glTF（X 东、**Y=高度**、Z=−Y_blender，米）。热点坐标 = `(x/1000, z/1000, -y/1000)`；
2. **视角按钮**改 `camera-orbit` 属性即可，格式"方位角 仰角 距离"；正俯视 `0deg 0deg 60m`，室内立面 `180deg 86deg 45m`（距离按模型尺寸给，`auto` 只适合默认取景）；
3. 打开模型后显式设 `cameraTarget` 到模型包围盒中心（L 型等非对称模型自动取景点会偏）；
4. CDN 国内优先 **jsdelivr**（unpkg 部分网络不稳）；首次打开必须联网加载组件（约 1.5MB），之后走缓存；
5. 侧边栏放修订要点、分色图例、"非测绘级、不作为施工依据"声明，查看页本身就是汇报材料。

## 四、单文件化（IM/邮件直接发）

把 GLB base64 内嵌为 data URI，外部只依赖 CDN 脚本，`file://` 双击即可打开（已实测）：

```python
import base64
b64 = base64.b64encode(open('asbuilt.glb','rb').read()).decode()
html = open('index.html', encoding='utf-8').read()
html = html.replace('src="./asbuilt.glb"',
                    'src="data:model/gltf-binary;base64,%s"' % b64)
open('模型分享-单文件.html','w',encoding='utf-8').write(html)
```

- 需要**完全离线**时，再把 model-viewer.min.js 下载下来内联进 `<script>`（文件总大小约再增 1.5MB）；
- 微信里文件可能被重命名/拦截，引导用户"用浏览器打开"；邮件和飞书文件最稳。

## 五、无头 Chrome 交付前验证（不依赖人工开浏览器）

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu \
  --enable-unsafe-swiftshader --use-angle=swiftshader \
  --screenshot=check.png --window-size=1500,950 \
  --virtual-time-budget=30000 --hide-scrollbars \
  "file:///.../单文件.html"     # 或 http://127.0.0.1:8000/index.html
```

- 不加 `--enable-unsafe-swiftshader` 时无头环境 WebGL 可能起不来，画面只剩 UI 框架（模型区空白）——这是最常见的"页面做好了但模型不显示"误判；
- `--virtual-time-budget` 给模块加载 + GLB 解码留时间（20–40s）；
- 验证 GLB 本体另做一道：新开 Blender 进程**重新导入 GLB** 渲染俯视图，核对包围盒尺寸、构件数量、中文标注是否随网格导出；
- 本地静态服务 `python3 -m http.server 端口`，验完即关。

## 六、飞书文档归档模式（不公开数据的标准做法）

交互网页无法在飞书文档内运行，采用"**内嵌关键渲染图 + 附件挂全套成果**"：

1. 文档正文放：成果概览表（数据源/版本/对象数/分区面积）、俯视/透视/专项内视图、新旧对照图、修订要点、待现场复核清单；
2. 附件区挂 4 个文件：① 单文件交互 HTML；② GLB；③ Blender 源模型；④ 模型修订说明；
3. 附件用文档 XML 的 `<source>` 标签随文档创建一次上传，图片用 `<img>` 内嵌并配图注；
4. 文档开头声明"方案推演模型，非测绘级，不作为施工依据"；
5. 若后续改为公网托管，可在文档中追加"嵌入网页"块直接交互，但**嵌入即意味着模型对有链接者公开**，需先走脱敏（项目名、业主信息、内网地址）。

## 七、踩坑清单

| 现象 | 原因/处理 |
|---|---|
| GLB 导出后中文标注全没了 | FONT 对象不进 glTF，先 convert 成 MESH |
| 网页模型区空白，UI 正常 | WebGL 未初始化（加 SwiftShader 参数）或虚拟时间预算不够；也可能是 CDN 被网络拦截，换 jsdelivr |
| 模型显示但全白/过曝 | Blender 自发光/世界强度随 GLB 材质带过去了；网页端用 `environment-image="neutral"` 并简化材质，别导出灯光 |
| 热点位置飘 | 忘了 Y-up 与毫米→米换算，公式见 §三 |
| 俯视/立面按钮取景错乱 | 距离用了 `auto` 或模型尺寸量级不匹配，按包围盒给明确米数 |
| 单文件发给同事打不开 | 引导用系统浏览器打开（不要用内置文档预览）；完全离线场景内联 JS |
| 飞书里上传 HTML 只能下载不能点开交互 | 平台限制，属预期；交互发生在下载后的浏览器里 |

## 八、交付检查清单

- [ ] GLB 经"新进程重新导入渲染"验证：包围盒、构件数、文字、材质正确；
- [ ] 参考层/隐藏构件未混入导出，对象数与源模型验收口径一致；
- [ ] 页面经无头截图验证（模型真正渲染出来，而非只显示框架）；
- [ ] 单文件版经 `file://` 协议验证可打开；
- [ ] 热点坐标经 Y-up/米制换算并逐个目检；
- [ ] 页面含版本、数据源、日期、非施工依据声明；
- [ ] 公开路线已过脱敏；私有路线以附件形式归档进飞书并设置文档权限。
