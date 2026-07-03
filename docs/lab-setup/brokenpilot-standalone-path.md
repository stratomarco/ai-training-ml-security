# BrokenPilot Standalone Hands-On Path

This page explains the no-external-dependency lab path for the 40-hour course.

DVAIA is useful for extra practice, but BrokenPilot is the course-owned runnable target. If DVAIA is unavailable, instructors should continue with BrokenPilot instead of cancelling Modules 05, 06, or 11.

## Required flow

1. Run BrokenPilot locally.
2. Complete the Module 05 BrokenPilot standalone lab.
3. Complete the Module 06 BrokenPilot standalone lab.
4. Complete Module 07 tool and memory validation.
5. Use Module 11 to turn the evidence into strong findings.
6. Use Module 12 for the final report and readout.

## What BrokenPilot covers

| Topic | Covered by BrokenPilot | Notes |
|---|---:|---|
| Direct/model-instruction confusion | yes | deterministic mock behavior |
| Indirect prompt injection | yes | malicious retrieved document |
| Retrieval authorization | yes | tenant and role filtering |
| Tool confused deputy | yes | cross-tenant ticket update |
| Approval gates | yes | optional destructive-action control |
| Memory poisoning | yes | global memory as unsafe decision context |
| AI red-team reporting | yes | evidence and finding rewrite |
| Supply chain | tabletop only | not implemented in the runnable app |
| Privacy attacks | partial/tabletop | fake fragments only |
| Adversarial ML robustness | tabletop only | not implemented in the runnable app |

## DVAIA fallback rule

If DVAIA setup takes more than 20 minutes for more than one team, switch the cohort to BrokenPilot. Keep DVAIA as optional homework or instructor demo.

## Grading rule

Do not require students to find supply-chain, privacy, or adversarial-ML vulnerabilities in the BrokenPilot runnable target. Those topics are assessed through tabletop and written deliverables unless a separate target is added.
