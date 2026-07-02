# Assessment Exercise  -  Rewrite a Weak Finding

This assessment checks whether students can convert a vague AI security observation into a useful engineering finding.

## Input

Students receive this weak finding:

```text
The AI agent can be tricked and should have better guardrails.
```

They also receive evidence from the BrokenPilot tool-calling lab.

## Required output

Students must submit a rewritten finding using the finding rewrite template.

Required sections:

- title
- summary
- affected component
- security property violated
- evidence
- root cause
- impact
- recommended control
- implementation detail
- validation method
- residual risk
- leadership-facing explanation

## Grading

Use `finding-quality-rubric.md`.

## Expected learning outcome

Students should learn that a useful AI security finding is not only an exploit description. It is a security argument that helps engineers fix the system and helps leaders make a risk decision.
