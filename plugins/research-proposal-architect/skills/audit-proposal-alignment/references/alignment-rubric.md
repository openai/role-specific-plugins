# Alignment Rubric

## Evidence Channels

Use both:

1. semantic evidence: prose claims, visible labels, object metadata, connector direction, metrics, and mappings;
2. visual evidence: current renderer output and editable object inventory.

Do not approve from a screenshot alone or from object metadata alone.

## Categories And Weights

| Category | Weight | Hard-failure examples |
|---|---:|---|
| Required claim coverage | 0.25 | missing topic, task, mechanism, output, validation |
| Terminology accuracy | 0.20 | renamed fixed concept, term collision |
| Metric/formula fidelity | 0.15 | changed unit, threshold, inequality, formula role |
| Relationship/topology | 0.20 | reversed arrow, false sequence, missing feedback |
| Hierarchy/granularity | 0.10 | route shown as content hierarchy or vice versa |
| Caption/lead-in correspondence | 0.10 | caption claims a scope the figure does not show |

Semantic accuracy, terminology, and metric fidelity must equal 1.00. Weighted averages cannot override a hard failure.

## Finding Format

```text
finding_id:
claim_ids:
figure_objects:
category:
severity: hard | warning
evidence:
required_correction:
acceptance:
confidence:
```

## Hard Failures

- Required prose claim has no mapped figure object.
- Figure contains an unapproved semantic object with no prose basis.
- A connector reverses dependency, control, feedback, or data flow.
- A metric, equation, unit, threshold, standard, or named model class differs.
- A core technology is attributed to the wrong topic.
- Feedback exists without evidence source, trigger, or update target.
- Figure type does not match the declared target.

## Warnings

- Supporting detail is uneven across peer modules.
- A label is too verbose or duplicates nearby prose.
- A valid secondary claim is omitted by scope but not documented.
- Color roles are inconsistent without changing meaning.
- Caption is generic but not false.

## Correction Order

1. factual text and immutable terms;
2. metrics, equations, and standards;
3. missing or invented objects;
4. relationship direction and topology;
5. hierarchy and granularity;
6. caption and lead-in;
7. palette roles;
8. visual geometry and text fit.

After correction, regenerate the mapping matrix and collect fresh visual evidence.

## Pass Gate

- semantic/text accuracy = 1.00;
- terminology accuracy = 1.00;
- metric/formula fidelity = 1.00;
- required claim coverage >= 0.95;
- zero hard failures;
- no unresolved warning except a documented source ambiguity;
- Scientific Illustrator geometry and connector clarity >= 0.95;
- clipping, overlap safety, and reconstructable editability = 1.00.
