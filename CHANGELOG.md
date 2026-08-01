# Changelog

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
