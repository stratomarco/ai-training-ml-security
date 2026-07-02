# Exercise — Rewrite a Weak AI Security Finding

## Purpose

Students often find a vulnerability but describe it in a way that is not useful to engineers or leadership.

This exercise teaches students to turn a weak finding into a decision-grade security finding with:

- clear evidence
- violated security property
- root cause
- impact
- implementable control
- validation method
- residual risk

This exercise can be used after Module 07, Module 08, Module 11, or before the BrokenPilot capstone.

## Scenario

A student tested BrokenPilot and wrote the following finding:

> The AI agent can be tricked and should have better guardrails.

This is not a useful finding. It is vague, not reproducible, does not explain the system failure, and gives engineers no clear remediation path.

Your job is to rewrite it into a strong finding.

## Weak finding to rewrite

```text
The AI agent can be tricked and should have better guardrails.

Severity: High

Recommendation: Add more AI safety checks and make the prompt stronger.
```

## Available evidence

Use the following evidence from the BrokenPilot tool-calling lab:

```text
User: alice
User tenant: alpha
User role: ops
Target ticket: TCK-2001
Target ticket tenant: beta
Control state: ENABLE_TOOL_AUTHZ=False
Action: POST /tools/update-ticket
Result: ticket updated
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

## Student task

Rewrite the weak finding into a strong finding with the following sections:

1. Title
2. Summary
3. Affected component
4. Security property violated
5. Evidence
6. Root cause
7. Impact
8. Recommended control
9. Implementation detail
10. Validation method
11. Residual risk
12. Leadership-facing explanation

## Constraints

Your rewritten finding must:

- avoid saying only "add guardrails"
- include the exact authorization rule that failed
- distinguish model behavior from tool enforcement
- include at least one concrete acceptance criterion
- explain how the fix was validated or should be validated
- be understandable to both an engineer and a security leader

## Expected strong direction

A strong answer should say something like:

> BrokenPilot allowed a user from tenant `alpha` to update a ticket in tenant `beta` because the ticket update tool did not independently enforce target-object authorization. The model or agent must not be trusted to decide whether a tool action is authorized. The tool must check that the acting user is permitted to modify the specific ticket before applying the update.

## Discussion questions

1. Why is "the agent can be tricked" not sufficient as a finding?
2. What is the difference between a model behavior failure and an authorization failure?
3. Why is the tool layer the correct place to enforce this control?
4. What evidence would make this finding reproducible?
5. What would still remain risky after enabling tool authorization?

## Instructor notes

Students should not be rewarded only for saying the issue is high severity. They should be rewarded for explaining why the system failed and what engineers must implement.

The strongest submissions will identify the issue as a confused-deputy / broken object-level authorization problem in an agentic workflow.
