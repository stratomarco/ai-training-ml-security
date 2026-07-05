# Teaching Modules 08 to 11 after the depth pass

## Purpose

Modules 08 to 11 are reading-heavy compared with the BrokenPilot agent labs. This guide helps instructors keep them practical and decision-driven.

## Module 08

Keep the discussion focused on evidence. The student should leave able to say whether a model artifact can be promoted and why. Do not let the class drift into generic dependency scanning only.

Best classroom question: what exact evidence binds the evaluated model to the deployed model?

## Module 09

Keep the discussion focused on data paths. Privacy is not only what the model says to the user. It includes retrieval, logs, traces, support tooling, retention, and inference.

Best classroom question: where else could the sensitive fragment go after the first control is fixed?

## Module 10

Keep the discussion focused on model authority. The toy classifier is small by design. The lesson is whether the model should be a hard gate and what controls are required if it is.

Best classroom question: what happens if the model is wrong in the direction an attacker wants?

## Module 11

Keep the discussion focused on evidence for decisions. A red team report is not a prompt transcript. It is a decision document for engineering and leadership.

Best classroom question: what evidence would change the launch decision?

## Grading reminder

For every module in this block, reward:

- evidence;
- root cause;
- implementable control;
- validation;
- residual risk;
- clear recommendation.

Do not reward only the number of issues found.
