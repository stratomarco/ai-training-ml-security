# Toy Classifier Debrief Guide

Use this debrief after students run the four toy-classifier scripts. The goal is to connect a small synthetic exercise to real engineering decisions without overstating what the toy model proves.

## Debrief opening

Start with this statement:

> The toy classifier is not realistic because it is supposed to be realistic. It is useful because it makes four classes of ML security failure observable, repeatable, and discussable.

Then ask students to separate three ideas:

1. What happened in the toy lab.
2. What this represents in a real ML system.
3. What evidence would be needed before changing a production control.

## Attack-by-attack debrief

### Evasion

Observed failure: the input changed enough to cross the model boundary, while the synthetic intent stayed similar.

Real-world analogue: a fraud, spam, abuse, malware, or policy classifier sees changed features that preserve attacker intent.

Engineering decision: do not use a brittle classifier as the only hard enforcement gate unless there is fallback, monitoring, challenge flow, or review.

Good control language:

- Maintain adversarial and regression test sets.
- Track confidence and uncertainty.
- Route uncertain decisions to review or step-up controls.
- Monitor feature and phrase drift.
- Avoid using the classifier as the sole authorization mechanism.

### Poisoning

Observed failure: training labels were changed and the retrained model behaved differently.

Real-world analogue: feedback loops, analyst labels, customer reports, vendor datasets, or automated labeling pipelines can corrupt training data.

Engineering decision: training data needs provenance, review, versioning, and promotion controls.

Good control language:

- Version datasets and labels.
- Separate label submission from label approval.
- Compare retrained models against clean holdout sets.
- Require promotion evidence before deployment.
- Keep rollback paths for model and data versions.

### Extraction

Observed failure: repeated queries revealed rough boundary behavior.

Real-world analogue: externally exposed models can be probed for model theft, policy bypass, or sensitive behavior inference.

Engineering decision: the model interface is an attack surface.

Good control language:

- Rate-limit suspicious query patterns.
- Minimize unnecessary confidence or explanation output.
- Monitor query distributions.
- Use tenant-aware abuse detection.
- Avoid logging sensitive user content without controls.

### Output integrity

Observed failure: decision threshold tampering changed outcomes without changing the model.

Real-world analogue: configuration or policy-layer changes can bypass model validation.

Engineering decision: protect the whole decision path, not only the model artifact.

Good control language:

- Treat thresholds and feature transforms as controlled artifacts.
- Require review for threshold changes.
- Record threshold and config versions with each decision.
- Alert on unauthorized changes.
- Test the deployed decision path, not only the model file.

## Common student mistakes

| Mistake | How to redirect |
|---|---|
| Treating the toy attack as the whole lesson | Ask what production decision it represents. |
| Saying the fix is more training data | Ask how they prevent poisoned training data. |
| Saying the fix is hiding the model | Ask whether the exposed API still leaks behavior. |
| Focusing only on accuracy | Ask whether accuracy proves safe use as a hard gate. |
| Ignoring thresholds and policy | Ask what happens if config changes after model validation. |

## Closing question

Ask each group to answer:

> In what mode would you allow this classifier to operate: automatic enforcement, assisted triage, monitoring only, or not at all?

They must defend the answer with evidence from the lab, proposed controls, validation, and residual risk.
