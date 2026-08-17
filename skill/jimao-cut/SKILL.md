---
name: jimao-cut
description: JiMaoCut (鸡毛飞剪) is the primary entry point for end-to-end self-media video editing from talking-head video, footage, transcript, script, PPT/PPTX, PDF deck, or presentation outline. Use when an agent should ask one consolidated creative intake, choose narration, re-author source material into a video story, select evidence-aware media, design shots, clean A-roll, and build captions, B-roll, motion, music, and SFX in one editable master review timeline. For fresh work, default timeline and render ownership to Remotion Studio, use remotion-semantic-effects-pro baseline pro-approved-2026-08-03-all-16-v3, and keep ChatCut, HyperFrames, video-shotcraft, presentation parsers, generators, and local tools as analysis, asset, shot-design, or approved intermediate providers. Compatible with Agent-Skills hosts including Codex and WorkBuddy. Also use for revisions. Stop at review unless the user explicitly approves final rendering or export.
---

# 鸡毛飞剪 JiMaoCut

Produce a coherent, editable creator-video timeline from source material with minimal user intervention. Treat the shared semantic edit plan as the source of truth; let specialized tools own only the work they are best at. Keep the workflow host-neutral so the same skill can run in Codex, WorkBuddy, CodeBuddy, or another Agent-Skills-compatible host with capability fallbacks.

## Non-negotiable contract

- Build or update an editable timeline first. Give the user a playable review entry and accept timecode feedback.
- Never render, export, download, publish, or share the final video before explicit final approval. A request to “auto edit” is not render approval.
- Inspect the project `AGENTS.md` and `MEMORY.md` before rendering. Project rules override generic codec guidance.
- Preserve source media and unrelated user changes. Never overwrite originals.
- Keep one `timelineOwner` and one `renderOwner`. Other engines provide assets, overlays, or shot specifications.
- For fresh creator-video work, set both owners to `remotion`. Remotion Studio is the only full-piece review surface and Remotion is the default final renderer.
- When Remotion creates semantic motion, use `remotion-semantic-effects-pro` with `baselineVersion=pro-approved-2026-08-03-all-16-v3`.
- Do not create competing full-piece timelines. HyperFrames may own an isolated segment preview; ChatCut may analyze media or provide an explicit cut decision list. Neither becomes the master owner without an explicit user choice or existing-project continuity.
- Make reversible creative decisions autonomously. Ask only for missing high-impact choices, paid generation, credentials, publication, or destructive action.
- Never claim a tool was used unless it is callable and the result was verified.
- Treat a PPT or slide deck as structured source material, not as a sequence that must be played slide by slide. Re-author it into video beats while preserving factual meaning and source provenance.
- When no recorded voice exists, let the user choose the narration source in the consolidated intake. Never clone or imitate a voice without explicit authorization.

## Start every run

1. Read project instructions and locate current media, script, prior review project, and design references.
2. Run `node scripts/inventory_capabilities.mjs` from this skill directory. Merge that result with the live skill/plugin/tool list; the live list is authoritative for MCP, app, or host tools.
3. Read [references/personal-editing-profile.md](references/personal-editing-profile.md) and apply confirmed defaults before asking questions.
4. Read [references/intake-gate.md](references/intake-gate.md). For a fresh build, present one consolidated structured choice card before creative design; skip answered fields and skip the gate for a specific revision.
5. Read [references/capability-router.md](references/capability-router.md) and select one timeline owner.
6. If an existing project already owns the timeline, continue it unless the user asks to migrate or consolidate it into Remotion.
7. Record unavailable capabilities and choose the documented fallback. Do not install a plugin unless the user asked to use that specific unavailable plugin.
8. Read [references/host-compatibility.md](references/host-compatibility.md) when the host is not Codex or when packaging this skill for another host.

## Establish the brief

Infer what is clear from the media and request. Classify `sourceMode` as `talking-head`, `footage`, `script`, `deck`, or `mixed`, then capture only what changes the outcome:

