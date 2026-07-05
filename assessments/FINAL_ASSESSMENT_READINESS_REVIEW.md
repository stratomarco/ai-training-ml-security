# Final Assessment Readiness Review

This document checks whether assessment matches the actual course outcomes.

## Assessment principle

Students should not be graded for being clever with payloads. They should be graded for security reasoning:

- evidence quality
- root-cause explanation
- control design
- validation plan
- residual risk
- leadership communication

## Assessment map

| Course area | Primary artifact | What strong work looks like |
|---|---|---|
| Foundations | architecture risk review | clear assets, trust boundaries, controls, and assumptions |
| LLM/RAG | lab journal finding | concrete evidence and control placement |
| Agent/tool | permission matrix or finding | tool broker enforcement and target-object authorization |
| MLOps | evidence-pack review | promotion decision with provenance and integrity evidence |
| Privacy | leakage review | data boundary, disclosure path, control, and residual risk |
| Adversarial ML | toy-classifier lab report | model-risk decision, not only attack output |
| Red team | scoped plan and report | testable objective and decision-useful evidence |
| Capstone | final report | prioritized findings, remediation backlog, executive recommendation |

## Red flags

A submission should not receive high marks if it:

- only says the model can be tricked
- recommends stronger prompts as the primary fix
- lacks evidence from the lab or evidence pack
- lacks validation steps
- lacks residual risk
- proposes controls the engineering team could not implement
- treats all findings as equally severe
- confuses privacy leakage with only policy noncompliance

## Final assessment readiness checks

Before release, confirm that each major assessed artifact has:

1. a template
2. a rubric
3. a strong example, weak example, or model answer
4. a short instructor debrief
5. a clear relationship to the module learning objective

## Capstone assessment check

The capstone should use current BrokenPilot evidence. If the capstone report still references only older RAG/tool behavior and not direct injection, output handling, privacy leakage, and memory poisoning, it is stale.
