# Technical Depth Ladder

Use this ladder to decide what belongs at each proposal level.

| Level | Must contain | May contain | Exclude by default |
|---|---|---|---|
| Overall research content | problem cluster, topic decomposition, dependencies, integrated outcome | named core mechanisms | algorithms, formulas, parameter values, implementation steps |
| Overall technical route | ordered stages, information flow, feedback, integration, validation, outcomes | representative methods and indicators | full branch detail, long algorithm lists |
| Branch research content | research object, subproblems, target mechanisms/capabilities, upstream/downstream interfaces | representative method families | equations, deployment instructions, exhaustive validation procedure |
| Branch technical route | inputs, constraints, method sequence, outputs, validation, feedback, rollback/iteration | algorithms, equations, thresholds, standards | unrelated project context, repeated overall objectives |
| Core technology/module | entities, topology, transformation, routing conditions, interface, failure/conflict handling | equations and algorithm internals central to the mechanism | complete project route, every scenario and outcome |

## Promotion And Demotion Rules

Promote a detail upward only when it differentiates the project's core contribution. Demote a detail downward when it explains implementation rather than project logic.

Examples:

- “多模型协同” may appear in overall research content when it is a core topic.
- “置信度阈值触发条件路由” belongs in branch route or core module.
- A quantitative target belongs in the overall outcome rail only when it is a representative acceptance result; its derivation belongs below.
- A named protocol belongs in branch route or system architecture unless it is a project-wide interoperability commitment.

## Completeness Gates

### Overall Research Content

Pass only when a reviewer can answer:

- What are the major topics?
- Why are they ordered or connected this way?
- What does each provide to the next?
- What integrated research system results?

### Overall Technical Route

Pass only when a reviewer can trace:

- initial inputs and constraints;
- major research stages;
- forward information flow;
- feedback and iteration;
- final validation and outcomes.

### Branch Research Content

Pass only when subitems are non-overlapping, collectively sufficient, and connected to the parent objective.

### Branch Technical Route

Pass only when each task has an input, method, output, and validation or downstream handoff. Closed-loop claims require a visible feedback object and trigger.

### Core Module

Pass only when the mechanism explains why outputs differ for different inputs, states, rules, or conditions.

## Failure Modes

- Too shallow: only nouns and slogans, no research action or mechanism.
- Too deep: overall paragraphs contain implementation parameters and algorithm pipelines.
- Misleveled: a branch route repeats the project objective instead of describing execution.
- Disconnected: the content lists tasks but no inputs, outputs, or interfaces.
- Unfalsifiable: validation is claimed without an observable test or criterion.
