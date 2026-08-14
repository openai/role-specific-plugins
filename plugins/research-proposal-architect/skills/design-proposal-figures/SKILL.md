---
name: design-proposal-figures
description: Convert Chinese proposal research text into a backend-neutral semantic specification and an editable overall research, overall technical route, branch research, branch technical route, or core technology figure. Use when the user needs PowerPoint, WPS, or draw.io proposal diagrams whose hierarchy, terminology, palette, connectors, captions, and feedback paths correspond exactly to the prose.
---

# Design Proposal Figures

Design proposal-domain semantics, then delegate editable construction to Scientific Illustrator. Do not replace Scientific Illustrator or reproduce its drawing implementation.

## Confirm Readiness

Require a complete `proposal_task_spec`. If target, source, palette mode, or backend is missing, invoke `$route-proposal-work`.

Read:

- [references/figure-patterns.md](references/figure-patterns.md);
- [references/text-figure-contracts.md](references/text-figure-contracts.md);
- [references/scientific-illustrator-integration.md](references/scientific-illustrator-integration.md).

## Resolve Color Before Design

- `custom`: use the supplied tokens exactly unless contrast fails; report any necessary accessibility adjustment.
- `default`: load [assets/default-palette.json](assets/default-palette.json).
- `reference`: inspect the reference image, propose a semantic role mapping for six to eight colors, and obtain confirmation before drawing.
- `pending`: pause figure work and request the missing palette decision.

Do not use gradients, decorative black backgrounds, large red text fields, or color without a semantic role.

## Produce Figure Semantics

Create a `figure_semantic_spec` containing:

- `target`, one-sentence message, audience, reading order, aspect ratio, and output size;
- exact terms, facts, metrics, equations, and labels that must be preserved;
- regions, nodes, node roles, hierarchy levels, and concise editable copy;
- directed and bidirectional relationships, feedback loops, interfaces, and validation evidence;
- claim ids mapping every semantic object back to prose;
- palette roles, prohibited additions, source ambiguities, and acceptance conditions.

Limit the primary visual hierarchy to three levels. Move nonessential algorithm detail to prose or a branch figure instead of shrinking text.

## Select The Figure Grammar

Use exactly one primary grammar from `figure-patterns.md`:

- system decomposition for `overall_research`;
- staged system route with feedback and outcomes for `overall_route`;
- task decomposition with interfaces for `branch_research`;
- input-method-output-validation loop for `branch_route`;
- mechanism topology or conditional routing for `core_module`.

Do not substitute a technical route for a research-content map.

## Hand Off To Scientific Illustrator

1. Invoke `$design-scientific-figure` with the complete semantic specification.
2. Use `$edit-powerpoint-live` for PowerPoint/WPS or `$recreate-scientific-figure-in-drawio` for draw.io.
3. After each logical region, require `$audit-scientific-figure`.
4. Send every finding to `$correct-scientific-figure`, apply only the responsible object changes, rerender, and audit again.
5. Repeat the same loop for the whole figure.

Deliver the editable source, a high-resolution preview, and matched lead-in/caption text unless the user requested a narrower deliverable.
