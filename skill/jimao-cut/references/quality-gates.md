# Quality gates

Pass each applicable gate before asking the user to review.

## Source and A-roll

- All source files resolve and were probed.
- The edit preserves complete meaning, must-keep lines, names, numbers, and causal links.
- No duplicate take, accidental gap, lip-sync jump, black/flash frame, or clipped word at cut points.
- Playback-rate changes are reflected in source-to-timeline mapping.

## Captions

- One canonical cue list follows the cleaned A-roll.
- Text matches speech and intended language; uncertain names/numbers are flagged.
- Lines remain readable at target size and do not cover face, mouth, hands, UI, evidence, or burned-in captions.
- Bilingual hierarchy is consistent; English is secondary when Chinese is primary.
- Dynamic word focus is used only when word timing supports it.

## Visuals

- Each beat has at most one primary motion.
- Information cards add meaning rather than duplicate captions.
- Real evidence is legible at actual review size.
- No template color or style conflicts with semantic role or project design tokens.
- No motion loops, ghosts, stale components, or visual from a prior baseline.

For every important object inspect six states:

1. one frame before entry;
2. entry midpoint;
3. first fully visible frame;
4. stable hold;
5. last frame before exit;
6. one frame after exit.

Then play the whole transition at normal speed.

## Audio

- Voice remains intelligible and continuous.
- Music enters after timing is stable, has no distracting lyrics by default, and ducks under speech.
- SFX aligns to visible events and does not mask consonants or peaks.
- No clipping, abrupt cut, unintended silence, duplicated audio, or sample-rate drift.

## Timeline and ownership

- Exactly one timeline owner and render owner are recorded.
- Review and Final share the same duration, media, semantic data, and approved changes.
- All layers remain editable where the selected engine supports editing.
- The user receives a real review entry and critical timecodes.
- The default creator workflow exposes one full-piece Remotion Review URL. Any HyperFrames URL is labeled and scoped to one isolated segment.
- Every provider intermediate matches the Remotion master dimensions, fps, exact frame duration, alpha/background contract, and color intent.
- Replacing a provider asset at its stable path preserves master timing and is rechecked in Remotion Studio.

## Render gate

- Explicit final approval exists.
- Project instructions and memory were reread.
- Final specs and output path were reported.
- An actual 5–10 second test used the exact resolution, fps, codec, pixel format, color space, and audio parameters.
- The project-required confirmation of that test exists before full render.
