# Tabletop Lab — Poisoning, Backdoors, and Feedback-Loop Abuse

## Purpose

Review how training data, labels, model artifacts, feedback, and retraining pipelines can create targeted or systemic model failures.

## Scenario

**CaseFlow** is a support-ticket triage model.

It assigns tickets to priority levels and routing queues.

The system learns from:

- historical tickets;
- user-selected categories;
- support-agent corrections;
- post-resolution labels;
- monthly retraining jobs.

A product team wants to increase automation and reduce human review.

## Architecture

```text
incoming ticket
  |
  v
triage model
  |
  +-- priority label
  +-- routing queue
  +-- confidence score
  |
  v
support workflow
  |
  +-- agent corrections
  +-- feedback store
  +-- monthly retraining
  +-- model registry
```

## Tabletop event

Over several weeks, a specific category of abuse reports begins to receive lower priority.

The model still performs well on the general validation dashboard.

The team suspects one of the following:

1. poisoned feedback data;
2. low-quality labels;
3. distribution shift;
4. backdoor-like trigger behavior;
5. evaluation set blind spots;
6. model registry or artifact promotion error.

## Student tasks

1. Identify data and model assets.
2. Map where untrusted data enters the lifecycle.
3. Identify poisoning paths.
4. Identify possible trigger or backdoor conditions.
5. Review evaluation blind spots.
6. Define evidence needed to investigate.
7. Propose containment and recovery.
8. Define long-term controls.
9. Write residual risk.

## Investigation prompts

- Who can create training examples?
- Who can edit labels?
- Which labels are trusted?
- Can feedback be generated at scale?
- Can feedback bypass review?
- Are training examples linked to source and time?
- Can data be quarantined?
- Can the model be rolled back?
- Are targeted failure cases in evaluation?
- Does monitoring detect segment-specific degradation?

## Possible controls

| Control | Purpose |
|---|---|
| Data provenance | Trace examples to source, time, tenant, and labeler. |
| Feedback gating | Prevent untrusted feedback from directly becoming labels. |
| Label review | Catch suspicious or low-quality labels. |
| Segment evaluation | Detect targeted degradation. |
| Backdoor tests | Look for trigger-specific behavior. |
| Registry approvals | Prevent unreviewed model promotion. |
| Data quarantine | Remove suspected poisoned examples. |
| Rollback | Restore known-good model. |
| Monitoring | Detect drift and abuse patterns. |

## Deliverable

Use [`../../templates/drift-abuse-monitoring-template.md`](../../templates/drift-abuse-monitoring-template.md) and include a short incident-response plan.

## Instructor note

The important lesson is that poisoning is not only a data science problem. It is supply chain security, identity, authorization, data governance, monitoring, and incident response.
