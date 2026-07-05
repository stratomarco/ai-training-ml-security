# Student lab journal template

Use one copy of this template per lab or checkpoint.

## Lab identity

- Student or team:
- Module:
- Lab:
- Date:
- Lab class: attack lab / reasoning lab
- Target: BrokenPilot / toy classifier / evidence pack / tabletop

## Initial state

- Reset performed:
- User, tenant, and role:
- Relevant control flags:
- Dataset or evidence pack used:
- Assumptions:

## Observation 1: vulnerable behavior or review evidence

### Action taken

Record the command, API request, UI action, or review step.

```text
paste command, request, or review note here
```

### Result observed

```text
paste relevant local output or short paraphrase here
```

### Security property affected

Examples: authorization, tenant isolation, instruction/data separation, output handling, provenance, model robustness, privacy, auditability.

## Root cause

Explain the design weakness. Avoid saying only that the model was tricked.

## Naive fix and why it is insufficient

Describe the quick fix a team might suggest and why it does not fully address the root cause.

## Proposed control

Name the concrete control, owner, and enforcement point.

## Validation

Show how the same scenario changes after the control or design rule is applied.

```text
paste validation result here
```

## Residual risk

What still needs monitoring, approval, rollback, incident response, or follow-up review?

## Graded conclusion

One paragraph that a technical lead or security reviewer could act on.
