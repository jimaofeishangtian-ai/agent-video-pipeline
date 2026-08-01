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
- current Seedance entitlement and displayed credit estimate
- free disk space and write access

## Installation policy

1. Prefer project-local, version-pinned packages.
2. Use official package managers and vendor sources. Do not download random binaries from mirrors or execute unreviewed remote scripts.
3. Present one install plan containing the exact packages, scope, estimated download/disk impact, and commands.
4. Ask for confirmation before system-wide installs, PATH changes, authentication, or paid service activation. After approval, continue without repeatedly asking for each local package.
5. Verify versions and run the smallest smoke test after installation.
6. Never store tokens in tracked files. Use the host credential store, connector OAuth, or environment variables excluded from version control.

## Expected local setup

- HyperFrames: use the project-pinned CLI where available; for a new project, scaffold with the current official CLI and keep the pin reproducible. Before render-affecting work on an existing project, check whether the pinned CLI needs a verified upgrade.
- Remotion: keep packages in the project `devDependencies`; provide `studio`, `lint`, and typecheck scripts. Do not render during setup.
- ChatCut: inspect the current agent's actual tool registry. On Codex, `codex mcp get chatcut` may be used when available; on other agents use their documented connector registry. Authenticate with the supported flow. Do not invent or locally bootstrap an undocumented MCP server.
- Seedance: treat it as a ChatCut paid generation capability. Verify entitlement at runtime. If unavailable, offer existing/stock footage or HyperFrames/Remotion motion graphics; do not claim another paid model is a free substitute.

## Cross-platform strategy

Use the system's native package manager only after detecting the OS. On Windows prefer `winget` when available; on macOS prefer Homebrew when already installed; on Linux use the distribution package manager. If a package manager is absent, give the user the official download path instead of silently installing a new package manager.

## Smoke tests

- `node --version`, `npm --version`, `npx --version`
- `ffmpeg -version`, `ffprobe -version`; probe the source and create at most one shared review proxy when required
- HyperFrames project: `npx hyperframes check` after a composition exists
- Remotion: start Studio and open the Review composition; do not render a still/video for setup verification
- ChatCut: list/create/target the intended project and surface the editor URL

Record results under `pipeline-state.json.environment`.
