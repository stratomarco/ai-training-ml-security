# Grading Calibration Exercise

This exercise helps instructors and teaching assistants calibrate grading before running the BrokenPilot capstone.

It should be completed before grading student submissions.

## Purpose

The goal is to reduce grading inconsistency.

AI security deliverables often include qualitative judgment. This exercise gives instructors shared scoring anchors for threat models, evidence logs, remediation plans, permission matrices, and executive readouts.

## Inputs

Use the worked examples under:

```text
labs/brokenpilot/worked-examples/
```

Required examples:

- strong threat model example
- weak threat model example
- strong evidence log example
- weak evidence log example
- strong remediation backlog example
- weak remediation backlog example
- strong executive readout example
- weak executive readout example

Optional examples:

- strong risk register example
- weak risk register example
- strong tool permission matrix example
- weak tool permission matrix example

## Scoring scale

| Score | Meaning |
|---|---|
| 4 | Strong |
| 3 | Acceptable |
| 2 | Weak |
| 1 | Insufficient |

## Part 1 — Independent scoring

Each instructor should score the examples independently before discussing them.

| Example | Score | Reason |
|---|---:|---|
| Strong threat model |  |  |
| Weak threat model |  |  |
| Strong evidence log |  |  |
| Weak evidence log |  |  |
| Strong remediation backlog |  |  |
| Weak remediation backlog |  |  |
| Strong executive readout |  |  |
| Weak executive readout |  |  |

## Part 2 — Compare scoring

Discuss any score that differs by more than one point between instructors.

Use these questions:

- Did the example provide evidence or only assertions?
- Did it identify the root cause?
- Did it connect the issue to a trust boundary or security property?
- Was the mitigation implementable?
- Was residual risk described honestly?
- Was the communication appropriate for the target audience?

## Part 3 — Define local grading anchors

Before grading student submissions, define local anchors.

### Threat model anchor

For full credit, a threat model must include:

- assets;
- actors;
- trust boundaries;
- data flows;
- abuse cases;
- violated security properties;
- at least one control or mitigation area.

Local instructor additions:

```text

```

### Evidence anchor

For full credit, evidence must include:

- environment or control settings;
- request, prompt, or action;
- observed response;
- affected asset;
- security meaning;
- reproducibility notes.

Local instructor additions:

```text

```

### Remediation anchor

For full credit, remediation must include:

- owner;
- priority;
- implementation detail;
- enforcement point;
- validation method;
- residual risk.

Local instructor additions:

```text

```

### Executive communication anchor

For full credit, an executive readout must include:

- business impact;
- risk severity;
- decision needed;
- recommended next steps;
- concise language;
- no unnecessary exploit detail.

Local instructor additions:

```text

```

## Part 4 — Practice grading

Take one student-like deliverable or one weak example and write feedback that is:

- specific;
- actionable;
- tied to the rubric;
- focused on improvement.

Bad feedback:

```text
Needs more detail.
```

Better feedback:

```text
The finding identifies tool misuse, but it does not show the user, target ticket, tenant boundary, control state, or observed response. Add enough evidence for another engineer to reproduce the issue and implement the authorization rule.
```

## Output

At the end of this exercise, instructors should have:

- agreed grading anchors;
- shared expectations for strong vs weak deliverables;
- a consistent understanding of partial credit;
- example feedback language.

## When to reuse this exercise

Use this exercise:

- before the first cohort;
- when a new instructor joins;
- when the capstone changes;
- after any major BrokenPilot prototype update;
- when grading disagreement appears.
