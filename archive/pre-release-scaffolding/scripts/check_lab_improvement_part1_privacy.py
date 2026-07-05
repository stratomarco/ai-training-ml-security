from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

required_files = [
    ROOT / "labs/privacy-labs/brokenpilot-cross-tenant-leakage-lab.md",
    ROOT / "labs/brokenpilot/prototype-app/tests/test_basic.py",
    ROOT / "labs/brokenpilot/prototype-app/data/documents.json",
]

missing = [path for path in required_files if not path.exists()]
if missing:
    raise SystemExit("Missing required files: " + ", ".join(str(p.relative_to(ROOT)) for p in missing))

with (ROOT / "labs/brokenpilot/prototype-app/data/documents.json").open("r", encoding="utf-8") as f:
    docs = json.load(f)

doc_ids = {doc.get("id") for doc in docs}
if "DOC-002" not in doc_ids or "DOC-006" not in doc_ids:
    raise SystemExit("DOC-002 and DOC-006 must both exist in BrokenPilot documents.json")

tests = (ROOT / "labs/brokenpilot/prototype-app/tests/test_basic.py").read_text(encoding="utf-8")
expected_tests = [
    "test_privacy_cross_tenant_retrieval_leaks_when_authz_disabled",
    "test_privacy_cross_tenant_retrieval_blocks_when_authz_enabled",
]
for name in expected_tests:
    if name not in tests:
        raise SystemExit(f"Missing privacy regression test: {name}")

worked = ROOT / "modules/07-agent-tool-security/worked-example.md"
if worked.exists():
    text = worked.read_text(encoding="utf-8")
    if "| Eve | beta | ops |" in text:
        raise SystemExit("Module 07 worked example still lists Eve as beta / ops")

print("Lab improvement Part 1 and privacy checks passed.")
