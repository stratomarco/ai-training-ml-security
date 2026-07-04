# 40-hour student experience runbook

This runbook helps the instructor manage the course as a one-week professional training, not as twelve independent lectures.

## Course rhythm

Use the same rhythm each day:

1. Frame the security property.
2. Demonstrate the vulnerable or risky condition.
3. Let students reproduce or review the evidence.
4. Discuss why naive fixes are insufficient.
5. Convert evidence into a graded artifact.
6. Close with a checkpoint.

## What to protect

Do not let the class become a prompt-hacking tournament. The purpose is security engineering. The best student output is a control decision with validation and residual risk.

## Daily instructor flow

### Start of day

- State the day theme.
- Name the required deliverable.
- Show one strong example and one weak example when available.
- Remind students which target is in use: BrokenPilot, toy classifier, evidence pack, or tabletop.

### During labs

Watch for these failure modes:

- Students focus on clever payloads instead of root cause.
- Students propose prompt wording as the primary control.
- Students record screenshots without explaining the security property.
- Students overclaim from toy data.
- Students ignore residual risk.

Intervene by asking:

- What is the enforcement point?
- What changes when the control is enabled?
- What would an engineer implement?
- What would you monitor after rollout?
- What could still go wrong?

### End of day

Collect a short checkpoint. Give feedback on one item only: the highest-leverage gap for the next day.

## Suggested checkpoint timing

| Day | Checkpoint time | Main artifact |
|---|---:|---|
| 1 | 30 minutes | system boundary and abuse cases |
| 2 | 45 minutes | LLM/RAG/output-handling evidence |
| 3 | 45 minutes | tool control or supply-chain review |
| 4 | 45 minutes | privacy/adversarial/finding rewrite |
| 5 | 90 minutes | capstone report and readout |

## Instructor grading anchors

Strong submissions are concise, evidence-based, and implementable.

Weak submissions are long, clever, or dramatic, but do not identify an enforcement point or validation method.
