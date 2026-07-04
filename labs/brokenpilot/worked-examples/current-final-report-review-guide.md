# Instructor Review Guide: Current BrokenPilot Final Report

This guide helps instructors grade the current BrokenPilot capstone report after the latest lab improvements.

## Minimum acceptable evidence

A complete report must include at least four of the five evidence paths:

1. Direct prompt injection.
2. Output handling.
3. Cross-tenant retrieval or privacy leakage.
4. Tool authorization.
5. Memory poisoning and defense in depth.

A strong report includes all five and explains how they relate.

## Strong report indicators

- The student describes trust boundaries, not only payloads.
- The student distinguishes model behavior from application enforcement.
- The tool finding checks authorization against the target object.
- The privacy finding explains why post-retrieval filtering is too late.
- The output-handling finding explains sink context.
- The memory finding includes the defense-in-depth lesson.
- The launch recommendation is conditional and testable.

## Weak report indicators

- Says "add guardrails" without naming where enforcement happens.
- Treats prompt injection as only a prompt-writing issue.
- Reports that a fake secret appeared but does not explain retrieval authorization.
- Reports that memory is unsafe but ignores tool authorization.
- Gives a launch/no-launch recommendation without control evidence.

## Suggested debrief questions

1. Which finding would block production launch first, and why?
2. Which finding can be mitigated without changing the model?
3. Which control remains necessary even if prompt injection filtering improves?
4. What evidence proves that the fix changed the security property?
5. What residual risk remains after the controlled branch passes?
