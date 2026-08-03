# Seedance stage

Seedance owns actual generated photographic shots. It does not own transcript editing, captions, final assembly, or UI/motion-graphic simulations.

## Required channel gate

Inspect the current connector/SDK schema or official model list first. A marketing name is not proof that a model is callable. If the runtime does not expose Seedance 2.5, report it unavailable; never invent a model ID or silently substitute another model.

Show these choices before paid generation and query the current account/UI for entitlement and credits because prices can change:

- **A — ChatCut-managed Seedance high quality (recommended):** use the logged-in ChatCut connector and ChatCut credits. Do not request a Seedance API key. For the current ChatCut alias, submit one 4–5 second 9:16 shot with `model: "seedance2"` and `resolution: "1080p"`. Do not omit resolution, because the connector may default to 720p. Do not use `seedance2mini` as a final high-quality shot.
- **B — Direct Volcengine Ark Seedance high quality:** use this only when the user explicitly chooses direct API billing. Link the mainland China official Seedance page `https://www.volcengine.com/activity/seedance2` and Ark API-key console `https://console.volcengine.com/ark/region:ark+cn-beijing/apikey`. Require the user to configure `ARK_API_KEY` in the host secret store or local environment; never ask them to paste the secret into chat, a group message, screenshot, or tracked file. Resolve the exact official endpoint/model ID at runtime, test auth without echoing the key, check balance, then generate and import the result into ChatCut with source URL/hash and ChatCut asset ID.
- **C — No Seedance:** incur no Seedance charge and request no key. Choose HyperFrames for visual exploration/layered art direction, Remotion for exact copy/layout/timing/animation, or HyperFrames then Remotion when both are needed. Label the ledger `simulated` or `skipped` and state that Seedance was not called.

Display the verified execution channel, exact model ID, resolution, ratio, duration, reference mode, credit estimate, and subscription requirement before submission. Authorization covers only the first named job, not retries, variants, resolution upgrades, or additional shots.

## High-quality call contract

Create a call card and obtain approval before submission:

- `executionChannel`: `chatcut-managed` or `volcengine-ark-direct`
- provider and exact resolved model ID
- `resolution`, `ratio`, and `durationSeconds`
- input mode and concrete reference asset IDs
- target beat/viewer job and expected cost

After submission, read back the provider job parameters. A job may be marked `generated` only when the actual model, resolution, ratio, duration, references, job ID, and output asset ID match the approved call card. A successful provider response without a usable output asset is not an approved shot.

## Eight-part prompt contract

Every shot specifies:

1. Subject—appearance, material, defining features.
2. Action—one clear physical action.
3. Scene—place, time, weather, production details.
4. Lighting/color—key direction/softness, contrast, practicals, palette, grade.
5. Camera—shot size, angle, lens feel, movement, speed, stabilization.
6. Style—genre/reference without copying protected IP.
7. Quality—detail, physical consistency, usable handles.
8. Negative constraints—anatomy/object/text/crop/camera errors.

Translate “cinematic” into decisions. Example: motivated soft side key, cool fill, shallow depth with subject plane sharp, subject on right third and negative space left, 50 mm lens feel, slow push-in only, restrained grain, no plastic skin or conflicting camera motion.

## Execution and review

1. Use the G2 visual tokens and exact G1 beat frame range.
2. Confirm mode, references, 9:16 output, explicit resolution, duration, and one primary movement per sub-shot. Strict first/last-frame mode and reference mode are mutually exclusive unless the current tool explicitly documents otherwise.
3. For recurring products, characters, or scenes, establish an approved image/video anchor and pass it on every related shot. Confirm authorization and the provider's trusted-asset rules before using a real face.
4. Submit one job. Record channel/provider/model/resolution/ratio/duration/reference IDs/job ID/estimated credits immediately, then read the submitted params back from the job record.
5. Wait for completion, inspect actual pixel dimensions, identity/anatomy/object count/camera/light/composition/action/text artifacts/physical coherence/usable handles, and record actual asset ID/cost.
6. Mark an objectively weak result `rejected`; state the failed checks and ask whether to edit with the best output as a reference, retry with a stronger anchor, or use graphics. Do not accept it merely because generation completed.
7. Approved outputs enter `shot-plan.json`; rejected outputs never become anchors.
8. Generated audio is treated as a side effect. Mute it under authoritative A-roll unless explicitly needed and approved.
9. If identity/style text corrections fail twice, switch anchor/edit strategy instead of a third blind retry.

Most Seedance clips are shorter than a spoken segment. Never claim a single 5-second clip covers a 12-second section; combine it with A-roll, graphics, or an approved second clip.
