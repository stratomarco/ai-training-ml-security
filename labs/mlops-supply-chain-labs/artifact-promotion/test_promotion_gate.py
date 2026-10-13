import json
import tempfile
import unittest
from pathlib import Path

from promotion_gate import ROOT, evaluate


FIXTURES = ROOT / "fixtures"


class PromotionGateTests(unittest.TestCase):
    def test_approved_artifact_passes(self):
        report = evaluate(FIXTURES / "approved-v1.weights.json", FIXTURES / "approved-v1.manifest.json")
        self.assertEqual(report["decision"], "allow")
        self.assertTrue(all(report["checks"].values()))

    def test_changed_artifact_fails_both_integrity_checks(self):
        report = evaluate(FIXTURES / "tampered-v1.weights.json", FIXTURES / "approved-v1.manifest.json")
        self.assertEqual(report["decision"], "deny")
        self.assertFalse(report["checks"]["manifest_matches_artifact"])
        self.assertFalse(report["checks"]["artifact_digest_is_approved"])

    def test_internally_consistent_unapproved_candidate_still_fails_policy(self):
        report = evaluate(FIXTURES / "unapproved-v2.weights.json", FIXTURES / "unapproved-v2.manifest.json")
        self.assertEqual(report["decision"], "deny")
        self.assertTrue(report["checks"]["manifest_matches_artifact"])
        self.assertFalse(report["checks"]["revision_is_approved"])

    def test_unapproved_format_and_missing_candidate_fail_closed(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            changed = json.loads((FIXTURES / "approved-v1.manifest.json").read_text(encoding="utf-8"))
            changed["artifact_format"] = "pickle"
            manifest = Path(directory) / "changed.manifest.json"
            manifest.write_text(json.dumps(changed), encoding="utf-8")
            report = evaluate(FIXTURES / "approved-v1.weights.json", manifest)
            self.assertEqual(report["decision"], "deny")
            self.assertFalse(report["checks"]["format_is_allowed"])
            self.assertEqual(evaluate(Path(directory) / "missing", manifest)["decision"], "deny")

    def test_invalid_trusted_policy_is_an_error_not_an_allow(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            policy = Path(directory) / "policy.json"
            policy.write_text("{}", encoding="utf-8")
            report = evaluate(FIXTURES / "approved-v1.weights.json", FIXTURES / "approved-v1.manifest.json", policy_path=policy)
            self.assertEqual(report["decision"], "error")


if __name__ == "__main__":
    unittest.main()
