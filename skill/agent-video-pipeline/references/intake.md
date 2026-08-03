# Intake and adaptive questions

Ask only questions whose answers change the build. Prefer one round of up to three questions, then continue. Never ask the user for facts already discoverable from source files, project state, or transcript.

## Minimum brief

Resolve these fields:

1. `goal`: what should the viewer think, feel, or do?
2. `audience_platform`: audience, platform, aspect ratio, expected duration.
3. `source_strategy`: real-person A-roll, voiceover, generated shots, existing B-roll, or a mixture.
4. `content_lock`: supplied script, source transcript, outline, or agent-proposed structure.
5. `visual_direction`: brand assets/reference, named direction, or permission to propose three directions.
6. `editing_intensity`: conservative, standard, or aggressive speech cleanup.
7. `generation_budget`: ChatCut-managed Seedance, direct Ark Seedance, no-Seedance fallback, or a separately authorized ceiling.
8. `deliverable`: editable timelines only, final video after approval, or both.

## Adaptive follow-ups

- If real-person footage exists, ask only for target length, transcript invariants, product-name glossary, and cleanup intensity when those are unclear.
- If “cinematic” or a similar adjective is the only visual input, ask which emotional reading matters most: restrained/premium, intimate/documentary, tense/dramatic, energetic/commercial, or another named reference.
- If multiple recurring characters/products appear, identify the exact approved anchor asset for each before Seedance.
- If B-roll mode is unclear, ask whether it should replace A-roll full-screen or appear as PiP.
- If user wants automatic execution, still pause at authentication, Seedance execution-channel/model/resolution choice and paid generation, intermediate render, and final export gates.

## Defaults that are safe to infer

- Use 9:16 and 30 fps for Douyin when not contradicted by existing project state.
- Use conservative semantic cleanup: preserve meaning, compress long pauses rather than deleting all silence, keep natural sentence gaps.
- Keep captions within a protected lower band and keep face/mouth/hands/product areas protected.
- Use one coherent visual language across graphics; use distinct graphic forms for distinct viewer jobs.
- When the source codec is not browser-safe, preserve it and create one shared H.264/AAC proxy used by every review stage.

Write confirmed answers to `project-manifest.yaml` and record assumptions separately. Never disguise an assumption as a user decision.
