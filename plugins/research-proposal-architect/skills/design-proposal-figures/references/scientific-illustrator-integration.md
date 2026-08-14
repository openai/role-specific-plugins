# Scientific Illustrator Integration

Scientific Illustrator is a separate prerequisite and remains the authority for editable figure construction.

## Handoff Contract

Pass a complete `figure_semantic_spec` to `$design-scientific-figure`. Include:

- message, audience, reading order, aspect ratio, and output size;
- exact text and immutable facts;
- regions, object ids, roles, hierarchy, and construction order;
- source and target for every relationship;
- connector type, direction, label, and feedback semantics;
- palette tokens and role mapping;
- claim ids and acceptance conditions;
- ambiguities that must not be guessed.

## Backend Mapping

- PowerPoint or WPS: use `$edit-powerpoint-live`.
- draw.io: use `$recreate-scientific-figure-in-drawio`.

Honor capability detection performed by Scientific Illustrator. Do not promise native charts, live application control, or connector behavior beyond the selected adapter's reported capabilities.

## Review Loop

For each logical region:

1. construct named editable objects;
2. collect fresh structure evidence and renderer output;
3. invoke `$audit-scientific-figure`;
4. send findings to `$correct-scientific-figure`;
5. apply minimal object-level corrections;
6. rerender and review again.

Repeat after assembling the whole figure.

## Combined Pass Gate

The proposal-domain audit requires:

- semantic and text accuracy: 1.00;
- terminology and metrics: 1.00;
- required claim coverage: at least 0.95;
- no invented semantic objects;
- no wrong connector direction.

Scientific Illustrator additionally requires editable reconstructable content, clipping/overlap safety at 1.00, and geometry and connector clarity at least 0.95.