- purpose, audience, platform, aspect ratio, target duration, language;
- source assets and must-keep statements;
- desired tone, visual references, brand constraints, CTA;
- privacy, licensing, publication, and paid-generation boundaries.
- narration source and voice authorization when the source has no usable spoken audio;
- for a deck, content fidelity versus creative reinterpretation and any slides or claims that must remain verbatim.

If duration or platform is absent, inspect the source and choose a reversible review default. State the assumption in the review notes.

Do not spread intake across repeated conversational questions. Ask only outcome-changing choices in the single intake gate, recommend the profile-backed option first, and include an “I will describe another style” choice when collecting visual direction.

## Inspect and normalize sources

- Probe every media file for duration, dimensions, frame rate, codec, audio streams, rotation, and corruption.
- Detect burned-in captions, black frames, duplicate clips, clipping, low audio, and mismatched sample rates.
- Transcribe speech with word timing when possible. Mark uncertain words, names, products, numbers, and language switches.
- Keep source time, timeline time, and playback-rate transformations distinct.
- Create an `asset-ledger.json` entry for every source, capture, stock item, generated asset, font, song, and SFX.
- For PPT/PPTX/PDF decks, read [references/ppt-to-video.md](references/ppt-to-video.md), extract slide text, notes, images, charts, diagrams, and reading order, then create `deck-analysis.json` before visual design.
- For scripts or outlines without usable A-roll, read [references/script-first-video.md](references/script-first-video.md) and lock narration before final scene timing.

## Create the semantic edit plan

Read [references/semantic-ir.md](references/semantic-ir.md). Create `edit-plan.json` before building effects. Validate it with:

```bash
node scripts/validate_edit_plan.mjs path/to/edit-plan.json
```

For every semantic beat, record the spoken text, purpose, logical relation, visual evidence, caption cue, shot mechanism, audio cue, protected regions, and review state.

Distinguish these layers:

- captions show what was said;
- information cards show what the segment means;
- B-roll or screen evidence shows what supports the claim;
- motion guides attention and may be omitted when evidence already explains the point.

## Route work by ownership

Read [references/engine-playbooks.md](references/engine-playbooks.md) for the chosen engines.

- Prefer Remotion as the master timeline and render owner for new talking-head, tutorial, AI-tool, workflow, screen-demo, and creator explainer videos. Apply A-roll ranges, captions, B-roll, audio, and graphics in the Remotion project from one shared manifest.
- Use ChatCut by default for source inspection, transcription, semantic cut assistance, asset discovery, or a cut decision list. Let ChatCut own the timeline only when the user explicitly chooses a ChatCut-native edit or an existing ChatCut project should continue without migration.
- Use Remotion semantic-effects Pro/V3 for parameterized React motion and every semantic graphic that it can implement cleanly.
- For script-first, faceless, and deck-reinterpretation work, prefer HyperFrames for approved isolated scene groups when motion carries the explanation; keep narration, captions, assembly, and full-piece review in Remotion.
- Use video-shotcraft automatically when available and when a beat needs a recognizable shot mechanism, especially for real product UI, line drawing, skeleton reveal, diagram trace, marker emphasis, workflow, or evidence reveal. Do not ask the user to select this internal provider and do not make it the full timeline owner merely because a recipe card exists.
- Use a presentation parser for deck extraction and an available vector/diagram provider for editable line-art assets. These providers do not own timing or the master review.
- Use generators only after a beat has a visual purpose, shot constraints, duration, aspect ratio, continuity requirements, and an approved cost choice.

When Remotion owns the full piece, Review and Final must share the same data and media manifest. Read [references/remotion-master-timeline.md](references/remotion-master-timeline.md) before using HyperFrames or ChatCut as a provider.

## Build in dependency order

