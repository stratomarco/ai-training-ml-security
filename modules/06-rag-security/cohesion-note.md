# Cohesion note: RAG Security

## Why this module exists

This module gives students a shared way to talk about who can retrieve which context and why. It should not be taught as a list of isolated risks. It should be taught as one step in the course story: AI systems are software systems with unusual trust boundaries, feedback loops, and evidence problems.

## Language to keep consistent

Use retrieval boundary language. Avoid treating the model as the only security boundary. The central question is: how retrieval and generation inherit data-access risk?

## Handoff from the previous module

The previous module, LLM Application Security, gives students the vocabulary needed for this module. Start by reconnecting the class to that vocabulary before introducing new terms.

## Handoff to the next module

The next module, Agent and Tool Security, should feel like a consequence of this module, not a restart. End this module by naming what is still unresolved and what the next module will make concrete.

## Instructor emphasis

Keep the discussion grounded in engineering decisions. A good answer names the boundary, the evidence, the control, the validation method, and the residual risk. A weak answer only names the attack or says to add guardrails.

## Student exit line

By the end of this module, a student should be able to say: I can explain who can retrieve which context and why, show what evidence supports the risk, recommend a control, and describe how I would validate that the control worked.
