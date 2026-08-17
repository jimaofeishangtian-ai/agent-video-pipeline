# Host compatibility

This skill follows the portable Agent Skills layout: one `SKILL.md` plus relative `references/`, `scripts/`, and `assets/`. Keep core decisions independent of a host brand.

## Discovery and installation

- Codex user scope: `~/.codex/skills/creator-auto-edit/`
- WorkBuddy user scope: `~/.workbuddy/skills/creator-auto-edit/`
- CodeBuddy user scope: `~/.codebuddy/skills/creator-auto-edit/`
- Project scope: use the host's project-level skills directory when the user explicitly requests a project-only installation.

Copy the complete directory; do not copy `SKILL.md` alone. A host may ignore `agents/openai.yaml`; this does not affect the workflow.

## Capability mapping

Treat capability names as roles, then map them to installed tools:

- presentation parser: structured PPTX/PPT/PDF extraction;
- transcript/cut analyzer: word timing and source-range decisions;
- shot library: exact shot recipes and motion vocabulary;
- motion provider: isolated HTML/3D/chart/UI/diagram segments;
- master timeline: editable whole-piece review and final assembly;
- media providers: real capture, licensed stock, image/video generation, voice, music, and SFX.

If a named provider is unavailable, preserve the role and use the documented fallback. Do not pretend a Codex plugin or MCP tool exists in WorkBuddy. Do not auto-install missing providers unless the user explicitly asks.

## Portable execution rules

- Resolve all references relative to this skill directory.
- Use Node scripts only when `node` is available; otherwise reproduce their read-only checks with host-native file tools.
- Use structured forms/cards when supported and one compact numbered intake otherwise.
- Keep `edit-plan.json`, `asset-ledger.json`, review notes, and provider contracts portable across hosts.
- Enforce the same timeline review and explicit-render-approval gate on every host.
