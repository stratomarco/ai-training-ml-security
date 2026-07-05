# BrokenPilot Tool Calling Lab

## Purpose

This lab focuses on one specific agent security failure: a tool that trusts the model or orchestrator to make authorization decisions.

The goal is to show why agent tools must enforce their own security rules, even when the model appears to be following a legitimate user goal.

## Scenario

BrokenPilot can update incident tickets. Alice is an Alpha tenant ops user. `TCK-2001` is a Beta tenant ticket.

In the default vulnerable configuration, Alice can update the Beta ticket through the tool endpoint because the tool does not check tenant authorization.

## Start the app

```powershell
cd labs\brokenpilot\prototype-app
uvicorn app.main:app --reload --host 127.0.0.1 --port 8010
```

Open:

```text
http://127.0.0.1:8010
```

## Step 1  -  Reset state

```powershell
Invoke-RestMethod http://127.0.0.1:8010/reset -Method Post
```

## Step 2  -  Inspect users and tickets

```powershell
Invoke-RestMethod http://127.0.0.1:8010/users
Invoke-RestMethod http://127.0.0.1:8010/tickets
```

Confirm:

- `alice` belongs to tenant `alpha`
- `TCK-2001` belongs to tenant `beta`

## Step 3  -  Trigger vulnerable tool behavior

```powershell
Invoke-RestMethod http://127.0.0.1:8010/tools/update-ticket `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"user_id":"alice","ticket_id":"TCK-2001","status":"closed","note":"training update from alpha user to beta ticket"}'
```

Expected result:

- HTTP 200
- `result` is `updated`
- `authorization_decision` is `not_checked`
- ticket status becomes `closed`

## Step 4  -  Trigger the same behavior through the agent simulation

```powershell
Invoke-RestMethod http://127.0.0.1:8010/reset -Method Post

Invoke-RestMethod http://127.0.0.1:8010/agent/run `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"user_id":"alice","goal":"Resolve the vendor onboarding issue and close TCK-2001"}'
```

Expected result:

- `agent_decision` is `tool_call_update_ticket`
- ticket status becomes `closed`
- authorization is still `not_checked`

## Step 5  -  Enable tool authorization

Stop the app and restart with:

```powershell
$env:ENABLE_TOOL_AUTHZ="true"
uvicorn app.main:app --reload --host 127.0.0.1 --port 8010
```

Repeat Step 3.

Expected result:

- HTTP 403
- error is `tool_authorization_denied`
- the response explains that the user must be an ops user in the same tenant as the ticket

## Step 6  -  Enable approval gates

Restart with:

```powershell
$env:ENABLE_TOOL_AUTHZ="true"
$env:ENABLE_TOOL_APPROVAL="true"
uvicorn app.main:app --reload --host 127.0.0.1 --port 8010
```

Now try a same-tenant update as Alice on `TCK-1001`:

```powershell
Invoke-RestMethod http://127.0.0.1:8010/tools/update-ticket `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"user_id":"alice","ticket_id":"TCK-1001","status":"closed","note":"same tenant but no approval"}'
```

Expected result:

- HTTP 403
- error is `approval_required`

Now add the training approval token:

```powershell
Invoke-RestMethod http://127.0.0.1:8010/tools/update-ticket `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"user_id":"alice","ticket_id":"TCK-1001","status":"closed","note":"approved training update","approval_token":"APPROVED-FOR-LAB"}'
```

Expected result:

- HTTP 200
- `approval_decision` is `approved_by_lab_token`

## Security lesson

This is not a prompt-engineering problem. It is a security boundary problem.

A model may help decide what the user is asking for, but it must not be the authority for whether an action is allowed.

Controls should be enforced by:

- the tool implementation
- an external policy engine
- scoped credentials
- per-action authorization checks
- approval workflows
- audit logging

## Student deliverable

Write one finding with:

- title
- affected endpoint
- violated security property
- exploit path
- root cause
- impact
- recommended control
- residual risk

Recommended title:

> Tool confused-deputy allows cross-tenant ticket updates

## Validation record

The validated Module 07 record is maintained in `../../modules/07-agent-tool-security/brokenpilot-tool-validation.md` in the course source and `docs/modules/07-agent-tool-security/brokenpilot-tool-validation.md` in the website mirror.
