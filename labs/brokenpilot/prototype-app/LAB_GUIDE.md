# BrokenPilot Prototype Lab Guide

## Goal

Use the minimal BrokenPilot prototype to demonstrate how AI application risk emerges from normal application architecture decisions: retrieval authorization, instruction/data separation, logging, tool authorization, and approval placement.

## Prerequisites

- Python 3.11+ or Docker Desktop
- Local checkout of this repository
- No cloud API keys required

## Exercise 1  -  Confirm the app is running

Start the app and visit:

```text
http://127.0.0.1:8010
```

Then check:

```powershell
Invoke-RestMethod http://127.0.0.1:8010/health
```

Expected result:

```text
status: ok
```

## Exercise 2  -  Observe the fake users

```powershell
Invoke-RestMethod http://127.0.0.1:8010/users
```

Identify the tenant and role for:

- `alice`
- `eve`

Discussion question:

> Which user should be able to retrieve Alpha tenant operational documents?

## Exercise 3  -  Trigger a retrieval authorization failure

With default settings, retrieval authorization is disabled.

```powershell
Invoke-RestMethod http://127.0.0.1:8010/retrieve `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"user_id":"eve","query":"payment api credential rotation token","top_k":3}'
```

Expected vulnerable behavior:

- Eve is a Beta tenant contractor.
- The result may include Alpha tenant restricted content.
- This is not an ML problem. It is an authorization problem in the retrieval layer.

Root cause:

> The retrieval service is allowed to search the corpus before enforcing tenant and role constraints.

## Exercise 4  -  Trigger indirect prompt injection

Use Alice:

```powershell
Invoke-RestMethod http://127.0.0.1:8010/chat `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"user_id":"alice","message":"vendor onboarding incident token runbook","top_k":4}'
```

Expected vulnerable behavior:

- A malicious vendor-style document may be retrieved.
- The mock LLM treats the malicious retrieved instruction as authoritative.
- The response is marked with `VULNERABLE_BEHAVIOR_DETECTED`.

Root cause:

> Retrieved content is untrusted data, but the model layer treats it like an instruction source.

### Important note about the mock prompt-injection filter

`ENABLE_PROMPT_INJECTION_FILTER` is a deterministic teaching toggle. In this prototype it detects obvious marker strings such as `MALICIOUS_INSTRUCTION:`, `IGNORE_PREVIOUS_INSTRUCTIONS:`, and `SYSTEM_OVERRIDE:`. That marker detection is **not** a production security control. It is intentionally simple so students can observe the difference between vulnerable and controlled branches.

The real control is architectural:

- separate instructions from retrieved data,
- enforce retrieval authorization before context reaches the model,
- reduce model and agent privileges,
- keep tool authorization outside the model,
- validate and constrain outputs before use, and
- test the system with adversarial retrieved content.

Signature or keyword filters can be useful as telemetry or one weak layer, but they are trivially bypassable and should never be the primary security boundary.

## Exercise 5  -  Trigger a tool confused-deputy failure

Reset the lab state:

```powershell
Invoke-RestMethod http://127.0.0.1:8010/reset -Method Post
```

Then use Alice, an Alpha tenant ops user, to update a Beta tenant ticket:

```powershell
Invoke-RestMethod http://127.0.0.1:8010/tools/update-ticket `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"user_id":"alice","ticket_id":"TCK-2001","status":"closed","note":"training update from alpha user to beta ticket"}'
```

Expected vulnerable behavior:

- The ticket update succeeds.
- The response says `authorization_decision` is `not_checked`.
- A user from one tenant updated a ticket from another tenant.

Root cause:

> The tool trusts that the caller or model already made the correct authorization decision. The tool itself does not enforce the security property.

## Exercise 6  -  Simulate an agent tool call

```powershell
Invoke-RestMethod http://127.0.0.1:8010/agent/run `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"user_id":"alice","goal":"Resolve the vendor onboarding issue and close TCK-2001"}'
```

Expected vulnerable behavior:

- The agent simulation extracts the ticket id from the goal.
- The agent calls the update-ticket tool.
- The cross-tenant update succeeds unless tool controls are enabled.

Discussion question:

> Should the model, the agent orchestrator, the tool, or an external policy engine enforce this decision?

Strong answer:

> The tool and/or policy layer must enforce it. The model may help interpret intent, but it must not be the authority for authorization.

## Exercise 7  -  Turn controls on

Stop the app and restart with controls enabled.

PowerShell local run:

```powershell
$env:ENABLE_RETRIEVAL_AUTHZ="true"
$env:ENABLE_PROMPT_INJECTION_FILTER="true"
$env:ENABLE_TOOL_AUTHZ="true"
$env:ENABLE_TOOL_APPROVAL="true"
uvicorn app.main:app --reload --host 127.0.0.1 --port 8010
```

Docker Compose run:

Edit `.env` or set the variables in `docker-compose.yml`, then:

```powershell
docker compose up --build
```

Repeat Exercises 3, 4, 5, and 6.

Expected improved behavior:

- Eve should not retrieve Alpha restricted documents.
- Retrieved malicious instructions should be treated as untrusted data.
- Cross-tenant tool updates should be blocked.
- Workflow-ending tool updates should require approval.

## Exercise 8  -  Write the findings

Students should produce one finding for each issue:

1. Cross-document authorization failure
2. Indirect prompt injection through retrieved document
3. Tool confused-deputy update
4. Missing approval for workflow-ending agent actions

Each finding should include:

- violated security property
- exploit path
- business impact
- root cause
- recommended control
- residual risk

## Instructor notes

This lab is intentionally deterministic. Students should not waste time trying to create clever prompts. The teaching point is that architecture controls must exist outside the model.

Strong answers should mention:

- retrieval authorization
- tenant isolation
- role filtering
- preserving document metadata
- treating retrieved instructions as untrusted content
- tool-level authorization
- approval gates for destructive actions
- auditability
- security properties rather than only model behavior

## Memory poisoning extension

For the Module 07 memory poisoning scenario, use `MEMORY_POISONING_LAB.md` in the runnable prototype app or the website page `memory-poisoning-lab.md`. This extension demonstrates persistent memory as an agent authority source and validates `ENABLE_MEMORY_REVIEW` / `ENABLE_MEMORY_ISOLATION` controls.

## Module 05 additions: direct injection and output handling

BrokenPilot now has two Module 05 flows in addition to the indirect prompt-injection path:

- `DIRECT_PROMPT_INJECTION_LAB.md` shows user-message prompt injection.
- `OUTPUT_HANDLING_LAB.md` shows model-derived text reaching an HTML sink raw unless `ENABLE_OUTPUT_ENCODING=true`.

Direct and indirect injection have the same root cause: untrusted text is treated as instruction. The boundary is different. In direct injection, the text comes from the user message. In indirect injection, the text comes from retrieved content.

The marker strings are deterministic lab stand-ins, not production controls. A real design uses instruction/data separation, privilege reduction, authorization outside the model, and context-appropriate output handling at the sink.
