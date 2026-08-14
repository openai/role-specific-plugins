import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "skills"
    / "route-proposal-work"
    / "scripts"
    / "validate_task_spec.py"
)
SPEC = importlib.util.spec_from_file_location("validate_task_spec", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class TaskSpecTests(unittest.TestCase):
    def test_all_fifteen_target_action_combinations(self):
        targets = sorted(MODULE.TARGETS)
        actions = sorted(MODULE.ACTIONS)
        count = 0
        for target in targets:
            for action in actions:
                count += 1
                spec = {
                    "action": action,
                    "target": target,
                    "source_scope": "synthetic proposal section",
                    "constraints": {},
                }
                if action == "write":
                    spec["deliverables"] = ["text"]
                    spec["palette_mode"] = "not_applicable"
                elif action == "draw":
                    spec["deliverables"] = ["editable_figure", "preview"]
                    spec["palette_mode"] = "default"
                    spec["backend"] = "powerpoint"
                else:
                    spec["deliverables"] = ["audit_report", "corrected_artifacts"]
                    spec["palette_mode"] = "default"
                    spec["backend"] = "drawio"
                with self.subTest(target=target, action=action):
                    result = MODULE.validate_spec(spec)
                    self.assertTrue(result["ready"], result)
        self.assertEqual(count, 15)

    def test_missing_target_and_action_trigger_only_needed_questions(self):
        result = MODULE.validate_spec({"source_scope": "text"})
        self.assertIn("ask_action", result["questions"])
        self.assertIn("ask_target", result["questions"])

    def test_draw_requires_palette_and_backend(self):
        result = MODULE.validate_spec(
            {
                "action": "draw",
                "target": "overall_route",
                "source_scope": "text",
            }
        )
        self.assertIn("ask_palette", result["questions"])
        self.assertIn("ask_backend", result["questions"])
        self.assertFalse(result["ready"])

    def test_pending_palette_blocks_work(self):
        result = MODULE.validate_spec(
            {
                "action": "draw",
                "target": "core_module",
                "source_scope": "text",
                "palette_mode": "pending",
                "backend": "wps",
            }
        )
        self.assertIn("wait_palette", result["questions"])
        self.assertFalse(result["ready"])

    def test_custom_and_reference_palette_require_sources(self):
        custom = MODULE.validate_spec(
            {
                "action": "draw",
                "target": "branch_route",
                "source_scope": "text",
                "palette_mode": "custom",
                "backend": "powerpoint",
            }
        )
        reference = MODULE.validate_spec(
            {
                "action": "draw",
                "target": "branch_route",
                "source_scope": "text",
                "palette_mode": "reference",
                "backend": "powerpoint",
            }
        )
        self.assertIn("ask_custom_palette", custom["questions"])
        self.assertIn("ask_palette_reference", reference["questions"])


if __name__ == "__main__":
    unittest.main()
