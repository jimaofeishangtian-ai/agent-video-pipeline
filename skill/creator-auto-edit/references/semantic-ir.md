# Semantic edit intermediate representation

`edit-plan.json` is the cross-engine source of truth. Use seconds for semantic timing and derive frames from the target fps at the engine boundary.

## Required top-level fields

```json
{
  "schemaVersion": "1.0",
  "project": {"id": "slug", "title": "", "status": "planning"},
  "ownership": {"timelineOwner": "remotion", "renderOwner": "remotion", "overlayProviders": ["hyperframes"], "analysisProviders": ["chatcut"], "intermediateAssets": []},
  "brief": {"sourceMode": "script", "purpose": "", "audience": "", "platform": "", "aspectRatio": "9:16", "fps": 60, "targetDurationSec": 60, "language": "zh-CN", "adaptationLevel": "reinterpret"},
  "narration": {"source": "tts", "voiceId": "", "authorization": "user-approved", "status": "planned"},
  "sources": [],
  "designTokens": {},
  "beats": [],
  "tracks": [],
  "review": {"status": "not_started", "criticalTimecodesSec": []},
  "render": {"authorized": false, "preflight": {"status": "not_run"}}
}
```

## Source object

Record `id`, `kind`, `pathOrUri`, `durationSec`, `dimensions`, `fps`, `hasAudio`, `provenance`, `license`, `sensitive`, and `notes`. Generated media must record model, prompt/version, cost choice, and creation time.

For a cross-engine intermediate, also record the provider project, source composition, provider version, approval state, stable output path, dimensions, fps, duration in frames, alpha mode, codec/container, color intent, and the Remotion Sequence or beat IDs that consume it.

For a deck source, also record slide/page number, element type, reading order, speaker notes, chart labels and units, source links/citations, extraction confidence, and whether the element is `verbatim`, `rephrased`, `visualized`, or `omitted` in the video.

## Narration object

When the source has no usable recorded speech, record `source` as `user-recording`, `authorized-recording`, `tts`, `authorized-clone`, or `silent-prototype`. Record provider/voice ID when applicable, consent or authorization state, generation cost boundary, audio path, duration, and review status. Narration timing becomes authoritative before provider segments are finalized.

## Beat object

Each beat requires:

- `id`, `startSec`, `endSec`, `sourceStartSec`, `sourceEndSec`;
- `spokenText`, `captionText`, `summary`;
- `purpose`: `hook`, `context`, `claim`, `step`, `comparison`, `evidence`, `transition`, `result`, `cta`, or `breath`;
- `relation`: `parallel`, `sequence`, `progress`, `compare`, `cause`, `evidence`, or `none`;
- `role`: `neutral`, `tech`, `success`, `growth`, `money`, `result`, `risk`, or `warning`;
- `visualType`: `face`, `real-screen`, `broll`, `topic`, `viewpoint`, `number`, `process`, `evidence`, `chart`, `tool-screen`, or `no-effect`;
- `evidence`: source ID, region, claim supported, and provenance strength;
- `shot`: framing, primary motion, recipe/card, in/out timing, and hold time;
- `caption`: cue IDs, layout zone, and confidence;
- `audio`: voice action, music intent, SFX event, and ducking;
- `protectedRegions`: face, mouth, gesture, UI, evidence, and caption rectangles;
- `review`: automatic checks, human status, and notes.

## Timing invariants

- `0 <= startSec < endSec` and beats do not overlap unless explicitly layered.
- Source timing remains separate from timeline timing.
- A-roll edits invalidate all downstream beat timing until recalculated.
- Captions, graphics, B-roll, and SFX reference beat IDs rather than duplicating prose matching.
- A visual can enter only after its spoken concept becomes inferable and must exit before the next competing focus.

## Information hierarchy

Use only one primary visual action per beat. A caption may coexist because it is a reading aid, but an information card must add meaning rather than repeat the caption. Set `visualType` to `no-effect` when the face or real screen is already the strongest evidence.
