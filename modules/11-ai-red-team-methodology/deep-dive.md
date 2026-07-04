# Deep dive: AI red team methodology

## The decision this module teaches

This module teaches one core decision:

> What evidence would change the launch, scope, control, or monitoring decision for this AI system?

AI red teaming is not a contest to produce alarming screenshots. It is a structured method for testing whether the system's controls hold under realistic abuse. The best red team work helps leaders decide what to fix, what to monitor, what to accept, and what not to launch yet.

## Red team work starts with scope

A good red team scope defines:

- the system boundary;
- permitted users and roles;
- allowed attack paths;
- prohibited actions;
- data handling rules;
- success criteria;
- evidence requirements;
- stop conditions;
- reporting format.

Without scope, a red team can become noisy, unsafe, or irrelevant. With scope, the team can test meaningful hypotheses and produce findings that engineering teams can act on.

## Hypotheses beat random probing

A strong test begins with a hypothesis:

- A user can retrieve cross-tenant context because retrieval filters are missing.
- A poisoned memory entry can influence agent intent.
- Tool authorization blocks execution even when the model is manipulated.
- A model output reaches an HTML sink without encoding.
- A promotion workflow deploys an artifact without verifying its digest.

These hypotheses map to controls. That makes the result useful whether the attack succeeds or fails.

## Evidence must be reproducible

A red team finding should include enough detail for another person to reproduce the behavior:

- role and tenant;
- control settings;
- input or request;
- observed result;
- expected result;
- affected asset;
- root cause;
- remediation;
- validation test.

For AI systems, this matters because outputs can be variable. BrokenPilot uses deterministic behavior so students can focus on security reasoning. Real systems need even more careful evidence collection.

## The fix matters more than the exploit

A weak report says, "we got the agent to do something bad." A strong report says, "the tool broker failed to enforce target-object authorization, allowing a cross-tenant ticket update; add authorization at the tool boundary and validate with this test."

The exploit shows that a control failed. The finding should explain the control.

## Defense-in-depth findings are the most valuable

The best AI red team findings often show interactions between controls. For example, poisoned memory may steer the agent's intent, while tool authorization still blocks execution. That is not a failed attack. It is a successful demonstration of defense in depth.

Students should learn to report both:

- where the system failed;
- where a control prevented worse impact.

That is more useful than a simple pass/fail narrative.

## Lab transfer

In BrokenPilot, students should build attack chains that connect:

- retrieval exposure;
- prompt or memory manipulation;
- tool execution;
- audit evidence;
- remediation validation.

The final deliverable should read like a security review, not a transcript dump. The target audience is an engineering leader deciding what must change before launch.
