# Environment bootstrap

## Audit first

Run `python scripts/diagnose_env.py --json` from the skill directory. Check the target project's own `package.json`, lockfile, and scripts before proposing installs. Detect, do not assume:

- Git
- Node.js LTS, npm, npx
- Python 3
- FFmpeg/ffprobe for read-only media diagnostics
- HyperFrames CLI/project state
- Remotion packages and Studio script
- any native ChatCut connector/plugin registration and authentication
- current Seedance execution channel, exact callable model IDs, supported resolutions, entitlement, authentication state, and displayed credit estimate
- free disk space and write access

## Installation policy

1. Prefer project-local, version-pinned packages.
2. Use official package managers and vendor sources. Do not download random binaries from mirrors or execute unreviewed remote scripts.
3. Present one install plan containing the exact packages, scope, estimated download/disk impact, and commands.
4. Ask for confirmation before system-wide installs, PATH changes, authentication, or paid service activation. After approval, continue without repeatedly asking for each local package.
5. Verify versions and run the smallest smoke test after installation.
6. Never store tokens in tracked files or request them in chat. Use the host credential store, connector OAuth, or environment variables excluded from version control. Report only whether `ARK_API_KEY` is configured; never echo its value.

## Expected local setup

- HyperFrames: use the project-pinned CLI where available; for a new project, scaffold with the current official CLI and keep the pin reproducible. Before render-affecting work on an existing project, check whether the pinned CLI needs a verified upgrade.
- Remotion: keep packages in the project `devDependencies`; provide `studio`, `lint`, and typecheck scripts. Do not render during setup.
- ChatCut: inspect the current agent's actual tool registry. On Codex, `codex mcp get chatcut` may be used when available; on other agents use their documented connector registry. Authenticate with the supported flow. Do not invent or locally bootstrap an undocumented MCP server.
- Seedance: distinguish ChatCut-managed generation from direct Volcengine Ark. ChatCut-managed calls use ChatCut login/OAuth and credits, not a user-supplied API key. Direct Ark calls require the user to configure `ARK_API_KEY` securely and explicitly choose direct billing. Resolve exact model IDs at runtime. For a high-quality current ChatCut final, explicitly request `seedance2` at `1080p`; do not accept the default 720p or `seedance2mini` as equivalent. If unavailable, offer existing/stock footage or HyperFrames/Remotion graphics without claiming Seedance ran.

## Cross-platform strategy

Use the system's native package manager only after detecting the OS. On Windows prefer `winget` when available; on macOS prefer Homebrew when already installed; on Linux use the distribution package manager. If a package manager is absent, give the user the official download path instead of silently installing a new package manager.

## Smoke tests

- `node --version`, `npm --version`, `npx --version`
- `ffmpeg -version`, `ffprobe -version`; probe the source and create at most one shared review proxy when required
- HyperFrames project: `npx hyperframes check` after a composition exists
- Remotion: start Studio and open the Review composition; do not render a still/video for setup verification
- ChatCut: list/create/target the intended project and surface the editor URL

Record results under `pipeline-state.json.environment`.
