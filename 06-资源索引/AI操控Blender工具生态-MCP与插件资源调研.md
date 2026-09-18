---
title: "AI 操控 Blender 工具生态：MCP 协议、AI 插件与资源站点调研"
type: 资源索引
scope: 通用
source: "GitHub 开源社区调研 + 各工具官网文档"
date: 2026-09-18
tags: [Blender, MCP, AI Agent, 3D建模, 材质生成, 资源索引, AI工具]
---

# AI 操控 Blender 工具生态：MCP 协议、AI 插件与资源站点调研

> 调研时间：2026-09-18 ｜ 定位：补充 [实景三维重建-AI驱动Blender原生建模工作流.md](../02-空间搭建/实景三维重建-AI驱动Blender原生建模工作流.md) 的工具选型上下文——从"扫描产物→可编辑模型"这一条具体路线，延伸到"AI 通过自然语言直接操控 Blender"的通用工具生态
> 适用场景：用 AI 做空间方案建模、快速出渲染图、批量修改场景、生成贴图材质、自动摆放设备

---

## 〇、文档关系

| 相关文档 | 与本文档的关系 |
|----------|---------------|
| [实景三维重建-AI驱动Blender原生建模工作流.md](../02-空间搭建/实景三维重建-AI驱动Blender原生建模工作流.md) | 本库已有的 Blender 具体工作流。本文为其"工具选型"横向扩展，覆盖 MCP 协议与 AI 插件生态 |
| [AI辅助创客空间规划-方法与工具库.md](../02-空间搭建/AI辅助创客空间规划-方法与工具库.md) | AI 空间规划的全局方法论；Blender AI 工具可作为其"深化输出"阶段的渲染/建模手段 |
| [SketchUp自动化与AI设备自动摆放-工作方法与踩坑记录.md](SketchUp自动化与AI设备自动摆放-工作方法与踩坑记录.md) | SketchUp 路线与本文 Blender 路线互为备选，选型对比见本文 §五 |
| [开源软件工具链清单.md](../03-设备与工具/开源软件工具链清单.md) | 列出 Blender 本体作为开源 3D 建模工具；本文补充 AI 操控层的能力 |
| [AI应用现状全景-创客空间各领域调研.md](AI应用现状全景-创客空间各领域调研.md) | AI 全领域应用背景地图；本文聚焦 3D 建模这个子领域 |

---

## 一、技术路线概述

AI 操控 Blender 目前有三种主流技术路线：

| 路线 | 原理 | 代表项目 | 适合场景 |
|------|------|---------|---------|
| **MCP 协议**（Model Context Protocol） | Blender 内装插件起 Socket 服务，AI 客户端（Claude Desktop、Cursor、Ollama 本地模型）通过 MCP 协议调用工具，直接操作 Blender API | blender-mcp、blender-mcp-enhanced、Rogue-AI-Assistant | 开发者自定义 Agent；对接本地大模型；批量自动化 |
| **内置 AI 面板插件** | Blender 侧边栏直接出现 AI 聊天面板，输入自然语言生成 Python 脚本并执行 | Blender-Copilot、BlenderGPT、Rogue-AI-Assistant | 艺术家在 Blender 内直接对话，不切换外部软件 |
| **本地 AI 生成插件** | 在 Blender 内部调用本地 AI 模型（如 Stable Diffusion）生成贴图/3D 资产 | Dream-Textures、Rapid-Assets AI | 隐私优先的贴图/资产生成，不依赖云端 API |

---

## 二、MCP 协议类（主流，AI 外部代理控制 Blender）

> MCP（Model Context Protocol）是 AI 模型与工具之间的开放协议标准。Blender MCP 系列工具让 AI 客户端能直接创建/修改物体、材质、灯光、相机、几何节点，执行任意 Python 脚本。

### 2.1 blender-mcp（原版，最活跃）

