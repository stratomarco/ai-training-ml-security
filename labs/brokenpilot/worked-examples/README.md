# BrokenPilot Worked Examples

These examples help instructors calibrate grading and help students understand the expected quality of capstone deliverables.

The purpose is not to give students a full answer key. The purpose is to show the difference between vague security commentary and actionable security work.

## Included examples

### Threat modeling

- [Strong threat model example](strong-threat-model-example.md)
- [Weak threat model example](weak-threat-model-example.md)

### Risk register

- [Strong risk register example](strong-risk-register-example.md)
- [Weak risk register example](weak-risk-register-example.md)

### Tool permissions and concrete controls

- [Strong tool permission matrix example](strong-tool-permission-matrix-example.md)
- [Weak tool permission matrix example](weak-tool-permission-matrix-example.md)

### Evidence and reproducibility

- [Strong evidence log example](strong-evidence-log-example.md)
- [Weak evidence log example](weak-evidence-log-example.md)

### Remediation backlog

- [Strong remediation backlog example](strong-remediation-backlog-example.md)
- [Weak remediation backlog example](weak-remediation-backlog-example.md)

### Executive communication

- [Strong executive readout example](strong-executive-readout-example.md)
- [Weak executive readout example](weak-executive-readout-example.md)

## How instructors should use these

Use these examples in three ways:

1. **Before the capstone** — show students what good deliverables look like.
2. **During grading calibration** — align instructors on what counts as strong, acceptable, or weak.
3. **During feedback** — point students to a specific example when their submission is too vague.

## What makes a strong deliverable

A strong BrokenPilot deliverable is:

- Specific enough to reproduce.
- Clear about assets and trust boundaries.
- Clear about root cause.
- Mapped to a violated security property.
- Connected to business or operational impact.
- Paired with an implementable mitigation.
- Clear about what was tested and what remains residual risk.

## What makes a weak deliverable

A weak BrokenPilot deliverable usually has one or more of these problems:

- It says "add security" or "check authorization" without defining the rule.
- It lists vulnerabilities without evidence.
- It describes model behavior but not system impact.
- It does not distinguish prevention, detection, and response.
- It gives recommendations that engineers cannot implement.
- It has no acceptance criteria or validation method.
