# Finding Rewrite Template

Use this template to rewrite a vague AI security observation into a decision-grade finding.

## Title

Write a specific title.

Weak:

```text
The AI can be tricked.
```

Strong:

```text
Agent ticket-update tool allows cross-tenant ticket modification without target-object authorization.
```

## Summary

Describe the issue in two to four sentences.

Include:

- what happened
- who could do it
- what asset was affected
- why it matters

## Affected component

- System:
- Endpoint/tool:
- Data/object affected:
- User role involved:
- Trust boundary crossed:

## Security property violated

Select the main property:

- Authorization
- Tenant isolation
- Data confidentiality
- Data integrity
- Availability
- Auditability
- Human approval / workflow integrity

Explain the property in one sentence.

## Evidence

Provide enough detail for another tester to reproduce the issue.

```text
Request:
Observed response:
Control state:
Affected object before:
Affected object after:
```

## Root cause

Explain why the issue happened.

Avoid vague causes like:

- "bad AI"
- "weak prompt"
- "no guardrails"

Prefer concrete causes like:

- missing target-object authorization
- retrieved content treated as trusted instruction
- memory entries consumed without review or scope enforcement
- tool action executed without approval gate
- security decision delegated to model output

## Impact

Explain the consequence in system terms.

Include:

- affected asset
- affected user/tenant
- possible business impact
- operational impact
- abuse path

## Recommended control

Describe the primary control.

The control should be implementable by engineers.

Example:

```text
Before updating a ticket, the tool must check that the acting user has permission to modify the target ticket's tenant and workflow state. If the user is not authorized, the tool must reject the request before applying any state change.
```

## Implementation detail

Define concrete rules or pseudocode.

```text
IF user.role != "ops": deny
IF user.tenant != ticket.tenant: deny
IF ticket.status is terminal and action is destructive: require approval
ELSE allow
```

## Validation method

Explain how the fix will be tested.

Include:

- negative test
- positive test
- regression test
- logging/audit check

## Residual risk

Explain what remains after the control.

Examples:

- legitimate but mistaken authorized actions
- compromised authorized account
- missing approval for high-risk changes
- incomplete audit review
- future tools without the same authorization pattern

## Leadership-facing explanation

Summarize the issue without technical overload.

Example:

```text
The AI agent was able to cause a ticket update across tenant boundaries because the tool trusted the workflow instead of enforcing authorization itself. The fix is to make every tool action check user and object permissions before changing state. This preserves developer velocity while preventing the model from becoming an implicit authorization layer.
```
