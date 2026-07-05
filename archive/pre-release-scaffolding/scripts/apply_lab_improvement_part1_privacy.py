from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC_006 = {
    "id": "DOC-006",
    "title": "Alpha On-Call PagerDuty Escalation Contacts",
    "tenant": "alpha",
    "visibility": "restricted",
    "classification": "confidential",
    "allowed_roles": ["ops"],
    "allowed_users": [],
    "tags": ["oncall", "escalation", "contact", "pager", "alpha"],
    "training_secret": "FAKE-ALPHA-ONCALL-PHONE-000-000",
    "body": "Alpha on-call escalation contacts. Fake training-only sensitive fragment: FAKE-ALPHA-ONCALL-PHONE-000-000. Restricted to Alpha ops.",
}

PRIVACY_LAB = r"""# Lab - BrokenPilot Cross-Tenant Privacy Leakage

## Purpose

Make Module 09 observable with the BrokenPilot prototype.

Students will show that a beta tenant user can retrieve alpha tenant restricted documents when retrieval authorization is disabled, then enable the control and verify that the privacy property changes.

This lab uses only fake local data. Do not run these steps against real systems or real tenant data.

## Lab class

Attack lab.

This lab should clear the same standard used by the stronger BrokenPilot labs:

1. Observable failure and observable fix.
2. The graded artifact is the control and validation, not the leak.
3. The naive fix is rejected.
4. There is a defense-in-depth moment.
5. The decision maps to a real engineering design choice.
6. The lab is deterministic and resettable.

## System under test

BrokenPilot is a fake internal AI operations assistant with users, tenants, documents, retrieval, chat, memory, audit events, and ticket-update tools.

Relevant fake users:

| User | Tenant | Role |
|---|---|---|
| `alice` | alpha | ops |
| `chris` | beta | viewer |
| `eve` | beta | contractor |

Relevant fake documents:

| Document | Tenant | Classification | Why it matters |
|---|---|---|---|
| `DOC-002` | alpha | restricted | Contains `FAKE-ALPHA-PAYMENT-TOKEN-DO-NOT-USE` |
| `DOC-006` | alpha | confidential | Contains `FAKE-ALPHA-ONCALL-PHONE-000-000` |

Expected security property:

> A beta viewer must not retrieve alpha restricted or confidential documents, even if the query text matches document tags.

## Setup

From the prototype directory:

```powershell
cd labs\brokenpilot\prototype-app
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8010
```

macOS or Linux:

```bash
cd labs/brokenpilot/prototype-app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8010
```

Reset lab state:

```powershell
Invoke-RestMethod -Method Post http://127.0.0.1:8010/reset
```

## Step 1: Observe the vulnerable behavior

Keep retrieval authorization disabled. This is the default vulnerable mode.

PowerShell:

```powershell
$body = @{
  user_id = "chris"
  query = "payment credential token alpha"
  top_k = 5
} | ConvertTo-Json

Invoke-RestMethod -Method Post http://127.0.0.1:8010/retrieve -ContentType "application/json" -Body $body
```

curl:

```bash
curl -s http://127.0.0.1:8010/retrieve \
  -H 'Content-Type: application/json' \
  -d '{"user_id":"chris","query":"payment credential token alpha","top_k":5}'
```

Expected vulnerable observation:

```text
user: chris
tenant: beta
retrieved document: DOC-002
retrieved document tenant: alpha
fake sensitive fragment: FAKE-ALPHA-PAYMENT-TOKEN-DO-NOT-USE
```

This is a privacy failure and a tenant isolation failure. The model is not the primary boundary here. The retrieval layer returned data the user should never have received.

## Step 2: Enable retrieval authorization

PowerShell:

```powershell
$env:ENABLE_RETRIEVAL_AUTHZ = "true"
```

macOS or Linux:

```bash
export ENABLE_RETRIEVAL_AUTHZ=true
```

Run the same request again:

```powershell
$body = @{
  user_id = "chris"
  query = "payment credential token alpha"
  top_k = 5
} | ConvertTo-Json

Invoke-RestMethod -Method Post http://127.0.0.1:8010/retrieve -ContentType "application/json" -Body $body
```

Expected controlled observation:

```text
DOC-002 is not returned
DOC-006 is not returned
alpha restricted or confidential documents are not returned to the beta viewer
```

The control changes the security property because authorization is applied before documents become model context.

## Step 3: Reject the naive fix

A weak proposed fix is:

```text
Tell the model not to reveal secrets or other tenants' data.
```

That is not sufficient.

Why it fails:

- the restricted document has already crossed the trust boundary;
- the model may summarize, transform, or quote the content;
- downstream logs or tools may store the retrieved content;
- prompt instructions do not enforce tenant authorization;
- the user can still infer that a restricted document exists.

The real fix is to prevent unauthorized documents from being retrieved in the first place.

## Step 4: Defense-in-depth moment

Enable audit logging and repeat the vulnerable request:

```powershell
$env:ENABLE_RETRIEVAL_AUTHZ = "false"
$env:ENABLE_AUDIT_LOG = "true"

$body = @{
  user_id = "chris"
  query = "payment credential token alpha"
  top_k = 5
} | ConvertTo-Json

Invoke-RestMethod -Method Post http://127.0.0.1:8010/retrieve -ContentType "application/json" -Body $body
Invoke-RestMethod http://127.0.0.1:8010/audit
```

Observation:

The audit log records the user, query, retrieved document IDs, and controls. Even when a log does not store full document bodies, privacy-sensitive facts can appear in telemetry:

- a user's sensitive query;
- document identifiers;
- tenant-crossing access attempts;
- evidence that a restricted topic exists.

Design implication:

Retrieval authorization is necessary, but not enough. Production systems also need log minimization, redaction, access control, retention limits, and incident review procedures.

## Student deliverable

Write a short privacy finding with the following sections:

1. Affected security property.
2. Evidence from vulnerable mode.
3. Root cause.
4. Why prompt-only mitigation is insufficient.
5. Implementable control.
6. Validation result after enabling retrieval authorization.
7. Residual risk, including logging and telemetry.

## Strong finding anchor

```text
Finding: Cross-tenant retrieval authorization failure exposes alpha restricted documents to beta users.

Evidence: With retrieval authorization disabled, beta user chris can query for "payment credential token alpha" and retrieve DOC-002, an alpha restricted document containing the fake training token FAKE-ALPHA-PAYMENT-TOKEN-DO-NOT-USE.

Root cause: The retrieval layer ranks all documents before enforcing tenant and role authorization. Authorization is not applied before context is returned to the application.

Control: Enforce document authorization inside the retrieval service before ranking results are returned to the model or caller. Authorization must check tenant, visibility, allowed roles, and allowed users.

Validation: With ENABLE_RETRIEVAL_AUTHZ=true, the same request no longer returns DOC-002 or DOC-006 to chris.

Residual risk: Audit logs may still expose sensitive query text, document IDs, or attempted cross-tenant access patterns. Logs need minimization, retention limits, and restricted access.
```

## Weak finding anchor

```text
The AI leaked a secret. Add better guardrails and tell it not to reveal tokens.
```

Why this is weak:

- it blames the model instead of the retrieval boundary;
- it gives no tenant, user, document, or control evidence;
- it does not specify where authorization must be enforced;
- it has no validation method;
- it ignores telemetry residual risk.

## Reset

PowerShell:

```powershell
Remove-Item Env:\ENABLE_RETRIEVAL_AUTHZ -ErrorAction SilentlyContinue
Remove-Item Env:\ENABLE_AUDIT_LOG -ErrorAction SilentlyContinue
Invoke-RestMethod -Method Post http://127.0.0.1:8010/reset
```

macOS or Linux:

```bash
unset ENABLE_RETRIEVAL_AUTHZ
unset ENABLE_AUDIT_LOG
curl -s -X POST http://127.0.0.1:8010/reset
```
"""

