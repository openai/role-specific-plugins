---
name: audit-proposal-alignment
description: Audit and, when authorized, correct correspondence between Chinese proposal research prose and an overall research, overall technical route, branch research, branch technical route, or core technology figure. Use for missing claims, invented figure content, terminology drift, wrong arrow direction, metric mismatch, inappropriate hierarchy, palette inconsistency, or visual/editability defects.
---

# Audit Proposal Alignment

Review semantics before aesthetics. An attractive figure fails when it changes the proposal's meaning.

## Load The Audit Contract

Read:

- [references/alignment-rubric.md](references/alignment-rubric.md);
- [../design-proposal-figures/references/text-figure-contracts.md](../design-proposal-figures/references/text-figure-contracts.md).

Use [scripts/audit_alignment.py](scripts/audit_alignment.py) after creating a structured claim/object mapping.

## Build The Evidence Matrix

Extract atomic prose claims with stable ids. For each claim record:

- text and hierarchy level;
- required terms and exact metrics;
- input, method, output, validation, and feedback roles;
- required relationships and direction;
- whether omission is a hard failure.

Inventory each figure object and connector with stable ids, exact visible text, claim ids, direction, and semantic role. Keep decorative objects explicitly marked non-semantic.

## Run Semantic Review

Treat these as hard failures:

- missing a required task, mechanism, output, or validation claim;
- adding a technical claim absent from the prose;
- reversing dependency, control, feedback, or data-flow direction;
- changing a metric, threshold, unit, equation, or named standard;
- using one term for two concepts or two terms for one fixed concept;
- representing a research-content hierarchy as an implementation sequence, or the reverse.

Treat density imbalance, weak visual emphasis, unnecessary duplication, or a secondary omission as warnings when meaning remains intact.

## Run Visual And Editability Review

For PowerPoint/WPS or draw.io, invoke `$audit-scientific-figure` with fresh structure and renderer evidence. Apply its geometry, connector, text-fit, raster atomicity, editability, and clipping gates in addition to this skill's semantic gates.

## Correct Only When Authorized

For audit-only requests, return findings without mutation.

For correction requests:

1. fix factual text, terminology, metrics, and topology;
2. restore missing or remove invented semantic objects;
3. correct hierarchy and granularity;
4. correct palette-role violations;
5. send visual findings through `$correct-scientific-figure`;
6. rerender and rerun both semantic and visual audits.

Preserve approved objects and prose. Do not flatten the figure or rewrite unrelated sections.

Pass only with semantic accuracy 1.00, terminology and metrics 1.00, zero hard failures, claim coverage at least 0.95, and Scientific Illustrator geometry/connector scores at least 0.95.
