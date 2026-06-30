# Common Mistakes — RAG Security

## Mistake 1 — Treating retrieval as only a relevance problem

Many teams optimize retrieval for semantic similarity and answer quality but ignore authorization, classification, and source trust.

Why it is dangerous:

- the most relevant document may be unauthorized,
- the closest chunk may be stale or poisoned,
- and similarity does not imply permission.

Better approach:

```text
authorized subset first, semantic ranking second
```

## Mistake 2 — Filtering after the model sees the content

A weak design retrieves sensitive content, sends it to the model, and then tries to filter the answer.

Why it is dangerous:

- the content already crossed the boundary,
- the model may summarize it indirectly,
- logs may retain it,
- and citations or intermediate traces may expose it.

Better approach:

```text
do not put unauthorized content into model context
```

## Mistake 3 — Losing access-control metadata during chunking

A document may have correct ACLs, but chunks may be stored without those ACLs.

Why it is dangerous:

- the vector database may retrieve chunks without knowing permissions,
- citations may point to inaccessible sources,
- and cross-tenant leakage becomes likely.

Better approach:

- copy security metadata to every chunk,
- fail closed when metadata is missing,
- and test chunk-level authorization.

## Mistake 4 — Trusting internal documents by default

Internal does not mean safe. Internal systems contain drafts, comments, stale pages, support tickets, user uploads, and low-trust notes.

Better approach:

- classify source trust,
- distinguish authoritative from unreviewed content,
- and prevent low-trust content from authorizing actions.

## Mistake 5 — Depending on prompt wording as the main control

Prompts can help communicate policy to the model, but they are not hard boundaries.

Weak control:

```text
The model is instructed not to reveal confidential information.
```

Stronger control:

```text
Confidential information is not retrieved unless the user is authorized.
```

## Mistake 6 — Ignoring indirect prompt injection

Some teams test only user prompts and forget that documents, tickets, emails, webpages, and code comments can also carry instructions.

Better approach:

- test with malicious documents,
- label retrieved content as data,
- prevent retrieved content from controlling tools,
- and monitor source influence.

## Mistake 7 — Assuming citations prove correctness

Citations are useful but not sufficient.

A cited answer may still be:

- unsupported by the source,
- based on a stale source,
- based on a poisoned source,
- inaccessible to the user,
- or a hallucinated interpretation of a valid source.

Better approach:

- validate citations for sensitive answers,
- expose source trust/freshness,
- and require human review for high-impact actions.

## Mistake 8 — Building one shared vector index without tenant controls

A single shared index can be acceptable only if metadata filtering is strong and tested. Without reliable filtering, it creates a cross-tenant data leakage path.

Better approach:

- use separate indexes for strong isolation where needed,
- or enforce tenant filters at query time with tests that prove isolation.

## Mistake 9 — Logging too much

RAG traces can contain full prompts, retrieved chunks, sensitive source text, and generated answers.

Better approach:

- log source IDs and policy decisions,
- minimize raw content logging,
- protect traces with access control,
- and define retention limits.

## Mistake 10 — No security regression tests

RAG behavior changes when documents, embeddings, prompts, models, and ranking logic change.

Better approach:

Maintain regression tests for:

- cross-tenant retrieval,
- malicious documents,
- missing metadata,
- stale source conflicts,
- source trust conflicts,
- and sensitive output leakage.
