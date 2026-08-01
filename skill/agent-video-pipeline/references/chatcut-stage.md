# ChatCut stage

ChatCut enters twice in a talking-head workflow: first to establish factual speech timing, and last to conform all approved assets into an editable timeline.

## First pass: ingest and lock A-roll

1. Establish the exact project/timeline and expose the editor URL early.
2. Inspect the asset library before asking for another upload. Probe the original. If browser playback requires normalization, create/import one shared H.264 `yuv420p` + AAC proxy and preserve the original.
3. Build a glossary before transcript correction: brands, products, people, acronyms, capitalization, and forbidden substitutions.
4. Transcribe and verify word timings. Correct the transcript source, not just rendered caption text.
5. Separate constraints:
   - **Semantic invariants:** sentences/takes/claims that cannot be removed or reordered.
   - **Delivery cleanup:** filler policy, long-pause threshold, retained sentence gap, failed-take rule.
6. Produce a dry-run edit report before structural application: exact protected sentence count, proposed removed/shortened ranges, before/after duration, and ambiguity list.
7. Use ChatCut Script for semantic editing: `read_script` → refresh/clean if needed → edit complete semantic units in `timeline.md` → `apply_script` → read back and verify. Use mechanical operations only for fixed fillers and pause rules.
8. Conservative default: compress obvious pauses above 0.8–1.0 s to about 0.3–0.5 s; preserve emphasis and topic changes. If “keep every sentence,” retain every approved sentence exactly.
9. Review speech, cuts, breathing, lip continuity, and protected content in the ChatCut timeline.
10. After approval, write `timeline-manifest.json` and `edit-lock.json`. Downstream stages must not reconstruct timing independently.

Do not use transcript search plus manual clip splitting to build the spoken version when Script editing is available.

## Final pass: online conform

1. Refresh external project/timeline state before writing.
2. Keep A-roll, captions, Seedance B-roll, Remotion graphics, music, and SFX on separate named tracks.
3. Place only approved assets from manifests. A Seedance clip's generated audio is always muted/removed when A-roll voice remains authoritative unless the user explicitly approves it.
4. Choose full-screen vs PiP by viewer job. Protect face, mouth, hands, product, brand marks, and the caption band.
5. Enable captions only after timing is locked. Use an actually available preset and correct spelling from the glossary.
6. Run a collision pass at hook, dense middle, each B-roll boundary, and CTA. Inspect entrance, settled, and exit frames.
7. Play the full editable timeline; verify cuts, pauses, lip-sync, captions, crop, transitions, motion timing, first/last frames, and audio balance.
8. Stop for timeline approval. Export only at G7 after explicit authorization.
