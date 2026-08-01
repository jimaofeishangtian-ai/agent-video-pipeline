# Cross-agent adapter contract

The pipeline is portable because its artifacts and gates are portable. Do not make success depend on one agent product's hidden tool names.

## Capability discovery

At G0 classify each capability:

| Capability | Status values | Acceptable execution path |
|---|---|---|
| Shell and files | AVAILABLE / MISSING | Native terminal and workspace APIs |
| Media diagnostics | AVAILABLE / INSTALLABLE | `ffprobe` and `ffmpeg` |
| HyperFrames | AVAILABLE / INSTALLABLE | Installed Skill plus project-pinned CLI |
| Remotion | AVAILABLE / INSTALLABLE | Project-local npm packages and Studio |
| ChatCut | AVAILABLE / MISSING / AUTH | Native connector/plugin and logged-in editor |
| Seedance | AVAILABLE / PAID/AUTH / MISSING | Verified provider capability and current credits |
| Timeline review | AVAILABLE / LIMITED | Browser/GUI or a URL the user can open |

Do not infer an integration from the agent name. Inspect exposed tools, project dependencies, executable paths, and authenticated app state.

## Product profiles

- **Codex:** prefer installed Skills and MCP/app tools; fall back to project-local CLI and shell. Obey workspace `AGENTS.md` review rules.
- **Claude Code:** prefer available Skills/MCP servers and shell. A project `CLAUDE.md` may explain local commands, but canonical pipeline state remains in the shared manifests.
- **Trae and WorkBuddy:** use terminal/files/browser capabilities that are actually exposed. If no native ChatCut connector exists, prepare the manifest/assets and pause at the ChatCut handoff.
- **OpenClaw:** install/use the local Skill in its workspace only when authorized; use provider tools if present. For unavailable online stages, emit an operator handoff rather than claiming completion.
- **Unknown agent:** use the generic capability table and the canonical files. Never guess product-specific configuration paths.

## Fallback behavior

If a stage cannot run:

1. Mark the module `blocked` or `skipped`, never `complete`.
2. Keep upstream work and create a concise handoff containing required input, expected output schema, exact next gate, and any account action the user must take.
3. Do not replace Seedance with graphics and still call it Seedance. Record `simulated` with `provider: hyperframes-remotion`.
4. Do not download unofficial binaries or ask for secrets in chat. Use official authentication and credential storage.

## Portable workspace layout

Use a scoped project directory:

```text
inputs/                 untouched originals
proxy/                  one shared browser-safe proxy
manifests/              canonical JSON/YAML contracts
assets/seedance/        approved generated clips only
hyperframes/            live visual prototype
remotion/               Review and Final compositions
review/                 review log and representative captures
pipeline-state.json     resumable gate state
```

Absolute local paths may appear in runtime state, but distributable manifests should prefer paths relative to the project root.
