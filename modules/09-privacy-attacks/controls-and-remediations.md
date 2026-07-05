# Controls and remediations: Privacy attacks and data protection

## Control objective

The goal is to prevent unauthorized disclosure, reconstruction, inference, and retention of sensitive data through all AI system paths.

## Primary controls

### Retrieval authorization

Filter retrieval by tenant, role, user, classification, and purpose before documents are added to model context. Do not retrieve first and ask the model to decide what is safe.

Validation: run a beta user query that matches alpha restricted tags. The result set should contain no alpha restricted documents.

### Data minimization

Send only the minimum necessary context to the model. Avoid loading complete documents when a smaller authorized fragment is enough.

Validation: inspect traces and confirm that retrieved context is limited and classified.

### Output controls

Classify and inspect outputs before display or downstream use. Redact known sensitive markers when appropriate, but do not treat redaction as a replacement for retrieval authorization.

Validation: seed a fake sensitive fragment and confirm it is not displayed to unauthorized users.

### Logging and trace controls

Treat prompts, retrieved context, tool arguments, responses, embeddings, and traces as potentially sensitive. Apply redaction, retention limits, access control, and purpose limitation.

Validation: after a blocked request, inspect logs. They should not contain unauthorized sensitive context.

### Training and fine-tuning controls

Do not use restricted production data for training or fine-tuning without a clear legal basis, data minimization, retention policy, and removal process.

Validation: check dataset manifests and training metadata for source classification and approval.

### Inference-risk controls

For membership inference and model inversion risk, reduce overfitting, limit confidence exposure where appropriate, monitor query patterns, and avoid returning unnecessary per-record signals.

Validation: compare model behavior on member and non-member synthetic records; evaluate whether confidence scores reveal membership more than necessary.

## Weak controls

- Relying on a system prompt that says not to reveal secrets.
- Redacting outputs while still storing raw restricted context in traces.
- Checking authorization after retrieval.
- Assuming internal logs are safe because they are not customer-facing.
- Treating synthetic evaluation data as proof that production data is safe.

## Strong remediation language

Use implementation-focused remediation:

- Add tenant, role, and classification filters to retrieval before context construction.
- Add a trace redaction layer for retrieved context and tool arguments.
- Deny logging of restricted fragments unless a security-approved debug mode is active.
- Add retention limits for chat transcripts and retrieved-context traces.
- Add privacy regression tests for cross-tenant retrieval and log leakage.

## Residual risk

Privacy risk is rarely zero. Even with retrieval filters and redaction, users may infer sensitive facts from aggregate outputs, timing, ranking, or repeated queries. Good security work states what remains and what monitoring or governance process owns it.