1. **Narrative and voice:** clean A-roll when it exists; otherwise lock the approved script and narration source. Remove confirmed false starts, duplicates, mistakes, and excessive pauses while preserving complete semantic units. Lock speech structure before visual timing.
2. **Captions:** create one canonical cue list from the cleaned timeline. Keep bilingual language, layout, and animation as separate settings.
3. **Evidence and B-roll:** follow [references/media-evidence-ladder.md](references/media-evidence-ladder.md). Prefer real user/product evidence over generated decoration.
4. **Motion graphics:** map each beat to one primary visual mechanism. Re-skin recipes with the project design tokens; do not inherit a template’s palette blindly.
5. **Audio:** keep voice as the anchor. Add music after timing is stable, duck it under speech, and place SFX only on meaningful visual events.
6. **Transitions and polish:** add only where they clarify a section, cover a necessary cut, or establish rhythm.

## Build the review timeline

- Open only the Remotion Review composition as the full-piece review entry for the default workflow.
- Keep editable tracks for source video, B-roll, graphics, captions, voice, music, and SFX where the engine supports them.
- Keep Remotion Review and Final synchronized from one manifest. Use named top-level sequences and editable layer controls when the applicable Remotion review workflow requires them.
- Treat an approved HyperFrames render as a replaceable intermediate asset with a stable path and ledger entry. Never represent it as a second master timeline.
- Preview the real timeline, not screenshots alone. Check cut points, lip sync, speech continuity, caption timing, audio transitions, compositing, and motion entry/exit.
- Provide the review URL/project entry, specs, duration, known assumptions, and a short list of critical timecodes.

## Verify before asking the user to review

Read [references/quality-gates.md](references/quality-gates.md) and [references/historical-lessons.md](references/historical-lessons.md).

For every important visual object inspect: pre-entry, mid-entry, fully visible, stable, pre-exit, and one frame after exit. Also play continuously at normal speed. Fail review if any layer obscures a face, mouth, gesture, caption, product control, evidence, or intended focal point.

Verify representative beginning, transition, dense-information, media-handoff, and ending frames. For ChatCut, use its project readback and preview/verification capabilities; for Remotion or HyperFrames, use their Studio or preview workflow. Do not treat successful compilation as visual verification.

## Handle revisions

- Parse feedback into timecoded changes and update `edit-plan.json` first.
- Recalculate downstream timing after any A-roll edit.
- Change the requested layer only; protect approved tracks and source media.
- Append a concise entry to `changes.jsonl` and re-run the relevant gates.
- Separate project-specific corrections from durable preferences. Promote a rule into [references/personal-editing-profile.md](references/personal-editing-profile.md) only after explicit user confirmation or repeated approval across projects; never infer a permanent preference from one correction.

## Render only after explicit approval

After the user explicitly confirms the final version:

1. Read project `AGENTS.md` and `MEMORY.md` again.
2. Report composition/project ID, resolution, frame rate, total frames or duration, codec, pixel format, color space, audio parameters, and intended output path.
3. Run an actual 5–10 second encode and mux test using the exact final parameters.
4. Show the preflight result and wait for confirmation if the project requires confirmation of the short test.
5. Start the full render/export only through the project’s approved command or engine export workflow.

On the current RTX 3060 workspace, prefer `hevc_nvenc`, then `libx265`; never try `h264_nvenc` first, and do not use H.264 NVENC above 4096 px width. Treat these as machine-specific rules and re-detect limits elsewhere.

## Deliverables

Maintain these portable artifacts when the engine permits:

- `VIDEO_BRIEF.md`
- `edit-plan.json`
- `asset-ledger.json`
- `review-manifest.json`
- `changes.jsonl`
- `deck-analysis.json` for PPT/PPTX/PDF-deck routes
- `narration-manifest.json` when narration is generated or recorded separately
- the editable engine project and review entry

The first delivery is the reviewed timeline plus verification notes, not a final media file.

## 作者与交流

- 作者 ID：鸡毛飞上天
- 个人微信：`jimaofeishangtianai`
- 添加时请备注“视频 Skill”或“鸡毛飞剪”，方便识别。
