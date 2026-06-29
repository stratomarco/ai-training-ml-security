# Module 5 Student Handout — LLM Application Security

## Core idea

LLM applications are software systems that use a model as one component.

They still need:

- authentication
- authorization
- input validation
- output handling
- secrets management
- secure APIs
- logging
- monitoring
- incident response
- supply chain controls

The model adds new behavior risks, especially when it receives untrusted language and can access privileged data or tools.

## Key principle

> Prompts are not hard security boundaries.

Prompts can guide behavior, but security enforcement should happen outside the model.

## Basic LLM application architecture

```text
User
  -> Application UI/API
  -> Authentication and authorization
  -> Prompt/context builder
  -> Retrieval system
  -> LLM gateway
  -> Model
  -> Tool/function gateway
  -> Output handling
  -> Logs and monitoring
```

## Main risk categories

| Risk | Meaning | Security lesson |
|---|---|---|
| Prompt injection | Untrusted input changes model behavior | Do not rely on prompts as enforcement |
| Insecure output handling | Model output is passed unsafely downstream | Treat model output as untrusted |
| Training data poisoning | Bad training/fine-tuning data changes behavior | Control data provenance and review |
| Model DoS | Prompts or workflows exhaust resources | Add budgets, limits, and timeouts |
| Supply chain vulnerabilities | Models, packages, datasets, or tools are compromised | Manage AI dependencies as supply chain assets |
| Sensitive disclosure | Model reveals data it should not expose | Authorize before retrieval and minimize context |
| Tool/plugin risk | LLM uses tools unsafely | Use scoped tools and external policy checks |
| Excessive agency | Model can take too many actions | Add least privilege and approval gates |
| Overreliance | Humans/systems trust output too much | Require verification for high-risk decisions |
| Model theft | Model behavior, weights, or prompts are stolen | Control access and monitor abuse |

## Direct vs indirect prompt injection

Direct prompt injection:

```text
The attacker directly sends malicious instructions to the assistant.
```

Indirect prompt injection:

```text
The attacker places malicious instructions in data the assistant later reads.
```

Indirect injection is common in:

- web browsing agents
- email assistants
- document summarizers
- RAG systems
- ticket summarizers
- code review assistants
- workflow agents

## Insecure output handling

LLM output may become dangerous when used as:

- HTML
- Markdown
- SQL
- shell command
- code
- JSON
- YAML
- API arguments
- workflow instructions

Security rule:

> Validate, encode, constrain, or review model output before downstream use.

## Sensitive data disclosure

Sensitive data can leak through:

- retrieved documents
- chat history
- tool results
- logs
- prompts
- memory
- embeddings
- system messages
- generated output

Security rule:

> Do not retrieve data the user is not authorized to access.

A prompt saying “do not reveal secrets” is not a replacement for access control.

## Model denial of service

LLM DoS may affect:

- availability
- latency
- inference cost
- token budget
- context capacity
- tool-call budget
- queue capacity

Controls:

- input size limits
- token budgets
- rate limits
- timeouts
- per-user quotas
- tool-call limits
- recursion limits
- anomaly detection

## Good mitigation patterns

| Problem | Better control |
|---|---|
| Prompt injection | Context separation, least privilege, external policy checks |
| Unauthorized retrieval | Authorization before retrieval |
| Unsafe tool call | Tool gateway with schema validation and per-action auth |
| Sensitive output | Data minimization, redaction, output review |
| Unsafe rendering | Output encoding and safe Markdown/HTML rendering |
| Model DoS | Budgets, limits, timeouts, queue controls |
| Overreliance | Human review and verification for high-risk decisions |
| Model theft | Access control, rate limits, anomaly detection |

## Questions to ask during review

1. What does the attacker control?
2. What can the model see?
3. What can the model do?
4. Which data sources are trusted?
5. Which data sources are untrusted?
6. Where is authorization enforced?
7. What happens if the model ignores the system prompt?
8. Is output passed to another interpreter?
9. Are tool calls independently checked?
10. What is logged for investigation?
11. Which actions need human approval?
12. What is the residual risk?

## Final takeaway

The model may be probabilistic.

The security controls around it should not be.
