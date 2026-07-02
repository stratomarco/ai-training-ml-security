# Module 6 Checklist  -  RAG Security

Use this checklist during RAG architecture reviews.

## 1. Data inventory

- [ ] Do we know which document sources are indexed?
- [ ] Do we know who owns each source?
- [ ] Do we know which sources are internal, external, user-generated, or vendor-provided?
- [ ] Are sensitive sources explicitly identified?
- [ ] Are deprecated or draft documents marked?
- [ ] Are secrets excluded from indexing?
- [ ] Are regulated data types identified before ingestion?

## 2. Ingestion controls

- [ ] Is document ingestion authenticated and authorized?
- [ ] Are source permissions captured at ingestion time?
- [ ] Are document classification labels captured?
- [ ] Are documents scanned for secrets or sensitive data?
- [ ] Are external documents marked as lower trust?
- [ ] Is ingestion logged?
- [ ] Is there a review process for high-risk sources?

## 3. Chunking and metadata

- [ ] Do chunks preserve document ID?
- [ ] Do chunks preserve owner?
- [ ] Do chunks preserve tenant?
- [ ] Do chunks preserve classification?
- [ ] Do chunks preserve source trust level?
- [ ] Do chunks preserve access-control labels?
- [ ] Are chunks tied back to original source version?
- [ ] Are chunk transformations reproducible?

## 4. Vector database and retrieval

- [ ] Is access control enforced before retrieval results reach the model?
- [ ] Are tenant filters mandatory?
- [ ] Are role/group filters mandatory?
- [ ] Are classification filters mandatory?
- [ ] Is fallback retrieval constrained?
- [ ] Is query rewriting constrained by user authorization?
- [ ] Are retrieval results traceable?
- [ ] Are unauthorized retrieval attempts logged?

## 5. Prompt construction

- [ ] Are system instructions separated from retrieved content?
- [ ] Is retrieved content clearly labeled as untrusted data?
- [ ] Are source IDs included for traceability?
- [ ] Is the amount of retrieved context minimized?
- [ ] Are high-risk documents excluded unless specifically authorized?
- [ ] Are conflicting sources handled explicitly?

## 6. Output controls

- [ ] Are answers checked for sensitive disclosure?
- [ ] Are citations shown only for sources the user can access?
- [ ] Does the UI avoid rendering unsafe HTML or Markdown?
- [ ] Are generated answers labeled as generated content?
- [ ] Are low-confidence answers handled safely?
- [ ] Are high-impact answers routed to human review?

## 7. Logging and monitoring

- [ ] Are retrieved document IDs logged?
- [ ] Are blocked retrievals logged?
- [ ] Are logs protected with appropriate access control?
- [ ] Are raw prompts and retrieved chunks minimized or redacted in logs?
- [ ] Are anomalous retrieval patterns monitored?
- [ ] Are cross-tenant hits alerted?
- [ ] Are prompt injection strings in documents detected or reviewed?

## 8. Testing

- [ ] Are malicious documents included in tests?
- [ ] Are unauthorized user scenarios tested?
- [ ] Are cross-tenant scenarios tested?
- [ ] Are stale or deprecated documents tested?
- [ ] Are source-conflict scenarios tested?
- [ ] Are prompt injection attempts in documents tested?
- [ ] Are regression tests run after index or prompt changes?

## 9. Governance

- [ ] Is there an owner for the RAG index?
- [ ] Is there an owner for retrieval policy?
- [ ] Is there an approval process for new data sources?
- [ ] Is there a retention policy for embeddings and logs?
- [ ] Is there a deletion process for removed source documents?
- [ ] Is there an incident response process for RAG leakage?

