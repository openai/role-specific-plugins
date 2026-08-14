#!/usr/bin/env python3
import argparse
import json
import re
import sys


def _compact(text):
    return re.sub(r"\s+", "", str(text or ""))


def _ratio(matched, total):
    return 1.0 if total == 0 else round(matched / total, 4)


def audit_alignment(data):
    claims = data.get("claims", [])
    objects = data.get("figure_objects", [])
    relations = data.get("figure_relations", [])
    allowed_extra = set(data.get("allowed_extra_object_ids", []))
    findings = []

    claim_by_id = {}
    for claim in claims:
        claim_id = claim.get("id")
        if not claim_id or claim_id in claim_by_id:
            findings.append(
                {
                    "category": "schema",
                    "severity": "hard",
                    "evidence": f"missing or duplicate claim id: {claim_id}",
                }
            )
        else:
            claim_by_id[claim_id] = claim

    object_by_id = {}
    mapped = {claim_id: [] for claim_id in claim_by_id}
    for obj in objects:
        object_id = obj.get("id")
        if not object_id or object_id in object_by_id:
            findings.append(
                {
                    "category": "schema",
                    "severity": "hard",
                    "evidence": f"missing or duplicate figure object id: {object_id}",
                }
            )
            continue
        object_by_id[object_id] = obj
        claim_ids = obj.get("claim_ids", [])
        for claim_id in claim_ids:
            if claim_id not in claim_by_id:
                findings.append(
                    {
                        "category": "invented",
                        "severity": "hard",
                        "figure_objects": [object_id],
                        "evidence": f"object maps to unknown claim id: {claim_id}",
                    }
                )
            else:
                mapped[claim_id].append(obj)
        if obj.get("semantic", True) and not claim_ids and object_id not in allowed_extra:
            findings.append(
                {
                    "category": "invented",
                    "severity": "hard",
                    "figure_objects": [object_id],
                    "evidence": "semantic object has no prose claim mapping",
                }
            )

    required_claims = [claim for claim in claims if claim.get("required", True)]
    covered = 0
    term_total = term_matched = 0
    metric_total = metric_matched = 0

    for claim in required_claims:
        claim_id = claim.get("id")
        mapped_objects = mapped.get(claim_id, [])
        if not mapped_objects:
            findings.append(
                {
                    "category": "coverage",
                    "severity": "hard",
                    "claim_ids": [claim_id],
                    "evidence": "required prose claim has no mapped figure object",
                }
            )
            continue

        covered += 1
        visible = _compact(" ".join(obj.get("text", "") for obj in mapped_objects))
        object_ids = [obj.get("id") for obj in mapped_objects]

        for term in claim.get("required_terms", []):
            term_total += 1
            if _compact(term) in visible:
                term_matched += 1
            else:
                findings.append(
                    {
                        "category": "terminology",
                        "severity": "hard",
                        "claim_ids": [claim_id],
                        "figure_objects": object_ids,
                        "evidence": f"required term missing: {term}",
                    }
                )

        for metric in claim.get("metrics", []):
            metric_total += 1
            if _compact(metric) in visible:
                metric_matched += 1
            else:
                findings.append(
                    {
                        "category": "metric",
                        "severity": "hard",
                        "claim_ids": [claim_id],
                        "figure_objects": object_ids,
                        "evidence": f"exact metric missing or changed: {metric}",
                    }
                )

        for forbidden in claim.get("forbidden_terms", []):
            if _compact(forbidden) in visible:
                findings.append(
                    {
                        "category": "invented",
                        "severity": "hard",
                        "claim_ids": [claim_id],
                        "figure_objects": object_ids,
                        "evidence": f"forbidden or unsupported term present: {forbidden}",
                    }
                )

    expected_relations = []
    for claim in claims:
        source = claim.get("id")
        for relation in claim.get("relationships", []):
            expected_relations.append(
                (source, relation.get("target"), relation.get("type", "flow"))
            )

    actual_relations = {
        (
            relation.get("source_claim"),
            relation.get("target_claim"),
            relation.get("type", "flow"),
        )
        for relation in relations
    }
    relation_matched = 0
    for expected in expected_relations:
        if expected in actual_relations:
            relation_matched += 1
        else:
            findings.append(
                {
                    "category": "relationship",
                    "severity": "hard",
                    "claim_ids": [expected[0], expected[1]],
                    "evidence": "missing or directionally incorrect relation: "
                    + " -> ".join(expected[:2])
                    + f" ({expected[2]})",
                }
            )

    scores = {
        "claim_coverage": _ratio(covered, len(required_claims)),
        "terminology_accuracy": _ratio(term_matched, term_total),
        "metric_fidelity": _ratio(metric_matched, metric_total),
        "relationship_accuracy": _ratio(relation_matched, len(expected_relations)),
    }
    hard_failures = [finding for finding in findings if finding["severity"] == "hard"]
    scores["semantic_accuracy"] = 1.0 if not hard_failures else 0.0

    passed = (
        not hard_failures
        and scores["claim_coverage"] >= 0.95
        and scores["terminology_accuracy"] == 1.0
        and scores["metric_fidelity"] == 1.0
        and scores["relationship_accuracy"] == 1.0
    )
    return {
        "pass": passed,
        "scores": scores,
        "hard_failure_count": len(hard_failures),
        "findings": findings,
    }


def main():
    parser = argparse.ArgumentParser(description="Audit a structured text-figure mapping.")
    parser.add_argument("input", help="JSON path or - for stdin")
    parser.add_argument("--strict", action="store_true", help="Exit nonzero on failure")
    args = parser.parse_args()

    if args.input == "-":
        data = json.load(sys.stdin)
    else:
        with open(args.input, "r", encoding="utf-8") as handle:
            data = json.load(handle)

    report = audit_alignment(data)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if args.strict and not report["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
