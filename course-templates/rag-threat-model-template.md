# RAG Threat Model Template

## 1. System name

`<system name>`

## 2. Business purpose

Describe what the RAG system is supposed to help users do.

## 3. Users and roles

| Role | Description | Data/tools allowed |
|---|---|---|
| | | |

## 4. Data sources

| Source | Owner | Trust level | Classification | Tenant/scope | Indexed? |
|---|---|---|---|---|---|
| | | | | | |

## 5. Architecture diagram

```text
<draw user -> app -> retrieval -> vector DB -> prompt builder -> model -> output>
```

## 6. Assets

List security-relevant assets.

- source documents
- chunks
- embeddings
- metadata
- access-control labels
- prompts
- retrieved context
- model responses
- logs
- API keys
- user identity

## 7. Trust boundaries

| Boundary | Description | Risk |
|---|---|---|
| User to app | | |
| App to retriever | | |
| Retriever to vector DB | | |
| App to model provider | | |
| Model output to UI | | |
| Tenant boundary | | |
| Authorization boundary | | |

## 8. Threats

| Threat | Asset | Attacker goal | Root cause | Impact |
|---|---|---|---|---|
| Indirect prompt injection | | | | |
| Unauthorized retrieval | | | | |
| Cross-tenant leakage | | | | |
| Poisoned document | | | | |
| Sensitive logging | | | | |
| Source trust failure | | | | |
| Citation laundering | | | | |

## 9. Controls

| Stage | Existing controls | Missing controls | Recommendation |
|---|---|---|---|
| Ingestion | | | |
| Chunking | | | |
| Indexing | | | |
| Retrieval | | | |
| Prompt construction | | | |
| Generation | | | |
| Output handling | | | |
| Logging | | | |
| Monitoring | | | |

## 10. Test cases

| Test | User role | Expected result | Actual result | Pass/fail |
|---|---|---|---|---|
| Unauthorized finance query | employee | no finance content | | |
| Cross-tenant query | tenant A user | no tenant B content | | |
| Malicious document | employee | instruction treated as data | | |
| Deprecated document | employee | warning or exclusion | | |

## 11. Residual risk

Describe what remains possible after controls.

Include:

- accepted risks
- monitoring requirements
- human review triggers
- incident response triggers
- future improvements

