# CutPilot / Agent Video Pipeline

一套面向自媒体视频的自动剪辑 Skill。当前生产入口是 **CutPilot**，调用名为 `$cutpilot`：它可以从真人口播、素材、文案、PPT/PPTX、PDF 或混合输入开始，自动选择剪辑与动效路线，并把整条视频统一放到 Remotion Studio 主时间轴审片。

旧版 `agent-video-pipeline` 仍保留在仓库中，供已有项目兼容使用。

## 当前生产路线

```text
素材 / 口播 / 文案 / PPT
        ↓
CutPilot 统一理解、提问与语义规划
        ↓
按内容自动选择能力
├─ 真人口播整理、转录、字幕、B-roll
├─ video-shotcraft：镜头语言与模板化镜头设计
├─ HyperFrames：独立高级动效片段
├─ Remotion Semantic Effects Pro：语义信息动效
└─ ChatCut / 生成工具：按能力作为分析或中间素材提供者
        ↓
Remotion Studio 唯一完整主审片时间轴
        ↓
用户最终确认后由 Remotion 渲染
```

默认 Remotion 动效基线：`pro-approved-2026-08-03-all-16-v3`。

## 主要能力

- 支持真人口播、普通素材、纯文案、PPT/PPTX、PDF 和混合输入。
- 新任务通过一次合并式选项卡确认风格、声音和关键约束，减少反复沟通。
- 根据内容与当前宿主能力，自动判断是否使用 Video Shotcraft、HyperFrames、ChatCut、素材搜索或生成工具。
- PPT 不按幻灯片机械播放，而是重写为视频叙事、线稿图解、动态图表或镜头化表达。
- 只有文案时先锁定旁白，再进行场景与动效设计。
- Remotion Studio 默认是唯一完整主审片时间轴；HyperFrames 只提供确认后的独立中间片段。
- 未获得“最终确认 / 可以渲染 / 开始导出”等明确授权前，不渲染最终视频。
- 支持 Codex、WorkBuddy、CodeBuddy 及其他 Agent-Skills 兼容宿主，并提供能力降级路线。

## 安装

将完整的 `skill/cutpilot` 文件夹复制到宿主的自定义 Skills 根目录，不能只复制 `SKILL.md`。

常见目录：

```text
Codex:      ~/.codex/skills/cutpilot
WorkBuddy:  ~/.workbuddy/skills/cutpilot
CodeBuddy:  ~/.codebuddy/skills/cutpilot
```

也可以把下面这段话连同仓库链接交给 Agent：

```text
请从这个仓库安装并验证 CutPilot Skill：
https://github.com/jimaofeishangtian-ai/agent-video-pipeline

完整复制 skill/cutpilot 文件夹到当前宿主实际使用的自定义 Skills 根目录，
运行 scripts/inventory_capabilities.mjs，并用 assets/edit-plan.example.json
执行 scripts/validate_edit_plan.mjs 冒烟测试。安装阶段不要生成或渲染视频。
```

## 使用

```text
使用 $cutpilot，根据我的素材自动选择合适流程，先给我一次合并式创意选项，
然后建立 Remotion Studio 主审片时间轴；没有最终确认前不要渲染。
```

针对明确的局部修改，Skill 会跳过重复问答，直接延续现有项目与已确认内容。

## 仓库结构

```text
skill/
├─ cutpilot/                # 当前生产入口
│  ├─ SKILL.md
│  ├─ agents/
│  ├─ assets/
│  ├─ references/
│  └─ scripts/
└─ agent-video-pipeline/    # 旧版兼容入口
```

## 验证过的场景

- 纯口播视频的自动包装与 Remotion 主时间轴审片。
- PPT 重写为带旁白、BGM、字幕和语义动效的视频。
- Video Shotcraft 镜头语言版本，并回到 Remotion Studio 统一审片与 1080P/60FPS 渲染。
- 云舟中文旁白、BGM 与多层 SFX 的完整音轨输出。

## 版本

当前生产版：`v3.0.0`，参见 [CHANGELOG.md](CHANGELOG.md)。

本仓库公开可读，但未附带开源许可证。除非另有书面授权，保留全部权利。
