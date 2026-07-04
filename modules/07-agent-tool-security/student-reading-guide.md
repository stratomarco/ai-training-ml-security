# Student Reading Guide: Module 07: Agent and Tool Security

## What this module is really about

Agents become risky when model-generated intent can trigger tools with real authority. The memorable lesson is defense in depth: memory or retrieved content may steer the agent, but the tool broker must still authorize the action against the target object.

## Question to keep in mind

What action is being requested, who requested it, what target object is affected, and who authorizes execution?

## Decisions students must learn to make

- Distinguish model intent from tool execution authority.
- Define per-tool, per-user, and per-target authorization checks.
- Decide which actions need approval, rollback, and audit evidence.
- Handle memory as untrusted or reviewed context, not as authority.

## Lab or exercise connection

Use BrokenPilot tool authorization, approval, memory poisoning, and audit flows. This remains the reference attack lab for the course.

## What a strong submission looks like

A strong submission shows the same malicious intent under different controls, explains the root cause as model intent being confused with execution authority, and explains why one layer can fail while another prevents execution.

## Common misreadings to avoid

- Assuming a better system prompt can enforce tool policy.
- Checking only user role and not the target object tenant.
- Forgetting rollback and audit in the remediation plan.

## Exit ticket

Write the authorization rule for closing a ticket in one precise sentence.
