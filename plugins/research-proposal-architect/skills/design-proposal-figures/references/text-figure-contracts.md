# Text-Figure Contracts

## General Contract

Every semantic figure object must map to one or more prose claim ids. Every required prose claim must map to at least one figure object unless the figure's declared communication job intentionally excludes that detail.

Use these mapping statuses:

- `exact`: same term, metric, or assertion;
- `compressed`: meaning preserved with shorter wording;
- `grouped`: several claims represented by one labeled region;
- `omitted_by_scope`: intentionally excluded and documented;
- `conflict`: figure and prose disagree;
- `invented`: figure assertion has no prose basis.

`conflict` and `invented` are hard failures.

## Overall Research Content

Must represent:

- shared problem or demand;
- each major topic;
- topic-level research focus;
- explicit topic dependencies and feedback;
- integrated project-level result.

Must not introduce:

- branch algorithms or parameter settings;
- implementation chronology not stated in the content;
- application outcomes that belong only to targets or indicators.

## Overall Technical Route

Must represent:

- objective or route purpose;
- ordered major stages;
- stage inputs and outputs;
- project-wide feedback or iteration;
- system integration;
- application validation and representative outcomes.

Must not:

- duplicate every branch step;
- convert parallel topics into a false sequence;
- add a feedback arrow without a defined evidence source and update target.

## Branch Research Content

Must represent:

- topic objective or research object;
- all named subitems;
- distinct mechanism or capability per subitem;
- integration of subitem results;
- upstream/downstream interfaces when stated.

Must not imply:

- an execution order when the subitems are parallel;
- validation completion when only research is proposed.

## Branch Technical Route

Must represent:

- input data, knowledge, rules, or upstream result;
- each task and its method chain;
- technical outputs and handoffs;
- validation or evaluation;
- feedback, update, and rollback conditions when stated.

Exact preservation is mandatory for formulas, metrics, thresholds, standards, model classes, and interface names.

## Core Technology Or Module

Must represent:

- entities, model classes, or layers;
- mappings, interactions, or routing conditions;
- central mechanism;
- output and parent-route interface;
- conflict, uncertainty, or exception path when central to the mechanism.

Must not expand into unrelated scenarios or project-wide outcomes.

## Caption And Lead-In

The lead-in explains the figure's organizing logic and ends with a direct figure reference. It does not narrate every label.

The caption names the communication job. Prefer “总体研究内容及课题关系”, “课题X技术路线与反馈闭环”, or “核心模块条件路由机制” over a generic “示意图.”
