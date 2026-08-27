---
name: hol-guard
description: Set up and operate HOL Guard to protect Codex tool execution, review approvals and receipts, and verify Codex plugins, skills, and MCP packages before release.
---

# HOL Guard for Codex

Use HOL Guard when a Codex workspace needs a local security boundary around tool execution or when agent packages need verification before they are trusted.

## Safety rules

- Never read `.env` files.
- Never bypass a HOL Guard approval.
- Do not claim the workspace is protected until a Guard command confirms it.
- Prefer Guard-owned install and repair commands over manual edits to Codex configuration.
- Treat scanner failures as real until they are inspected.

## Install

Check for the runtime by invoking the CLI directly:

```bash
hol-guard --version
```

If it is missing, prefer an isolated CLI installation:

```bash
pipx install hol-guard
```

Then confirm the runtime can see the workspace:

```bash
hol-guard status
hol-guard detect --json
```

## Protect Codex

Bootstrap Guard, install its Codex protection, preview the launch path, and then run Codex through Guard:

```bash
hol-guard bootstrap
hol-guard install codex
hol-guard run codex --dry-run
hol-guard run codex
hol-guard status
```

For a diagnostic check:

```bash
hol-guard doctor codex --json
```

HOL Guard owns the Codex protection path. Do not hand-edit `.codex/hooks.json` as a substitute for `hol-guard install codex`.

## Handle blocked requests

When Guard blocks or queues a tool request, inspect it before changing state:

```bash
hol-guard approvals
hol-guard approvals open
hol-guard receipts
hol-guard diff codex
```

For terminal-only resolution:

```bash
hol-guard approvals approve <request-id>
hol-guard approvals deny <request-id>
```

Only approve after reading the risk reason and understanding the requested scope.

## Collect evidence

Use Guard's evidence surfaces when the user needs proof or an audit trail:

```bash
hol-guard receipts
hol-guard inventory
hol-guard abom --format json
hol-guard events
hol-guard explain <artifact-id>
```

Cloud sync is optional and should be user-directed:

```bash
hol-guard connect
hol-guard connect status
hol-guard sync
```

## Verify Codex plugins, skills, and MCP packages

HOL Guard ships separately from the plugin scanner. Check the scanner independently by invoking its CLI directly:

```bash
plugin-scanner --version
```

If it is missing and package verification is requested:

```bash
pipx install plugin-scanner
```

Scan the package or workspace root:

```bash
plugin-scanner lint .
plugin-scanner verify .
```

For JSON evidence:

```bash
plugin-scanner verify . --json
```

When scanning a Codex marketplace, run from the repository root containing `.agents/plugins/marketplace.json` so local plugin entries can be discovered.

## Report results

After using HOL Guard, report:

- the command that ran;
- what Guard found;
- what remains blocked or risky;
- the evidence or receipt produced; and
- the exact next command if user action is required.

Do not claim protection, approval, or release readiness without command output proving it.
