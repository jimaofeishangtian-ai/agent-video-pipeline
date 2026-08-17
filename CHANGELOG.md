# Changelog

## v3.0.0 - 2026-08-17

- 新增 `cutpilot`（CutPilot）作为经过多轮实测、易于记忆的生产入口，旧版 `agent-video-pipeline` 保留兼容。
- Remotion Studio 成为默认唯一完整主审片时间轴和最终渲染所有者。
- 固定 Remotion Semantic Effects Pro 基线 `pro-approved-2026-08-03-all-16-v3`。
- 增加一次合并式创意 intake，减少风格、旁白和细节的多轮追问。
- 增加真人口播、纯文案、PPT/PPTX/PDF 和混合输入的自动路由。
- 增加 Video Shotcraft 镜头设计、HyperFrames 独立中间片段以及 Remotion 回装规则。
- 增加个人剪辑偏好、PPT 视频化、纯文案成片、宿主兼容、语义中间表示和能力盘点说明。
- 增加可移植的能力盘点与 `edit-plan.json` 校验脚本，支持 Codex、WorkBuddy 和 CodeBuddy。
- 完成口播、PPT 和 Shotcraft 路线的前向验证；继续强制先审片、明确确认后再渲染。

## v2.1.0 - 2026-08-03

- 将 Seedance 选择门改为 ChatCut 托管、火山方舟直连、不调用 Seedance 三条执行通道。
- ChatCut 高质量最终镜头显式锁定 `seedance2 + 1080p`，阻止默认 720p 或 `seedance2mini` 冒充高质量成片。
- 明确 ChatCut 托管调用不需要用户提供 API Key；方舟直连只读取 Secret Store/`ARK_API_KEY` 是否配置，禁止在聊天、群消息、截图或提交文件中传递密钥。
- 增加模型 schema 探测和参数读回；运行环境未暴露 Seedance 2.5 时禁止伪造或静默替换。
- 增加参考锚点、真人授权、输入模式互斥、实际像素与物理一致性验收规则。
- 扩充项目模板中的执行通道、模型、分辨率、认证和 job/asset 证据字段。
- 校验器会拒绝把 720p 或 `seedance2mini` 标记为 `high-quality-final`。
- 环境诊断只报告 `ARK_API_KEY` 是否配置，不输出密钥值。

## v2.0.0 - 2026-08-01

- 将真人口播顺序优化为 ChatCut → HyperFrames → Seedance → Remotion → ChatCut。
- 增加跨 Codex、Claude Code、Trae、WorkBuddy、OpenClaw 的能力适配协议。
- 增加 `timeline-manifest.json`，统一所有模块的帧级时间。
- 增加 `generation-ledger.json`，区分 generated、simulated、skipped、blocked 和 failed。
- 增加 `glossary.json`，避免产品名与品牌词转录错误。
- 增加 Seedance A/B/免费替代选择门、单 job 审片和费用证据。
- 增加共享代理策略、字幕/主体碰撞检查和生成音频静音规则。
- 增加环境诊断、项目初始化和状态校验脚本。
- 强制 Remotion/ChatCut 时间轴审片，最终确认前不渲染、不导出。
