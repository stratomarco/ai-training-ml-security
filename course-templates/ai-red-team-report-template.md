# AI Red Team Report Template

## Executive summary

<!-- Summarize what was tested, what matters most, and what decisions are needed. -->

## Scope

### In scope

- 

### Out of scope

- 

### Environment

- 

## Methodology

<!-- Describe threat modeling, test categories, attack planning, evidence collection, and safety boundaries. -->

## System overview

<!-- Include architecture summary, major components, trust boundaries, model role, RAG, tools, memory, and logging. -->

## Threat model summary

### Assets

- 

### Attacker personas

- 

### Trust boundaries

- 

### High-risk assumptions

- 

## Findings summary

| ID | Finding | Severity | Affected component | Status |
|---|---|---|---|---|
| AI-RT-001 | | | | |

---

# Finding AI-RT-001  -  Title

## Summary

<!-- One-paragraph explanation. -->

## Affected component

- 

## Security property violated

- [ ] Confidentiality
- [ ] Integrity
- [ ] Availability
- [ ] Authorization
- [ ] Privacy
- [ ] Safety
- [ ] Auditability
- [ ] Workflow integrity

## Preconditions

- 

## Attack path

```text
entry point
  -> step
  -> failed control
  -> impact
```

## Evidence

| Evidence | Description |
|---|---|
| Input/prompt | |
| Retrieved context | |
| Model output | |
| Tool call | |
| Logs/traces | |
| Screenshot/transcript | |

## Impact

<!-- Explain realistic impact, affected assets, blast radius, and business consequence. -->

## Root cause

<!-- Explain the design/control failure. -->

## Severity rationale

| Factor | Assessment |
|---|---|
| Asset sensitivity | |
| Required privilege | |
| Attacker control | |
| Reproducibility | |
| Blast radius | |
| Detectability | |
| Compensating controls | |

## Recommended remediation

### Quick fix

- 

### Architectural fix

- 

### Detection/monitoring

- 

### Regression test

- 

## Residual risk

<!-- What risk remains even after remediation? -->

---

## Overall remediation roadmap

| Priority | Action | Owner | Target date |
|---|---|---|---|
| P0 | | | |
| P1 | | | |
| P2 | | | |

## Executive decisions needed

- 

## Appendix

<!-- Include test matrix, transcripts, diagrams, or extra evidence. -->
