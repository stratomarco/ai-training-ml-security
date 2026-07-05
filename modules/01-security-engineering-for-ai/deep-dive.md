# Deep Dive: Security Engineering for AI

## What this module is really about

This module is not about memorizing AI risk lists. It is about learning to treat an AI feature as a security-relevant system. The model matters, but the system around the model usually decides whether the failure becomes a harmless odd answer, a privacy incident, an unauthorized action, or a production outage.

A useful mental model is simple: AI changes the shape of uncertainty, but it does not remove the need for security engineering. Inputs still cross trust boundaries. Outputs still flow into sinks. Privileges still need to be scoped. Logs still leak. Supply chains still need provenance. Users still abuse ambiguity. The difference is that part of the system now makes probabilistic decisions from untrusted data, and that probabilistic component is often placed in positions where deterministic controls used to be.

The first security question is therefore not "Which AI attack applies?" It is: "What decision, boundary, asset, or privilege has the AI system been allowed to influence?"

## The core engineering decision

By the end of this module, a student should be able to decide whether a proposed AI feature is:

1. A low-risk assistant that only drafts or summarizes content.
2. A decision-support component that influences human decisions.
3. A control-plane component that can retrieve sensitive data, trigger tools, change state, or affect customers.
4. A security-critical gate that must not rely on model behavior alone.

That classification drives the controls. A summarizer can tolerate mistakes if data boundaries and output sinks are controlled. An incident agent that can close tickets, modify documents, or trigger operational workflows needs authorization, approval, audit, rollback, and abuse-case coverage. A model used as an access-control decision point needs an entirely different risk argument, and often should not be used as the only gate.

## Why classic security still applies

Many AI failures look new only because the mechanism is new. The engineering principles are old.

Least privilege still matters. A model that can call a tool should receive only the permissions needed for that action, not the permissions of the user, developer, or service account by default.

Complete mediation still matters. Every sensitive action needs authorization at the point of action. It is not enough to check whether the conversation seemed safe earlier.

Economy of mechanism still matters. A fragile chain of prompts, retrieval rules, hidden conventions, and undocumented tool behavior is difficult to reason about. Security-critical behavior should be explicit, small, and testable.

Fail-safe defaults still matter. When the model is unsure, when retrieval is incomplete, when policy is ambiguous, or when a tool argument cannot be validated, the system should fail closed or ask for review instead of guessing.

Separation of privilege still matters. The component that proposes an action should not be the same component that authorizes the action. In agent systems this becomes one of the most important design rules: the model may propose, but the system must decide and enforce.

## What changes with AI

AI systems add several patterns that classic security teams must learn to see.

First, untrusted text can act like instructions. A support ticket, document, web page, chat message, or retrieved note may contain text that tries to override the system's goal. The root cause is not "the model is bad." The root cause is that the system failed to preserve the distinction between data and authority.

Second, behavior is probabilistic. A test that passes once does not prove the control works. Security validation must focus on enforced boundaries, not only model responses. If the control is implemented outside the model, a single deterministic test can prove the boundary. If the control relies on the model refusing, the test proves much less.

Third, the data lifecycle becomes part of the attack surface. Training data, fine-tuning data, retrieval corpora, embeddings, feedback logs, prompts, evaluation sets, and monitoring data can all carry sensitive information or malicious instructions.

Fourth, model output often flows into other systems. If output is displayed as HTML, inserted into a ticket, passed as a tool argument, stored in memory, used as a query, or sent to a user, the receiving context determines the required validation.

## Security mindset for AI features

A strong review does not start with a list of attacks. It starts with system intent.

What is the AI feature supposed to help someone do? What action can it influence? What data can it read? What data can it write? What external systems can it reach? What would be embarrassing, expensive, unsafe, illegal, or operationally disruptive if the AI feature behaved incorrectly?

Then the review maps boundaries. Which inputs are trusted? Which are user-controlled? Which are retrieved from sources with different owners? Which outputs are only displayed, and which outputs are executed, stored, or used to change state?

Only after that does the reviewer map attack types. Prompt injection, poisoning, model extraction, privacy leakage, excessive agency, supply-chain compromise, and adversarial examples are not independent checkboxes. They are ways the system can violate a boundary or control objective.

## Security properties to name explicitly

AI reviews are stronger when they name the security property being protected.

Confidentiality: the system must not reveal restricted data, secrets, private records, or cross-tenant information.

Integrity: the system must not let untrusted text, poisoned data, tampered artifacts, or model output corrupt decisions, documents, tools, or workflows.

Availability: the system must not be easy to overload, stall, route into expensive loops, or make critical workflows unavailable.

Authorization: the system must not use a model response as proof that an action is allowed.

Accountability: the system must preserve enough evidence to understand what happened, who requested it, what context was used, which control allowed or blocked it, and how to recover.

Privacy: the system must avoid leaking, memorizing, reconstructing, inferring, logging, or over-retaining personal and sensitive data.

## A practical review sequence

A practical AI security review can follow this order:

1. Describe the user goal and business workflow.
2. Identify assets, actions, and decisions influenced by the model.
3. Draw trust boundaries around users, retrieved content, tools, data stores, model services, logs, and external integrations.
4. List credible abuse cases.
5. Identify where deterministic controls must exist outside the model.
6. Decide which failures can be tolerated, which need human review, and which must be technically impossible.
7. Write validation tests for the controls.
8. Define residual risk and monitoring.

The goal is not to make AI perfect. The goal is to make the system safe enough for the role it plays, and honest about what remains uncertain.

## Reading-to-lab transfer

When students move from this module into later labs, they should carry one question with them: "Where is the security boundary actually enforced?"

In BrokenPilot, the most important lessons happen when the model is wrong or manipulated, but a separate system control still blocks unsafe execution. In the toy-classifier lab, the most important lesson is that model confidence is not the same as a security guarantee. In the MLOps evidence pack, the most important lesson is that a model artifact without provenance and promotion evidence is not ready for production, even if it performs well in a notebook.

## Exit ticket

A student is ready to leave this module if they can explain this sentence in their own words:

"The model may influence a decision, but the system must define, enforce, validate, and audit the security boundary."