RELEASE_NOTE = """# v1.1-dev Lab Improvement Part 1 and Privacy Lab

This package follows the BrokenPilot and Labs Improvement Plan sequencing.

Implemented:

- Removed two self-study dead ends by rewording labs that referenced data not yet shipped.
- Aligned the Module 07 worked example with BrokenPilot seed data: Eve is beta / contractor.
- Added a runnable Module 09 BrokenPilot privacy lab for cross-tenant retrieval leakage.
- Added a second alpha confidential fake document so the privacy leak is not a single-document coincidence.
- Added BrokenPilot pytest coverage for vulnerable and controlled privacy retrieval behavior.

Not included yet:

- Direct prompt injection.
- Insecure output handling.
- Toy classifier app for Modules 03 and 10.
- MLOps evidence pack.
- Strict MkDocs release cleanup.
"""

CHECK_SCRIPT = r'''from __future__ import annotations

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
'''


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def replace_if_present(path: Path, old: str, new: str) -> bool:
    if not path.exists():
        print(f"skip missing: {path.relative_to(ROOT)}")
        return False
    text = read(path)
    if old not in text:
        return False
    write(path, text.replace(old, new))
    print(f"updated: {path.relative_to(ROOT)}")
    return True


def ensure_contains(path: Path, marker: str, insert: str, after: str | None = None) -> None:
    if not path.exists():
        print(f"skip missing: {path.relative_to(ROOT)}")
        return
    text = read(path)
    if marker in text:
        return
    if after and after in text:
        text = text.replace(after, after + insert, 1)
    else:
        text = text.rstrip() + "\n\n" + insert.lstrip("\n")
    write(path, text)
    print(f"updated: {path.relative_to(ROOT)}")


