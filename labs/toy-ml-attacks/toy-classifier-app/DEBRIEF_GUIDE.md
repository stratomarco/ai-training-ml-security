# Student Debrief: Toy Classifier Lab

After running the four scripts, answer these questions before writing your final memo.

## 1. Authority

What decision does the classifier make in the scenario you are reviewing? Is it automatic enforcement, assisted triage, monitoring, or advisory output?

## 2. Evidence

For each script, record one observed before/after result.

| Script | Before | After | Security meaning |
|---|---|---|---|
| evasion.py |  |  |  |
| poisoning.py |  |  |  |
| extraction.py |  |  |  |
| output_integrity.py |  |  |  |

## 3. Naive fix

Pick one naive fix and explain why it is insufficient.

Examples:

- Block the exact words from the evasion example.
- Retrain with more data without provenance.
- Hide confidence scores but keep unlimited query access.
- Validate the model file but ignore threshold configuration.

## 4. Better control

Describe one control that changes the security property. Include how you would validate it.

## 5. Residual risk

What risk remains after your control? What monitoring, fallback, review, or rollback should exist?

## 6. Decision

Would you allow this classifier to be used as a hard gate? Answer one:

- Yes, automatic enforcement is acceptable.
- Yes, but only with step-up or review.
- No, assisted triage only.
- No, monitoring only.
- No, do not deploy yet.

Defend the answer with evidence.
