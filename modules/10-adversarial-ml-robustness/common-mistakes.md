# Common mistakes: Adversarial ML and robustness

## Mistake 1: Treating attack success as the whole assignment

A label flip is evidence, not the final deliverable. The final deliverable is the decision: what control, fallback, monitoring, or product change follows from the label flip?

## Mistake 2: Overfitting the defense to the toy attack

Blocking the exact perturbation from the lab does not prove robustness. The lab is a teaching instrument. The control should address the class of failure.

## Mistake 3: Ignoring thresholds

Many production failures happen after the model score, when thresholds, rules, and routing logic turn probabilities into decisions. Output integrity is part of adversarial ML security.

## Mistake 4: Treating confidence as truth

A confident model can be wrong, especially outside its training distribution. Confidence should inform routing and monitoring, not replace risk analysis.

## Mistake 5: Forgetting business context

The same classifier can be low risk in one workflow and high risk in another. The security review must state what decision the model controls.

## Mistake 6: Making every model a security gate

Some models should support human prioritization rather than enforce hard decisions. A good security answer may be to reduce the model's authority.

## How to correct these mistakes in class

When a student celebrates a label flip, ask what decision the model controls. A flipped label is important only because it changes an action: allow, block, escalate, suppress, route, or ignore. The finding should name that action.

When a student proposes "train on more examples," ask what happens before retraining works. Good answers add fallback, abstention, review, monitoring, threshold governance, and release criteria. Better training is valuable, but it is not a complete security control by itself.

The expected correction is an authority answer: decide whether the model is a signal, a prioritizer, or a hard gate, and then design controls that match that authority.
