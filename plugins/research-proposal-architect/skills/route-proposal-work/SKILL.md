---
name: route-proposal-work
description: Classify and route Chinese science and technology proposal work across overall research content, overall technical routes, branch research content, branch technical routes, and core technology or module tasks. Use when a request is ambiguous, spans writing and figures, omits the target section or operation, or needs palette and drawing-backend intake before invoking the other Research Proposal Architect skills.
---

# Route Proposal Work

Normalize every request into one decision-complete `proposal_task_spec` before drafting, drawing, or correcting artifacts.

## Read The Contract

Read [references/proposal-task-spec.md](references/proposal-task-spec.md) before routing. Run [scripts/validate_task_spec.py](scripts/validate_task_spec.py) when the specification is represented as JSON.

## Classify Two Axes

Determine:

- `target`: `overall_research`, `overall_route`, `branch_research`, `branch_route`, or `core_module`;
- `action`: `write`, `draw`, or `audit_correct`.

If either is missing, ask only for the missing decision. Present the five targets or three actions in Chinese exactly as defined in the contract. Do not infer a technical route merely because the user mentions a figure.

## Establish Source And Constraints

Record the source chapter, paragraphs, document, figure, or user-supplied text in `source_scope`. Record known word limits, page geometry, required terminology, metrics, proposal template, confidentiality constraints, and requested deliverables.

Inspect supplied files before asking for discoverable facts. Ask only when a missing choice materially changes the output.

## Apply The Palette Gate

For `write`, set `palette_mode: not_applicable` and do not ask about color.

For drawing or figure correction:

1. Detect whether the user already supplied colors, a style guide, or a reference image.
2. If no palette was supplied, ask whether to use the default palette, pause for a custom palette, or use a reference image.
3. Set `palette_mode` to `custom`, `default`, `reference`, or `pending`.
4. Do not begin figure design while `palette_mode` is `pending`.

When `palette_mode` is `custom` or `reference`, preserve the source in `constraints.palette` or `constraints.palette_reference`.

## Apply The Backend Gate

For new or corrected editable figures, require `backend: powerpoint`, `wps`, or `drawio`. Ask when missing; do not choose silently. A source PPTX, WPS deck, or draw.io file may determine the backend without asking.

Verify that Scientific Illustrator is installed before promising editable construction. If unavailable, report the prerequisite and stop before drawing.

## Summarize And Route

State a compact task summary containing target, action, source scope, deliverables, palette, backend, and material constraints. Then route:

- writing to `$write-research-sections`;
- drawing to `$design-proposal-figures`;
- review/correction to `$audit-proposal-alignment`;
- extraction of a new reusable house style to `$distill-proposal-patterns`.

When a request combines writing and drawing, finish the text/content map first, then design the figure, then run alignment review. Do not ask again for values already present in the task specification.
