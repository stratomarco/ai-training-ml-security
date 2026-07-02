# BrokenPilot Finding Rewrite — Before and After

This example shows how to rewrite a vague AI security finding into a decision-grade finding.

## Weak version

```text
The AI agent can be tricked and should have better guardrails.

Severity: High

Recommendation: Add more AI safety checks and make the prompt stronger.
```

## Why this is weak

This finding is not useful because it does not say:

- what component failed
- what security property was violated
- what evidence proves the issue
- what root cause created the issue
- what engineers should implement
- how to validate the fix
- what risk remains

It also frames the issue as an "AI trick" instead of a system security failure.

## Strong version

### Title

Agent ticket-update tool allows cross-tenant ticket modification without target-object authorization.

### Summary

BrokenPilot allowed an `alpha` tenant user to update a `beta` tenant ticket because the ticket update tool did not independently enforce target-object authorization. The model or agent workflow was able to initiate the action, and the tool applied the state change without checking whether the acting user was permitted to modify the specific ticket. This violates tenant isolation and ticket integrity.

### Affected component

- Component: BrokenPilot tool execution layer
- Endpoint: `POST /tools/update-ticket`
- Acting user: `alice`
- User tenant: `alpha`
- Target object: `TCK-2001`
- Target tenant: `beta`
- Control state: `ENABLE_TOOL_AUTHZ=False`

### Security property violated

The issue violates **authorization** and **tenant isolation**.

A user from one tenant should not be able to modify another tenant's ticket unless explicitly authorized by a policy outside the model.

### Evidence

Observed vulnerable behavior:

```text
User: alice
User tenant: alpha
Target ticket: TCK-2001
Ticket tenant: beta
Action: update ticket status to closed
Result: updated
Authorization decision: not_checked
Ticket status after request: closed
```

Controlled retest:

```text
Control state: ENABLE_TOOL_AUTHZ=True
Same request result: HTTP 403
Error: tool_authorization_denied
Reason: User must be an ops user in the same tenant as the ticket.
```

### Root cause

The tool execution layer did not apply complete mediation for state-changing actions. It allowed an agent-initiated ticket update without checking the acting user's permissions against the target ticket's tenant and workflow state.

The root cause is not simply that the model can be tricked. The deeper failure is that the tool trusted the workflow instead of enforcing authorization independently.

### Impact

An attacker or confused workflow could cause unauthorized ticket updates across tenant boundaries. In a real operations system, this could close incidents, modify support records, disrupt operational workflows, or hide unresolved issues belonging to another tenant.

### Recommended control

The ticket update tool must enforce target-object authorization before applying any state change.

Minimum rule:

```text
Allow update only if:
- user.role == "ops"
- user.tenant == ticket.tenant
- requested transition is allowed by workflow policy
Otherwise deny before modifying state.
```

For destructive or high-impact transitions, require an approval gate.

### Validation method

Negative test:

- `alice` from tenant `alpha` attempts to update `TCK-2001` in tenant `beta`
- expected result: HTTP 403
- expected error: `tool_authorization_denied`

Positive test:

- authorized beta ops user updates `TCK-2001`
- expected result: update succeeds

Regression test:

- every new state-changing tool must include target-object authorization tests before release

### Residual risk

This control does not prevent a legitimate authorized user from making a bad decision. It also does not prevent abuse from a compromised account inside the correct tenant. High-impact actions may still require approval gates, audit review, anomaly detection, and rollback.

### Leadership-facing explanation

The agent was able to trigger a cross-tenant ticket update because the tool did not enforce authorization itself. The fix is not simply to make the model safer; every state-changing tool must check user and object permissions before making changes. This keeps AI assistance useful while preventing the model from becoming an implicit authorization layer.

## What changed between weak and strong

| Weak finding | Strong finding |
|---|---|
| Says the AI can be tricked | Identifies the failing component |
| Recommends guardrails | Defines an enforceable authorization rule |
| No evidence | Includes vulnerable and controlled evidence |
| No root cause | Explains missing complete mediation |
| No validation | Gives negative, positive, and regression tests |
| No residual risk | Explains what remains after the fix |
