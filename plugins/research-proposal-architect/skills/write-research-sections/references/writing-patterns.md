# Writing Patterns For Chinese Research Proposals

## Contents

1. Governing logic
2. Paragraph functions
3. Overall research content
4. Branch research content
5. Overall technical route
6. Branch technical route
7. Core technology or module
8. Verb discipline
9. Style and quality checks

## 1. Governing Logic

Use a controlled progression:

`problem or demand -> organizing mainline -> research action -> technical mechanism -> capability or output -> validation and feedback`.

Not every paragraph needs all six roles, but the complete section must cover them. Each paragraph should have one dominant job.

Use a problem-led opening when the project must justify technical necessity. Use a demand-led opening when the application context already establishes the problem and the paragraph needs to organize the solution.

## 2. Paragraph Functions

| Function | Question answered | Typical language |
|---|---|---|
| Problem framing | Why is this work necessary? | 针对、面向、围绕……需求 |
| Mainline | What logic organizes the work? | 按照、沿着、围绕……主线 |
| Research action | What unresolved work is performed? | 研究、揭示、解析 |
| Construction | What artifact or framework is built? | 构建、建立、设计 |
| Capability | What becomes possible? | 实现、支撑、提升 |
| Integration | What is formed after combination? | 形成、贯通、集成 |
| Validation | How is it tested? | 开展验证、评价、对照 |
| Feedback | How does evidence change the system? | 反馈、反哺、校正、迭代、回退 |

Avoid using all verbs as interchangeable decoration. Every verb should predict the type of object that follows it.

## 3. Overall Research Content

### Communication Job

Explain what the entire project studies, how topics divide, how they depend on each other, and what integrated research system results.

### Recommended Paragraph Architecture

1. State the shared problem cluster.
2. State the organizing logic with three to five parallel themes.
3. Introduce each topic in dependency order.
4. Express cross-topic inputs and feedback explicitly.
5. Close with the integrated capability, technical system, or research paradigm.

### Sentence Skeleton

“围绕[共同问题群]，按照[主题A、主题B、主题C、验证主题]的逻辑开展研究。[课题一]研究[对象与能力]，为[课题二]提供[输入]；[课题二]构建[关键能力]，向[课题三]输出[结果]，并反馈驱动[前序对象]更新；[课题三]研究[交互、调控或决策能力]，其核验结果反哺[相关能力]；[课题四]完成[集成、评价和示范]，最终形成[总体技术体系或范式]。”

### Boundaries

- Name topic-level mechanisms, not detailed algorithms.
- Preserve the dependency topology.
- Include feedback only when the research design actually contains it.
- End with a project-level outcome, not a repetition of the last topic.

## 4. Branch Research Content

### Communication Job

Define one topic's internal decomposition. Each subitem should have a distinct research object and resulting capability.

### Subitem Pattern

“（n）[名词化标题]。研究[理论、方法或机制]，构建[model/framework/system]，解析或建立[关键关系]，形成或实现[research capability/output]。”

Use two to four subitems. Keep titles parallel:

- all mechanism-led;
- all capability-led;
- or all object + action combinations.

### Three-Part Topic Pattern

A reliable topic sequence is:

1. perception, representation, or foundational construction;
2. modeling, inference, adaptation, or collaboration;
3. feedback, evaluation, self-iteration, or deployment validation.

This is a heuristic, not a mandatory taxonomy. Do not force a feedback item when the source topic has no feedback mechanism.

## 5. Overall Technical Route

### Communication Job

Explain the project-wide sequence, information flow, feedback paths, integration, validation, and outcomes.

### Recommended Architecture

1. Open with the ordered route: “按照A、B、C、D的技术路线”.
2. Describe each stage with research action + constructed mechanism + resulting flow.
3. Connect stages with explicit inputs and outputs.
4. State the system integration and application validation.
5. Close the loop with evidence return or iterative update when supported.

### Sentence Skeleton

“本项目按照[阶段A、阶段B、阶段C、阶段D]的技术路线，研究[阶段A方法]，构建[stage-A artifacts]，实现[output A]；基于[output A]构建[stage-B mechanism]，形成[output B]；面向[stage-C demand]研究[interaction/control mechanism]，支撑[functions]；集成形成[system]，并在[scenes]开展[validation]，以[feedback evidence]驱动[updated objects]。”

Do not write the overall route as four unrelated topic abstracts.

## 6. Branch Technical Route

### Topic Overview Before The Figure

Use:

“本课题面向[需求或问题]，围绕[A-B-C]研究主线，构建[task framework]，通过[critical mechanism]形成[closed-loop capability]。具体技术路线如图X所示。”

This paragraph should explain why the figure is organized as it is. It should not narrate every box.

### Detailed Task Paragraph

Use the following order when applicable:

1. “针对[precise technical difficulty]”;
2. identify input data, rules, constraints, or upstream result;
3. name the researched method and why it is used;
4. state transformations, models, algorithms, or formal relations in execution order;
5. define output and downstream interface;
6. state validation, low-confidence handling, feedback, rollback, or update conditions.

### Formula Integration

Introduce a formula only when:

- its variables have defined semantic roles;
- it materially explains selection, fusion, loss, routing, or evaluation;
- the text explains how the formula changes the process;
- the figure does not need to reproduce the whole equation unless the equation is the core mechanism.

### Feedback Paragraph

A complete feedback task distinguishes:

- evidence source;
- diagnosis or classification;
- priority or trigger;
- adjusted object;
- comparison or validation;
- accept/update versus reject/rollback outcome.

Avoid vague closures such as “持续优化模型.”

## 7. Core Technology Or Module

### Communication Job

Explain the internal mechanism of one named technology without expanding back into the entire project.

### Mechanism Pattern

“针对[input or conflict]，构建[central space/router/module]，将[entity A]、[entity B]与[entity C]通过[relations]组织起来；采用[mechanism]完成[state/data transformation]，并通过[constraint/check]处理[exception or conflict]，向[parent route]输出[capability].”

Include:

- entities or model classes;
- transformations or interactions;
- routing or activation conditions;
- outputs and interfaces;
- conflict, uncertainty, or failure handling when relevant.

## 8. Verb Discipline

| Verb | Preferred object |
|---|---|
| 研究 | theory, method, mechanism, law, strategy |
| 揭示 | relationship, mechanism, evolution law |
| 解析 | influence, composition, semantics, cause |
| 构建 | model, framework, space, dataset, system |
| 建立 | mapping, rule, indicator, protocol, association |
| 设计 | architecture, process, algorithm, experiment |
| 形成 | integrated method, technical system, paradigm, output |
| 实现 | supported capability or operational effect |
| 验证 | hypothesis, performance, applicability, stability |
| 评价 | quality, effectiveness, consistency, cost |

Do not use “实现” to assert a result before the route explains how it is achieved.

## 9. Style And Quality Checks

- Prefer compact formal prose over promotional slogans.
- Use semicolons to separate coordinated topic routes; use full stops when the sentence function changes.
- Keep headings noun-led and parallel.
- Keep one concept-one term throughout the chapter.
- Replace “采用多种先进技术” with named roles and mechanisms.
- Distinguish research uncertainty from engineering implementation.
- Preserve supplied metrics exactly, including symbols, units, inequality direction, and precision.
- Keep outcome claims within the supplied project scope.
- Ensure the last sentence closes at the same level as the heading.
