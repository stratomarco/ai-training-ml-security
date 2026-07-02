# Module 03  -  Quiz

## Questions

### 1. Why is model accuracy not enough to claim that an ML system is secure?

A. Accuracy does not measure adversarial robustness, privacy leakage, supply chain integrity, or access control.  
B. Accuracy is never useful.  
C. Accuracy only applies to LLM systems.  
D. Accuracy automatically includes security testing.

### 2. Which OWASP ML category best describes an attacker modifying an inference-time input so the model misclassifies it?

A. Model theft  
B. Input manipulation  
C. Model inversion  
D. Transfer learning attack

### 3. Which category is primarily about corrupting training or feedback data?

A. Data poisoning  
B. Output integrity  
C. Model theft  
D. Membership inference

### 4. Which category asks whether an attacker can determine if a specific record was part of the training set?

A. Model skewing  
B. Membership inference  
C. Input manipulation  
D. Output integrity

### 5. What is the main difference between model inversion and model theft?

A. Model inversion targets privacy leakage; model theft targets the model or its behavior as an asset.  
B. Model inversion only affects networks; model theft only affects images.  
C. Model inversion is always harmless.  
D. There is no difference.

### 6. Which of the following is part of the ML supply chain?

A. Dataset  
B. Training script  
C. Model artifact  
D. All of the above

### 7. A recommender system uses user feedback to retrain every week. Attackers create many fake accounts to shape recommendations. Which category is most relevant?

A. Model skewing  
B. Model inversion  
C. Output integrity  
D. Transfer learning attack

### 8. An attacker changes the threshold used after model inference so more transactions are approved. Which category is most relevant?

A. Output integrity attack  
B. Membership inference  
C. Transfer learning attack  
D. Model inversion

### 9. Which control is most directly useful for protecting model artifacts in a registry?

A. Artifact signing and registry access control  
B. Larger training data  
C. More GPUs  
D. A longer model card only

### 10. What is a good residual-risk statement?

A. “All risk is gone.”  
B. “The model is accurate, so no risk remains.”  
C. “Input manipulation risk is reduced by validation, monitoring, and review, but adaptive attackers may still find bypasses.”  
D. “Security owns this completely.”

## Answer key

1. A
2. B
3. A
4. B
5. A
6. D
7. A
8. A
9. A
10. C

## Short-answer questions

### 1. Pick one OWASP ML category and explain the relevant lifecycle stage.

Expected answer should name the category, identify a stage such as training, inference, registry, monitoring, or feedback, and explain what the attacker can influence.

### 2. Give one preventive, one detective, and one recovery control for data poisoning.

Example answer:

- Preventive: dataset provenance and source validation.
- Detective: anomaly detection in training data or behavior changes.
- Recovery: quarantine poisoned data and retrain from known-good version.

### 3. Explain why model theft can happen through API access even if the attacker cannot download the model file.

Expected answer should mention repeated queries, observing outputs, approximating model behavior, and the need for rate limits, output minimization, and query monitoring.

### 4. What is the difference between securing the model and securing the model-dependent decision?

Expected answer should explain that the decision also includes input handling, feature pipelines, thresholds, post-processing, downstream systems, human review, and business workflow.
