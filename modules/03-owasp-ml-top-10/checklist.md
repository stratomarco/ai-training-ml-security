# Module 03  -  OWASP ML Security Top 10 Checklist

Use this checklist during design review, threat modeling, or security testing of classical ML systems.

## 1. System context

- [ ] What decision does the model influence?
- [ ] Is the model advisory or authoritative?
- [ ] Who relies on the model output?
- [ ] What happens when the model is wrong?
- [ ] Is there a human review path for high-impact decisions?
- [ ] Are model limitations documented?

## 2. Assets

- [ ] Training data identified.
- [ ] Label data identified.
- [ ] Feature pipeline identified.
- [ ] Evaluation data identified.
- [ ] Model artifact identified.
- [ ] Model registry identified.
- [ ] Inference API identified.
- [ ] Output and post-processing logic identified.
- [ ] Logs and monitoring data identified.
- [ ] Feedback loop identified.

## 3. ML01  -  Input manipulation

- [ ] Are inference inputs validated and normalized?
- [ ] Are out-of-distribution inputs detected?
- [ ] Are adversarial or abuse-case inputs included in testing?
- [ ] Is there rate limiting for suspicious input patterns?
- [ ] Does the system have safe fallback behavior?
- [ ] Are high-risk predictions reviewed or challenged?

## 4. ML02  -  Data poisoning

- [ ] Is data provenance tracked?
- [ ] Are training data sources trusted and documented?
- [ ] Are labels reviewed or sampled for quality?
- [ ] Are data changes versioned?
- [ ] Are anomalous training records detected?
- [ ] Is poisoned data removable or quarantinable?
- [ ] Can the model be retrained from a known-good dataset?

## 5. ML03  -  Model inversion

- [ ] Could outputs reveal sensitive features?
- [ ] Are confidence scores necessary?
- [ ] Are outputs minimized to what users need?
- [ ] Is access to sensitive model endpoints restricted?
- [ ] Is repeated probing detected?
- [ ] Has privacy testing been performed?

## 6. ML04  -  Membership inference

- [ ] Is training membership sensitive?
- [ ] Are outputs calibrated or minimized?
- [ ] Are overfitting risks evaluated?
- [ ] Are high-confidence outputs necessary?
- [ ] Are privacy-preserving techniques considered where appropriate?
- [ ] Is query abuse monitored?

## 7. ML05  -  Model theft

- [ ] Are model artifacts protected by access control?
- [ ] Are model registries private and audited?
- [ ] Are downloads logged?
- [ ] Are inference APIs rate-limited?
- [ ] Is unusual query behavior monitored?
- [ ] Are secrets and credentials separated from notebooks and training jobs?
- [ ] Is model IP classified as an asset?

## 8. ML06  -  AI supply chain attacks

- [ ] Are datasets, models, dependencies, and containers inventoried?
- [ ] Are model artifacts signed or checksummed?
- [ ] Are dependencies pinned and scanned?
- [ ] Are notebooks reviewed before production use?
- [ ] Are model registries access-controlled?
- [ ] Are third-party models evaluated before use?
- [ ] Is there a rollback path for compromised artifacts?

## 9. ML07  -  Transfer learning attacks

- [ ] Is the base model source trusted?
- [ ] Is model provenance documented?
- [ ] Is the pretrained model evaluated for the intended domain?
- [ ] Are inherited backdoor risks considered?
- [ ] Are licenses and data-use constraints reviewed?
- [ ] Is fine-tuning data validated?

## 10. ML08  -  Model skewing

- [ ] Does the system use production feedback for future training?
- [ ] Can attackers influence feedback?
- [ ] Are feedback sources weighted or trusted differently?
- [ ] Is drift monitored?
- [ ] Are sudden distribution changes investigated?
- [ ] Are coordinated manipulation attempts detected?

## 11. ML09  -  Output integrity

- [ ] Is model output protected from tampering?
- [ ] Are thresholds and post-processing rules access-controlled?
- [ ] Are output changes logged?
- [ ] Are explanations or reports generated safely?
- [ ] Is downstream decision logic reviewed?
- [ ] Can output integrity be verified during incident response?

## 12. ML10  -  Model poisoning

- [ ] Are model artifacts immutable after approval?
- [ ] Are registry writes restricted?
- [ ] Are model deployments approved?
- [ ] Are artifacts signed or integrity checked?
- [ ] Are training runs reproducible?
- [ ] Are independent evaluation checks performed before deployment?
- [ ] Can the system roll back to a known-good model?

## 13. Monitoring and response

- [ ] Are model behavior changes monitored?
- [ ] Are data drift and concept drift monitored?
- [ ] Are suspicious queries logged?
- [ ] Are anomalous training or feedback records detected?
- [ ] Are model deployments auditable?
- [ ] Is there an ML-specific incident response playbook?
- [ ] Are model owners and security owners defined?

## 14. Residual risk

- [ ] Which attacks are reduced but not eliminated?
- [ ] Which controls are intentionally deferred?
- [ ] Which risks require leadership acceptance?
- [ ] Which risks require product or business process change?
- [ ] Is residual risk documented in plain language?
