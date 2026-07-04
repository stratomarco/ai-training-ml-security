# Student lab journal guide

This guide gives students one consistent way to record evidence across BrokenPilot, the toy classifier, and reasoning labs.

The journal is not a screenshot dump. It is a short engineering record that proves the student understood the failure, the control, the validation method, and the remaining risk.

## What every lab entry must contain

1. Lab name and module.
2. System state before the test, including user, tenant, role, control flags, and reset status when relevant.
3. Exact command, HTTP request, UI action, or review step used to produce the observation.
4. Observable failure or review evidence.
5. Root cause in security-engineering terms.
6. Control or design change proposed.
7. Validation step that proves the security property changed.
8. Residual risk and operational follow-up.

## Attack lab entries

Attack labs must show both the vulnerable behavior and the controlled behavior when the lab supports it.

For BrokenPilot this usually means:

```text
/reset
controls off
run the request
record the unsafe observation
controls on
run the same request
record the changed security property
```

For the toy classifier this usually means:

```text
train the baseline model
run the attack script
record the before and after prediction or score
explain why the model should not be used as a hard authorization gate without fallback
```

## Reasoning lab entries

Reasoning labs are graded differently. They may not have a runnable failure. They must still end with an engineering artifact.

Examples:

- architecture risk review
- supply-chain evidence review
- privacy risk assessment
- red-team scope
- residual-risk memo

A good reasoning entry names the decision a real team must make, the evidence that supports the decision, the control backlog, and the residual risk.

## Evidence hygiene

Use fake local data only. Do not paste real tokens, customer records, production logs, or proprietary incident details. When a lab uses a fake secret, label it clearly as training-only evidence.
