#!/usr/bin/env python3
import argparse
import json
import sys
from copy import deepcopy


ACTIONS = {"write", "draw", "audit_correct"}
TARGETS = {
    "overall_research",
    "overall_route",
    "branch_research",
    "branch_route",
    "core_module",
}
DELIVERABLES = {
    "text",
    "editable_figure",
    "preview",
    "audit_report",
    "corrected_artifacts",
}
PALETTE_MODES = {"custom", "default", "reference", "pending", "not_applicable"}
BACKENDS = {"powerpoint", "wps", "drawio"}


def _nonempty(value):
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return value is not None


def validate_spec(spec):
    normalized = deepcopy(spec) if isinstance(spec, dict) else {}
    errors = []
    questions = []

    action = normalized.get("action")
    target = normalized.get("target")

    if action is None:
        questions.append("ask_action")
    elif action not in ACTIONS:
        errors.append(f"invalid action: {action}")

    if target is None:
        questions.append("ask_target")
    elif target not in TARGETS:
        errors.append(f"invalid target: {target}")

    if not _nonempty(normalized.get("source_scope")):
        questions.append("ask_source_scope")

    constraints = normalized.get("constraints")
    if constraints is None:
        constraints = {}
        normalized["constraints"] = constraints
    elif not isinstance(constraints, dict):
        errors.append("constraints must be an object")
        constraints = {}

    deliverables = normalized.get("deliverables")
    if deliverables is None:
        if action == "write":
            deliverables = ["text"]
        elif action == "draw":
            deliverables = ["editable_figure", "preview"]
        elif action == "audit_correct":
            deliverables = ["audit_report"]
        else:
            deliverables = []
        normalized["deliverables"] = deliverables
    elif not isinstance(deliverables, list):
        errors.append("deliverables must be a list")
        deliverables = []
    else:
        unknown = sorted(set(deliverables) - DELIVERABLES)
        if unknown:
            errors.append("invalid deliverables: " + ", ".join(unknown))

    figure_work = action == "draw" or (
        action == "audit_correct"
        and bool({"editable_figure", "corrected_artifacts"} & set(deliverables))
    )

    palette_mode = normalized.get("palette_mode")
    backend = normalized.get("backend")

    if action == "write":
        if palette_mode is None:
            normalized["palette_mode"] = "not_applicable"
        elif palette_mode != "not_applicable":
            errors.append("write tasks require palette_mode=not_applicable")
        if backend is not None:
            errors.append("write tasks must not set a drawing backend")
    elif figure_work:
        if palette_mode is None:
            questions.append("ask_palette")
        elif palette_mode not in PALETTE_MODES - {"not_applicable"}:
            errors.append(f"invalid figure palette_mode: {palette_mode}")
        elif palette_mode == "pending":
            questions.append("wait_palette")
        elif palette_mode == "custom" and not _nonempty(constraints.get("palette")):
            questions.append("ask_custom_palette")
        elif palette_mode == "reference" and not _nonempty(
            constraints.get("palette_reference")
        ):
            questions.append("ask_palette_reference")

        if backend is None:
            questions.append("ask_backend")
        elif backend not in BACKENDS:
            errors.append(f"invalid backend: {backend}")
    else:
        if palette_mode is None:
            normalized["palette_mode"] = "not_applicable"
        elif palette_mode not in PALETTE_MODES:
            errors.append(f"invalid palette_mode: {palette_mode}")
        if backend is not None and backend not in BACKENDS:
            errors.append(f"invalid backend: {backend}")

    questions = list(dict.fromkeys(questions))
    return {
        "valid": not errors,
        "ready": not errors and not questions,
        "errors": errors,
        "questions": questions,
        "normalized": normalized,
    }


def main():
    parser = argparse.ArgumentParser(description="Validate a proposal_task_spec JSON file.")
    parser.add_argument("input", help="JSON path or - for stdin")
    parser.add_argument("--strict", action="store_true", help="Exit nonzero unless ready")
    args = parser.parse_args()

    if args.input == "-":
        spec = json.load(sys.stdin)
    else:
        with open(args.input, "r", encoding="utf-8") as handle:
            spec = json.load(handle)

    result = validate_spec(spec)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if args.strict and not result["ready"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