def fix_module07_eve_role() -> None:
    path = ROOT / "modules/07-agent-tool-security/worked-example.md"
    replace_if_present(path, "| Eve | beta | ops |", "| Eve | beta | contractor |")


def fix_toy_ml_lab_text() -> None:
    path = ROOT / "labs/toy-ml-attacks/classical-ml-attack-lab.md"
    old = """## Suggested toy-code extension

In a local notebook, students can implement a tiny classifier using a small synthetic dataset.

Suggested safe exercises:

- Train a spam/not-spam classifier on toy messages.
- Change a few words and observe prediction changes.
- Flip a small number of labels and observe behavior changes.
- Compare predictions before and after poisoning.
"""
    new = """## Current self-study mode

Until the dedicated toy classifier app is added, this lab is a tabletop exercise.

Do not tell students that a dataset or classifier is already provided. Students may either stay in tabletop mode or create a small synthetic dataset with this schema:

```json
{
  "id": "msg-001",
  "text": "fake training message using synthetic words only",
  "label": "spam"
}
```

Allowed labels for self-created data:

- `spam`
- `not_spam`

Safe exercises:

- train a local classifier on synthetic messages;
- change a few synthetic words and observe prediction changes;
- flip a small number of labels and observe behavior changes;
- compare predictions before and after poisoning.

The planned `labs/toy-ml-attacks/toy-classifier-app/` will replace this section with concrete scripts and a shipped dataset.
"""
    if not replace_if_present(path, old, new):
        ensure_contains(
            path,
            "## Current self-study mode",
            "\n" + new,
            after="## Suggested toy-code extension\n",
        )


def fix_evasion_lab_text() -> None:
    path = ROOT / "labs/adversarial-ml-labs/evasion-robustness-lab.md"
    if not path.exists():
        print(f"skip missing: {path.relative_to(ROOT)}")
        return
    text = read(path)
    text = text.replace(
        "Students receive a small fake dataset and a set of example messages. The objective is not to attack a real email system. The objective is to understand how small controlled input changes can produce different model outcomes.",
        "For now, students create a small fake dataset from the schema below or use the dedicated toy-classifier dataset once `labs/toy-ml-attacks/toy-classifier-app/data/messages.json` is added. The objective is not to attack a real email system. The objective is to understand how small controlled input changes can produce different model outcomes.",
    )
    if "## Synthetic data schema" not in text:
        marker = "## Architecture\n"
        insert = """
## Synthetic data schema

Until the toy-classifier app is added, use fake local records with this schema:

```json
{
  "id": "msg-001",
  "text": "synthetic phishing-like message for training only",
  "label": "high"
}
```

Allowed labels:

- `low`
- `medium`
- `high`

Do not use real phishing emails, real customer data, or real URLs.

"""
        text = text.replace(marker, insert + marker, 1)
    write(path, text)
    print(f"updated: {path.relative_to(ROOT)}")


def add_doc_006() -> None:
    path = ROOT / "labs/brokenpilot/prototype-app/data/documents.json"
    if not path.exists():
        print(f"skip missing: {path.relative_to(ROOT)}")
        return
    docs = json.loads(read(path))
    if any(doc.get("id") == "DOC-006" for doc in docs):
        return
    docs.append(DOC_006)
    write(path, json.dumps(docs, indent=2) + "\n")
    print(f"updated: {path.relative_to(ROOT)}")


def add_privacy_lab() -> None:
    path = ROOT / "labs/privacy-labs/brokenpilot-cross-tenant-leakage-lab.md"
    write(path, PRIVACY_LAB)
    print(f"wrote: {path.relative_to(ROOT)}")


