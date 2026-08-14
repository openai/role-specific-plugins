---
name: write-research-sections
description: Draft, rewrite, expand, or structurally repair Chinese science and technology proposal sections for overall research content, overall technical routes, branch research content, branch technical routes, and core technologies or modules. Use when proposal prose must have the correct abstraction level, research logic, technical depth, terminology, evidence boundaries, and handoff to a corresponding figure.
---

# Write Research Sections

Write proposal prose at the requested level without inventing technical facts, metrics, dependencies, or validation results.

## Load The Relevant Rules

Read:

- [references/writing-patterns.md](references/writing-patterns.md) for paragraph architecture, sentence functions, verbs, and style;
- [references/technical-depth-ladder.md](references/technical-depth-ladder.md) for the permitted detail level.

If the text will drive a figure, also read [../design-proposal-figures/references/text-figure-contracts.md](../design-proposal-figures/references/text-figure-contracts.md).

## Build A Content Map

Before drafting, identify:

- the governing problem or demand;
- the organizing research mainline;
- research objects and tasks;
- methods or mechanisms;
- resulting capabilities, models, systems, or datasets;
- interfaces to other tasks;
- validation, feedback, iteration, and expected outcomes.

Mark unsupported details as missing inputs. Do not convert plausible domain knowledge into asserted project commitments.

## Match The Requested Level

- `overall_research`: define what the project studies, how topics divide, how they depend on each other, and what integrated capability results. Keep algorithms and equations out.
- `overall_route`: explain how the project proceeds across stages, how information and feedback move, and where application validation closes the loop.
- `branch_research`: define one topic's research object, two to four subproblems, target mechanisms or capabilities, and interfaces to adjacent topics.
- `branch_route`: explain inputs, constraints, methods, implementation sequence, outputs, validation, feedback, rollback, and iteration at an executable research depth.
- `core_module`: explain entities, internal mechanism, state or data transitions, routing conditions, interfaces, and the module's contribution to the parent route.

## Draft With Functional Sentences

Use the recurring logic:

`problem/demand -> mainline -> research action -> mechanism -> capability/output -> validation/feedback`.

Use research verbs deliberately:

- use `研究` for unresolved theory, method, or mechanism;
- use `构建` for models, spaces, frameworks, datasets, and systems;
- use `建立` for rules, mappings, indicators, protocols, and feedback mechanisms;
- use `形成` for integrated methods, technical systems, reusable paradigms, and final outputs;
- use `实现` only for a capability supported by the proposed method;
- use `验证` for an explicit experiment, deployment, comparison, or acceptance activity.

Keep parallel items grammatically parallel. Maintain one term for one concept across headings, prose, captions, and figures.

## Self-Review

Reject a draft that:

- repeats the problem without stating research action;
- lists fashionable algorithms without explaining their role;
- places branch-level details in an overall paragraph;
- describes a route as a static inventory;
- claims results, metrics, or maturity not supplied by the user;
- omits interfaces, validation, or feedback when the source requires a closed loop.

Return clean proposal-ready prose. Include a content-to-figure map only when a drawing or audit task follows.
