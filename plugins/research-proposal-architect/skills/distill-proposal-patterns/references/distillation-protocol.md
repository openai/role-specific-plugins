# Distillation Protocol

## Purpose

Convert a strong proposal sample into reusable patterns without copying project-specific content or treating every source choice as a best practice.

## Evidence Collection

1. Identify the complete chapter boundaries.
2. Extract paragraphs inside body text and tables.
3. Map embedded figures to lead-ins and captions.
4. Render relevant pages and inspect the figures at readable resolution.
5. Record word limits, heading levels, equations, metrics, and cross-topic references.

## Prose Analysis

For every paragraph, label:

- section level;
- dominant function;
- opening strategy;
- sentence sequence;
- research verbs and their objects;
- abstraction depth;
- upstream and downstream references;
- closure type;
- claims that must remain source-specific.

Analyze both macrostructure and microstructure. A transferable rule must explain why a structure works, not merely repeat its wording.

## Figure Analysis

For every figure, record:

- communication job and declared target;
- reading order;
- major regions and hierarchy levels;
- object roles;
- connector types and directions;
- feedback lanes;
- palette roles;
- density and text compression;
- correspondence to prose claims;
- source defects that should not be reproduced.

## Observation Classes

| Class | Treatment |
|---|---|
| `source_fact` | keep only in local evidence; never add to reusable rules |
| `transferable_pattern` | add when its function is clear and general |
| `candidate_rule` | test against another sample or synthetic counterexample |
| `source_defect` | add as a failure mode when generalizable |

## Privacy And Open-Source Gate

Do not bundle:

- original proposal files or extracted figures;
- organization, person, project, or customer names;
- unpublished metrics, budgets, schedules, or deployment locations;
- full source paragraphs;
- proprietary diagrams or branding.

Publish de-identified structural descriptions and synthetic examples only.

## Knowledge Delta

A proposed update must identify:

- affected reference file and rule;
- evidence supporting the change;
- whether the change narrows or broadens behavior;
- conflicting existing rule;
- one positive and one negative synthetic test.
