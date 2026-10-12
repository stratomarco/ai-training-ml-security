# Lab - BrokenPilot Cross-Tenant Privacy Leakage

## Purpose

Make Module 09 observable with the BrokenPilot prototype.

Students will show that a beta tenant user can retrieve alpha tenant restricted documents when retrieval authorization is disabled, then enable the control and verify that the privacy property changes.

This lab uses only fake local data. Do not run these steps against real systems or real tenant data.

## Lab class

Attack lab.

This lab should clear the same standard used by the stronger BrokenPilot labs:

1. Observable failure and observable fix.
2. The practice artifact explains the control and its validation, not only the leak.
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
python run_lab.py --profile vulnerable
```

macOS or Linux:

```bash
cd labs/brokenpilot/prototype-app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run_lab.py --profile vulnerable
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

Stop the vulnerable server with `Ctrl+C`, then restart it from the prototype directory:

```powershell
python run_lab.py --profile retrieval-authz
```

Confirm `ENABLE_RETRIEVAL_AUTHZ: true` at `GET /controls` before repeating the request. Changing an environment variable in another shell while the server remains running does not switch the active control.

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

Stop the controlled server and restart with `python run_lab.py --profile vulnerable`. Audit logging is enabled by this launcher. Repeat the vulnerable request:

```powershell
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

Use `POST /reset` to clear fake tickets, memory, and audit events within the running profile. Stop the server with `Ctrl+C` before switching profiles.
