---
name: distill-proposal-patterns
description: Extract reusable writing, hierarchy, visual grammar, and text-figure correspondence patterns from strong Chinese science and technology proposal examples. Use when adding a new reference proposal, comparing house styles, evolving Research Proposal Architect knowledge, or separating transferable methods from project-specific facts without bundling confidential source material.
---

# Distill Proposal Patterns

Learn from complete evidence chains while keeping source facts, transferable methods, and normative rules separate.

## Read The Protocol

Read:

- [references/distillation-protocol.md](references/distillation-protocol.md);
- [references/seed-observations.md](references/seed-observations.md) for the de-identified first corpus observations.

Use [scripts/extract_docx_evidence.py](scripts/extract_docx_evidence.py) for DOCX sources. Use the `documents` skill to render and inspect relevant pages and figures; use the `pdf` skill for PDF sources.

## Collect Complete Evidence

Read the full target chapter, not only the paragraph next to a figure. Capture:

- section hierarchy and word limits;
- overall goals, research content, technical route, task schemes, indicators, and adjacent cross-references;
- every relevant figure, caption, lead-in, and follow-on explanation;
- exact terminology, metrics, equations, and dependency directions;
- visible strengths and defects in layout or correspondence.

## Extract At Multiple Levels

For prose, identify paragraph functions, sentence functions, abstraction level, research verbs, transition logic, evidence boundaries, and closure patterns.

For figures, identify communication job, reading order, region grammar, object roles, connector topology, density, palette roles, and the relation between visible labels and prose claims.

Classify each observation as:

- `source_fact`: specific to the source project and never reusable as a rule;
- `transferable_pattern`: repeatedly useful structure or technique;
- `candidate_rule`: a proposed constraint requiring comparison or testing;
- `source_defect`: something not to reproduce.

## Produce A Safe Delta

Return:

- a de-identified observation set;
- proposed additions or changes to writing patterns, depth rules, figure patterns, contracts, or audit criteria;
- conflicts with existing rules;
- synthetic examples that test the proposed change.

Do not copy full paragraphs, original figures, organization names, unpublished metrics, or sensitive project details into the plugin. Do not modify the plugin knowledge base unless the user explicitly requests an update.
