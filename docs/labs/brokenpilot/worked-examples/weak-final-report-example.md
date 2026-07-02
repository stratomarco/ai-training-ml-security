# Weak BrokenPilot Final Report Example

This example is intentionally weak. It shows the type of submission that should receive low marks because it is vague, hard to reproduce, and not useful for engineering decision-making.

## Executive summary

BrokenPilot has some AI security issues. The model can be jailbroken and should be made safer before going to production. The team should add guardrails and monitor the system.

## Findings

### Finding 1 — The model can be tricked

The assistant followed a bad instruction. This is prompt injection. It is high risk because attackers can abuse it.

Recommendation: improve the prompt and tell the model not to follow attacker instructions.

### Finding 2 — Tools are dangerous

The agent can update tickets. This is risky because agents can make mistakes.

Recommendation: add authorization.

### Finding 3 — Memory can be poisoned

Memory is risky because attackers can store bad things.

Recommendation: check memory.

## Evidence

I tested some prompts and got bad behavior. I do not have the exact commands but the system seemed vulnerable.

## Remediation

- Add guardrails.
- Add monitoring.
- Add access control.
- Train users.
- Use a safer model.

## Residual risk

There will always be some AI risk.

## Why this is weak

This report is weak because it:

- Does not show reproducible commands or outputs.
- Does not identify which object was accessed or changed.
- Does not explain the violated security property.
- Says "add authorization" without defining the rule.
- Does not distinguish prevention, detection, and response.
- Does not validate any fix.
- Gives leadership no clear decision.
- Treats "the model was jailbroken" as the finding instead of explaining system impact.

A stronger report would show the exact user, tenant, ticket, endpoint, configuration, observed result, root cause, remediation rule, and validation result.