| 项 | 值 |
|----|-----|
| 仓库 | [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) |
| 官网 | [blendermcp.org](https://blendermcp.org/zh-cn)（含中文文档） |
| 协议 | MIT |
| 核心能力 | 创建/修改物体、材质、灯光、相机；执行任意 Blender Python 脚本；对接 PolyHaven 素材库；可接 Claude / GPT-4o / Gemini / Ollama 本地模型 |
| 使用方式 | Blender 安装 `addon.py` 插件 → 启动 Socket 服务；AI 客户端配置 MCP 服务（`uvx blender-mcp`） |
| 安全提醒 | MCP 模式允许 AI 执行任意 Python 脚本，不要在不受信任的模型下打开重要工程 |

**典型工作流**：
1. Blender 安装 `addon.py` 插件，启用插件，启动 Socket 服务
2. AI 客户端配置 MCP 服务（`uvx` 运行 `blender-mcp`）
3. 提示词示例："在场景创建一个金属材质的杯子，布置三点灯光，设置相机角度，渲染一张图"
4. AI 自动调用工具，生成/运行 Blender Python 代码完成操作

### 2.2 blender-mcp-enhanced（社区增强 Fork）

| 项 | 值 |
|----|-----|
| 仓库 | [zachhandley/blender-mcp-enhanced](https://github.com/zachhandley/blender-mcp-enhanced) |
| PyPI | `blender-mcp-enhanced` |
| 新增能力 | 几何节点支持、多轮对话上下文、工具链增强、更多资源接口 |

在原版基础上增加了几何节点（Geometry Nodes）操作能力，适合需要参数化生成的场景。

### 2.3 Rogue-AI-Assistant-Blender（内置聊天面板，支持本地 LM-Studio）

| 项 | 值 |
|----|-----|
| 仓库 | [MakanAnsariCG/rogue-ai-assistant-blender](https://github.com/MakanAnsariCG/rogue-ai-assistant-blender) |
| 下载 | [itch.io 页面](https://makan-shturl.cc/GHRgOY99Cv-ai-assistant-mcp) |
| 特点 | Blender 内部 UI 聊天窗口，不需要外部 AI 客户端；同时兼容 MCP 协议；支持 OpenAI / Claude / Gemini / 本地 Ollama / LM-Studio |

**最适合的选型场景**：艺术家不想开外部软件，直接在 Blender 窗口聊天即可操控一切，且支持本地大模型保护隐私。

---

## 三、AI 面板/脚本生成类（Blender 内直接使用）

### 3.1 Blender-Copilot

| 项 | 值 |
|----|-----|
| 仓库 | [pedronaugusto/blender-copilot](https://github.com/pedronaugusto/blender-copilot) |
| PyPI | `blender-copilot` |
| 定位 | 轻量 Copilot 插件，在 Blender 侧边栏对话，生成并执行 Python 脚本 |

适合快速脚本自动化、批量修改物体、灯光设置等日常操作。

### 3.2 BlenderGPT（老牌，自然语言 → Python 脚本）

| 项 | 值 |
|----|-----|
| 仓库 | [gd3kr/BlenderGPT](https://github.com/gd3kr/BlenderGPT) |
| 定位 | 把自然语言转为 Blender Python 脚本（OpenAI API），适合自动化工作流 |
| 局限 | 不支持 MCP 协议，单轮生成，不保留场景上下文 |

属于早期探索项目，适合简单的一次性脚本生成任务。

---

## 四、本地 AI 生成类插件（贴图/3D 资产）

### 4.1 Dream-Textures（本地 Stable Diffusion 贴图生成）

| 项 | 值 |
|----|-----|
| 仓库 | [cgtinker/DreamTextures](https://github.com/cgtinker/DreamTextures) |
| 协议 | GPL-3.0 |
| 核心能力 | Blender 内部运行本地 Stable Diffusion 模型，生成 PBR 贴图/图像/视频纹理；不需要云端 API 密钥；隐私优先 |
| 适用场景 | 创客空间内网环境下的贴图生成，无需外部网络 |

### 4.2 Rapid-Assets AI（文本 → 3D 资产）

| 项 | 值 |
|----|-----|
| 官网 | [rapidassets.ai](https://rapidassets.ai) |
| 定位 | Blender 插件；文本直接生成带贴图的 3D 资产并导入场景；云端生成 |
| 适用场景 | 快速填充场景资产（家具、道具等），降低人工建模时间 |

---

## 五、配套文档与 MCP 资源站点

| 资源 | 链接 | 说明 |
|------|------|------|
| blendermcp.org | https://blendermcp.org/zh-cn | 中文文档，对比各 Blender AI Agent 工具，快速上手教程 |
| HiMCP AI MCP 市场 | https://himcp.ai/server/blender-mcp-fvv | 搜索 blender-mcp，查看配置样例 |
| LobeHub MCP 库 | https://lobehub.com/mcp/yuri-schmaltz-blender-mcp | Blender-MCP 本地模型配置参考 |

---

## 六、选型建议

### 6.1 按角色推荐

| 使用角色 | 推荐工具 | 理由 |
|---------|---------|------|
| **开发者**（用 Cursor/Claude Desktop） | blender-mcp（原版） | 可自定义 Agent，对接 Ollama 本地大模型，最活跃的生态 |
| **AI 空间规划师**（批量化建模、渲染） | blender-mcp + Dream-Textures | 先 MCP 批量建场景，再本地 SD 生成贴图，适合离线工作流 |
| **艺术家/设计师**（不想开外部软件） | Rogue-AI-Assistant-Blender | Blender 内直接聊天，支持本地 LM-Studio |
| **快速脚本自动化**（批量修改物体、灯光） | Blender-Copilot / BlenderGPT | 轻量、零配置，适合一次性任务 |
| **内网/隐私优先**（贴图生成） | Dream-Textures | 本地 Stable Diffusion，不依赖云端 API |
| **快速填充场景资产** | Rapid-Assets AI | 文本直接生成带贴图的 3D 资产 |

### 6.2 与现有知识库工具的路线对比

| 对比维度 | Blender 路线（本文） | SketchUp 路线（知识库已有） |
|----------|---------------------|--------------------------|
| 核心接口 | Python `bpy`，可通过 MCP 或 AI Agent 调用 | Ruby API + MCP `eval_ruby` |
| AI 操控生态 | 丰富：MCP 生态成熟，多个项目活跃迭代 | 有限：仅有 SketchUp自动化文档中的自建工具链 |
| 渲染输出 | Cycles / Eevee（照片级渲染） | V-Ray / Enscape（建筑可视化为主） |
| 优势场景 | 自由曲面、有机形态、精细材质、动画 | 精确建筑尺寸、施工图对接、快速体块推敲 |
| 建议策略 | 空间方案深化设计 + 渲染可视化 | 前期平面布局 + 尺寸校验 |

---

## 七、安全提醒

MCP 模式允许 AI 执行任意 Python 脚本，以下风险需要知晓：

- ⚠️ **不要在不受信任的模型下打开重要工程文件**——AI Agent 可能执行意外操作（删除物体、修改场景、导出文件）
- ⚠️ **MCP Server 监听本地端口**，默认不设认证，同一机器上的其他进程可连接——在多用户环境中注意端口隔离
- ⚠️ **本地大模型外挂 MCP 时**，模型获得的 Blender 读写权限等同于当前用户——建议用专用测试工程文件操作，不直接处理生产资产

---

## 八、延伸阅读

- [实景三维重建-AI驱动Blender原生建模工作流.md](../02-空间搭建/实景三维重建-AI驱动Blender原生建模工作流.md)——将实景扫描产物重建为可编辑 Blender 模型的具体工作流（本文的生态中，"扫描→重建"输入侧的选配工具之一）
- [AI辅助创客空间规划-方法与工具库.md](../02-空间搭建/AI辅助创客空间规划-方法与工具库.md)——AI 空间规划七步工作流与提示词模板
- [SketchUp自动化与AI设备自动摆放-工作方法与踩坑记录.md](SketchUp自动化与AI设备自动摆放-工作方法与踩坑记录.md)——SketchUp 路线的自动化方案与踩坑记录，可与本文 Blender 路线二选一或互补使用
- [开源软件工具链清单.md](../03-设备与工具/开源软件工具链清单.md)——Blender 本体作为开源软件在创客空间教学中的应用

---

## 变更记录

| 版本 | 日期 | 变更内容 |
|------|------|---------|
| v1.0 | 2026-09-18 | 首次成文。收录 blender-mcp 系列、Rogue-AI-Assistant、Blender-Copilot、BlenderGPT、Dream-Textures、Rapid-Assets AI 等工具，配套选型建议与安全提醒 |
