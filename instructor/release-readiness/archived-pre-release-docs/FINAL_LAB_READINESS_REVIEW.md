# Final Lab Readiness Review

This review checks whether the labs support the course promise: read first, lab supported, security-engineering focused.

## Lab classes

| Class | Requirement |
|---|---|
| Attack lab | Observable failure, observable control comparison, deterministic reset or repeatability |
| Reasoning lab | Concrete evidence, graded artifact, strong/weak or model-answer anchor |
| Capstone | Multi-finding evidence, business decision, remediation plan, residual risk |

## BrokenPilot readiness

BrokenPilot is the primary runnable target for LLM/RAG/agent/privacy/red-team flows.

### Required observable paths

- direct prompt injection
- indirect prompt injection or retrieved instruction confusion
- retrieval authorization
- tool authorization
- memory poisoning
- memory review or isolation
- cross-tenant privacy leakage
- insecure output handling

### Required validation

Run from `labs/brokenpilot/prototype-app`:

```powershell
pytest
```

A passing test suite is not the whole lab, but failing tests mean the course should not be released.

### Instructor check

For each BrokenPilot lab, the instructor should be able to answer:

- What is the vulnerable behavior?
- What control changes the behavior?
- What naive fix fails?
- What residual risk remains?
- What should the student submit?

## Toy-classifier readiness

The toy classifier is the primary runnable target for Modules 03 and 10.

### Required observable paths

- evasion changes a model decision
- poisoning changes model behavior after retraining
- extraction approximates a decision boundary through queries
- output threshold tampering changes the final decision without changing the model

### Required validation

Run from `labs/toy-ml-attacks/toy-classifier-app`:

```powershell
pytest
```

### Instructor check

The instructor should frame the lab around the hard-gate decision: when a classifier can be wrong under plausible perturbation, what decision should it be allowed to make automatically?

## MLOps evidence-pack readiness

The evidence pack is a reasoning lab. Its purpose is to teach artifact and promotion review, not to simulate a production ML pipeline.

### Required evidence points

- dependency provenance
- dataset provenance
- artifact identity
- artifact hash mismatch
- notebook hygiene
- storage mutability
- promotion approval
- rollback evidence
- residual risk

### Instructor check

The instructor should emphasize that the output is not a list of smells. The output is a promotion decision with evidence and controls.

## Reasoning-lab readiness

Reasoning labs should not be penalized for being non-runnable. They should be judged on whether they produce a defensible engineering artifact.

### Required anchors

- architecture risk review anchor
- privacy reasoning anchor
- poisoning/backdoor tabletop anchor
- red-team scope anchor
- MLOps model answer

## Final lab release criteria

A lab is ready when:

1. students know what to run or review
2. students know what to submit
3. instructors know how to debrief it
4. grading has a strong or weak anchor
5. the lab does not overclaim what it demonstrates
