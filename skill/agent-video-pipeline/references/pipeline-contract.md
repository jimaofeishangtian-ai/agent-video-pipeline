# Pipeline contract

## State machine

Allowed gate states: `pending`, `in_progress`, `needs_user`, `approved`, `complete`, `failed`, `blocked`, `skipped`, `stale`.

| Gate | Required input | Canonical output | Approval |
|---|---|---|---|
| G0 preflight | brief, workspace, source media | manifest, capability report, glossary, provenance ledger, optional shared proxy | install/auth/cost boundary |
| G1 ChatCut lock | source/proxy, glossary, content invariants | ChatCut Script/timeline, `timeline-manifest.json`, `edit-lock.json` | spoken content and rhythm |
| G2 HyperFrames | locked semantic beats and timing | `BRIEF.md`, `frame.md`, `STORYBOARD.md`, `creative-contract.json`, prototype URL | visual direction |
| G3 Seedance | shot plan, visual anchors, chosen option | approved asset IDs and ledger entries, or explicit free fallback | option and per-job cost |
| G4 Remotion | canonical timing, creative contract, approved assets | Review/Final, `motion-manifest.json`, Studio URL | motion/timing/placement |
| G5 intermediate | approved Final composition | named overlay/full-frame assets | explicit intermediate render |
| G6 ChatCut conform | all approved assets | editable final timeline and captions | timeline playback |
| G7 delivery | approved timeline | final export and `qc-report.md` | explicit final export |

## Canonical artifacts

### `timeline-manifest.json`

Include source/proxy identity, width/height/fps, clean duration in frames, ordered semantic beats, caption word/phrase timings, and source-to-clean frame segments. Every downstream timing reads this file. Use integers and state the seconds-to-frame rounding rule.

### `edit-lock.json`

Include ChatCut project/timeline IDs, transcript version, protected sentences, approved spoken sequence, pause policy, clean duration, protected regions by beat, and a content hash. Changing spoken order, selected takes, or pauses marks G2–G7 `stale`.

### `creative-contract.json`

Include canvas/fps, palette/type/spacing/radius/material tokens, caption-safe and subject-protected regions, depth recipe, density policy, motion verbs/easing, transition policy, asset provenance, and stable layer IDs.

### `shot-plan.json`

Each shot includes stable ID, viewer job, linked beat/frame range, source type, eight-part photographic prompt, references, generation mode, expected duration, audio policy, option, status, fallback, and approved asset ID.

### `generation-ledger.json`

Each module records `planned`, `running`, `generated`, `simulated`, `skipped`, `blocked`, or `failed`; execution path; provider/model; job/asset IDs; requested/actual duration; credit estimate/actual cost; verification evidence; and timestamp. A visual imitation is `simulated`, not `generated`.

### `motion-manifest.json`

Each motion item includes stable ID, role, content/source, frame range, z/track role, safe rectangle, props, reviewed position, entrance/hold/exit, and alpha/opaque intent.

## Invalidation rules

- Source/proxy identity change: invalidate G1–G7.
- Spoken content or pause timing change: invalidate G2–G7.
- Visual token change: invalidate G3–G7, not G1.
- Rejected Seedance shot: invalidate only that shot and dependent placements.
- Remotion timing/position change: sync Final and invalidate G5–G7.
- Caption spelling correction without audio change: invalidate caption verification and G7 only.

Use stable IDs across files. Verify artifacts and timelines after tool calls; tool success alone never completes a gate.
