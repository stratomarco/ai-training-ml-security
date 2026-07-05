# Module 08 Slides  -  Secure MLOps and AI Supply Chain

## Slide 1  -  Title

# Secure MLOps and AI Supply Chain

Securing the path from data to production model behavior.

---

## Slide 2  -  Why this module matters

In traditional software, supply chain security asks:

> Can we trust the code, dependencies, build, and artifact?

In ML systems, we must also ask:

> Can we trust the data, labels, training job, model artifact, prompts, adapters, embeddings, evaluation results, and feedback loop?

---

## Slide 3  -  Core thesis

# ML pipelines are software supply chains with extra artifacts.

The production model is shaped by:

- data;
- labels;
- features;
- code;
- parameters;
- dependencies;
- containers;
- training infrastructure;
- evaluation gates;
- registry permissions;
- deployment workflows;
- feedback data.

---

## Slide 4  -  What is MLOps?

MLOps is the engineering discipline for moving ML systems from experimentation to production.

It usually includes:

- data management;
- feature generation;
- training orchestration;
- model evaluation;
- model registry;
- deployment;
- monitoring;
- retraining;
- rollback.

Secure MLOps adds security controls to each stage.

---

## Slide 5  -  The ML supply chain

```text
data source -> dataset -> labels -> features -> training code
     -> dependencies -> training job -> model artifact
     -> evaluation -> registry -> deployment -> inference
     -> monitoring -> feedback -> retraining
```

Every arrow is a trust decision.

---

## Slide 6  -  Classic supply chain risks still apply

Examples:

- dependency confusion;
- typosquatting;
- compromised package;
- malicious build step;
- leaked CI/CD secret;
- overprivileged runner;
- unsigned artifact;
- weak registry permissions;
- production deployment without review.

ML does not remove these risks.

---

## Slide 7  -  ML adds new supply chain risks

ML systems add artifacts such as:

- datasets;
- labels;
- features;
- embeddings;
- vector indexes;
- prompts;
- adapters and LoRA weights;
- model checkpoints;
- tokenizer files;
- evaluation datasets;
- model cards;
- monitoring feedback.

Each artifact can be wrong, poisoned, tampered with, leaked, or misused.

---

## Slide 8  -  Security goal

A secure ML delivery process should prove or strongly evidence:

1. where the model came from;
2. what produced it;
3. who approved it;
4. what it was tested against;
5. why it was allowed into production;
6. how it can be removed or rolled back.

---

## Slide 9  -  Dataset provenance

Dataset questions:

- Who owns the data?
- Where did it come from?
- Is it licensed for this use?
- Does it contain sensitive data?
- Was it modified?
- Who can write to it?
- How is lineage tracked?
- Can bad records be removed?

Data is part of the program.

---

## Slide 10  -  Label integrity

Labels can be attacked or corrupted.

Risks:

- malicious label changes;
- low-quality labeling;
- biased or inconsistent labeling;
- insider tampering;
- feedback abuse;
- poisoned examples inserted into retraining.

Controls:

- review sampling;
- anomaly detection;
- dual review for critical labels;
- lineage;
- labeler identity;
- rollback.

---

## Slide 11  -  Notebook security

Notebooks are often treated as experiments.

But notebooks may contain:

- secrets;
- production data access;
- shell commands;
- dependency installs;
- unsafe downloads;
- unreviewed code;
- exported models.

A notebook can become the build script for a production model.

---

## Slide 12  -  Dependency risk

ML projects often rely on large Python dependency graphs.

Risks:

- unpinned versions;
- vulnerable packages;
- malicious packages;
- dependency confusion;
- GPU-specific packages from unclear sources;
- abandoned libraries;
- unsafe model helper utilities.

Controls:

- lockfiles;
- dependency scanning;
- internal package mirrors;
- review of high-risk dependencies;
- reproducible environments.

---

## Slide 13  -  Training environment risk

Training jobs often have access to:

- large datasets;
- cloud storage;
- GPUs;
- secrets;
- model registries;
- artifact stores;
- experiment tracking systems.

Compromising training infrastructure can compromise the model and the data.

---

## Slide 14  -  Model artifact risk

A model artifact may contain:

- learned behavior;
- memorized data;
- malicious triggers;
- unsafe serialized objects;
- metadata;
- tokenizer files;
- adapters;
- configuration files.

Treat model files as untrusted artifacts until proven otherwise.

---

## Slide 15  -  Unsafe model loading

Some model formats and loading patterns can execute code or trigger unsafe behavior.

Bad pattern:

```python
model = load_untrusted_model("random_model.pkl")
```

Security question:

> What is the trust boundary around this artifact?

Controls include safe formats, sandboxing, provenance, scanning, and restricted loaders.

---

## Slide 16  -  Model registry security

A model registry is a production control point.

It should enforce:

- authentication;
- role-based access;
- write restrictions;
- artifact immutability;
- version history;
- approval workflow;
- signing or integrity checks;
- promotion gates;
- audit logs;
- rollback.

---

## Slide 17  -  Promotion workflow

Not every model should reach production.

Promotion should require evidence:

