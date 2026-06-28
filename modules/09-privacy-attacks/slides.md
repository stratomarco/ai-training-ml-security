# Module 09 Slides — Privacy Attacks and Data Protection

## Slide 1 — Title

# Privacy Attacks and Data Protection

Securing sensitive data across ML, LLM, RAG, and agent systems.

---

## Slide 2 — Why this module matters

AI systems handle sensitive information in new ways.

They can:

- ingest it;
- transform it;
- summarize it;
- embed it;
- retrieve it;
- log it;
- infer it;
- memorize parts of it;
- reuse it through feedback loops;
- expose it through model outputs or tools.

Privacy risk becomes a lifecycle problem.

---

## Slide 3 — Core thesis

# AI privacy risk is not only about the model.

It is about the full system:

```text
data -> training -> model -> prompt -> retrieval -> tool -> memory -> log -> feedback
```

Every stage can expose sensitive information.

---

## Slide 4 — Privacy versus confidentiality

Confidentiality asks:

> Who can access this data?

Privacy asks:

> What can this system reveal, infer, retain, or misuse about a person or group?

A system can pass a basic access-control review and still create privacy risk.

---

## Slide 5 — Sensitive data in AI systems

Sensitive data may appear in:

- raw datasets;
- labels;
- features;
- training records;
- evaluation datasets;
- prompts;
- completions;
- embeddings;
- vector indexes;
- logs;
- model outputs;
- agent memory;
- feedback queues;
- screenshots and exports.

Do not only search the database schema.

---

## Slide 6 — Classic security still applies

Useful principles:

- data minimization;
- least privilege;
- need-to-know access;
- complete mediation;
- tenant isolation;
- secure logging;
- encryption;
- retention limits;
- auditability;
- deletion workflows;
- incident response.

The AI twist is that data may be transformed into harder-to-see artifacts.

---

## Slide 7 — Membership inference

Membership inference asks:

> Was this person's record included in the training data?

Why it matters:

- training membership may itself be sensitive;
- exposure may reveal medical, financial, employment, or legal associations;
- high-confidence model behavior can leak information about training data.

Security question:

> Does the system expose enough signal for an attacker to infer training membership?

---

## Slide 8 — Model inversion

Model inversion asks:

> Can an attacker reconstruct sensitive features, attributes, or representative records from model behavior?

Examples:

- reconstructing a face-like image from a classifier;
- inferring hidden attributes from outputs;
- recovering representative samples from a model.

The risk grows when outputs reveal too much detail or confidence.

---

## Slide 9 — Training data extraction

Training data extraction asks:

> Can the model emit memorized training content?

This may include:

- personal data;
- secrets;
- source code;
- legal text;
- customer records;
- proprietary documents.

Root causes often include excessive data collection, weak filtering, overtraining, poor deduplication, and weak output controls.

---

## Slide 10 — Prompt and completion leakage

Prompts and completions are often sensitive.

They may contain:

- customer data;
- employee data;
- incident details;
- credentials;
- internal architecture;
- legal or health information;
- confidential business plans.

Question:

> Are prompts treated as production sensitive data, or as disposable text?

---

## Slide 11 — Log and telemetry leakage

AI systems produce rich telemetry.

Logs may include:

- user prompt;
- full model response;
- retrieved context;
- tool arguments;
- tool results;
- model traces;
- embeddings metadata;
- evaluation examples;
- human feedback.

Logging is useful for debugging and safety, but it must be designed with privacy controls.

---

## Slide 12 — Embedding leakage

Embeddings are not harmless.

They may enable:

- semantic discovery of sensitive content;
- reconstruction or approximation attacks;
- cross-tenant retrieval;
- inference of document topics;
- accidental exposure through nearest-neighbor search.

Treat vector databases as sensitive data stores.

---

## Slide 13 — RAG privacy failures

Common RAG privacy failures:

- authorization only happens in the UI;
- retrieval occurs before permission checks;
- chunks lose document ACLs;
- metadata is stripped during ingestion;
- embeddings mix tenants;
- citations reveal document names;
- retrieved context is stored in logs;
- one user's prompt causes another user's data to be retrieved.

RAG turns search into a security boundary.

---

## Slide 14 — Agent memory leakage

Agent memory can create privacy persistence.

Risks:

- private data stored without consent;
- poisoned or sensitive memory reused in future sessions;
- memory shared across users;
- no expiry;
- no review or deletion workflow;
- no provenance.

Memory needs the same governance as any other data store.

---

## Slide 15 — Feedback-loop privacy

Feedback can become future training or evaluation data.

Examples:

- users paste customer records to correct an answer;
- analysts label sensitive examples;
- operators include incident details in feedback;
- support teams upload screenshots.

Question:

> What happens to feedback after the user submits it?

---

## Slide 16 — Privacy threat modeling

Ask:

1. What sensitive data exists?
2. Where does it flow?
3. Who can access it?
4. What can the model infer?
5. What gets logged?
6. What gets retained?
7. What becomes an embedding?
8. What enters feedback loops?
9. What crosses tenant boundaries?
10. What can be deleted?

---

## Slide 17 — Control: data minimization

Collect less.

Train on less.

Retrieve less.

Log less.

Retain less.

Data that does not exist cannot leak.

Data minimization is one of the strongest AI privacy controls.

---

## Slide 18 — Control: retrieval authorization

For RAG systems:

- preserve source ACLs during ingestion;
- attach tenant/user metadata to chunks;
- enforce authorization before retrieval results reach the model;
- filter by user, tenant, purpose, and role;
- test cross-tenant retrieval explicitly;
- log retrieval decisions without overlogging sensitive content.

---

## Slide 19 — Control: prompt and log governance

Good controls include:

- prompt data classification;
- PII/secrets detection;
- redaction or masking;
- log sampling;
- retention limits;
- restricted log access;
- encryption;
- deletion workflows;
- audit trails;
- incident response playbooks.

Do not let debugging become a data lake of sensitive prompts.

---

## Slide 20 — Control: privacy testing

Privacy testing should include:

- membership inference assessment;
- model inversion risk review;
- training data extraction testing;
- prompt leakage testing;
- RAG cross-tenant tests;
- vector DB authorization checks;
- log exposure review;
- memory persistence review;
- feedback-loop review.

---

## Slide 21 — Differential privacy

Differential privacy can reduce certain training-data leakage risks.

But it is not magic.

It must be evaluated against:

- model utility;
- threat model;
- training process;
- privacy budget;
- deployment context;
- regulatory expectations.

For many application teams, basic data minimization and access control will come first.

---

## Slide 22 — Secure design pattern

```text
user request
  -> input classification
  -> policy check
  -> retrieval with ACL filter
  -> context minimization
  -> model call
  -> output privacy check
  -> safe logging
  -> retention policy
```

The model is only one step in a privacy-preserving workflow.

---

## Slide 23 — Bad design pattern

```text
all documents -> chunking without ACLs -> shared vector DB
  -> retrieve top-k for any user
  -> send full chunks to model
  -> log prompt + retrieved context + answer forever
```

This is a privacy incident waiting to happen.

---

## Slide 24 — Exercise

Students review a fake HR assistant that:

- indexes employee documents;
- uses a shared vector database;
- logs prompts and completions;
- stores conversation memory;
- allows managers and HR users to ask questions;
- has weak retrieval authorization.

Goal: produce a privacy risk assessment.

---

## Slide 25 — Closing message

# Privacy is a system property.

Do not rely on the model to protect sensitive data after the architecture already exposed it.

The safest sensitive data is:

- not collected;
- not embedded;
- not retrieved;
- not logged;
- not retained;
- not exposed to broad tools or agents.
