# Research Proposal Architect

Research Proposal Architect is a companion Codex plugin for Chinese science and technology proposals. It routes, drafts, diagrams, and audits:

- overall research content;
- overall technical routes;
- branch research content;
- branch technical routes;
- core technologies or modules.

It supports three operations: writing, editable figure design, and text-figure alignment review/correction.

## Install

Install Scientific Illustrator first, then install this repository as a Codex plugin. The plugin entry skill will ask for the target section, requested operation, source scope, deliverables, and any writing constraints. Figure tasks also require an explicit palette choice and a PowerPoint, WPS, or draw.io backend.

## Prerequisite

Install [Scientific Illustrator](https://github.com/icebird1998/scientific-illustrator) for editable PowerPoint, WPS, or draw.io figure construction. This plugin does not copy or replace Scientific Illustrator. It prepares proposal-domain semantic specifications and invokes its design, drawing, review, and correction workflow.

## Skills

- `route-proposal-work`
- `write-research-sections`
- `design-proposal-figures`
- `audit-proposal-alignment`
- `distill-proposal-patterns`

The plugin does not include source proposal documents or extracted figures. Bundled examples are synthetic and contain no project-sensitive information.

## Privacy

Research Proposal Architect runs through Codex skills and does not provide its own network service. Proposal content is processed only through the Codex tools and figure backends selected by the user. Do not publish confidential proposal materials in issue reports or pull requests.

## License

MIT. See [LICENSE](./LICENSE).
