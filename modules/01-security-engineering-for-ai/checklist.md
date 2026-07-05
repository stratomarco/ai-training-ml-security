# Checklist  -  Security Engineering for AI Systems

Use this checklist during design review, threat modeling, and security testing of AI-enabled applications.

## 1. System understanding

- [ ] What is the business purpose of the AI feature?
- [ ] Is this a chatbot, RAG system, classifier, recommender, agent, or workflow automation?
- [ ] What model or model provider is used?
- [ ] What data is sent to the model?
- [ ] What data can the model retrieve?
- [ ] What actions can the model trigger?
- [ ] What human decisions depend on the model output?

## 2. Assets

- [ ] User prompts
- [ ] System prompts
- [ ] Retrieved context
- [ ] Documents
- [ ] Embeddings
- [ ] Vector index
- [ ] Model outputs
- [ ] Chat history
- [ ] Logs
- [ ] Model artifacts
- [ ] API keys and service tokens
- [ ] Tool credentials
- [ ] Customer data
- [ ] Employee data
- [ ] Source code or internal configuration

## 3. Trust boundaries

- [ ] User to application
- [ ] Application to identity provider
- [ ] Application to model gateway
- [ ] Application to model provider
- [ ] Application to retrieval service
- [ ] Retrieval service to document store
- [ ] Application to vector database
- [ ] Model output to renderer
- [ ] Model output to tool execution
- [ ] Tool execution to business systems
- [ ] Logs to monitoring or analytics
- [ ] Chat history to future sessions or memory

## 4. Authorization

- [ ] Is user authorization enforced before retrieval?
- [ ] Are document chunks filtered by user permission?
- [ ] Does the AI backend use a broad service account?
- [ ] Are tool calls authorized per user and per action?
- [ ] Are high-risk actions approved by a human?
- [ ] Are cross-tenant or cross-team boundaries enforced?
- [ ] Are admin functions isolated from normal assistant functions?

## 5. Prompt and context handling

- [ ] Are system instructions separated from user input?
- [ ] Is retrieved content clearly labeled as untrusted data?
- [ ] Are tool outputs treated as untrusted input?
- [ ] Are hidden prompts protected from unnecessary disclosure?
- [ ] Are prompts versioned and reviewed?
- [ ] Are prompt changes included in change management?

## 6. RAG and retrieval

- [ ] Is the ingestion pipeline authenticated and authorized?
- [ ] Can users poison documents that later influence other users?
- [ ] Is document provenance tracked?
- [ ] Are outdated or revoked documents removed from the index?
- [ ] Is the vector database access-controlled?
- [ ] Is retrieval scoped to user permissions?
- [ ] Are source links shown to users?

## 7. Tool and agent safety

- [ ] Are tools allowlisted?
- [ ] Are tool schemas strict?
- [ ] Are tool arguments validated outside the model?
- [ ] Are destructive actions blocked or approval-gated?
- [ ] Is there a maximum number of tool calls per task?
- [ ] Are loops and runaway plans limited?
- [ ] Is network egress restricted for tool execution?
- [ ] Is code execution sandboxed?

## 8. Output handling

- [ ] Is model output treated as untrusted?
- [ ] Is output encoded before rendering as HTML or Markdown?
- [ ] Is model-generated code reviewed before execution?
- [ ] Are URLs, commands, SQL, YAML, JSON, and scripts validated before use?
- [ ] Are citations or sources displayed where useful?
- [ ] Are confidence and uncertainty communicated appropriately?

## 9. Logging and monitoring

- [ ] Are security-relevant events logged?
- [ ] Are prompts and responses logged only when necessary?
- [ ] Are sensitive values redacted from logs?
- [ ] Who can access logs?
- [ ] Are unusual retrieval patterns detected?
- [ ] Are high-volume or high-cost requests detected?
- [ ] Are tool calls auditable?
- [ ] Are denied actions logged?

## 10. Privacy and retention

- [ ] Are prompts retained?
- [ ] Are responses retained?
- [ ] Are retrieved snippets retained?
- [ ] Is there a retention period?
- [ ] Can users request deletion where applicable?
- [ ] Is personal data minimized?
- [ ] Is sensitive data redacted where appropriate?
- [ ] Is training or fine-tuning on user data explicitly controlled?

## 11. Supply chain

- [ ] Are model artifacts trusted and verified?
- [ ] Are datasets versioned and sourced?
- [ ] Are dependencies scanned?
- [ ] Are notebooks reviewed before production use?
- [ ] Are containers hardened?
- [ ] Are API keys stored securely?
- [ ] Are model, prompt, and dataset changes auditable?

## 12. Residual risk

- [ ] What can still go wrong after controls are applied?
- [ ] What risk is accepted?
- [ ] Who accepts it?
- [ ] What should be monitored?
- [ ] What is the incident response plan?
- [ ] What should be improved in the next release?
