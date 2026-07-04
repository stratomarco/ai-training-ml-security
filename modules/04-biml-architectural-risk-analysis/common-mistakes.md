# Common Mistakes: BIML Architectural Risk Analysis

## Mistake 1: Producing a generic risk list

A list of generic AI risks does not help the team change the design.

Better approach: tie each risk to a specific architecture assumption and control location.

## Mistake 2: Waiting until implementation

By the time code is written, data stores chosen, and tools connected, important security choices may be expensive to change.

Better approach: review architecture before sensitive data and state-changing tools are connected.

## Mistake 3: Treating human review as magic

Human review is only useful when the human has time, context, authority, and evidence.

Better approach: design the approval workflow and review evidence explicitly.

## Mistake 4: Ignoring lifecycle paths

Architecture reviews often focus on inference and ignore data collection, training, promotion, monitoring, feedback, and rollback.

Better approach: review the full lifecycle.

## Mistake 5: Failing to define validation

A design recommendation without validation is easy to misunderstand or skip.

Better approach: include an acceptance test or review evidence for each major control.

## Mistake 6: Overloading prompts with security duties

Prompts are useful for behavior shaping, not for enforcing critical boundaries.

Better approach: place critical controls in application, data, tool, pipeline, and policy layers.
