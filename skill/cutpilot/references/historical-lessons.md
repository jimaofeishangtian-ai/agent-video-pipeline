# Historical lessons

These rules come from the local creator-video history through 2026-08-15. Treat the counts as historical evidence, not universal benchmarks.

## Frequent failures observed

- Exit, disappearance, or hold timing errors: about 25 instances.
- Obstruction of face, main evidence, screen, or caption: about 12.
- Subtitle content, placement, or timing errors: about 11.
- Entry timing errors: about 9; at least 6 entered too early.
- Sizing or aspect-ratio problems: about 8.
- Source, audio, lip-sync, black, or flash issues: about 5.
- Review timeline not truly editable or not matching Final: about 5.
- Style/transparency and ghost/repeat/excess-effect problems: about 4 each.

## Root causes and preventive rules

| Root cause | Preventive rule |
|---|---|
| Visuals timed by rough keyword search | Time visuals from semantic beats and spoken inferability |
| Safe regions reused across shots | Recalculate protected regions per beat and actual crop |
| Review and Final maintained separately | Share one data/asset manifest and validate parity |
| Batch edits changed unrelated layers | Update the requested track and rerun dependency checks |
| Source or audio not locked before effects | Lock A-roll, then captions, then visuals, then music/SFX |
| Old and new baselines coexisted | Name the rule source/version and reject stale components |
| “More effects” treated as better | Permit `no-effect`; one primary motion per beat |
| Multiple engines exposed competing full timelines | Keep one master owner; treat other engines as analysis or approved segment providers |
| Provider HTML embedded without a shared frame contract | Review the segment in its native preview, render an approved deterministic intermediate, then replace it in the Remotion master |

## Proven distinctions

- Captions transcribe speech; information cards summarize meaning.
- The strongest creator-video system is content-sensitive orchestration, not a large fixed prompt.
- A tool is not a workflow owner merely because it can render video.
- The default creator workflow uses Remotion Studio as the single full-piece review timeline; provider previews are scoped to isolated segments.
- A reviewable timeline is the default deliverable; repeated full renders are not a review method.
- Real product screens are stronger than simulated UI when explaining real functionality.
