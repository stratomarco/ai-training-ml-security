"""Offline teaching gate for fake model-artifact promotion.

Only hashes artifact bytes. It never deserializes or executes the artifact.
The checked-in policy stands in for a separately protected approval record.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TRUSTED_POLICY = ROOT / "trusted_policy.json"
MAX_ARTIFACT_BYTES = 1024 * 1024
MAX_METADATA_BYTES = 16 * 1024
MANIFEST_FIELDS = {
    "model_id", "revision", "artifact_format", "artifact_sha256", "source_commit", "dataset_id"
}
POLICY_FIELDS = {
    "model_id", "approved_revision", "allowed_format", "approved_artifact_sha256",
    "approved_source_commit", "approved_dataset_id"
}


def _read_bounded(path: Path, limit: int) -> bytes:
    with path.open("rb") as stream:
        data = stream.read(limit + 1)
    if len(data) > limit:
        raise ValueError("input_too_large")
    return data


def _read_record(path: Path, required_fields: set[str]) -> dict[str, str]:
    raw = _read_bounded(path, MAX_METADATA_BYTES)
    value = json.loads(raw.decode("utf-8"))
    if not isinstance(value, dict) or set(value) != required_fields:
        raise ValueError("invalid_metadata_fields")
    if any(not isinstance(item, str) or not item or len(item) > 200 for item in value.values()):
        raise ValueError("invalid_metadata_value")
    return value


def evaluate(artifact: Path, manifest: Path, *, policy_path: Path = TRUSTED_POLICY) -> dict:
    try:
        policy = _read_record(policy_path, POLICY_FIELDS)
    except (OSError, ValueError, UnicodeError, json.JSONDecodeError):
        return {"decision": "error", "reason": "trusted_policy_invalid", "checks": {}}

    try:
        manifest_data = _read_record(manifest, MANIFEST_FIELDS)
        artifact_bytes = _read_bounded(artifact, MAX_ARTIFACT_BYTES)
    except (OSError, ValueError, UnicodeError, json.JSONDecodeError):
        return {"decision": "deny", "reason": "candidate_unreadable_or_invalid", "checks": {}}

    actual_digest = hashlib.sha256(artifact_bytes).hexdigest()
    checks = {
        "manifest_matches_artifact": manifest_data["artifact_sha256"] == actual_digest,
        "model_is_approved": manifest_data["model_id"] == policy["model_id"],
        "revision_is_approved": manifest_data["revision"] == policy["approved_revision"],
        "format_is_allowed": manifest_data["artifact_format"] == policy["allowed_format"],
        "artifact_digest_is_approved": actual_digest == policy["approved_artifact_sha256"],
        "source_is_approved": manifest_data["source_commit"] == policy["approved_source_commit"],
        "dataset_is_approved": manifest_data["dataset_id"] == policy["approved_dataset_id"],
    }
    return {
        "decision": "allow" if all(checks.values()) else "deny",
        "checks": checks,
        "artifact_sha256": actual_digest,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact", type=Path, default=ROOT / "fixtures" / "approved-v1.weights.json")
    parser.add_argument("--manifest", type=Path, default=ROOT / "fixtures" / "approved-v1.manifest.json")
    args = parser.parse_args()
    report = evaluate(args.artifact, args.manifest)
    print(json.dumps(report, indent=2))
    return 0 if report["decision"] == "allow" else 2 if report["decision"] == "error" else 1


if __name__ == "__main__":
    raise SystemExit(main())
