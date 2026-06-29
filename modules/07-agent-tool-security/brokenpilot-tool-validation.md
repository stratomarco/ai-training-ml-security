# BrokenPilot Tool Authorization Validation

## Purpose

This validation record belongs in Module 07 because the exercise is about agent and tool security: a model-mediated workflow attempts to update a ticket, but the tool must enforce authorization outside the model.

The point of this validation is to show that the Module 07 lesson is testable:

1. Run BrokenPilot in vulnerable mode.
2. Trigger a cross-tenant tool action.
3. Observe that the tool updates the target without authorization.
4. Enable the authorization control.
5. Repeat the same request.
6. Observe that the control blocks the action.

This turns the module from a paper design exercise into a concrete security exercise: exploit, explain, fix, retest.

## Environment

Validated by: Marco Constantino  
Validation date: 2026-06-29  
Host OS: Windows / PowerShell  
Python version: 3.14.2  
Test result: `7 passed, 1 warning`  
Application path: `labs/brokenpilot/prototype-app`  
Application URL: `http://127.0.0.1:8010`

## Scenario

BrokenPilot has a simulated ticket-update tool.

Alice is an `ops` user in tenant `alpha`.

`TCK-2001` is a ticket in tenant `beta`.

In vulnerable mode, the tool trusts the caller and does not enforce tenant authorization. Alice can update a Beta ticket even though she belongs to Alpha.

This is a tool confused-deputy problem: the agent or workflow causes a privileged tool to act across a boundary without the tool independently verifying whether the action is allowed.

## Validation 1 — Vulnerable mode

### Configuration

```text
ENABLE_TOOL_AUTHZ=False
ENABLE_TOOL_APPROVAL=False
```

### Reset state

```powershell
Invoke-RestMethod http://127.0.0.1:8010/reset -Method Post
```

Observed reset response:

```text
status: reset
```

### Request

```powershell
Invoke-RestMethod http://127.0.0.1:8010/tools/update-ticket `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"user_id":"alice","ticket_id":"TCK-2001","status":"closed","note":"training update from alpha user to beta ticket"}'
```

### Observed result

```text
user.id: alice
user.tenant: alpha
user.role: ops
controls.ENABLE_TOOL_AUTHZ: False
controls.ENABLE_TOOL_APPROVAL: False
tool: update_ticket
result: updated
authorization_decision: not_checked
approval_decision: not_required
ticket.id: TCK-2001
ticket.tenant: beta
ticket.status: closed
```

### Security interpretation

The vulnerable behavior is confirmed.

Alice belongs to tenant `alpha`, but she updated a ticket belonging to tenant `beta`. The tool allowed the update because authorization was not checked at execution time.

The violated security property is tenant isolation / object-level authorization.

The root cause is missing complete mediation at the tool boundary.

## Validation 2 — Controlled mode

### Configuration

Restart the app with tool authorization enabled:

```powershell
$env:ENABLE_TOOL_AUTHZ="true"
uvicorn app.main:app --reload --host 127.0.0.1 --port 8010
```

Expected active control:

```text
ENABLE_TOOL_AUTHZ=True
```

### Request

Run the same cross-tenant update request:

```powershell
try {
  Invoke-RestMethod http://127.0.0.1:8010/tools/update-ticket `
    -Method Post `
    -ContentType "application/json" `
    -Body '{"user_id":"alice","ticket_id":"TCK-2001","status":"closed","note":"training update from alpha user to beta ticket"}'
} catch {
  $_.Exception.Response.StatusCode.value__
  $_.ErrorDetails.Message
}
```

### Observed result

```text
403
{"detail":{"error":"tool_authorization_denied","reason":"User must be an ops user in the same tenant as the ticket.","user_tenant":"alpha","ticket_tenant":"beta","user_role":"ops"}}
```

### Security interpretation

The mitigation is validated.

The same request that succeeded in vulnerable mode is blocked when tool authorization is enabled. The tool now verifies the acting user, role, and target tenant before performing the update.

This demonstrates that the fix is not merely a recommendation in a report. It is an enforceable control.

## Module 07 teaching points

This validation supports the following Module 07 concepts:

| Concept | Validated behavior |
|---|---|
| Model is not the security boundary | The tool must enforce authorization, not the model or prompt. |
| Complete mediation | The tool checks authorization at execution time. |
| Least privilege | Users should only update tickets in their authorized scope. |
| Object-level authorization | The target ticket's tenant must be checked. |
| Confused deputy | The workflow can cause a tool to act on a target the user should not control. |
| Control validation | The same exploit is retested after enabling the control. |
| Evidence quality | The result includes user tenant, ticket tenant, role, status, and decision fields. |

## Student deliverable

Students should produce a finding with:

- title;
- affected endpoint;
- violated security property;
- exploit path;
- evidence from vulnerable mode;
- evidence from controlled mode;
- root cause;
- business impact;
- recommended control;
- residual risk.

Recommended finding title:

> Tool confused-deputy allows cross-tenant ticket updates

## Strong remediation statement

A strong remediation should say more than "add authorization."

It should specify:

- the tool must resolve the authenticated user identity;
- the tool must load the target object;
- the tool must compare the user's tenant and role against the target ticket's tenant and required action;
- the authorization decision must happen inside the tool or an external policy decision point;
- the model must not be trusted to decide whether the action is allowed;
- denied actions must be logged;
- sensitive workflow-ending actions may also require approval.

Example control rule:

```text
Allow update_ticket only when:
  user.role == "ops"
  AND user.tenant == ticket.tenant
  AND ticket.status transition is allowed
  AND approval is present when the action is workflow-ending or destructive
Otherwise deny and log the attempt.
```

## Weak remediation statement

A weak remediation would be:

> Tell the model not to update tickets from another tenant.

This is weak because it treats the model as the enforcement boundary. Prompt instructions can guide behavior, but they do not provide reliable authorization enforcement.

## Related material

- `labs/brokenpilot/prototype-app/TOOL_CALLING_LAB.md`
- `labs/brokenpilot/prototype-app/README.md`
- `modules/07-agent-tool-security/exercise-agent-control-design.md`
- `templates/tool-permission-matrix-template.md`
- `templates/agent-action-approval-policy-template.md`
