# Deep dive: Privacy attacks and data protection

## The decision this module teaches

This module teaches one core decision:

> What information must the system never disclose, reconstruct, infer, log, or make available across tenant or role boundaries?

Privacy in AI systems is not only a legal topic. It is a security engineering topic because AI systems often create new paths from data to disclosure. A user may not have direct database access, but they may be able to retrieve documents, query a model, inspect logs, trigger summaries, or infer facts from confidence scores.

## The privacy threat model expands the data path

Traditional access control asks whether a user can read a record. AI systems require a broader question: can a user cause the system to reveal a sensitive fact derived from a record?

The answer may involve:

- retrieved documents;
- model outputs;
- embeddings and nearest-neighbor results;
- chat transcripts;
- tool arguments;
- logs and traces;
- evaluation examples;
- fine-tuning data;
- support exports;
- analytics dashboards.

A privacy failure often happens when one of these paths is treated as lower risk than the source data. For example, a restricted document may be protected in the document store but leaked through a retrieval result, model summary, debug log, or exported trace.

## Three privacy failure modes

### 1. Direct disclosure

The system returns a sensitive fragment to a user who should not see it. BrokenPilot demonstrates this with cross-tenant retrieval when retrieval authorization is disabled.

### 2. Reconstruction or extraction

The system reveals enough pieces over time that the user reconstructs a sensitive value, profile, or training example. This may happen through repeated prompts, summaries, embeddings, or model completions.

### 3. Inference

The system reveals whether a person, tenant, document, or event is present in data even if it never returns the raw record. Membership inference is the classic example: the attacker learns that a record was likely in the training set.

## Access control is necessary but not enough

Retrieval authorization is a core privacy control, but it is not the whole story. A system can block unauthorized retrieval and still leak through logs, cached responses, evaluation exports, or traces. This is the defense-in-depth lesson for Module 09.

A strong privacy design asks:

- Who can retrieve the source?
- Who can see the model output?
- Who can see logs and traces?
- How long are outputs retained?
- Are sensitive fragments redacted before storage?
- Can support or analytics tooling bypass normal tenant boundaries?
- What evidence proves that the control works?

## What students should stop believing

Students should stop treating privacy as a final compliance review. In AI systems, privacy is an architectural property. It must be designed into retrieval, prompting, logging, evaluation, retention, and access review.

Students should also stop believing that fake or synthetic labs make privacy less important. The course uses fake secrets to avoid harm, but the control lesson is real: restricted data must stay inside its authorized boundary through every system path.

## Lab transfer

In the BrokenPilot privacy lab, students should observe the security property directly:

- with retrieval authorization disabled, a beta user can retrieve alpha restricted material;
- with retrieval authorization enabled, the retrieval path blocks it;
- the remaining question is whether other paths, especially logs and traces, still expose sensitive fragments.

That last question is what makes the lab more than a simple access-control exercise. Privacy controls must cover the entire data path, not only the first read.
