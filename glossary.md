# Glossary

## Agent

An AI-enabled system that can plan or take actions through tools, APIs, workflows, or memory. Agents are higher risk than chatbots because they can affect external systems.

## Approval gate

A control that requires a human or external policy decision before a sensitive action is executed.

## Backdoor

A hidden behavior inserted into a model or system that activates only when a specific trigger appears.

## Confused deputy

A security failure where a privileged component performs an action on behalf of an untrusted or less-privileged actor. In AI systems, this often appears when an agent uses its own tool privileges based on instructions from untrusted content.

## Direct prompt injection

A user directly instructs the model to ignore rules, reveal hidden information, or perform unsafe behavior.

## Drift

A change in data, behavior, or environment that causes a model's assumptions or performance to degrade over time.

## Embedding

A numeric representation of text, images, or other data used for similarity search and retrieval.

## Excessive agency

A design problem where an AI system has more autonomy, permissions, or action capability than it needs.

## Guardrail

A control intended to constrain, detect, or correct unsafe model or system behavior. Guardrails can include filters, policy engines, validation, approval gates, monitoring, and sandboxing.

## Indirect prompt injection

A malicious instruction is placed in content that the model later reads, such as a document, web page, ticket, email, or retrieved RAG chunk.

## Jailbreak

A prompt or interaction pattern intended to bypass model safety behavior. In application security, jailbreaks matter most when they lead to violated security properties or real system impact.

## Membership inference

An attack that attempts to determine whether a specific record was part of a model's training data.

## Model extraction

An attack that attempts to copy or approximate a model by querying it and training a substitute.

## Model inversion

An attack that attempts to infer sensitive features or reconstruct representative training data from model outputs.

## Policy engine

A component outside the model that evaluates security rules and decides whether an action is allowed.

## Poisoning

Manipulation of training data, retrieved documents, labels, feedback, or memory to influence model behavior.

## RAG

Retrieval-Augmented Generation. A pattern where a system retrieves external context and provides it to a model to improve or ground responses.

## Retrieval authorization

The process of checking whether the current user is allowed to retrieve each document or chunk before it is added to model context.

## Tool calling

A pattern where a model or orchestrator invokes functions, APIs, commands, or workflows.

## Unbounded consumption

A cost or availability failure where an AI system consumes excessive tokens, compute, API calls, or tool executions.

## Vector database

A database optimized for storing and searching embeddings by similarity.
