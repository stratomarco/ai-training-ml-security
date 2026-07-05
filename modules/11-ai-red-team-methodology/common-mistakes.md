# Common mistakes: AI red team methodology

## Mistake 1: Reporting prompts instead of findings

Prompts are evidence, not findings. A finding explains the failed control, affected asset, impact, remediation, validation, and residual risk.

## Mistake 2: Treating blocked attacks as uninteresting

A blocked attack can be valuable evidence. If poisoned memory changes intent but tool authorization blocks execution, the report should highlight that control interaction.

## Mistake 3: Testing outside scope

Out-of-scope testing creates safety, legal, and trust problems. A professional red team earns credibility by respecting boundaries.

## Mistake 4: Ignoring reproducibility

AI behavior can vary. Without role, tenant, settings, inputs, and outputs, a finding becomes hard to verify and easy to dismiss.

## Mistake 5: Overstating impact

A model saying something unsafe is not the same as a tool executing an unsafe action. Distinguish proposed action, displayed output, stored memory, and executed tool call.

## Mistake 6: Ending at exploit success

The course grades the fix and the validation, not only the exploit. If the report does not tell engineering what to change, it is incomplete.

## How to correct these mistakes in class

When a student submits a transcript, ask for the finding. The transcript is supporting evidence. The finding names the boundary, control failure, impact, remediation, validation, and residual risk.

When a student reports only successful attacks, ask what blocked attempts showed. A blocked action may prove that a control works, or that impact is lower than the initial narrative suggests. That nuance is what separates a professional red team report from a collection of screenshots.

The expected correction is decision-grade reporting: enough evidence for engineering to fix the issue and enough context for leadership to choose launch, delay, or limited pilot.
