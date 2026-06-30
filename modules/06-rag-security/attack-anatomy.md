# Attack Anatomy — RAG Indirect Prompt Injection and Retrieval Leakage

## Scenario

An internal assistant helps operations staff answer questions from engineering documentation, incident notes, and support tickets. It uses RAG to retrieve relevant chunks and pass them to an LLM.

The organization has two tenants:

- `alpha`
- `beta`

A user from `alpha` should not receive `beta` documents. The assistant should also not treat retrieved documents as instructions.

## Attack 1 — Indirect prompt injection through a retrieved document

### Attacker objective

Influence the assistant's answer or behavior by placing malicious instructions inside content that will later be retrieved.

### Precondition

The attacker can introduce or modify content in a source that enters the RAG index, such as:

- wiki page,
- support ticket,
- uploaded document,
- comment field,
- external webpage,
- customer document,
- or shared incident note.

### Attack path

```text
1. Attacker creates a document that looks relevant to a normal user query.
2. The document contains hidden or explicit instructions aimed at the assistant.
3. The ingestion pipeline indexes the document.
4. A legitimate user asks a normal question.
5. Retrieval selects the attacker's document because it is semantically relevant.
6. The prompt builder inserts the malicious chunk into the model context.
7. The model treats the chunk as authoritative or instruction-like.
8. The assistant gives an unsafe answer or attempts an unsafe action.
```

### Root cause

The root cause is not simply that “the LLM followed a bad prompt.” The deeper causes are:

- untrusted content entered the model context,
- the prompt did not clearly separate retrieved data from application instructions,
- source trust was not enforced,
- output/action controls relied on the model,
- and retrieved content had more authority than it should.

### Security principle violated

| Principle | Violation |
|---|---|
| Input validation | Retrieved documents were treated as safe context |
| Complete mediation | The system did not mediate whether the chunk should influence the answer/action |
| Least privilege | The model received more influence/context than needed |
| Separation of privilege | The model blended application instructions and retrieved text |
| Fail-safe defaults | The system used ambiguous content rather than blocking or downgrading it |

### Weak mitigations

- “Tell the model to ignore malicious documents.”
- “Add a stronger system prompt.”
- “Block obvious phrases like ignore previous instructions.”
- “Trust internal documents by default.”

These may reduce simple demonstrations, but they do not enforce a reliable boundary.

### Stronger controls

- classify source trust at ingestion,
- label retrieved context explicitly,
- strip or downgrade instruction-like text from untrusted sources,
- never allow retrieved content to authorize tool calls,
- require policy checks outside the model,
- test with malicious documents,
- and log which source influenced the answer.

## Attack 2 — Cross-tenant retrieval leakage

### Attacker objective

Cause the assistant to reveal information from another tenant or group.

### Precondition

The vector index contains chunks from multiple tenants or sensitivity levels.

### Attack path

```text
1. User from tenant alpha asks a broad or semantically similar question.
2. Retriever searches the whole index.
3. A beta document is semantically similar and ranks highly.
4. The prompt builder inserts the beta chunk into the model context.
5. The model summarizes or cites beta content to the alpha user.
```

### Root cause

The system confused semantic relevance with authorization. The retriever answered “what is similar?” but not “what is this user allowed to retrieve for this purpose?”

### Security principle violated

| Principle | Violation |
|---|---|
| Complete mediation | Authorization was not checked at retrieval time |
| Least privilege | The model received content outside the user's need-to-know |
| Fail-safe defaults | Ambiguous or unlabeled chunks were returned |
| Privacy by design | Sensitive data was included in a broad retrieval path |

### Stronger controls

- tenant-filtered retrieval,
- per-chunk access labels,
- post-index authorization tests,
- separate indexes for strong isolation where needed,
- citation access checks,
- and cross-tenant regression tests.

## Attack 3 — Citation laundering

### Attacker objective

Make a generated answer appear trustworthy by attaching citations, even when the answer misuses or misrepresents the source.

### Attack path

```text
1. Model retrieves a source that is weak, stale, poisoned, or unrelated to the final claim.
2. The generated answer includes the citation.
3. The user sees a citation and assumes the answer is verified.
4. The user acts on a false or unsafe recommendation.
```

### Root cause

The system treats citations as trust signals without validating whether the cited text supports the generated claim.

### Stronger controls

- citation-source access checks,
- source freshness labels,
- evidence-to-claim validation for high-risk answers,
- source trust scoring,
- and human review for high-impact decisions.

## Defender's mental model

A RAG system should answer four separate questions before using a chunk:

1. Is this chunk relevant?
2. Is this user allowed to access it?
3. Is this source trustworthy enough for the task?
4. Should this content be treated as data only, or can it influence a decision?

Many insecure RAG systems answer only the first question.
