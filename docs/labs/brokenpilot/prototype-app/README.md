# BrokenPilot Prototype App

This directory contains the minimal runnable BrokenPilot prototype.

It is intentionally small and deterministic. The goal is to make the BrokenPilot capstone testable without requiring a real LLM, cloud account, vector database, ticketing system, or production-like integrations.

## What this prototype demonstrates

The current MVP supports these endpoints:

| Endpoint | Purpose |
|---|---|
| `GET /health` | Confirm the app is running |
| `GET /users` | List fake users available for testing |
| `GET /tickets` | List fake tickets |
| `GET /controls` | Show active control toggles |
| `GET /audit` | Show in-memory audit events |
| `POST /reset` | Reset mutable lab state |
| `POST /retrieve` | Retrieve fake documents using keyword matching |
| `POST /chat` | Run a mock chat flow over retrieved documents |
| `POST /tools/update-ticket` | Simulate an agent/tool ticket update |
| `POST /agent/run` | Simulate a simple agent that may call the update-ticket tool |

The prototype demonstrates these BrokenPilot vulnerabilities:

| ID | Vulnerability | Status |
|---|---|---|
| BP-MVP-01 | Direct/model-instruction confusion in mock chat | Implemented through deterministic mock behavior |
| BP-MVP-02 | Indirect prompt injection through retrieved document | Implemented through malicious retrieved document content |
| BP-MVP-03 | Cross-document authorization failure | Implemented with `ENABLE_RETRIEVAL_AUTHZ=false` |
| BP-MVP-04 | Tool confused-deputy update | Implemented with `ENABLE_TOOL_AUTHZ=false` |
| BP-MVP-05 | Missing approval for workflow-ending tool actions | Implemented with `ENABLE_TOOL_APPROVAL=false` |

Memory poisoning is not implemented yet. It is planned for the next prototype increment.

## Safety model

This is a local training app. It uses:

- fake users
- fake documents
- fake tickets
- fake secrets
- deterministic mock LLM behavior
- no external network calls
- no real credentials
- no real ticketing system
- no real model provider

Do not connect this prototype to real systems or real data.

## Run locally on Windows PowerShell

From the repository root:

```powershell
cd labs\brokenpilot\prototype-app
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8010
```

Open:

```text
http://127.0.0.1:8010
```

## Run with Docker Compose

```powershell
cd labs\brokenpilot\prototype-app
docker compose up --build
```

Open:

```text
http://127.0.0.1:8010
```

Stop:

```powershell
docker compose down
```

## Control toggles

The app uses environment variables to demonstrate vulnerable and hardened behavior.

| Toggle | Default | Meaning |
|---|---:|---|
| `ENABLE_RETRIEVAL_AUTHZ` | `false` | If true, retrieved documents are filtered by tenant and role |
| `ENABLE_PROMPT_INJECTION_FILTER` | `false` | If true, retrieved instructions are treated as untrusted data |
| `ENABLE_TOOL_AUTHZ` | `false` | If true, ticket-update tools enforce tenant and role authorization |
| `ENABLE_TOOL_APPROVAL` | `false` | If true, workflow-ending ticket updates require explicit approval |
| `ENABLE_AUDIT_LOG` | `true` | If true, relevant actions are recorded in memory |

Default mode is intentionally vulnerable.

## Recommended demo queries

### Cross-document authorization failure

Use user:

```text
user_id: eve
```

Query:

```text
payment api credential rotation token
```

With `ENABLE_RETRIEVAL_AUTHZ=false`, Eve may retrieve Alpha tenant documents that she should not see.

With `ENABLE_RETRIEVAL_AUTHZ=true`, Eve should not retrieve Alpha-only documents.

### Indirect prompt injection

Use user:

```text
user_id: alice
```

Query:

```text
vendor onboarding incident token runbook
```

With default vulnerable settings, the retrieval step may include a malicious vendor document. The mock LLM will demonstrate unsafe behavior by treating a retrieved document instruction as authoritative.

With `ENABLE_PROMPT_INJECTION_FILTER=true`, the mock LLM treats retrieved instructions as data and reports that they were ignored.

### Tool confused-deputy update

Use Alpha ops user Alice to update a Beta tenant ticket:

```powershell
Invoke-RestMethod http://127.0.0.1:8010/tools/update-ticket `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"user_id":"alice","ticket_id":"TCK-2001","status":"closed","note":"training update"}'
```

With `ENABLE_TOOL_AUTHZ=false`, the update succeeds even though Alice belongs to the Alpha tenant and the ticket belongs to Beta.

With `ENABLE_TOOL_AUTHZ=true`, the update is blocked.

### Agent tool call simulation

```powershell
Invoke-RestMethod http://127.0.0.1:8010/agent/run `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"user_id":"alice","goal":"Resolve the vendor onboarding issue and close TCK-2001"}'
```

This simulates an agent deciding to call a tool as part of a user goal.

## API examples

### Health

```powershell
Invoke-RestMethod http://127.0.0.1:8010/health
```

### Users

```powershell
Invoke-RestMethod http://127.0.0.1:8010/users
```

### Retrieve

```powershell
Invoke-RestMethod http://127.0.0.1:8010/retrieve `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"user_id":"eve","query":"payment api credential rotation token","top_k":3}'
```

### Chat

```powershell
Invoke-RestMethod http://127.0.0.1:8010/chat `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"user_id":"alice","message":"vendor onboarding incident token runbook","top_k":4}'
```

### Reset lab state

```powershell
Invoke-RestMethod http://127.0.0.1:8010/reset -Method Post
```

## Test

```powershell
pytest
```

## Current limitations

- Retrieval is keyword-based, not vector search.
- The LLM is deterministic mock logic, not a real model.
- There is no persistent database.
- Tool calling is deterministic and local only.
- Memory poisoning is not implemented yet.
- The UI is intentionally basic.

These limitations are deliberate. The goal is a reliable teaching target before adding complexity.
