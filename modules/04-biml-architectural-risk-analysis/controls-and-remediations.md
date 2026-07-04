# Controls and Remediations: BIML Architectural Risk Analysis

## Control objective

The objective is to convert architecture risks into design changes that are enforceable, testable, and proportionate to system impact.

## Analysis controls

### Abuse-case review

For each major workflow, write abuse cases that describe what an attacker, malicious document, careless user, poisoned dataset, or weak pipeline step could cause.

### Trust-boundary review

Label boundaries between users, documents, data sources, model context, tools, logs, artifact stores, and external services.

### Security property mapping

For each asset and action, state which property matters: confidentiality, integrity, availability, authorization, privacy, or accountability.

### Control placement

Place controls at the boundary where the property can actually be enforced. Do not place all controls inside prompts.

### Evidence planning

Decide what evidence will prove the control works before the system ships. This includes tests, audit records, approval records, artifact metadata, and monitoring signals.

## Remediation patterns

If the design relies on trusted retrieved content, add retrieval authorization and source trust labels.

If the design relies on safe model tool use, add a tool broker with authorization and approval.

If the design relies on safe output display, add output encoding and sink validation.

If the design relies on artifact trust, add provenance and promotion gates.

If the design relies on human review, improve the review interface and require evidence-based approval.

If the design relies on logs for investigation, make logs structured, redacted, access-controlled, and retained appropriately.

## Prioritization

Prioritize risks where the AI system can:

- Access restricted or personal data.
- Cross tenant or role boundaries.
- Change operational state.
- Influence financial, legal, safety, or customer-impacting decisions.
- Promote model artifacts to production.
- Store long-lived memory or feedback.
- Produce outputs consumed by another interpreter or system.

## Validation

Architectural remediations should have acceptance tests. The test may be runnable, as in BrokenPilot, or review-based, as in the MLOps evidence pack.

A design control is credible when a reviewer can say: "This failure path is now blocked here, and this evidence proves it."

## Residual risk

Architectural risk analysis does not eliminate uncertainty. It records what remains: model mistakes, incomplete metadata, human review quality, monitoring gaps, or operational constraints. Residual risk should be owned by the team that accepts the design.
