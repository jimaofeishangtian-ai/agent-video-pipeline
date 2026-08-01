# Remotion stage

Remotion owns parameterized copy, color, layout, media placement, and frame-accurate motion. It consumes the canonical ChatCut timing and HyperFrames design contract; it does not independently recreate pause edits.

## Required structure

- Separate `Review` and `Final` compositions.
- One central config grouped as `format`, `copy`, `theme`, `layout`, `motion`, `rhythm`, and `media`.
- Named top-level `<Sequence layout="none">` items with numeric literal `from` and `durationInFrames` for every user-adjustable layer.
- Stable `compositionId`/`layerId` for review positions.
- Separate source media, captions, motion, Seedance, and hidden SFX roles.

## Media and timing rules

1. Import frame ranges from `timeline-manifest.json`; never hand-copy a second set of timecodes.
2. Use the one shared proxy during review. For portable final rendering, resolve assets through the project's supported static asset path; do not hard-code a temporary localhost media URL.
3. If a scoped local HTTP server is required only for Studio review, record the URL in runtime state and replace it with portable asset resolution before Final.
4. Mute Seedance audio whenever A-roll voice remains the sound source.
5. Treat the caption band and per-beat subject rectangles as layout constraints, then run a collision check at representative frames.

## Review loop

1. Open `Review` in Studio and verify hot refresh, playback, scrubbing, and frame stepping.
2. Explain that timeline bars change timing while canvas dragging changes position.
3. Inspect hook, every dense graphic, Seedance in/out boundaries, caption changes, and CTA at entrance/settled/exit states.
4. Collect feedback by timecode and stable layer name.
5. Before any intermediate render, copy reviewed timing/position into `Final`, compare Review vs Final, list exact outputs, then request G5 approval.

## Round-trip

- Render approved typography/overlay assets with alpha only when the chosen codec/container and ChatCut import path support it.
- Render full-frame beats opaque at exact canvas/fps.
- Export `motion-manifest.json` with deterministic frame placement and handles.
- G5 approval is not G7 final-export approval.
