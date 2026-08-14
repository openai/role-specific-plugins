# Figure Patterns

## Contents

1. Common visual grammar
2. Overall research content
3. Overall technical route
4. Branch research content
5. Branch technical route
6. Core technology or module
7. Density and connector rules

## 1. Common Visual Grammar

Use a figure to expose relationships that prose makes difficult to scan. Do not turn every sentence into a box.

Every semantic object must have one role:

- problem or demand;
- input or constraint;
- research topic or task;
- method or mechanism;
- output or capability;
- validation evidence;
- feedback or update;
- application scene or final outcome.

Use color by role, not by decorative variety. Use alignment and grouping for hierarchy; use connectors only for direction, dependency, feedback, mapping, or control.

## 2. Overall Research Content

### Job

Show what the project studies and how topics form one research system.

### Recommended Layout

- top rail: shared need or problem cluster;
- middle: three to five topic blocks in dependency order;
- between topics: labeled inputs, outputs, and feedback;
- bottom rail: integrated capability, technical system, or research paradigm.

Use topic blocks with two levels: topic title and two to four concise research components. Do not place task-level algorithms inside.

### Required Relationships

- foundation or data support;
- result supply to downstream topic;
- feedback to an upstream topic when supported;
- integration or validation topic connected to all contributing topics.

### Distinction

This figure is a decomposition and dependency map, not a chronological pipeline.

## 3. Overall Technical Route

### Job

Let a reviewer trace the whole project from objective through methods to validation and outcomes.

### Recommended Layout

- objective rail;
- key-technology rail;
- central route with three to five ordered stages;
- cross-stage input/output labels;
- feedback band or return lanes;
- application/validation band;
- representative outcome rail.

Prefer one dominant reading direction. Use a separate feedback band instead of a tangle of return arrows.

### Compression Rule

Show representative methods and outputs. Move detailed algorithms, task internals, and per-scene parameters to branch figures.

## 4. Branch Research Content

### Job

Show how one topic decomposes into research subproblems and how the results combine.

### Recommended Layout

- topic objective or research object at the top;
- two to four parallel subtask columns or a shallow hierarchy;
- for each subtask: research question, target mechanism, expected capability;
- bottom integration bar;
- side connectors for upstream input and downstream output.

Use this pattern when the source describes “what to study.” If the source describes ordered processing steps, use the branch technical route pattern instead.

## 5. Branch Technical Route

### Job

Show how one topic proceeds from inputs and constraints through methods to outputs, validation, and iteration.

### Pattern A: Sequential Tasks

Use for a clear stage order:

`upstream input -> task 1 -> task 2 -> task 3 -> output/validation`

Place feedback beneath the forward route with a distinct color and arrow convention.

### Pattern B: Parallel Foundations Plus Feedback

Use when two methods develop in parallel and a third task calibrates both:

- top inputs and knowledge/rules;
- two parallel method regions;
- shared result space;
- bottom feedback task spanning the width;
- integrated outcome band.

### Pattern C: Integration And Demonstration

Use for system topics:

- upstream results from other topics;
- architecture/deployment task;
- evaluation/productization task;
- scenario demonstration task;
- two-way support and evaluation feedback.

### Mandatory Roles

Each branch route must expose:

- inputs and boundary conditions;
- numbered tasks;
- method chain;
- output or handoff;
- validation evidence;
- feedback, rollback, or update when the prose claims iteration.

## 6. Core Technology Or Module

### Job

Explain one mechanism with minimal nodes and high semantic precision.

### Pattern A: Mechanism Topology

Use a central space or module with three to five interacting entities around it. Label each mapping or constraint directly. Use bidirectional connectors only when both directions have distinct meaning in the prose.

### Pattern B: Conditional Routing

Use:

- input classes on the left;
- router, scheduler, or decision condition in the center;
- differentiated model/module paths on the right;
- shared optimization or support band below.

Label route conditions such as routine, scene-specific, low-confidence, conflict, or high-risk. Do not imply a condition absent from the source.

### Pattern C: Layered Architecture

Use for a module with stable layers and interfaces. Keep it to the module boundary; do not reproduce the full system architecture.

## 7. Density And Connector Rules

- Use no more than three primary hierarchy levels.
- Use 6-14 Chinese characters for most module titles.
- Keep supporting text to two or three short lines.
- On an A4 portrait page, prioritize larger labels over more boxes.
- Reserve connector lanes before placing nodes.
- Avoid crossing, immediate backtracking, and arrows through labels.
- Use attached connectors for semantic relationships.
- Use a distinct feedback color, but keep feedback labels restrained.
- Keep exact metrics readable; move secondary metrics to prose.
- Recreate text, borders, arrows, legends, and regular diagrams as editable objects.