- approved data source;
- reviewed training code;
- dependency scan;
- container scan;
- provenance record;
- evaluation metrics;
- adversarial/security tests;
- privacy review;
- owner approval;
- rollback plan.

---

## Slide 18  -  Prompt and adapter supply chain

LLM systems add more artifacts:

- system prompts;
- prompt templates;
- tool schemas;
- policy prompts;
- RAG chunking logic;
- embeddings;
- vector indexes;
- LoRA/adapters;
- model routing rules.

These need versioning, review, access control, and rollback.

---

## Slide 19  -  Vector index supply chain

Vector indexes are derived artifacts.

Security questions:

- Which documents produced this index?
- Were ACLs preserved during chunking?
- Are chunks tenant-scoped?
- Who can write or update embeddings?
- Can poisoned content enter retrieval?
- Can old sensitive content be removed?

---

## Slide 20  -  Secrets in ML workflows

Common secret locations:

- notebooks;
- environment variables;
- pipeline YAML;
- experiment tracking logs;
- model registry metadata;
- container images;
- training logs;
- prompt logs.

Do not let experiments become secret storage.

---

## Slide 21  -  SBOM and ML-BOM thinking

A software bill of materials lists software components.

An ML bill of materials should also capture:

- datasets;
- data versions;
- feature sets;
- model base version;
- adapters;
- training code;
- evaluation sets;
- dependencies;
- container image;
- artifact hash;
- approvals.

---

## Slide 22  -  Provenance

Provenance answers:

- what was built;
- how it was built;
- from which inputs;
- by which process;
- under which identity;
- with which environment;
- producing which artifact.

Without provenance, production trust becomes guesswork.

---

## Slide 23  -  Reproducibility

Reproducibility supports security.

It helps answer:

- can we rebuild this model?
- can we compare the rebuilt artifact?
- can we investigate a bad release?
- can we remove bad data and retrain?
- can we prove which version is deployed?

Perfect reproducibility may be hard, but traceability is still required.

---

## Slide 24  -  Evaluation as a gate

Evaluation should not be only accuracy.

Include:

- security tests;
- privacy leakage tests;
- robustness tests;
- abuse-case tests;
- regression tests;
- fairness/safety checks where relevant;
- cost and latency tests;
- RAG and agent behavior tests.

A model that passes accuracy but fails security should not ship.

---

## Slide 25  -  Feedback loop risk

Feedback loops are useful and dangerous.

Risks:

- attacker submits malicious feedback;
- bad outputs become future training data;
- production abuse contaminates evaluation;
- poisoned data quietly enters retraining;
- sensitive prompts are retained too long.

Controls:

- quarantine;
- sampling review;
- abuse detection;
- retention limits;
- provenance tags.

---

## Slide 26  -  Runtime and infrastructure

Secure deployment also requires:

- isolated inference workloads;
- least-privilege runtime identities;
- egress controls;
- API authentication;
- rate limits;
- logging;
- GPU workload hardening;
- tenant isolation;
- monitoring.

MLOps is not finished at deployment.

---

## Slide 27  -  Rollback and emergency response

Production models need rollback.

Questions:

- Can we disable the model quickly?
- Can we route traffic to a previous version?
- Can we remove a poisoned dataset?
- Can we revoke a compromised model artifact?
- Can we identify affected users or outputs?
- Can we investigate the pipeline history?

---

## Slide 28  -  Common anti-patterns

Watch for:

- production model from a laptop notebook;
- shared admin credentials for registry access;
- public model pulled directly into production;
- no dataset lineage;
- no artifact hash;
- no dependency lockfile;
- no security gate;
- no rollback;
- retraining directly from user feedback.

---

## Slide 29  -  Better pattern

A better pattern:

```text
reviewed data + reviewed code + locked dependencies
  -> controlled training job
  -> signed/provenanced artifact
  -> security/evaluation gates
  -> registry promotion
  -> scoped production deployment
  -> monitored inference
  -> controlled feedback loop
```

---

## Slide 30  -  Student exercise

Students receive a broken ML pipeline.

They must identify:

- supply chain risks;
- missing controls;
- unsafe artifacts;
- weak identities;
- registry risks;
- evaluation gaps;
- deployment risks;
- feedback-loop risks.

Then they design a secure promotion workflow.

---

## Slide 31  -  Deliverable

The final deliverable is a Secure MLOps review with:

- architecture summary;
- artifact inventory;
- risk register;
- security gates;
- registry controls;
- provenance requirements;
- rollback plan;
- residual risk.

---

## Slide 32  -  Discussion question

You are asked to ship a model quickly.

The team says:

> It is only an internal model. We can add provenance and registry controls later.

How do you balance developer velocity with production security?

---

## Slide 33  -  Main takeaway

# Secure MLOps is production security.

If you cannot trace, verify, approve, deploy, monitor, and rollback model artifacts, you cannot responsibly operate them.

---

## Slide 34  -  Bridge to next module

Module 9 focuses on privacy attacks and data protection.

Secure MLOps prepares that discussion by asking:

- which data enters the system;
- where sensitive data is stored;
- how prompts and logs are retained;
- how training data can leak;
- how privacy controls fit into the pipeline.
