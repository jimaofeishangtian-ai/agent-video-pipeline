# Engine playbooks

Read only the sections for engines selected by the capability router. Always follow the installed engine skill if it is stricter or newer.

## ChatCut: analysis provider by default

1. Inspect project assets or source media and transcribe A-roll when ChatCut is available.
2. Produce canonical source ranges, transcript corrections, pause decisions, and asset candidates for the shared edit plan. Do not create a second user-facing timeline when Remotion is master.
3. Use mechanical cleanup only for unambiguous fillers and long silence. Preserve context-dependent fillers and intentional pauses.
4. Apply edits inside ChatCut only when the user explicitly selected ChatCut as owner or asked to continue an existing ChatCut project.
5. When ChatCut is owner, follow its talking-head, transcription, verification, and export skills and keep one canonical timeline.

## Remotion semantic-effects Pro/V3

1. Read the installed `remotion-semantic-effects-pro` and `remotion-review-workflow` skills.
2. Record `ruleSource=remotion-semantic-effects-pro` and `baselineVersion=pro-approved-2026-08-03-all-16-v3`.
3. Create dedicated named Review and Final compositions backed by the same data and asset manifest. Use Remotion for source ranges, captions, B-roll, screen recordings, voice, music, SFX, native graphics, and approved provider assets.
4. Use semantic relation and role to choose visuals and colors. Do not use list position as semantic color.
5. Prefer the approved V3 style library; re-skin through design tokens. Suitable patterns include hooks, comparison, workflow rails, process nodes, tool handoffs, production matrices, evidence, review timelines, result dashboards, package stacks, and CTA attention.
6. Keep top-level sequences explicit and editable where the current review contract requires it. Review controls must not alter Final timing.
7. Check face, eyes, mouth, gesture path, real UI, evidence, and caption zones before placing a card.
8. Use Studio for full-piece playback, dragging, scrubbing, and frame checks. Compilation is not review.
9. Target the confirmed delivery resolution and fps in the manifest; 4K/60 is a render choice, not permission to render.
10. Never run `remotion render`, `remotion still`, or an equivalent final script before approval and project preflight.

## HyperFrames

1. Read the installed `hyperframes` entry skill and `references/remotion-master-timeline.md`.
2. Use HyperFrames only when its HTML, 3D, complex chart, webpage, UI, or motion-design capability materially improves an isolated segment over Remotion V3.
3. Match the Remotion master contract exactly: aspect, pixel dimensions, fps, duration in frames, background/alpha, color intent, and audio ownership.
4. Review the isolated segment in HyperFrames Preview. This is a segment approval surface, not a second full-piece review timeline.
5. After explicit segment approval, render a stable intermediate: transparent WebM/MOV for an overlay, opaque MP4 for a full-frame insert, or PNG sequence when lossless RGBA interchange is required. An intermediate render does not authorize the final master render.
6. Import the result into Remotion at a stable path and preserve the HyperFrames source project. Changes return to HyperFrames, reuse the same contract, replace the asset, and refresh Remotion.
7. Do not embed a live HyperFrames HTML page directly in Remotion by default; separate clocks, loading, browser state, fonts, and media readiness make final-frame parity fragile.
8. For faceless scripts and deck reinterpretations, design coherent scene groups rather than a full duplicate program timeline. Keep narration timing authoritative in the shared edit plan and use stable frame contracts for every handoff.

## video-shotcraft

1. Read the installed `video-shotcraft` skill and its current catalog. Use exact local recipe sources instead of recalling card implementations from memory.
2. Treat recipe cards as motion vocabulary, not whole-video templates.
3. Use real screenshots or recordings for real product UI. Derive the visual skin from the product or creator brand.
4. Use one main motion per shot and allow information to hold.
5. For talking-head work, use crafted shots selectively around key proof or transitions, then return to the face or real screen.
6. Map semantic functions to mechanisms: hook punch, list assembly, process trace, before/after comparison, cursor tour, code typing, AI response stream, scan/highlight, metric change, or result reveal.
7. For line-art routes, prioritize exact local cards for SVG trace, sketch/skeleton reveal, marker emphasis, diagram assembly, and camera moves. Record the card path or identifier in the beat instead of merely naming a visual style.

## Presentation and vector providers

1. Use an available PPT/PPTX/PDF parser to extract content and assets; do not let its slide-layout assumptions dictate the video.
2. Preserve slide number, speaker-note provenance, chart labels, units, citations, and links in `deck-analysis.json`.
3. Use editable SVG or vector output for line-art whenever practical. Rasterize only at the provider boundary when the master engine requires it.
4. Use OpenPencil, Manim, or a similar provider only when installed and callable. Treat it as an asset or isolated-segment provider, never as an automatic second full-piece review timeline.
5. When a provider is missing, use native SVG paths and Remotion/HyperFrames motion instead of installing a new skill automatically.

## Image and video generation

1. Use stock or real capture first when it can prove the claim.
2. Build a shot brief with subject, action, environment, composition, lens/camera motion, lighting, continuity, negative constraints, duration, aspect ratio, and intended timeline beat.
3. Explain any paid/credit-bearing choice before execution and obtain the needed authorization.
4. Generate the minimum test asset first. Inspect it before requesting additional variants.
5. Log provenance and never label generated UI or data as real evidence.

## Local media tools

Use `ffprobe` for inspection. Use ffmpeg for reversible proxies, audio analysis, thumbnails, or explicitly approved preflight encodes. Do not use ffmpeg to silently flatten the editable review project or bypass the engine’s review/export gate.
