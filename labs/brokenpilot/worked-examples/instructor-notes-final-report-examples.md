# Instructor Notes  -  BrokenPilot Final Report Examples

Use these examples to calibrate expectations before the BrokenPilot capstone.

## Purpose

The gold-standard report is not intended to be a perfect answer key. It is a quality anchor. Students may find different issues or structure their report differently and still do excellent work.

The weak report is intentionally vague. It helps students see why generic AI security language is not enough for a professional security assessment.

## How to use in class

### Before the capstone

Show the weak report first. Ask students:

- What would an engineer be unable to implement from this report?
- What evidence is missing?
- What business decision is leadership supposed to make?
- Which finding is actually a model behavior issue and which is a system authorization issue?

Then show the gold-standard report and ask:

- What makes the evidence reproducible?
- Where does the report separate root cause from symptom?
- Which controls are preventive, detective, and responsive?
- How does the report validate that a control works?

### During grading calibration

Have each instructor score the same sample reports independently. Compare scores and resolve differences before grading real student submissions.

Suggested calibration dimensions:

| Dimension | Strong evidence |
|---|---|
| Threat model | Assets, trust boundaries, attacker goals, assumptions |
| Evidence | Exact command/request, configuration, observed response |
| Root cause | Security property violated, not just model behavior |
| Remediation | Implementable rule with owner and acceptance criteria |
| Validation | Same attack path replayed against the control |
| Executive communication | Clear decision and risk tradeoff |

## Scoring guidance

A strong final report should score highly only if it does all of the following:

1. Explains why the failure exists.
2. Shows reproducible evidence.
3. Defines implementable controls.
4. Validates at least one fix or control.
5. Communicates risk in a way leadership can act on.

A report should not receive high marks if it only lists prompts, screenshots, or generic advice.

## Common grading mistakes

### Over-rewarding exploit discovery

Finding an issue matters, but the course goal is security engineering. Reward students who explain root cause and remediation, not only students who produce dramatic exploit output.

### Accepting vague controls

"Add access control" is not enough. The report should define the access-control rule.

Weak:

```text
Add authorization to tools.
```

Strong:

```text
A user may update a ticket only if user.role permits the action and user.tenant equals ticket.tenant. The tool must evaluate this rule at the point of use and log the decision reason.
```

### Accepting leadership summaries with no decision

A strong executive summary should recommend a decision such as:

- approve read-only pilot;
- delay write-tool access;
- require P0 controls before production;
- accept residual risk with specific constraints.

## Suggested grading activity

Give students the weak report and ask them to rewrite one finding into a strong finding using:

1. Evidence.
2. Root cause.
3. Impact.
4. Control.
5. Validation.
6. Residual risk.

This turns the examples into an active learning exercise rather than passive reading.
