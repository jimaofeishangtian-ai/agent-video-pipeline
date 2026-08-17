# Remotion master timeline and provider bridge

Use this contract whenever Remotion owns the creator-video timeline.

## One user-facing master

- Keep `timelineOwner=remotion` and `renderOwner=remotion`.
- Put A-roll source ranges, screen recordings, captions, B-roll, evidence, music, SFX, native V3 motion, and provider intermediates in the same Remotion Review/Final manifest.
- Give the user one full-piece review URL: the Remotion Studio Review composition.
- A provider preview may be shown only for the isolated segment it owns. Label it as a segment approval step, not another full-video timeline.

## Prefer native Remotion first

Implement the graphic with Remotion Pro/V3 when it fits the approved semantic vocabulary. Use HyperFrames only when HTML layout, complex charts, webpage/UI animation, 3D/WebGL, or a specialized HyperFrames block materially improves the segment.

## HyperFrames bridge

1. Define the segment contract before authoring: beat IDs, start frame, exact duration in frames, width, height, fps, alpha/background, audio ownership, and color intent.
2. Author and verify the segment in HyperFrames Preview. Keep it seek-safe and deterministic.
3. Wait for explicit segment approval before rendering the intermediate.
4. Render only the segment:
   - transparent overlay: WebM or MOV with alpha;
   - opaque full-frame insert: MP4;
   - lossless interchange or alpha troubleshooting: PNG sequence.
5. Import it at a stable path recorded in `asset-ledger.json` and `edit-plan.json`. Remotion owns placement, trimming, final mix, full-piece review, and final rendering.
6. For a revision, change the HyperFrames source, review the segment, replace the same intermediate path, and verify the affected frames in Remotion Studio.

Do not directly embed a live HyperFrames HTML page into Remotion by default. The two frameworks do not automatically share one deterministic clock, asset-readiness state, font lifecycle, or browser state. A custom live bridge is allowed only when explicitly requested and must prove frame parity before adoption.

## Full HyperFrames pieces

For a pure motion-first or webpage-first video with no creator master timeline, HyperFrames may own the full piece when the user explicitly accepts its Studio as the review surface. Otherwise render the approved HyperFrames piece as an intermediate and place it in a Remotion wrapper, understanding that content revisions still return to HyperFrames.

## Render boundary

An approved HyperFrames intermediate render authorizes only that provider asset. It does not authorize the Remotion final render. After the complete Remotion Review is approved, run the final codec, 4K/60, color, audio, and hardware preflight separately.
