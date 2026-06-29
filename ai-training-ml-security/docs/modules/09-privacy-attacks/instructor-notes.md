# Module 09 Instructor Notes — Privacy Attacks and Data Protection

## Teaching intent

This module should make students uncomfortable with the common assumption that privacy risk is solved by access control at the main application layer.

The key point is that AI systems create additional data surfaces: prompts, completions, retrieved context, embeddings, traces, feedback, memory, evaluation examples, and model behavior.

## Suggested timing

For a 90-minute session:

| Time | Activity |
|---|---|
| 0–10 min | Privacy risk framing and AI lifecycle data surfaces |
| 10–25 min | Membership inference, model inversion, extraction |
| 25–40 min | Prompt, log, embedding, RAG, and memory leakage |
| 40–55 min | Privacy design patterns and controls |
| 55–80 min | Exercise: privacy review of HR/customer-support assistant |
| 80–90 min | Discussion, trade-offs, residual risk |

For a 2-hour session, expand the exercise and include group presentations.

## Instructor framing

Open with:

> In this module, the attacker does not always need to hack the database. Sometimes they can ask questions, inspect outputs, exploit retrieval, query the model repeatedly, or abuse logs and memory.

Then connect back to the course philosophy:

- This is still security engineering.
- The model does not replace access control.
- Logs are data stores.
- Embeddings are data stores.
- Memory is a data store.
- Retrieval is a security boundary.

## Concepts to emphasize

### 1. Privacy is broader than confidentiality

Confidentiality is about preventing unauthorized access.

Privacy is also about inference, purpose, retention, consent, minimization, and secondary use.

A user may be authorized to use the system but not authorized to learn everything the model can infer.

### 2. The model is not the only risk

Common mistake:

> “We do not train the model on customer data, so there is no privacy risk.”

Correction:

Prompt logs, RAG context, vector DBs, support traces, feedback queues, and agent memory can still expose sensitive information.

### 3. RAG can break access control

In many systems, document permissions live in the source system but are lost during chunking and embedding.

Ask students:

- What ACL is attached to this chunk?
- What tenant owns this embedding?
- Who can retrieve it?
- Can the model see it before the user is authorized?
- Does the citation reveal sensitive metadata?

### 4. Logs become sensitive datasets

AI logs are often more sensitive than normal web logs because they can include full user prompts, retrieved internal documents, tool outputs, and model reasoning traces.

### 5. Memory needs governance

Agent memory should not be treated as a magical feature. It needs provenance, access control, retention, deletion, user visibility, and review.

## Common student misconceptions

| Misconception | Correction |
|---|---|
| “If data is embedded, it is no longer sensitive.” | Embeddings can reveal semantic relationships and enable retrieval of sensitive content. |
| “The model provider handles privacy.” | The application still controls prompts, retrieval, logs, tools, retention, and authorization. |
| “We can tell the model not to reveal PII.” | Prompts are not security boundaries. Use system controls. |
| “Only training data matters.” | Inference-time context, logs, memory, and feedback matter too. |
| “Managers should see all employee data.” | Authorization must match purpose and role, not broad hierarchy. |

## Exercise facilitation

Divide students into groups.

Give each group the scenario from `exercise-privacy-risk-assessment.md`.

Ask them to produce:

1. Sensitive data inventory.
2. Data-flow map.
3. Top five privacy abuse cases.
4. Existing control gaps.
5. Mitigation plan.
6. Residual risk statement.

Encourage debate on trade-offs:

- How much logging is necessary for debugging?
- Can prompts be retained for quality improvement?
- How should deletion work when data was embedded?
- How can retrieval authorization avoid excessive latency?
- How much privacy testing is enough before release?

## Expected high-quality findings

Students should identify:

- prompts and completions are sensitive;
- retrieved context can leak documents;
- vector DB must preserve tenant and ACL metadata;
- logs need retention limits;
- memory needs provenance and deletion;
- HR data needs purpose-based access control;
- feedback must not silently become training data;
- model outputs need privacy review for high-risk domains;
- membership inference and inversion risks should be assessed for models trained on sensitive data;
- deletion from source systems must propagate to indexes and caches.

## Suggested instructor summary

End with:

> Privacy failures in AI systems are rarely isolated to one bug. They usually come from a chain: too much data collected, weak classification, lost authorization metadata, broad retrieval, verbose logging, long retention, and model-mediated output. The fix is not one guardrail. The fix is privacy engineering across the lifecycle.