def update_privacy_readme() -> None:
    path = ROOT / "labs/privacy-labs/README.md"
    marker = "brokenpilot-cross-tenant-leakage-lab.md"
    insert = "| `brokenpilot-cross-tenant-leakage-lab.md` | Runnable BrokenPilot lab showing cross-tenant retrieval leakage and the retrieval authorization fix. |\n"
    if not path.exists():
        return
    text = read(path)
    if marker in text:
        return
    if "| Lab | Purpose |" in text:
        lines = text.splitlines()
        out = []
        inserted = False
        for line in lines:
            out.append(line)
            if not inserted and line.strip() == "|---|---|":
                out.append(insert.rstrip())
                inserted = True
        write(path, "\n".join(out) + "\n")
    else:
        write(path, text.rstrip() + "\n\n" + insert)
    print(f"updated: {path.relative_to(ROOT)}")


def update_module09_readme() -> None:
    path = ROOT / "modules/09-privacy-attacks/README.md"
    marker = "labs/privacy-labs/brokenpilot-cross-tenant-leakage-lab.md"
    if not path.exists():
        return
    text = read(path)
    if marker in text:
        return
    old = """See:

- `labs/privacy-labs/privacy-leakage-cross-tenant-rag-lab.md`
- `labs/privacy-labs/membership-inference-model-inversion-tabletop.md`
"""
    new = """See:

- `labs/privacy-labs/brokenpilot-cross-tenant-leakage-lab.md`
- `labs/privacy-labs/privacy-leakage-cross-tenant-rag-lab.md`
- `labs/privacy-labs/membership-inference-model-inversion-tabletop.md`
"""
    if old in text:
        text = text.replace(old, new, 1)
    else:
        text = text.rstrip() + "\n\nRunnable BrokenPilot privacy lab:\n\n- `labs/privacy-labs/brokenpilot-cross-tenant-leakage-lab.md`\n"
    write(path, text)
    print(f"updated: {path.relative_to(ROOT)}")


def add_privacy_tests() -> None:
    path = ROOT / "labs/brokenpilot/prototype-app/tests/test_basic.py"
    if not path.exists():
        print(f"skip missing: {path.relative_to(ROOT)}")
        return
    text = read(path)
    if "test_privacy_cross_tenant_retrieval_leaks_when_authz_disabled" in text:
        return
    addition = r'''


def test_privacy_cross_tenant_retrieval_leaks_when_authz_disabled():
    response = client.post(
        "/retrieve",
        json={"user_id": "chris", "query": "payment credential token alpha", "top_k": 5},
    )
    assert response.status_code == 200
    body = response.json()
    doc_ids = [doc["id"] for doc in body["documents"]]
    assert "DOC-002" in doc_ids
    leaked_doc = next(doc for doc in body["documents"] if doc["id"] == "DOC-002")
    assert leaked_doc["tenant"] == "alpha"
    assert leaked_doc["training_secret"] == "FAKE-ALPHA-PAYMENT-TOKEN-DO-NOT-USE"


def test_privacy_cross_tenant_retrieval_blocks_when_authz_enabled(monkeypatch):
    monkeypatch.setenv("ENABLE_RETRIEVAL_AUTHZ", "true")
    response = client.post(
        "/retrieve",
        json={"user_id": "chris", "query": "payment credential token alpha oncall pager", "top_k": 5},
    )
    assert response.status_code == 200
    body = response.json()
    doc_ids = [doc["id"] for doc in body["documents"]]
    assert "DOC-002" not in doc_ids
    assert "DOC-006" not in doc_ids
    assert all(doc.get("tenant") in {"beta", "global"} for doc in body["documents"])
    monkeypatch.delenv("ENABLE_RETRIEVAL_AUTHZ", raising=False)
'''
    write(path, text.rstrip() + addition + "\n")
    print(f"updated: {path.relative_to(ROOT)}")


def write_support_files() -> None:
    write(ROOT / "release-notes/v1.1-dev-lab-improvement-part1-privacy.md", RELEASE_NOTE)
    write(ROOT / "scripts/check_lab_improvement_part1_privacy.py", CHECK_SCRIPT)
    print("wrote support files")


def main() -> None:
    fix_module07_eve_role()
    fix_toy_ml_lab_text()
    fix_evasion_lab_text()
    add_doc_006()
    add_privacy_lab()
    update_privacy_readme()
    update_module09_readme()
    add_privacy_tests()
    write_support_files()
    print("\nApplied lab improvement Part 1 and Module 09 privacy lab package.")


if __name__ == "__main__":
    main()
