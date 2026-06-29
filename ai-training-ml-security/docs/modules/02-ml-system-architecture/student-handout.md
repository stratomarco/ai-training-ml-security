# Module 02 Student Handout — ML System Architecture

## Core message

> ML security is lifecycle security.

A model is not an isolated object. It is created, deployed, queried, monitored, and sometimes updated through a system. Attackers can target any part of that lifecycle.

## Why this matters

Traditional application security focuses on source code, APIs, identity, sessions, databases, and infrastructure.

ML systems add additional security-sensitive components:

- Data sources
- Labels
- Feature pipelines
- Training code
- Model artifacts
- Evaluation datasets
- Model registries
- Inference APIs
- Monitoring systems
- Feedback loops
- Prompts
- Embeddings
- Vector databases
- Tools and agents

If attackers can influence these components, they may influence model behavior.

## Simplified ML lifecycle

```text
collect data
  -> label / curate data
  -> transform / engineer features
  -> train model
  -> evaluate model
  -> register model artifact
  -> deploy model
  -> serve predictions
  -> monitor behavior
  -> collect feedback
  -> retrain or update
```

## Key idea: data becomes behavior

In traditional software, source code mostly defines behavior.

In ML systems, behavior also comes from:

- Training data
- Labels
- Features
- Fine-tuning data
- Prompt templates
- Retrieved documents
- User feedback
- Evaluation choices

This means data integrity and provenance are security controls.

## Assets in ML systems

Common assets include:

| Asset | Why it matters |
|---|---|
| Training data | Shapes model behavior and may contain sensitive data |
| Labels | Often treated as ground truth |
| Feature code | Determines what the model sees |
| Training pipeline | Produces the model artifact |
| Model artifact | Deployable behavior and intellectual property |
| Evaluation data | Measures quality and may be sensitive |
| Model registry | Controls what can be deployed |
| Inference API | Public or internal attack surface |
| Logs | May contain sensitive prompts, outputs, and decisions |
| Feedback data | May influence future model behavior |
| Vector database | Controls retrieved context in RAG systems |
| Tool credentials | Determine what agents can do |

## Trust boundaries to look for

A trust boundary exists when data, control, or authority crosses from one trust level to another.

Common ML trust boundaries:

- External users submitting input
- Third-party data providers
- Labeling vendors
- Data science notebooks accessing production data
- Training pipeline accessing raw datasets
- CI/CD producing model artifacts
- Model registry deploying to production
- Inference API exposed to users
- Vector database retrieving internal documents
- Agent calling external tools
- Feedback becoming training data

## Attack categories by lifecycle stage

| Lifecycle stage | Example risks |
|---|---|
| Data collection | poisoned data, sensitive data ingestion, fake records |
| Labeling | malicious labels, low-quality labels, insider manipulation |
| Feature engineering | leakage, fragile features, manipulation-prone features |
| Training | compromised dependencies, secrets exposure, malicious notebooks |
| Model artifact | theft, tampering, backdoors, unsafe deserialization |
| Evaluation | benchmark leakage, weak test coverage, no adversarial tests |
| Deployment | wrong model version, no approval, no rollback |
| Inference | evasion, extraction, DoS, privacy leakage |
| Monitoring | missing abuse signals, unreviewed drift, log leakage |
| Feedback | poisoning, manipulation, persistent behavior changes |

## LLM/RAG/agent extension

Many organizations do not train their own foundation models. They still build AI systems by combining:

- A model provider
- Prompt templates
- Retrieved documents
- Embedding models
- Vector databases
- Tool/function calling
- Memory
- Logs
- Human approval workflows

These components create a new application architecture.

## Key review questions

When reviewing an ML system, ask:

1. What decision or workflow does the model influence?
2. What data shaped the model or prompt?
3. Who can write to that data?
4. Who can label or approve it?
5. How is the model artifact protected?
6. How is the model evaluated before release?
7. Can users repeatedly query the model?
8. Can users influence future training or memory?
9. What happens when the model is uncertain or wrong?
10. Can the system explain, audit, and roll back model behavior?

## Practical controls

Good ML architecture usually includes:

- Data provenance tracking
- Dataset access control
- Label quality review
- Separation of duties for high-risk labels
- Secure training pipeline
- Secrets management
- Dependency scanning
- Model signing or integrity checks
- Model registry approval workflow
- Evaluation gates
- Robustness testing
- Inference rate limits
- Abuse monitoring
- Privacy testing
- Feedback review
- Rollback plan
- Incident response process

## Main takeaway

A secure ML system protects the full lifecycle:

```text
data -> pipeline -> model -> serving -> output -> monitoring -> feedback
```

If any part of that chain is uncontrolled, the model may behave securely in tests but fail in production.
