# Deep Dive: OWASP ML Security Top 10

## What this module is really about

The OWASP ML Security Top 10 is a map of recurring failure classes. It is useful because it gives teams a shared vocabulary, but the list is not the goal. The goal is to connect each category to a concrete engineering decision.

A student should not leave this module saying, "I know the names of the ML risks." A student should leave saying, "I can identify which part of the ML lifecycle is exposed, what security property is at risk, and what control would change the outcome."

## The core engineering decision

The core decision is how to translate a risk category into a system-specific control.

For example, "input manipulation" is not a finding by itself. A good finding says that a classifier is used as a hard authorization gate, small input changes can flip the decision, there is no uncertainty fallback, and the remediation is to add confidence thresholds, secondary review, adversarial evaluation, and non-model enforcement for high-impact decisions.

The category helps name the risk. The system analysis makes it actionable.

## How to read the Top 10

Read each category through four questions:

1. Where does this risk enter the system?
2. What asset, decision, or boundary can it affect?
3. What control would prevent, detect, or limit the impact?
4. How would we validate that the control works?

This keeps the list from becoming compliance theater.

## Lifecycle view of the categories

Some risks appear before training. Data poisoning, dataset provenance failures, labeling issues, and weak data governance affect what the model learns.

Some risks appear at inference. Input manipulation, adversarial examples, prompt injection, model abuse, and privacy leakage affect runtime behavior.

Some risks appear around deployment. Supply-chain compromise, model artifact tampering, weak output integrity, insecure APIs, and excessive privileges affect how model behavior becomes system impact.

Some risks appear after release. Drift, feedback poisoning, monitoring gaps, extraction, and operational misuse affect long-term safety.

## Why the list is not enough

A Top 10 category does not automatically imply severity. Severity depends on how the model is used.

A spam classifier that labels a training exercise message incorrectly is low impact. A fraud classifier that blocks salary payments or approves transfers is high impact. The same input manipulation concept matters differently depending on the decision, reversibility, user harm, business impact, and fallback path.

## Connecting OWASP ML to labs

The toy-classifier lab turns several categories into observable behavior:

- Evasion shows input manipulation.
- Poisoning shows training data integrity risk.
- Extraction shows how query access can reveal decision behavior.
- Output integrity shows that the model can be unchanged while the decision threshold is tampered.

BrokenPilot covers the LLM application side:

- Direct and indirect prompt injection.
- Cross-tenant retrieval leakage.
- Tool confused deputy behavior.
- Insecure output handling.
- Memory poisoning.

The MLOps evidence pack covers supply-chain and promotion risk.

## What makes a good OWASP ML finding

A good finding should include:

- Category mapping.
- Affected component.
- Evidence.
- Root cause.
- Security property affected.
- Business impact.
- Implementable control.
- Validation method.
- Residual risk.

A weak finding only names the category.

## Exit ticket

A student is ready to leave this module if they can take one OWASP ML category and produce a system-specific finding with evidence, control, validation, and residual risk.
