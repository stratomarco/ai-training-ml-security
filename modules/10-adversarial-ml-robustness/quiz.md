# Module 10 Quiz — Adversarial ML and Robustness

## Questions

### 1. Why is model accuracy not the same as security?

### 2. What is an evasion attack?

### 3. What is a poisoning attack?

### 4. How is a backdoor different from ordinary model error?

### 5. Why are feedback loops security-sensitive?

### 6. What is distribution shift?

### 7. What is concept drift?

### 8. Why can confidence scores be misleading in security decisions?

### 9. Name five useful robustness test categories.

### 10. Why should high-impact decisions have policy checks outside the model?

### 11. What should a safe fallback design include?

### 12. What should be included in an adversarial test plan?

---

## Answer key

### 1. Why is model accuracy not the same as security?

Accuracy usually measures performance against a test set under expected conditions. Security asks how the system behaves under malicious input, attacker adaptation, data manipulation, distribution shift, and operational failure.

### 2. What is an evasion attack?

An inference-time attack where the attacker changes the input to cause a desired model output while preserving their underlying objective.

### 3. What is a poisoning attack?

An attack where the adversary influences training data, labels, feedback, or retraining so the model learns corrupted behavior.

### 4. How is a backdoor different from ordinary model error?

A backdoor is targeted hidden behavior that activates under a trigger or condition. The model may behave normally on ordinary test cases.

### 5. Why are feedback loops security-sensitive?

Feedback can become future training data. If attackers or low-quality signals influence feedback, they may corrupt future model behavior.

### 6. What is distribution shift?

A change where production data differs from the data used during training or evaluation.

### 7. What is concept drift?

A change over time in the relationship between input features and the correct label or outcome.

### 8. Why can confidence scores be misleading in security decisions?

Confidence may not be calibrated, may not represent real-world risk, and may be unreliable under adversarial input or shifted data.

### 9. Name five useful robustness test categories.

Examples include semantic variation, formatting variation, boundary testing, edge-case testing, drift simulation, poisoning tabletop, backdoor trigger review, malformed input testing, and fallback testing.

### 10. Why should high-impact decisions have policy checks outside the model?

Because the model can be wrong or manipulated. External policy checks provide deterministic enforcement, accountability, and defense in depth.

### 11. What should a safe fallback design include?

Defined behavior for low confidence, model unavailability, suspected drift, suspected poisoning, high-impact cases, and emergency rollback or human review.

### 12. What should be included in an adversarial test plan?

Scope, assets, attacker goals, attacker control points, evasion tests, poisoning scenarios, drift tests, threshold review, fallback behavior, monitoring signals, mitigations, and residual risk.
