# BrokenPilot Standalone Lab: LLM Application Security

This lab replaces or complements the DVAIA Module 05 lab when an instructor wants a deterministic local target.

## Learning objective

Students must distinguish prompt text from security control. The lab demonstrates that model-facing instructions can be influenced by attacker-controlled context and that a marker filter is only a teaching stand-in, not a real control.

## Setup

Start BrokenPilot:

Windows PowerShell:

```powershell
cd labs\brokenpilot\prototype-app
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --host 127.0.0.1 --port 8010
```

macOS or Linux:

```bash
cd labs/brokenpilot/prototype-app
source .venv/bin/activate
uvicorn app.main:app --reload --host 127.0.0.1 --port 8010
```

Reset lab state:

```powershell
Invoke-RestMethod http://127.0.0.1:8010/reset -Method Post
```

## Step 1: run the vulnerable chat flow

PowerShell:

```powershell
Invoke-RestMethod http://127.0.0.1:8010/chat `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"user_id":"alice","message":"vendor onboarding incident token runbook","top_k":4}'
```

Expected evidence:

```text
mode: vulnerable
VULNERABLE_BEHAVIOR_DETECTED
security_observation: Retrieved content was treated as instruction.
```

## Step 2: enable the deterministic teaching control

PowerShell:

```powershell
$env:ENABLE_PROMPT_INJECTION_FILTER="true"
```

Run the same request again.

Expected evidence:

```text
mode: controlled
security_observation: Instruction/data separation control was applied.
```

## Required student explanation

Students must not write that the control is signature detection. The lab uses marker matching only to make the result deterministic.

A good explanation says:

```text
The application must treat retrieved content as untrusted data. Filtering exact phrases is bypassable and is not a sufficient security control. The stronger control is architectural: separate instruction channels, limit what generated output can cause, enforce policy outside the model, and test that retrieved documents cannot become authority.
```

## Deliverable

Write one finding with:

- evidence from vulnerable and controlled runs;
- root cause;
- violated security property;
- control recommendation;
- validation method;
- residual risk.
