# Module 08 Quiz — Secure MLOps and AI Supply Chain

## Questions

### 1. Why is an ML supply chain broader than a traditional software supply chain?

A. Because ML systems do not use normal software dependencies.  
B. Because ML production behavior is shaped by data, labels, features, training configuration, model artifacts, prompts, adapters, and feedback loops in addition to code and dependencies.  
C. Because ML systems do not need CI/CD.  
D. Because model files are always safe to load.

### 2. Which artifact should be treated as security-relevant?

A. Only source code.  
B. Only model files.  
C. Any artifact that can influence production behavior.  
D. Only production logs.

### 3. What is the main risk of allowing a notebook to directly produce a production model artifact?

A. Notebooks are always slower than scripts.  
B. Notebooks may mix unreviewed code, secrets, exploratory state, dependency installs, and production data access.  
C. Notebooks cannot use GPUs.  
D. Notebooks cannot load data.

### 4. What does model provenance help answer?

A. Whether the model is always fair.  
B. Which inputs, code, process, identity, and environment produced the model artifact.  
C. Whether the model will never drift.  
D. Whether prompt injection is impossible.

### 5. Which is a weak model registry design?

A. Model promotion requires approval and audit logging.  
B. Registered artifacts are immutable.  
C. Any ML engineer can mark a model as production and trigger deployment.  
D. Previous production versions are preserved for rollback.

### 6. Why is unsafe model loading a supply chain concern?

A. Loading a model can never affect security.  
B. Some artifact formats or loaders may execute code or process untrusted content unsafely.  
C. Only cloud models have loading risk.  
D. It only affects accuracy.

### 7. What is a feedback-loop security risk?

A. Feedback can improve the product.  
B. Feedback can be slow to process.  
C. Attacker-controlled or low-quality feedback may enter retraining and poison future behavior.  
D. Feedback cannot contain sensitive data.

### 8. Which gate should exist before production promotion?

A. Only accuracy above a threshold.  
B. Only a successful notebook run.  
C. Evidence of approved data, reviewed code, dependency checks, artifact integrity, evaluation, security/privacy testing where relevant, and approval.  
D. Only a Slack message from the developer.

### 9. What does signing a model artifact prove?

A. The model is safe, fair, private, and robust.  
B. The artifact has integrity relative to the signing process and identity, but it does not prove the model is safe by itself.  
C. The dataset was never poisoned.  
D. The model cannot be stolen.

### 10. What should happen if a required provenance or evaluation gate fails?

A. Deployment should proceed because ML is experimental.  
B. The deployment should stop safely or require explicit risk acceptance.  
C. The model should be renamed.  
D. The error should be hidden from the registry.

## Answer key

1. B
2. C
3. B
4. B
5. C
6. B
7. C
8. C
9. B
10. B

## Discussion prompts

1. Which controls are mandatory for a fast-moving internal ML team?
2. Which controls should be reserved for high-risk production models?
3. What is the minimum acceptable provenance record for a production model?
4. How would you prevent security gates from becoming theater?
5. How should security teams support ML engineers without blocking experimentation?
