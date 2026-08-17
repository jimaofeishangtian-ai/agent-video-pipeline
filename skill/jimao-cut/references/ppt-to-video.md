# PPT and slide-deck to video route

Use this route for PPT, PPTX, PDF decks, exported slides, or presentation outlines.

## Core principle

Treat the deck as a structured evidence package, not a finished storyboard. Preserve factual meaning, numbers, units, citations, product evidence, and required wording while rebuilding pacing, hierarchy, and scene grammar for video.

## Extract before designing

Create `deck-analysis.json` with:

- deck metadata, page dimensions, theme colors, fonts, and language;
- per-slide title, body text, speaker notes, reading order, and semantic role;
- images, screenshots, charts, tables, diagrams, logos, citations, and links;
- chart labels, values, units, legend meaning, and extraction confidence;
- duplicate, low-value, contradictory, or context-dependent material;
- required-verbatim claims and material that needs user confirmation.

Use an available presentation/PPTX parser first. For PDF-only decks, use a PDF parser and page render inspection. Never rely on OCR alone when structured PPTX data is available.

## Re-author the story

1. Convert slides into claims and semantic beats.
2. Merge repeated setup slides and split overloaded slides.
3. Assign each beat one purpose: hook, context, claim, process, comparison, evidence, result, or CTA.
4. Select `reinterpret`, `balanced`, or `faithful` adaptation from the intake.
5. Draft narration and obtain the selected voice source before locking scene frames.
6. Maintain a mapping from every beat back to the source slide and element.

## Visual routing

- **Line-art blueprint:** SVG path drawing, diagram assembly, measured camera moves, restrained technical labels.
- **Playful marker/editorial sketch:** hand-drawn emphasis, skeleton reveal, marker underlines, paper-space transitions, selective imperfection.
- **Clean semantic motion:** Remotion V3 cards, comparisons, process rails, evidence frames, result dashboards, and controlled typography.
- **Real evidence:** retain screenshots, documents, charts, and product UI when they support the claim; redesign their framing rather than fabricating replacements.

Use exact installed video-shotcraft cards when available. Use HyperFrames for coherent motion-led scene groups. Use an installed vector or diagram animation provider only for isolated assets or segments. Keep Remotion as timeline and render owner.

## Timeline and review

Do not create one video clip per slide. Group adjacent beats into chapters and use the fewest provider intermediates that remain editable. Review provider segments independently only to approve the asset; import approved intermediates into Remotion and review the complete video in Remotion Studio.

Rendering a provider intermediate authorizes only that handoff asset. It never authorizes the final Remotion render.
