# Quality gates

## G0 preflight

- Capability table records AVAILABLE / INSTALLABLE / MISSING / PAID-AUTH.
- Original media is untouched; one shared proxy exists only if needed.
- Glossary, protected sentences, install plan, and Seedance cost boundary are explicit.

## G1 ChatCut A-roll lock

- Transcript product names match the glossary and word timing is usable.
- Dry-run report proves every protected sentence is retained.
- Cuts and compressed pauses sound natural; source-to-clean mapping is complete.
- User approved content/rhythm in the editable ChatCut timeline.

## G2 HyperFrames direction

- One direction is approved and expressed as machine-readable tokens.
- Every beat uses actual locked frames and has a viewer job/layer plan.
- Caption and speaker/product safe zones are reserved.
- Seekable prototype passes hook, middle, B-roll-boundary, and CTA checks.

## G3 Seedance

- User selected ChatCut-managed, Ark-direct, or no-Seedance after exact model/resolution/auth/cost disclosure.
- Every real job has execution channel, provider, resolved model, resolution, ratio, duration, reference IDs, job ID, output asset ID, and cost evidence read back from the provider record.
- A high-quality ChatCut final explicitly used `seedance2` and `1080p`; default 720p and `seedance2mini` fail this gate unless the user knowingly approved a draft/lower tier.
- Approved clips pass actual-pixel-size, camera/light/composition/anatomy/action/physical-coherence/text-artifact/handles review.
- No-Seedance fallback is labeled simulated/skipped; generated audio policy is recorded.

## G4 Remotion review

- Review/Final exist; timing comes from the canonical manifest.
- Copy, color, layout, rhythm, and media are parameterized.
- Adjustable layers are named; portable media resolution is ready for Final.
- Entrance/settled/exit frames pass safe-zone and collision checks.

## G5 intermediate render

- User explicitly authorized the named intermediate output.
- Review values are synchronized into Final; format matches alpha/opaque intent.

## G6 ChatCut final timeline

- A-roll, captions, B-roll, graphics, and audio are editable and organized.
- No gaps, overlaps, caption collisions, crop errors, or generated-audio conflicts.
- User reviewed the full editable timeline.

## G7 delivery

- User explicitly authorized final export.
- Output matches format/duration and passes first/last frame, A/V sync, caption, audio, and artifact QC.
- `qc-report.md` records evidence and accepted trade-offs.
