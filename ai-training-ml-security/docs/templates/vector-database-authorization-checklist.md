# Vector Database Authorization Checklist

Use this checklist when reviewing a vector database or retrieval layer for RAG.

## Identity and tenant scope

- [ ] Does every query include authenticated user identity?
- [ ] Does every query include tenant scope where relevant?
- [ ] Are tenant filters mandatory and non-bypassable?
- [ ] Is there a safe behavior when tenant metadata is missing?
- [ ] Are service accounts scoped to the minimum required corpora?

## Metadata and policy

- [ ] Does every vector/chunk include document ID?
- [ ] Does every vector/chunk include tenant?
- [ ] Does every vector/chunk include owner?
- [ ] Does every vector/chunk include classification?
- [ ] Does every vector/chunk include access-control labels?
- [ ] Does every vector/chunk include source trust level?
- [ ] Does every vector/chunk include version or freshness metadata?

## Query controls

- [ ] Are policy filters applied before results are returned?
- [ ] Are filters enforced server-side, not only client-side?
- [ ] Are fallback searches constrained by policy?
- [ ] Is query rewriting constrained by user authorization?
- [ ] Are broad queries rate-limited or reviewed?
- [ ] Are denied retrievals logged?

## Indexing controls

- [ ] Are sensitive documents excluded by default?
- [ ] Are secrets scanned before indexing?
- [ ] Is regulated data identified before indexing?
- [ ] Are high-risk corpora placed in separate indexes where appropriate?
- [ ] Are deleted source documents removed from the index?
- [ ] Are stale embeddings refreshed or removed?

## Retrieval result controls

- [ ] Are returned chunks traceable to source documents?
- [ ] Can the user open every cited source?
- [ ] Are low-trust sources marked?
- [ ] Are deprecated documents marked or excluded?
- [ ] Are conflicting sources surfaced safely?
- [ ] Is the number of chunks minimized?

## Monitoring

- [ ] Are cross-tenant retrieval attempts detected?
- [ ] Are unusual source combinations detected?
- [ ] Are repeated denied retrieval attempts detected?
- [ ] Are high-sensitivity source retrievals monitored?
- [ ] Are prompt-injection-like strings in indexed content detected?
- [ ] Are retrieval logs protected and retained appropriately?

