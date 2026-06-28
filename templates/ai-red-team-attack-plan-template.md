# AI Red Team Attack Plan Template

## System under test

<!-- Name and short description. -->

## Objective

<!-- What risk are we testing? -->

## Threat model summary

### Assets

- 

### Attacker persona

- 

### Entry points

- 

### Trust boundaries

- 

## Attack path

```text
entry point
  -> step 1
  -> step 2
  -> failed control
  -> impact
```

## Preconditions

| Preconditions | Notes |
|---|---|
| Attacker role | |
| Required access | |
| Required data/control point | |
| Required configuration | |

## Test steps

| Step | Action | Expected observation | Evidence to collect |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Safety controls

- [ ] Uses fake/synthetic data.
- [ ] Uses approved environment.
- [ ] Does not execute destructive actions.
- [ ] Tool calls are simulated or controlled.
- [ ] Stop condition is defined.

## Expected findings

| Finding | Impact | Likely severity |
|---|---|---|
| | | |

## Mitigations to validate

- [ ] Policy outside the model
- [ ] Retrieval authorization
- [ ] Tool authorization
- [ ] Approval gates
- [ ] Output validation
- [ ] Rate limits/budgets
- [ ] Monitoring/logging
- [ ] Fallback behavior

## Notes

<!-- Open assumptions, uncertainties, and constraints. -->
