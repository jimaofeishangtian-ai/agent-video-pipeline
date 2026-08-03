---
name: agent-video-pipeline
description: Build, resume, and quality-control a cross-agent, editable video pipeline using ChatCut for source ingestion, transcript and A-roll locking plus final assembly; HyperFrames for creative direction and layered visual prototyping; Seedance for explicitly approved cinematic B-roll; and Remotion for parameterized graphics and reviewable animation. Use for talking-head promos, automatic editing workflows, capability-aware setup across Codex, Claude Code, Trae, WorkBuddy, OpenClaw, or another shell-capable agent, and any project that must prove which modules actually ran before rendering or export.
---

# Agent Video Pipeline

Build an editable, resumable project—not a flattened one-off video. ChatCut and Remotion timelines are review surfaces. Never render, export, download, or share a final video until the user explicitly approves that gate.

## Start or resume

1. Search the target workspace for `pipeline-state.json`.
2. If it exists, run `scripts/validate_project.py <project-dir> --json`, re-read external project state, and resume at the first incomplete or stale gate.
3. If it does not exist, run `scripts/diagnose_env.py --project <project-dir> --json`, read `references/agent-adapters.md` and `references/intake.md`, ask only unresolved load-bearing questions, then run `scripts/init_workspace.py <project-dir>`.
4. Read `references/environment-bootstrap.md` only for missing dependencies. Prefer project-local packages and official sources. Never fabricate a connector, login, entitlement, asset ID, job ID, or tool result.

## Choose the run shape

- `talking-head-roundtrip`: ChatCut pre-pass → HyperFrames → Seedance decision → Remotion → ChatCut final assembly. This is the default when speech is the spine.
- `visual-first`: HyperFrames → optional Seedance → Remotion; use ChatCut only if final editable assembly/captions are needed.
- `graphics-only`: HyperFrames → Remotion. Mark ChatCut and Seedance `skipped` with reasons.

Do not force all four modules. Do not say “four modules completed” unless the provenance ledger proves all four actually ran.

## Execute talking-head gates

1. **G0 — Preflight and capability contract.** Inspect media, agent capabilities, accounts, cost boundaries, disk, dependencies, glossary, ratio, and protected content. Create the project state and one shared browser-safe proxy if needed.
2. **G1 — ChatCut ingest and A-roll lock.** Import/target the real source, transcribe, correct glossary terms, produce a pause/cut dry run, preserve protected sentences, apply the approved semantic edit, and write `timeline-manifest.json` plus `edit-lock.json`. Read `references/chatcut-stage.md`.
3. **G2 — HyperFrames direction.** Use the locked transcript beats and timing to select a visual system, storyboard, safe zones, and layered seekable prototype. Read `references/hyperframes-stage.md`.
4. **G3 — Seedance channel, model, and shots.** Present ChatCut-managed Seedance, direct Volcengine Ark, and no-Seedance fallback before any paid call. For a high-quality ChatCut final, explicitly request `model: "seedance2"` and `resolution: "1080p"`; never let the 720p default or `seedance2mini` pass as a high-quality final. Generate one job at a time, read back its real params, review it, record cost/provenance, and mute generated audio under the A-roll. Read `references/seedance-stage.md`.
5. **G4 — Remotion parameterization.** Consume the canonical timeline, creative contract, and approved assets. Build separate Review/Final compositions with parameterized copy, color, layout, media, and rhythm. Read `references/remotion-stage.md`.
6. **G5 — Intermediate render approval.** Ask before rendering any Remotion overlay/full-frame asset for ChatCut. A test render approval authorizes only the named test file.
7. **G6 — ChatCut online conform and final assembly.** Refresh the real project, place approved B-roll/graphics, enable captions, check collisions and sync, and stop on the editable timeline for review.
8. **G7 — Final export approval and QC.** Export once only after an explicit “final approved / render / export” instruction, then verify the delivered file.

The answer to “ChatCut or HyperFrames first?” is: for recorded talking-head footage, ChatCut first for factual timing, HyperFrames second for visual direction, then return to ChatCut at the end. HyperFrames first is correct only when no speech timeline exists or the user is still developing the concept before filming.

## Preserve one source of truth

Read `references/pipeline-contract.md` before authoring artifacts.

- `timeline-manifest.json` owns fps, clean duration, semantic beats, and source-to-clean frame mapping.
- `edit-lock.json` owns approved spoken content and a content hash.
- `creative-contract.json` owns design tokens, protected zones, visual layers, and motion language.
- `shot-plan.json` owns planned photographic shots and approved Seedance asset IDs.
- `generation-ledger.json` proves `generated`, `simulated`, `skipped`, or `failed` status with provider/model/job/asset/cost evidence.
- `motion-manifest.json` owns Remotion layers and exact frame placement.

Create at most one shared H.264/AAC proxy for browser review. Keep the original untouched. Downstream tools consume the same proxy and timeline manifest; never reconstruct pause trims by hand in multiple tools.

## Enforce decision and review gates

- Before G1 editing, distinguish semantic invariants from delivery cleanup. “Keep every sentence” still permits only the explicitly approved pause/filler policy.
- Before G3, show Seedance execution channels and current runtime model/cost/entitlement. Do not request a raw API key in chat. Submit one paid job, read back the actual model/resolution/references, wait, inspect, then continue.
- Before G4 approval, inspect hook, dense middle, every B-roll boundary, captions, and CTA at entrance/settled/exit frames.
- Before G6 approval, check face/mouth/hands/product/caption safe zones and generated-audio muting.
- Before G5 or G7 rendering, require explicit authorization. User approval and agent verification are separate facts.

## Apply cross-agent compatibility

Use capabilities, not brand assumptions. Read `references/agent-adapters.md`.

1. Emit a table with `AVAILABLE`, `INSTALLABLE`, `MISSING`, or `PAID/AUTH` for shell, filesystem, browser review, FFmpeg, Node, HyperFrames, Remotion, ChatCut, and Seedance.
2. Use native Skill/MCP tools when present. Otherwise use documented local CLI paths. If an online connector is missing, stop only that stage and preserve a handoff package; do not pretend to execute it.
3. Codex, Claude Code, Trae, WorkBuddy, and OpenClaw all consume the same canonical files. Product-specific memory/rule files are optional adapters, never the source of truth.
4. Record every external call and verification in `generation-ledger.json` and `pipeline-state.json`.

## Read references on demand

- Adaptive intake: `references/intake.md`
- Agent compatibility: `references/agent-adapters.md`
- Environment/bootstrap policy: `references/environment-bootstrap.md`
- Artifact schemas and invalidation: `references/pipeline-contract.md`
- ChatCut pre-pass and final assembly: `references/chatcut-stage.md`
- HyperFrames creative stage: `references/hyperframes-stage.md`
- Seedance choices and cinematic prompting: `references/seedance-stage.md`
- Remotion review and round-trip: `references/remotion-stage.md`
- Acceptance checks: `references/quality-gates.md`

After every gate, update state, provenance, review URL, approved timecodes, and next action, then run `scripts/validate_project.py <project-dir>`. Never overwrite user-authored files during initialization or migration.
