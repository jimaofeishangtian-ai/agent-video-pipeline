# Agent Video Pipeline

一套可编辑、可恢复、可审片、可验证真实调用的四模块自动剪辑 Skill。

```text
ChatCut 口播锁定
→ HyperFrames 视觉方向
→ Seedance 执行通道选择、1080p 模型锁与真实镜头生成
→ Remotion 参数化动效
→ ChatCut 字幕、多轨总装与最终时间轴
```

适用于 Codex、Claude Code、Trae、WorkBuddy、OpenClaw，以及其他具备文件和终端能力的 Agent。在线连接器是否可用，以用户当前 Agent、账号授权和订阅为准。

## 最简单的安装方式

把下面这段话连同本仓库链接发给你的 Agent：

```text
请安装并验证这个视频工作流 Skill：
https://github.com/jimaofeishangtian-ai/agent-video-pipeline

要求：
1. 下载最新 GitHub Release 中的 agent-video-pipeline ZIP。
2. 核对 Release 公布的 SHA256。
3. 解压并保留完整 agent-video-pipeline 文件夹，不能只复制 SKILL.md。
4. 优先安装到当前 Agent 实际显示的自定义 Skills 根目录；若当前 Agent 没有原生 Skill 加载器，就放入项目工作区并完整读取 SKILL.md。
5. 运行环境诊断和 Skill/项目结构校验。
6. 只汇报安装与验证结果，不要在安装阶段生成、渲染或导出视频。
```

最新版本入口：<https://github.com/jimaofeishangtian-ai/agent-video-pipeline/releases/latest>

## 使用方式

支持 Skills 调用的 Agent：

```text
使用 $agent-video-pipeline 检查我的素材与环境，从第一个未完成 gate 开始，并停在第一个需要我批准的步骤。
```

没有原生 Skill 加载器的 Agent：

```text
完整读取 agent-video-pipeline/SKILL.md，按 references 和 scripts 执行。先输出能力表；ChatCut 或 Seedance 连接器不存在时生成交接包并暂停，禁止伪造调用。
```

## 为什么 ChatCut 先进入

真人口播的字幕、B-roll 和动效都依赖最终口播时间。Skill 因此先用 ChatCut 建立真实转录、语义剪辑和停顿锁定，再让 HyperFrames、Seedance、Remotion 消费同一份 `timeline-manifest.json`；最后返回 ChatCut 总装。

没有真人口播或尚处于拍摄前概念阶段时，才使用 HyperFrames 先行。

## Seedance 选择门

- A：通过 ChatCut 托管调用，使用 ChatCut 登录/积分；高质量最终镜头显式锁定 `seedance2 + 1080p`，不需要另发 API Key。
- B：火山方舟直连；用户自行开通，并把 `ARK_API_KEY` 配置到 Secret Store 或本机环境变量，禁止粘贴到聊天或群消息。
- C：不调用 Seedance；Agent 根据内容选 HyperFrames、Remotion 或两者组合，并明确记录为 `simulated` 或 `skipped`。

Skill 本身不包含 ChatCut/Seedance 订阅或生成积分。Agent 必须在付费生成前显示执行通道、精确模型、分辨率、参考素材、当前账号权限和预计消耗，生成后读回 job 参数并等待用户审片。当前连接器没有暴露的模型（例如 Seedance 2.5）不得编造调用。

## 仓库结构

```text
agent-video-pipeline/
├─ README.md
├─ INSTALL_WITH_AGENT.txt
├─ CHANGELOG.md
└─ skill/
   └─ agent-video-pipeline/
      ├─ SKILL.md
      ├─ agents/
      ├─ assets/
      ├─ references/
      └─ scripts/
```

GitHub 仓库源码把说明文件与 Skill 分开；Release ZIP 的顶层直接是 `agent-video-pipeline/`，可以放入 Agent 的 Skills 根目录。

核心状态文件包括：

- `pipeline-state.json`：恢复点与 gate 状态；
- `timeline-manifest.json`：唯一帧级时间源；
- `generation-ledger.json`：四模块真实调用凭证；
- `glossary.json`：品牌、产品、人名和术语纠错；
- `edit-lock.json`：批准的口播内容；
- `creative-contract.json`：视觉系统和安全区；
- `shot-plan.json`：Seedance 镜头与批准资产；
- `motion-manifest.json`：Remotion 图层和时间。

## 安全与审片规则

- 不伪造连接器、登录、余额、job ID、asset ID 或生成结果。
- 原始媒体不覆盖；需要时只生成一份共享浏览器代理。
- Remotion/ChatCut 默认先在可编辑时间轴审片。
- 未获得明确“最终确认/可以渲染/开始导出”前，不渲染或导出最终视频。

## 版本

当前稳定版：`v2.1.0`。参见 [CHANGELOG.md](CHANGELOG.md)。

本仓库公开可读，但未附带开源许可证。除非另有书面授权，保留全部权利。
