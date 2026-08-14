# Proposal Task Specification

## Purpose

Use this contract to make routing deterministic while keeping interaction proportional to what is missing.

## Canonical Fields

| Field | Allowed values | Meaning |
|---|---|---|
| `action` | `write`, `draw`, `audit_correct` | What the user wants done |
| `target` | `overall_research`, `overall_route`, `branch_research`, `branch_route`, `core_module` | The proposal level being handled |
| `source_scope` | non-empty string or object | Chapter, paragraphs, files, figures, or supplied text |
| `deliverables` | list | Text, editable figure, preview, audit report, corrected artifacts |
| `palette_mode` | `custom`, `default`, `reference`, `pending`, `not_applicable` | Color decision |
| `backend` | `powerpoint`, `wps`, `drawio`, or omitted | Editable figure backend |
| `constraints` | object | Word limit, page size, terms, metrics, palette source, confidentiality |

## Target Labels

Present these labels when `target` is missing:

1. 总体研究内容
2. 总体技术路线
3. 分支研究内容
4. 分支技术路线
5. 核心技术/模块

Do not merge “research content” and “technical route.” Research content answers what is studied and how work is decomposed. A technical route answers how the work proceeds and closes the loop.

## Action Labels

Present these labels when `action` is missing:

1. 文字撰写或改写
2. 配图设计与绘制
3. 文字和配图的适配度检查及校正

## Requiredness Matrix

| Action | Source | Palette | Backend | Default deliverables |
|---|---|---|---|---|
| `write` | required | `not_applicable` | omitted | `text` |
| `draw` | required | custom/default/reference; pending blocks work | required | `editable_figure`, `preview` |
| audit only | text and figure required | `not_applicable` | inferred from source or optional | `audit_report` |
| audit and correct figure | text and figure required | custom/default/reference; pending blocks work | required | `audit_report`, `corrected_artifacts` |

## Palette Interaction

First detect whether the prompt or supplied assets already establish a palette.

If no palette is present, ask:

“当前没有检测到自定义配色要求。您希望使用插件默认配色，暂停并等待补充配色，还是提供一张参考图片用于提取配色？”

Map responses:

- default -> `palette_mode: default`;
- wait -> `palette_mode: pending` and pause figure design;
- reference image -> `palette_mode: reference` and record the path;
- explicit colors/style guide -> `palette_mode: custom` and record tokens.

For reference images, propose semantic roles for the extracted colors and obtain confirmation before drawing. Do not assume that the most frequent image color should become the structural color.

## Backend Interaction

If the source already is an editable PPTX/WPS/draw.io document, use its backend. Otherwise ask:

“配图需要在哪个可编辑后端中制作：PowerPoint、WPS，还是 draw.io？”

Do not default silently. If Scientific Illustrator or the selected adapter is unavailable, report the missing prerequisite before construction.

## Decision-Complete Example

```yaml
action: draw
target: branch_route
source_scope:
  document: proposal.docx
  section: 课题二研究方案
deliverables:
  - editable_figure
  - preview
  - text
palette_mode: reference
backend: powerpoint
constraints:
  palette_reference: reference.png
  page_context: A4 portrait document
  preserve_terms:
    - 统一认知空间
  confidentiality: local-only
```

## Routing Rules

- Route a complete `write` specification to `$write-research-sections`.
- Route a complete `draw` specification to `$design-proposal-figures`.
- Route `audit_correct` to `$audit-proposal-alignment`.
- Route “learn this sample,” “extract this style,” or knowledge-base evolution to `$distill-proposal-patterns`.
- For combined work, use write -> design -> audit in that order.
- Never ask again for a value already stated or discoverable from the source.
