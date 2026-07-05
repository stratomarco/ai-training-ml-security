# Toy Classifier Instructor Guide

This is the single instructor entry point for the toy-classifier labs used in Modules 03 and 10. Use the student-facing lab material for instructions, and use this guide for facilitation, debrief, and grading emphasis.

## Where this lab fits

- Module 03 uses the lab to make OWASP ML risks concrete with a small, inspectable classifier.
- Module 10 uses the same environment to discuss evasion, poisoning, model extraction, output-integrity failures, and robustness tradeoffs.
- The purpose is not to teach machine-learning performance tuning. The purpose is to show that security properties can fail around a model even when the model is small and deterministic.

## Instructor preparation

Before class, run the lab once from the app directory:

```powershell
cd labs/toy-ml-attacks/toy-classifier-app
pytest
python train.py
python attacks/evasion.py
python attacks/poisoning.py
python attacks/extraction.py
python attacks/output_integrity.py
```

Expected outcome: tests pass, the model trains locally, and each attack script prints a deterministic observation students can include in their lab report.

Student-facing entry points:

- `Classical ML attack lab`
- `Evasion and robustness lab`
- `Toy classifier app README`
- `Student debrief guide`

## How to run the session

1. Start by showing the baseline classifier and the data shape. Keep this short; students only need enough ML detail to understand what changes.
2. Have students run evasion first. The important observation is an intent-preserving input change that flips the classifier decision.
3. Move to poisoning. Ask students to separate model-quality degradation from security impact.
4. Run extraction. Emphasize that repeated queries can reveal boundary behavior even without direct model access.
5. Run output-integrity tampering. This is where students should notice that the system decision can be compromised without changing the trained model.
6. End with defense-in-depth: data validation, evaluation, provenance, monitoring, approval gates, output contracts, and rollback.

## Debrief prompts

Use these prompts after students have evidence from the scripts:

- Which attack changed the input, which changed the training process, which inferred behavior, and which changed the decision layer?
- Which failures would a normal accuracy metric miss?
- What would you log to make the failure explainable later?
- Which mitigations belong in the model pipeline, and which belong in the surrounding product system?
- What is the smallest control that would have prevented the demonstrated failure? What would still remain exposed?

## Common instructor corrections

- Do not let students describe the evasion as just a funny word swap. It is only security-relevant because malicious intent remains while the decision changes.
- Do not let poisoning become a pure data-science discussion. The security question is who can influence training data, labels, evaluation, and promotion.
- Do not let extraction be framed as only model theft. It is also reconnaissance against the decision boundary.
- Do not let output-integrity failures be dismissed as outside ML security. A model-containing system can be compromised after inference.

## Evidence students should produce

A strong submission includes:

- baseline behavior
- attack observation
- why the observed behavior matters
- control recommendation
- residual risk
- one naive mitigation that would not be enough

Reference material:

- `Strong toy-classifier lab report`
- `Weak toy-classifier lab report`
- `Lab deliverable quality checklist`
