import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "skills"
    / "audit-proposal-alignment"
    / "scripts"
    / "audit_alignment.py"
)
SPEC = importlib.util.spec_from_file_location("audit_alignment", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def passing_fixture():
    return {
        "claims": [
            {
                "id": "c1",
                "text": "构建统一数据底座",
                "required_terms": ["统一数据底座"],
                "required": True,
                "relationships": [
                    {"target": "c2", "type": "support"}
                ],
            },
            {
                "id": "c2",
                "text": "形成跨场景认知能力，准确率不低于90%",
                "required_terms": ["跨场景认知"],
                "metrics": ["不低于90%"],
                "required": True,
            },
        ],
        "figure_objects": [
            {
                "id": "n1",
                "text": "统一数据底座",
                "claim_ids": ["c1"],
                "semantic": True,
            },
            {
                "id": "n2",
                "text": "跨场景认知能力\n准确率不低于90%",
                "claim_ids": ["c2"],
                "semantic": True,
            },
            {
                "id": "title",
                "text": "分支研究内容",
                "claim_ids": [],
                "semantic": False,
            },
        ],
        "figure_relations": [
            {
                "source_claim": "c1",
                "target_claim": "c2",
                "type": "support",
            }
        ],
    }


class AlignmentAuditTests(unittest.TestCase):
    def test_passing_mapping(self):
        report = MODULE.audit_alignment(passing_fixture())
        self.assertTrue(report["pass"], report)
        self.assertEqual(report["scores"]["semantic_accuracy"], 1.0)

    def test_missing_metric_is_hard_failure(self):
        fixture = passing_fixture()
        fixture["figure_objects"][1]["text"] = "跨场景认知能力"
        report = MODULE.audit_alignment(fixture)
        self.assertFalse(report["pass"])
        self.assertTrue(
            any(item["category"] == "metric" for item in report["findings"])
        )

    def test_reversed_relation_is_hard_failure(self):
        fixture = passing_fixture()
        fixture["figure_relations"] = [
            {
                "source_claim": "c2",
                "target_claim": "c1",
                "type": "support",
            }
        ]
        report = MODULE.audit_alignment(fixture)
        self.assertFalse(report["pass"])
        self.assertTrue(
            any(item["category"] == "relationship" for item in report["findings"])
        )

    def test_unmapped_semantic_object_is_invented(self):
        fixture = passing_fixture()
        fixture["figure_objects"].append(
            {
                "id": "invented",
                "text": "自动决策",
                "claim_ids": [],
                "semantic": True,
            }
        )
        report = MODULE.audit_alignment(fixture)
        self.assertFalse(report["pass"])
        self.assertTrue(
            any(item["category"] == "invented" for item in report["findings"])
        )


if __name__ == "__main__":
    unittest.main()
