# Changelog

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
