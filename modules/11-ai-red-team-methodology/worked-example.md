# Worked example: Red team finding with defense in depth

## Weak finding

We poisoned the memory and the AI tried to close a beta ticket. This is critical and the agent should have better guardrails.

## Why this is weak

It overstates the issue, uses vague remediation, and fails to distinguish intent from execution. If tool authorization blocked the action, the report should say so.

## Strong finding

**Finding:** Unreviewed global memory can steer agent intent, but independent tool authorization prevents cross-tenant ticket execution.

**Evidence:** A malicious memory entry instructed the agent to close `TCK-2001`. When Alice later asked about the related workflow, the agent attempted to act on that instruction. With tool authorization enabled, the tool broker returned `tool_authorization_denied` because Alice's tenant and the ticket tenant did not match.

**Root cause:** Memory entries can influence planning before review or tenant scoping. However, execution is separately controlled by the tool authorization layer.

**Impact:** If tool authorization were disabled or incomplete, poisoned memory could lead to unauthorized ticket changes. With tool authorization enabled, impact is reduced to manipulated intent and a blocked action attempt.

**Remediation:** Require memory review before activation and isolate memory by tenant, user, and purpose. Keep tool authorization mandatory for every state-changing action. Add audit fields showing which memory entries influenced an agent run.

**Validation:** Add a malicious memory entry and run the scenario. With memory review enabled, the memory should not become active. With memory isolation enabled, cross-tenant memory should not be consumed. With tool authorization enabled, any attempted cross-tenant update should be denied.

**Residual risk:** Tool authorization prevents this execution path, but poisoned memory can still waste operator time, influence summaries, or affect lower-impact decisions. Monitoring and memory review remain necessary.

## Instructor note

This example is the model for mature red team reporting. It shows a weakness, a compensating control, a realistic impact statement, and validation steps.

## What an excellent submission adds

An excellent submission includes both sides of the defense-in-depth story. It explains that memory handling is weak because unreviewed memory can influence intent, and it also explains that tool authorization reduced impact by blocking execution.

The best reports avoid inflated severity. They say what happened, what did not happen, and what would have been required for worse impact. That makes the recommendation more credible.
