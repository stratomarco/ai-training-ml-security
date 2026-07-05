# Module 6 Deep Dive  -  RAG Security and Indirect Prompt Injection

## Why this module matters

Retrieval-augmented generation is often sold as a simple way to make LLM applications more accurate: connect the model to documents, retrieve relevant context, and ask the model to answer from that context. From a security perspective, that framing is incomplete.

RAG does not only add knowledge. It adds a new **input channel**, a new **data access path**, a new **authorization surface**, and a new **influence path** into the model.

A secure RAG review therefore asks more than “does the answer look right?” It asks:

- What content can enter the index?
- Who is allowed to retrieve each chunk?
- Which metadata survives chunking?
- Which retrieved sources are trusted, partially trusted, or untrusted?
- Can retrieved content change instructions, tool behavior, or workflow decisions?
- Can the assistant reveal content the user could not open directly?
- Can citations make an unsafe answer look authoritative?

The core lesson is:

> RAG makes retrieval a security boundary. The boundary must be enforced by the application, not by the model.

## What RAG changes in the trust model

A basic LLM application has at least three instruction/data sources:

```text
system/developer instructions
user prompt
model output
```

A RAG application adds more:

```text
source documents
indexed chunks
embeddings
retrieval metadata
query rewrites
ranked results
prompt templates
citations
logs and traces
```

This matters because retrieved content is usually written for humans, not for models. A document, wiki page, support ticket, or email may contain text that looks like an instruction. The model may not reliably know whether that text is:

- a fact to summarize,
- an instruction from the application,
- a malicious instruction inserted by an attacker,
- stale operational guidance,
- confidential content outside the user's authorization,
- or a business rule that should never override policy.

Security cannot depend on the model always making that distinction correctly.

## RAG as a classic security problem

RAG security is new in implementation details, but not new in principle.

| Classic security idea | RAG equivalent |
|---|---|
| Input is untrusted | Retrieved chunks are untrusted input |
| Complete mediation | Check authorization every time content is retrieved |
| Least privilege | Retrieve only the minimum content needed for the user and task |
| Confused deputy | The model has access to context the user should not control or see |
| Injection | Retrieved text can be interpreted as instruction |
| Data classification | Chunks need labels such as tenant, owner, sensitivity, source, and purpose |
| Secure logging | Prompt/context logs can become a secondary data leak |
| Output validation | Generated answers and citations need checks before use |

The model should not be the policy decision point. A model can help summarize, reason, and explain, but authorization, source trust, output handling, and tool-action controls need deterministic enforcement.

## Direct versus indirect prompt injection

Direct prompt injection happens when the user directly sends adversarial instructions to the assistant.

Indirect prompt injection happens when adversarial instructions are embedded in content the assistant later retrieves or reads.

The second case is more dangerous in many real systems because the malicious content may be invisible to the end user. The user asks a normal question. The retriever selects a poisoned document. The poisoned document enters the model context. The model then treats the document as if it were authoritative.

```text
attacker writes malicious document
        ↓
document enters index
        ↓
user asks normal question
        ↓
retriever selects malicious chunk
        ↓
prompt builder inserts chunk into context
        ↓
model follows or is influenced by chunk
        ↓
unsafe answer, data disclosure, or tool action
```

The root cause is not only “the model was fooled.” The deeper root causes are usually:

- untrusted content was allowed into the context,
- context was not labeled clearly,
- retrieved data was not separated from instructions,
- authorization was weak or missing,
- the model had too much agency,
- and downstream controls trusted the generated answer.

## Why retrieval authorization is the first hard control

A common insecure pattern is:

```text
retrieve broadly → give all context to model → ask model not to reveal unauthorized content
```

That is backwards. Once unauthorized content is in the model context, the system has already crossed a security boundary. The model may leak it directly, summarize it indirectly, combine it with other information, or expose it through citations, logs, traces, or tool calls.

A stronger pattern is:

```text
authenticate user
  → authorize task and purpose
  → filter retrievable corpus by tenant, role, classification, and need-to-know
  → retrieve from authorized subset only
  → build context with labels and source boundaries
  → generate answer
  → validate output and citations
  → log decisions safely
```

The model should never receive documents the user and task are not allowed to access.

## Metadata is security-critical

Chunking often breaks security. A source document may have a classification, owner, tenant, and access-control list. If chunking creates text fragments but drops those labels, the retriever may no longer know who is allowed to see each chunk.

Security metadata should survive the whole pipeline:

```text
source document
  → chunk
  → embedding
  → vector index
  → search result
  → prompt context
  → citation
  → logs
```

Important metadata includes:

- tenant/customer
- document owner
- source system
- access-control groups
- sensitivity classification
- retention category
- jurisdiction or regulatory label
- timestamp and version
- ingestion source
- trust level
- whether content is internal, external, user-generated, or third-party

If a chunk cannot prove its authorization and provenance, a fail-safe system should not use it for sensitive answers.

## Source trust and provenance

Not all retrieved content should have equal authority.

A signed production runbook, an internal wiki draft, a support ticket comment, an external webpage, and a customer-uploaded PDF should not be treated the same. They may all be “relevant,” but relevance is not trust.

A secure RAG system should distinguish:

- authoritative sources,
- internal but unreviewed sources,
- user-generated content,
- external web content,
- stale content,
- sensitive content,
- and content that can be used for background only but not for instructions or actions.

The retriever may rank by semantic similarity, but the application should also consider source trust, freshness, classification, and authorization.

## Output and citation risk

RAG systems often add citations to improve trust. That helps, but it also creates risks.

A citation can be wrong in several ways:

- the source was unauthorized,
- the answer misrepresented the source,
- the source was stale,
- the source was poisoned,
- the source was low-trust,
- the citation points to a document the user cannot open,
- or the model cites a source for a claim the source does not actually support.

Citations are not proof. They are evidence that must be validated when the decision is sensitive.

## Security controls by lifecycle stage

| Stage | Key controls |
|---|---|
| Ingestion | source allowlists, malware scanning, classification, provenance, owner mapping |
| Chunking | metadata preservation, sensitivity labels, chunk IDs, version tracking |
| Indexing | tenant separation, access labels, encryption, admin access control |
| Retrieval | pre-retrieval authorization, purpose limitation, query limits, source trust ranking |
| Prompt construction | instruction/data separation, source labels, context minimization |
| Generation | system constraints, refusal rules, no tool authority from retrieved content |
| Output handling | citation validation, redaction, safe rendering, sensitive output review |
| Logging | minimize stored prompts/chunks, protect traces, retention limits |
| Monitoring | blocked retrievals, unusual source mixes, repeated sensitive queries |
| Evaluation | malicious document tests, cross-tenant regression tests, citation accuracy tests |

## What good looks like

A good RAG security design does not claim the model will “understand” which content to trust. Instead, it constrains the environment around the model.

Good design includes:

- authorization before retrieval,
- strong tenant isolation,
- preserved chunk metadata,
- source trust scoring,
- context minimization,
- clear instruction/data separation,
- output validation for sensitive answers,
- controlled citations,
- safe logging,
- regression tests with malicious documents,
- and monitoring for suspicious retrieval patterns.

The final security posture should be understandable without inspecting the prompt. If the only meaningful control is “we told the model not to leak data,” the design is weak.
