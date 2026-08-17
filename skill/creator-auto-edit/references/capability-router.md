# Capability router

Choose one base timeline owner after capability discovery. For fresh creator-video work, default to Remotion. Prefer continuity when the user asks to continue an existing project; otherwise avoid multiplying full-piece review surfaces.

## Routing table

| Input and required work | Timeline owner | Supporting capabilities | Fallback |
|---|---|---|---|
| Fresh talking-head, tutorial, AI-tool, workflow, screen-demo, or creator explainer | Remotion | Pro/V3, Review/Final, ChatCut analysis, HyperFrames segments, media providers | Remotion with reduced provider set |
| Existing talking-head; cut mistakes, pauses, captions, B-roll, mix | Remotion | ChatCut transcript/cut decisions, captions, B-roll, audio | Continue an explicitly chosen ChatCut project |
| Existing talking-head should stay uncut; designed overlays only | Remotion | semantic-effects Pro/V3; HyperFrames isolated overlays | Remotion-native simplified graphics |
| Script-first explainer or faceless creator video | Remotion | HyperFrames scene/segment provider, media-use, generation | HyperFrames owner only for a pure HyperFrames deliverable |
| PPT, PPTX, PDF deck, or presentation outline re-authored as video | Remotion | presentation parser, video-shotcraft, HyperFrames scene groups, vector/diagram provider, Pro/V3 | Parse text/media locally, rebuild with Remotion-native line-art and semantic graphics |
| Premium parameterized information design or V3 templates | Remotion | semantic-effects Pro/V3 baseline `pro-approved-2026-08-03-all-16-v3` | HyperFrames approved intermediate segment |
| Product demo using real interface evidence | Current timeline owner | video-shotcraft recipes, browser/capture, real screenshots | Simple zoom/highlight on real recording |
| Music-driven montage inside a creator video | Remotion | beat analysis, media-use, optional HyperFrames segment | HyperFrames owner only when explicitly requested as a pure music piece |
| Fast conventional assembly with stock and captions | Remotion | ChatCut asset/transcript assistance, stock, captions, music | Explicit ChatCut-native edit |
| Explicit continuation of an existing Remotion, ChatCut, or HyperFrames project | Existing owner | Other engines remain providers | Migrate only on explicit request |

## Automatic provider rules

- Do not ask the user to choose an engine or provider when the outcome is unchanged.
- If `video-shotcraft` is installed and a beat matches an exact recipe family, use it to specify the shot; otherwise write the shot mechanism directly.
- For script/deck beats where abstract motion is the evidence, prefer HyperFrames for a small coherent scene group only when it is visibly stronger than Remotion V3. Keep Remotion as owner.
- For mathematical, geometric, or diagram-heavy beats, use an available vector/diagram animation provider only as an approved intermediate. Fall back to SVG path animation in HyperFrames or Remotion.
- Group adjacent provider beats into the fewest coherent intermediates that remain easy to revise. Avoid one provider render per sentence.

## Tool discovery

1. Read the current callable tool list and available skills.
2. Run `inventory_capabilities.mjs` for filesystem and executable discovery.
3. Treat callable tools as stronger evidence than installed files.
4. Mark each desired capability `available`, `degraded`, or `unavailable`.
5. Continue with a degraded path if it preserves the requested outcome.

## Ownership matrix

Record:

- `timelineOwner`: engine that owns clip positions and final duration;
- `renderOwner`: engine that encodes or exports the final timeline;
- `overlayProviders`: engines that deliver alpha or isolated graphics;
- `analysisProviders`: engines that inspect, transcribe, or propose cuts without owning the master timeline;
- `intermediateAssets`: approved rendered segments with source project, version, fps, dimensions, duration, alpha, and stable replacement path;
- `assetProviders`: stock, capture, generation, music, and SFX sources;
- `sourceOfTruth`: normally `edit-plan.json` plus the owner timeline.

Never let two engines independently cut the same A-roll or maintain different caption timing. When Remotion owns the timeline, apply the canonical source ranges and caption cues in Remotion. If a handoff is necessary, render only the approved intermediate segment, preserve its editable source project, and update the asset ledger.

## Installation boundary

Do not auto-install a missing plugin. If the user explicitly asked for that specific plugin and it is unavailable, exhaust tool discovery, then use the host’s plugin-install suggestion mechanism when available. Otherwise explain the fallback in the review notes.
