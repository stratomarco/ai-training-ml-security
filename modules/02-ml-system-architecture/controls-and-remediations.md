# Controls and Remediations: ML System Architecture

## Control objective

The architecture should make sensitive flows explicit and put controls at the boundaries where data, authority, artifacts, and outputs change trust level.

## Architecture controls

### Trust-boundary diagram

Every AI system should have a diagram that shows users, data sources, retrieval stores, model service, tools, output sinks, logs, and deployment path. Boundaries should be labeled by trust level and owner.

### Data classification and metadata

Documents, datasets, embeddings, features, logs, and generated outputs should carry classification and ownership metadata. Controls depend on these labels.

### Retrieval access control

Retrieval must enforce tenant, role, classification, allowed-user, and purpose before content enters model context. Filtering after the answer is too late.

### Tool broker

All tool execution should go through a broker that validates schema, user authority, target object, action, approval requirement, and audit logging.

### Output sink controls

Each output sink should define validation and encoding rules. Display, storage, search query, shell command, SQL query, tool argument, and memory all need different handling.

### Artifact promotion gates

Model artifacts should not move to production without provenance, dependency evidence, evaluation evidence, approval, integrity verification, and rollback metadata.

### Observability with privacy controls

Logs should be structured and useful for investigation, but not become a dumping ground for sensitive prompts and context. Redaction, retention, access control, and purpose limitation matter.

## Remediation patterns

When an architecture review finds a missing boundary, do not patch the diagram with a vague "guardrail." Add a specific enforcement point.

If retrieval leaks data, add pre-context authorization and tests.

If tools execute unsafe actions, add a broker with target-object authorization.

If output reaches unsafe sinks, add context-specific encoding and validation.

If artifacts lack provenance, add manifest, digest, dataset hash, lockfile, approval, and promotion policy.

If logs leak data, add redaction, retention, access control, and separate sensitive traces.

## Validation

Architecture controls must be testable. A diagram is not enough.

A retrieval boundary is validated with a cross-tenant negative test.

A tool boundary is validated with an unauthorized action test.

An output boundary is validated with a harmless marker that must be escaped or rejected.

A promotion boundary is validated by attempting to promote an artifact with missing or mismatched evidence.

A logging boundary is validated by checking that sensitive fragments do not appear in broad logs.

## Residual risk

Architecture controls reduce blast radius, but they do not eliminate model uncertainty, data drift, poor user judgment, or weak organizational process. Residual risk should be documented where controls rely on human review, incomplete metadata, probabilistic detection, or manual operation.
