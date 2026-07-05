from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MARKER_START = "<!-- module-depth-prose-pass-08-11:start -->"
MARKER_END = "<!-- module-depth-prose-pass-08-11:end -->"

MODULES = {
    "08-secure-mlops-supply-chain": {
        "title": "Module 08 depth pass: Secure MLOps and AI supply chain",
        "files": {
            "deep-dive.md": r'''# Deep dive: Secure MLOps and AI supply chain

## The decision this module teaches

This module teaches one core decision:

> Can this model artifact be promoted, deployed, and operated with enough evidence that we trust where it came from, what it depends on, and how it can be rolled back?

That is a different question from whether the model is accurate. Accuracy says something about observed behavior on an evaluation set. Supply-chain security says something about provenance, integrity, repeatability, access control, and operational control over the path from data to production.

In a real organization, most AI supply-chain failures are not dramatic. They look like normal engineering shortcuts:

- a notebook installs packages at runtime;
- a dataset is pulled from a shared bucket without a stable hash;
- a model is exported as a mutable `latest` artifact;
- a registry allows promotion without independent approval;
- a training secret is copied into a notebook or log;
- a CI job evaluates accuracy but never verifies artifact identity;
- rollback depends on someone remembering which file was good.

The security problem is that these shortcuts remove evidence. When evidence disappears, a team cannot answer basic launch and incident questions: what changed, who approved it, what data was used, what code ran, what artifact is deployed, and how to return to a known-good state.

## The supply chain is the security boundary

Traditional application security often focuses on code review, dependency scanning, identity, and runtime hardening. ML systems still need those controls, but the trust boundary expands. The model artifact, training data, feature code, evaluation logic, prompts, retrieval index, registry metadata, and deployment pipeline all become part of the system that can change production behavior.

A model does not have to be malicious to be risky. It can be stale, trained on the wrong slice, evaluated with the wrong metric, exported from a compromised environment, loaded from a mutable path, or promoted by a workflow that checks the wrong thing. The lesson is not that every model artifact is hostile. The lesson is that production behavior depends on a chain of artifacts, and the team needs evidence for the chain.

## What students should stop believing

A common mistake is to treat MLOps supply-chain security as dependency scanning plus a model registry. Those are useful, but not sufficient. A registry that stores a model without signed metadata, immutable versioning, training-data references, approval evidence, evaluation reports, and rollback linkage is mostly a filing cabinet.

Another mistake is to assume that reproducibility is a research nicety. In production security, reproducibility is an incident-response control. If the model behaves badly and the team cannot reconstruct the training run or identify the promoted artifact, the team cannot do root-cause analysis with confidence.

## Good evidence looks boring

Strong supply-chain evidence is not flashy. It usually looks like boring records:

- dataset identifiers and hashes;
- dependency lockfiles;
- training code commit;
- image digest;
- model artifact digest;
- evaluation report tied to that exact artifact;
- promotion approval;
- deployment record;
- rollback target;
- monitoring plan.

The evidence pack lab is designed around this reality. Students are not asked to run a toy pipeline. They inspect a realistic set of weak artifacts and decide whether promotion should proceed. That is how many engineers, security reviewers, and platform teams encounter MLOps risk in practice.

## The main engineering tradeoff

The tradeoff is not "security versus speed". The real tradeoff is between fast undocumented movement and fast repeatable movement.

A mature platform makes the secure path the easy path: default lockfiles, default artifact digests, default registry metadata, default approval gates, default rollback records, and default evaluation templates. Security work should reduce custom review burden over time, not add a bespoke meeting to every model release.

## Lab transfer

When students move from this reading to the evidence-pack lab, they should look for missing evidence before looking for exotic attacks. Ask:

1. Can we identify the exact artifact proposed for production?
2. Can we identify the exact data and code used to create it?
3. Can we tell whether the artifact was tampered with after training?
4. Can we tell who approved promotion and on what basis?
5. Can we roll back to a known-good version?
6. Can we explain the residual risk to a product or engineering leader?

If the answer to any of these is no, the finding should focus on the broken control path, not only the suspicious file.
''',
            "attack-anatomy.md": r'''# Attack anatomy: MLOps supply-chain failure

## Scenario

A team trains a fraud-prioritization model in a notebook. The notebook installs dependencies at runtime, reads training data from a shared bucket, exports `model.pkl`, and uploads it to a model registry under a mutable `latest` path. The CI promotion workflow checks that accuracy is above a threshold and then deploys the model.

Nothing in this story requires an advanced attacker. It can fail through accident, insider shortcut, compromised dependency, compromised storage, or weak promotion rules.

## Path 1: dependency drift

1. The notebook runs `pip install` without pinned versions.
2. A newer package version changes preprocessing behavior.
3. The model is retrained and passes a narrow accuracy check.
4. Production behavior changes, but the team cannot reproduce the old result.
5. Incident review cannot prove whether the change came from code, data, or dependencies.

Security property lost: repeatability.

Good finding: the pipeline lacks dependency locking and training-environment identity, so model behavior cannot be reproduced or audited after release.

Weak finding: dependencies should be updated carefully.

## Path 2: artifact tampering

1. The registry stores an artifact under `models/latest/model.pkl`.
2. A user or job with write access replaces the file.
3. The promotion workflow reads the mutable path.
4. The deployment job does not verify a signed manifest or expected digest.
5. A different artifact reaches production than the one evaluated.

Security property lost: artifact integrity.

Good finding: production promotion accepts a mutable artifact URI without digest verification, so evaluation and deployment are not bound to the same object.

Weak finding: the model registry needs better security.

## Path 3: poisoned or wrong data

1. Training data comes from a shared bucket.
2. The training metadata records a bucket path but not a dataset version or hash.
3. A data slice is changed before retraining.
4. Evaluation still passes aggregate accuracy.
5. A protected segment or high-risk case type is degraded.

Security property lost: data provenance.

Good finding: the training run records a mutable data location but no dataset identity, so reviewers cannot prove which records shaped the promoted model.

Weak finding: the data should be protected.

## Path 4: approval bypass

1. A workflow promotes any model with accuracy above 0.90.
2. No security approval, rollback target, model-card review, or risk owner signoff is required.
3. A model with weak provenance is promoted because the metric passes.
4. The release later causes business or privacy harm.

Security property lost: controlled promotion.

Good finding: promotion is metric-only and lacks independent checks for provenance, artifact identity, privacy risk, and rollback readiness.

Weak finding: the approval process should be improved.

## What makes this an AI security issue

The risk is not that the system uses ML. The risk is that production decisions now depend on artifacts and metadata outside normal application-code review. The model is part of the supply chain. If the organization cannot control that chain, it cannot make a trustworthy launch decision.
''',
            "controls-and-remediations.md": r'''# Controls and remediations: Secure MLOps and AI supply chain

## Control objective

The goal is to bind production behavior to reviewed evidence. A deployed model should be traceable to the data, code, dependencies, training environment, evaluation result, approval decision, and artifact digest that justified its release.

## Weak controls

Weak controls sound useful but do not create reliable evidence:

- "Use a model registry" without immutable versions or approval policy.
- "Scan dependencies" without a lockfile or training image digest.
- "Check accuracy" without checking the artifact identity that was evaluated.
- "Restrict bucket access" while allowing shared write paths for training data.
- "Document the release" after promotion instead of enforcing metadata before promotion.
- "Use a private notebook" while storing secrets, runtime installs, and exports in the notebook.

These controls may reduce some risk, but they do not answer the main question: can we prove that the promoted artifact is the reviewed artifact?

## Strong controls

Strong controls make the secure path enforceable:

1. **Immutable model artifacts**
   - Store every artifact under a versioned immutable path.
   - Record a digest for the exact artifact.
   - Reject promotion if the digest does not match the evaluated artifact.

2. **Training-run identity**
   - Record training code commit, data version, dependency lockfile, container image digest, and runtime parameters.
   - Treat missing metadata as a failed release gate, not a warning.

3. **Dataset provenance**
   - Use dataset version IDs or content hashes.
   - Separate read and write permissions for training data.
   - Record dataset approval and retention classification.

4. **Dependency and environment control**
   - Use lockfiles for Python dependencies.
   - Build training images from reviewed manifests.
   - Avoid runtime installs in production training jobs.

5. **Promotion policy**
   - Require checks for accuracy, robustness, privacy, provenance, and rollback readiness.
   - Require human approval for high-impact models.
   - Store approval evidence with the release record.

6. **Artifact signing or attestation**
   - Sign model artifacts or sign release manifests.
   - Verify signatures and digests before deployment.
   - Fail closed on mismatch.

7. **Rollback readiness**
   - Record the last known-good artifact.
   - Test rollback in staging.
   - Keep compatibility notes for feature schemas and serving code.

## Remediation backlog format

A strong remediation backlog should use implementation language, not aspiration language:

- Add a promotion gate that rejects artifacts without a digest and training-run ID.
- Modify the registry schema to require dataset version, code commit, image digest, and approval owner.
- Replace mutable `models/latest/model.pkl` deployment input with immutable artifact IDs.
- Add CI verification that deployed digest equals evaluated digest.
- Remove runtime `pip install` from notebooks used for release training.
- Move secrets from notebooks to managed secret storage and block secret-like strings in committed notebooks.

## Validation

A remediation is not complete when the policy is written. It is complete when the team can demonstrate enforcement:

- Try to promote an artifact without a digest. It should fail.
- Try to promote an artifact whose digest differs from the evaluation record. It should fail.
- Try to train from a mutable data path without a dataset version. It should fail.
- Try to deploy a model without a rollback target. It should fail or require explicit risk acceptance.

## Residual risk

Even with strong controls, residual risk remains:

- The approved data may still be biased or incomplete.
- The evaluation may miss important operating conditions.
- A signed artifact may still encode unsafe behavior.
- A rollback may not fix downstream decisions already taken.

A good review states this clearly. Supply-chain controls prove origin and integrity. They do not prove that the model is good for every use.
''',
            "common-mistakes.md": r'''# Common mistakes: Secure MLOps and AI supply chain

## Mistake 1: Treating model accuracy as release approval

Accuracy is an input to release approval. It is not approval. A model can be accurate on a benchmark and still have unknown provenance, weak privacy controls, no rollback plan, or a tampered artifact path.

Better question: what evidence ties this exact artifact to the exact evaluation result?

## Mistake 2: Assuming the registry is the control

A registry is only a control if it enforces immutability, metadata, access control, promotion workflow, and auditability. A registry that accepts arbitrary uploads and mutable paths is just storage with a nicer interface.

Better question: what does the registry reject?

## Mistake 3: Reviewing notebooks like normal scripts

Notebooks mix code, state, narrative, outputs, and sometimes secrets. They can be excellent for exploration and poor for controlled release training.

Better question: is the notebook an exploratory artifact, or is it part of the production training path?

## Mistake 4: Making security a manual reviewer memory test

A checklist that relies on reviewers noticing every missing field will fail under delivery pressure. The platform should enforce required metadata and reject incomplete releases.

Better question: can the insecure release path succeed automatically?

## Mistake 5: Ignoring rollback until incident response

Rollback is a release requirement, not an incident improvisation. If the model changes feature expectations, serving code, or downstream thresholds, rollback may not be simple.

Better question: what exact artifact and configuration are safe to restore?

## Mistake 6: Treating all supply-chain issues as malicious

Many supply-chain failures are accidental: unpinned dependencies, stale data, wrong dataset, wrong threshold, wrong artifact, missing metadata. Security review should catch both malicious and accidental paths because both can produce unsafe production behavior.
''',
            "worked-example.md": r'''# Worked example: Evidence-pack review finding

## Weak finding

The model pipeline is insecure because the notebook uses unpinned dependencies and the registry metadata is incomplete. The team should improve MLOps security before launch.

## Why this is weak

This finding names symptoms but does not explain the security property lost, how the release can fail, what control must change, or how to validate the fix. It sounds reasonable, but an engineering team cannot implement it directly.

## Strong finding

**Finding:** Production promotion does not bind the evaluated model to the deployed artifact.

**Evidence:** The evidence pack proposes deployment from `models/latest/model.pkl`, while the registry metadata records a different expected artifact hash than the observed artifact hash. The promotion workflow checks only model accuracy and does not verify an immutable artifact digest, signed manifest, approval record, or rollback target.

**Root cause:** The release process treats the model registry path as trusted storage rather than an enforced promotion boundary. The evaluation record, registry metadata, and deployment input are not cryptographically or procedurally bound to the same artifact.

**Impact:** A modified or wrong model can be deployed even if it was not the artifact evaluated by the team. This breaks auditability and makes incident response unreliable because the team cannot prove which model reached production.

**Remediation:** Replace mutable artifact paths with immutable artifact IDs. Require the promotion workflow to verify artifact digest, training-run ID, dataset version, evaluation report, approval owner, and rollback target before deployment. Fail promotion if any field is missing or mismatched.

**Validation:** Attempt to promote an artifact whose digest differs from the evaluation record. The workflow should fail. Attempt to promote an artifact with no rollback target. The workflow should fail or require explicit risk acceptance from the model owner and security reviewer.

**Residual risk:** This control proves artifact identity and promotion integrity. It does not prove the model is robust, fair, or privacy-preserving. Those still require evaluation and monitoring controls.

## Instructor note

Use this example to show the difference between finding symptoms and finding control failure. Students should leave Module 08 able to write findings that an MLOps platform team can implement.
''',
        },
    },
    "09-privacy-attacks": {
        "title": "Module 09 depth pass: Privacy attacks and data protection",
        "files": {
            "deep-dive.md": r'''# Deep dive: Privacy attacks and data protection

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
''',
            "attack-anatomy.md": r'''# Attack anatomy: Privacy leakage in AI systems

## Scenario

BrokenPilot stores fake internal documents for multiple tenants. `DOC-002` is an alpha restricted document with a fake token. A beta user, `chris`, searches for payment or credential information. When retrieval authorization is disabled, the retriever returns alpha material to a beta user, and the model can summarize or expose the fake sensitive fragment.

## Step-by-step failure

1. The user sends a query containing terms that match a restricted document.
2. The retriever searches across documents without enforcing tenant and role filters.
3. The restricted document appears in the context set.
4. The model treats retrieved context as available information.
5. The response includes a fake sensitive fragment or enough information to identify the restricted content.
6. Logs or traces may preserve the sensitive fragment even after retrieval authorization is fixed.

## Security property lost

The system loses tenant isolation and data minimization. The user does not need direct document access because the AI application becomes a proxy to the document store.

## Why prompt wording cannot fix this

A prompt such as "never reveal secrets" is not a reliable privacy boundary. The model should not receive unauthorized context in the first place. If the model sees restricted context, the design has already failed.

The real control is retrieval authorization before context construction, followed by output and log controls for defense in depth.

## Variant: logging still leaks

A team fixes retrieval authorization but keeps verbose traces that include previously retrieved restricted context. Support staff, developers, or analytics users may now see sensitive fragments through observability tooling. The system no longer leaks to the end user, but it still leaks to an unauthorized internal audience.

This is a realistic privacy failure. Many AI applications store prompts, retrieved context, tool arguments, and model responses for debugging. Those records need classification, redaction, retention limits, and access control.

## Good finding pattern

A strong privacy finding should include:

- the data boundary crossed;
- the user or role that crossed it;
- the system path that enabled disclosure;
- the sensitive class of data exposed;
- the control that must enforce the boundary;
- how to validate the boundary after remediation;
- what residual paths remain, especially logs and traces.

## Weak finding pattern

A weak privacy finding says only that "the AI leaked data" or "the model revealed a secret." That does not tell the team where the boundary failed or which control should be implemented.
''',
            "controls-and-remediations.md": r'''# Controls and remediations: Privacy attacks and data protection

## Control objective

The goal is to prevent unauthorized disclosure, reconstruction, inference, and retention of sensitive data through all AI system paths.

## Primary controls

### Retrieval authorization

Filter retrieval by tenant, role, user, classification, and purpose before documents are added to model context. Do not retrieve first and ask the model to decide what is safe.

Validation: run a beta user query that matches alpha restricted tags. The result set should contain no alpha restricted documents.

### Data minimization

Send only the minimum necessary context to the model. Avoid loading complete documents when a smaller authorized fragment is enough.

Validation: inspect traces and confirm that retrieved context is limited and classified.

### Output controls

Classify and inspect outputs before display or downstream use. Redact known sensitive markers when appropriate, but do not treat redaction as a replacement for retrieval authorization.

Validation: seed a fake sensitive fragment and confirm it is not displayed to unauthorized users.

### Logging and trace controls

Treat prompts, retrieved context, tool arguments, responses, embeddings, and traces as potentially sensitive. Apply redaction, retention limits, access control, and purpose limitation.

Validation: after a blocked request, inspect logs. They should not contain unauthorized sensitive context.

### Training and fine-tuning controls

Do not use restricted production data for training or fine-tuning without a clear legal basis, data minimization, retention policy, and removal process.

Validation: check dataset manifests and training metadata for source classification and approval.

### Inference-risk controls

For membership inference and model inversion risk, reduce overfitting, limit confidence exposure where appropriate, monitor query patterns, and avoid returning unnecessary per-record signals.

Validation: compare model behavior on member and non-member synthetic records; evaluate whether confidence scores reveal membership more than necessary.

## Weak controls

- Relying on a system prompt that says not to reveal secrets.
- Redacting outputs while still storing raw restricted context in traces.
- Checking authorization after retrieval.
- Assuming internal logs are safe because they are not customer-facing.
- Treating synthetic evaluation data as proof that production data is safe.

## Strong remediation language

Use implementation-focused remediation:

- Add tenant, role, and classification filters to retrieval before context construction.
- Add a trace redaction layer for retrieved context and tool arguments.
- Deny logging of restricted fragments unless a security-approved debug mode is active.
- Add retention limits for chat transcripts and retrieved-context traces.
- Add privacy regression tests for cross-tenant retrieval and log leakage.

## Residual risk

Privacy risk is rarely zero. Even with retrieval filters and redaction, users may infer sensitive facts from aggregate outputs, timing, ranking, or repeated queries. Good security work states what remains and what monitoring or governance process owns it.
''',
            "common-mistakes.md": r'''# Common mistakes: Privacy attacks and data protection

## Mistake 1: Treating privacy as only PII

Secrets, credentials, customer strategy, internal contacts, incident reports, and tenant-specific business data can all be privacy or confidentiality concerns. The course uses fake tokens and fake contacts because they are safe training examples, not because privacy risk is limited to tokens.

## Mistake 2: Filtering after retrieval

If unauthorized content enters the model context, the main boundary already failed. Output filtering may reduce harm, but it does not repair the architecture.

## Mistake 3: Ignoring internal viewers

Logs, traces, support tools, analytics exports, and evaluation dashboards can leak sensitive data to internal users. Internal does not mean authorized.

## Mistake 4: Confusing redaction with minimization

Redaction removes or masks selected content. Minimization avoids collecting or processing unnecessary content in the first place. Strong systems use both.

## Mistake 5: Overclaiming privacy from synthetic tests

Synthetic tests are useful for safe regression testing. They do not prove that production data has no privacy risk. They prove that specific control paths behave as expected.

## Mistake 6: Forgetting retention

A chat system may not leak data in the moment but may retain sensitive prompts and retrieved context for months. Retention is part of the privacy boundary.
''',
            "worked-example.md": r'''# Worked example: Cross-tenant privacy leakage finding

## Weak finding

Chris can ask for payment token information and the AI returns alpha data. Retrieval authorization should be enabled.

## Why this is weak

It names the symptom and a likely control, but it does not explain the boundary, evidence, validation, or residual risk. It also ignores logs and traces.

## Strong finding

**Finding:** Retrieval context construction allows beta users to receive alpha restricted documents.

**Evidence:** With `ENABLE_RETRIEVAL_AUTHZ=false`, user `chris` from tenant beta can query for payment or credential terms and receive alpha restricted context from `DOC-002`. The response path exposes a fake restricted fragment, `FAKE-ALPHA-PAYMENT-TOKEN-DO-NOT-USE`, showing that tenant isolation is not enforced before model context construction.

**Root cause:** Retrieval runs across documents without applying tenant, role, and classification filters before context is sent to the model.

**Impact:** The AI application can act as a cross-tenant disclosure proxy. A user who cannot directly read an alpha restricted document can still receive sensitive content through retrieval and summarization.

**Remediation:** Enforce tenant, role, classification, and user-specific authorization in the retriever before context construction. Add privacy regression tests for cross-tenant queries. Apply redaction and access control to traces that store retrieved context.

**Validation:** Re-run the same beta query with `ENABLE_RETRIEVAL_AUTHZ=true`. The result set should exclude `DOC-002` and `DOC-006`. Inspect audit logs and traces to confirm unauthorized restricted fragments are not retained in raw form.

**Residual risk:** Retrieval authorization blocks this direct leakage path, but membership inference, log retention, support exports, and aggregated analytics still require separate privacy controls.

## Instructor note

This example should be used to teach that privacy findings are boundary findings. The best answer is not "the model leaked." The best answer is "the system placed unauthorized restricted context in front of the model."
''',
        },
    },
    "10-adversarial-ml-robustness": {
        "title": "Module 10 depth pass: Adversarial ML and robustness",
        "files": {
            "deep-dive.md": r'''# Deep dive: Adversarial ML and robustness

## The decision this module teaches

This module teaches one core decision:

> Is this model safe to use as a hard decision gate, or must it be surrounded by uncertainty handling, fallback, monitoring, and human or rules-based review?

Adversarial ML is often taught as a collection of attacks. That is useful, but the engineering decision matters more. If a classifier is only a prioritization aid, a missed case may be tolerable. If the same classifier blocks access, approves payments, suppresses alerts, or routes incidents, robustness becomes a security property.

## Accuracy is not a security argument

A model can have good average accuracy and still fail under targeted perturbation, distribution shift, poisoning, extraction, or threshold tampering. Accuracy describes performance on the evaluation set. It does not prove behavior at the boundary, under manipulation, or after the data pipeline changes.

The toy-classifier lab exists to make this visible. Students see simple input changes, poisoned labels, query probing, and threshold tampering alter decisions. The lab is intentionally small. The point is not to build a realistic phishing detector. The point is to make failure modes observable and then ask what decision architecture is appropriate.

## The hard-gate question

The most important classroom question is:

> What happens if this classifier is wrong in the direction an attacker wants?

If the answer is "an attacker gets access," "a malicious message is allowed," or "a high-risk event is ignored," the model should not be the only control. It may still be useful as a signal, but it needs compensating controls.

## Four attack families in the toy lab

### Evasion

The attacker changes input features while preserving intent. In text classification, this can be word substitutions, formatting, token changes, or phrasing changes. The model sees a different feature pattern and changes its decision.

Security lesson: input validation and model robustness are different. A syntactically valid input can still be adversarial for the model.

### Poisoning

The attacker or faulty process changes training data or labels. The model learns a weaker or misleading boundary.

Security lesson: training data is part of the trusted computing base for ML behavior.

### Extraction

The attacker queries the model and uses outputs to approximate behavior. Even a small approximation can help tune evasion attempts.

Security lesson: query access, confidence exposure, and rate limits are part of model security.

### Output integrity

The model is unchanged, but the threshold or score-to-decision mapping is altered. Production outcomes change even though the trained model file is identical.

Security lesson: serving configuration is part of the model's security boundary.

## What students should stop believing

Students should stop treating adversarial ML as only exotic research. The course uses simple scripts because many real failures are simple: the model faces inputs unlike training data, labels are wrong, thresholds drift, or downstream systems treat a probabilistic score as a hard truth.

Students should also stop believing robustness means "make the model perfect." Robustness engineering is about knowing where the model is brittle and designing the system so brittleness does not become silent business or security failure.

## Lab transfer

The toy-classifier lab should end with a design decision. Students should not only report that an attack flips a label. They should answer:

- Should this classifier be a hard gate?
- What fallback is used when confidence is low or input is unusual?
- What data and threshold changes require review?
- What monitoring would detect drift or attack probing?
- What controls reduce harm when the classifier is wrong?

That is the difference between an attack demo and a security engineering exercise.
''',
            "attack-anatomy.md": r'''# Attack anatomy: Adversarial ML and robustness

## Scenario

A small message classifier labels synthetic messages as benign or risky. A team wants to use the classifier to decide whether messages can bypass human review. The lab shows four ways the decision can be changed without changing the user's underlying intent.

## Evasion path

1. The classifier learns that certain words strongly indicate risk.
2. The attacker changes wording to avoid those exact features.
3. The model score moves below the risky threshold.
4. The message bypasses review.

Security property lost: robust classification under plausible input change.

Engineering response: do not rely on a single model score as the only gate. Add uncertainty handling, review triggers, feature monitoring, and adversarial evaluation.

## Poisoning path

1. Training labels include a small number of wrong labels.
2. The model learns a weaker boundary.
3. Some risky messages are now classified as benign.
4. The team sees acceptable aggregate accuracy but misses targeted cases.

Security property lost: training-data integrity.

Engineering response: protect labeling workflows, sample high-impact classes, require dataset versioning, and compare model behavior before and after retraining.

## Extraction path

1. The attacker can query the model repeatedly.
2. The system returns labels or confidence-like outputs.
3. The attacker maps which tokens and changes move the decision.
4. Evasion attempts become cheaper.

Security property lost: confidentiality of decision behavior.

Engineering response: rate-limit probing, reduce unnecessary confidence exposure, monitor query patterns, and treat model behavior as sensitive when it gates important decisions.

## Output-integrity path

1. The trained model outputs a score.
2. The serving threshold maps score to decision.
3. A configuration change lowers or raises the threshold.
4. Outcomes change without retraining or changing the model file.

Security property lost: integrity of the decision function.

Engineering response: version and review thresholds, bind threshold changes to evaluation evidence, log score-to-decision mappings, and alert on threshold drift.

## Why this belongs in security review

The attacker does not need to compromise the model weights. They may manipulate inputs, data, query access, or serving configuration. A security review that checks only the model artifact misses the system paths that shape decisions.
''',
            "controls-and-remediations.md": r'''# Controls and remediations: Adversarial ML and robustness

## Control objective

The goal is not to make the model unbreakable. The goal is to prevent model brittleness from becoming silent unsafe behavior.

## Strong controls by failure mode

### Evasion

- Add adversarial and perturbation testing to evaluation.
- Monitor feature distributions and unusual input patterns.
- Use confidence thresholds and abstention for uncertain cases.
- Route high-impact or low-confidence cases to fallback review.
- Avoid using a single model as the only authorization or safety gate.

Validation: run known perturbation cases and confirm they are detected, abstained, or routed for review rather than silently accepted.

### Poisoning

- Version datasets and labels.
- Restrict write access to training data and labels.
- Review label changes for high-impact classes.
- Compare behavior before and after retraining on fixed evaluation slices.
- Use canary examples to detect unexpected boundary movement.

Validation: inject a small controlled label-flip test in a non-production dataset and confirm review gates catch behavior changes.

### Extraction

- Limit query rates and high-volume probing.
- Avoid exposing unnecessary confidence scores.
- Monitor systematic boundary exploration.
- Consider model access tiering for sensitive decision models.

Validation: run a query harness and confirm monitoring detects repeated boundary-probing patterns.

### Output integrity

- Version thresholds and serving configuration.
- Require review for threshold changes.
- Bind threshold changes to evaluation reports.
- Log the score, threshold, and decision for audit.
- Alert on threshold changes in production.

Validation: change a threshold in staging and confirm the promotion process requires approval and records the impact.

## Weak controls

- Claiming the model is safe because test accuracy is high.
- Adding a warning banner without changing decision handling.
- Blocking a few known words and calling it adversarial robustness.
- Hiding confidence scores while allowing unlimited probing.
- Reviewing the model file but ignoring serving thresholds.

## Remediation backlog language

Good backlog items are specific:

- Add an adversarial evaluation slice for message perturbations before release.
- Add an abstain state when confidence falls between 0.45 and 0.65.
- Require approval for threshold changes and store the approval with the deployment record.
- Add dataset hash and label-change summary to every training run.
- Add monitoring for repeated queries that differ by one or two tokens.

## Residual risk

Adversarial testing samples possible attacks. It does not cover every future input. The residual-risk statement should explain what the model is still allowed to decide, where fallback exists, and what monitoring will detect when assumptions fail.
''',
            "common-mistakes.md": r'''# Common mistakes: Adversarial ML and robustness

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
''',
            "worked-example.md": r'''# Worked example: Hard-gate robustness review

## Weak finding

The classifier can be bypassed by changing words. The model should be retrained with more examples.

## Why this is weak

Retraining may help, but the finding does not explain the decision risk, validation plan, or what happens when retraining still misses cases. It also assumes the model should remain a hard gate.

## Strong finding

**Finding:** The message classifier is not safe as the sole hard gate for bypassing review.

**Evidence:** In the toy-classifier evasion lab, small synthetic wording changes move a risky message below the review threshold while preserving the intended risky meaning. The output-integrity lab also shows that changing the threshold can alter decisions without modifying the model artifact.

**Root cause:** The workflow treats a probabilistic model score and serving threshold as a final authorization decision without an abstain state, fallback review, threshold-change control, or adversarial evaluation slice.

**Impact:** A user can craft inputs or exploit weak threshold governance to bypass review. Aggregate model accuracy does not protect the specific boundary where the decision matters.

**Remediation:** Use the classifier as a prioritization signal, not the only gate, until robustness controls are added. Add an abstain band, human review for low-confidence or high-impact cases, adversarial evaluation before release, versioned threshold configuration, and monitoring for probing behavior.

**Validation:** Re-run the evasion examples. They should either remain risky, fall into abstain/review, or trigger monitoring. Attempt a threshold change in staging. It should require approval and produce an evaluation delta.

**Residual risk:** New perturbations may still evade the model. The residual risk is acceptable only if the workflow can tolerate misses or if fallback controls catch high-impact cases.

## Instructor note

Use this example to redirect students from "I bypassed the classifier" to "what authority should the classifier have?" That is the engineering lesson.
''',
        },
    },
    "11-ai-red-team-methodology": {
        "title": "Module 11 depth pass: AI red team methodology",
        "files": {
            "deep-dive.md": r'''# Deep dive: AI red team methodology

## The decision this module teaches

This module teaches one core decision:

> What evidence would change the launch, scope, control, or monitoring decision for this AI system?

AI red teaming is not a contest to produce alarming screenshots. It is a structured method for testing whether the system's controls hold under realistic abuse. The best red team work helps leaders decide what to fix, what to monitor, what to accept, and what not to launch yet.

## Red team work starts with scope

A good red team scope defines:

- the system boundary;
- permitted users and roles;
- allowed attack paths;
- prohibited actions;
- data handling rules;
- success criteria;
- evidence requirements;
- stop conditions;
- reporting format.

Without scope, a red team can become noisy, unsafe, or irrelevant. With scope, the team can test meaningful hypotheses and produce findings that engineering teams can act on.

## Hypotheses beat random probing

A strong test begins with a hypothesis:

- A user can retrieve cross-tenant context because retrieval filters are missing.
- A poisoned memory entry can influence agent intent.
- Tool authorization blocks execution even when the model is manipulated.
- A model output reaches an HTML sink without encoding.
- A promotion workflow deploys an artifact without verifying its digest.

These hypotheses map to controls. That makes the result useful whether the attack succeeds or fails.

## Evidence must be reproducible

A red team finding should include enough detail for another person to reproduce the behavior:

- role and tenant;
- control settings;
- input or request;
- observed result;
- expected result;
- affected asset;
- root cause;
- remediation;
- validation test.

For AI systems, this matters because outputs can be variable. BrokenPilot uses deterministic behavior so students can focus on security reasoning. Real systems need even more careful evidence collection.

## The fix matters more than the exploit

A weak report says, "we got the agent to do something bad." A strong report says, "the tool broker failed to enforce target-object authorization, allowing a cross-tenant ticket update; add authorization at the tool boundary and validate with this test."

The exploit shows that a control failed. The finding should explain the control.

## Defense-in-depth findings are the most valuable

The best AI red team findings often show interactions between controls. For example, poisoned memory may steer the agent's intent, while tool authorization still blocks execution. That is not a failed attack. It is a successful demonstration of defense in depth.

Students should learn to report both:

- where the system failed;
- where a control prevented worse impact.

That is more useful than a simple pass/fail narrative.

## Lab transfer

In BrokenPilot, students should build attack chains that connect:

- retrieval exposure;
- prompt or memory manipulation;
- tool execution;
- audit evidence;
- remediation validation.

The final deliverable should read like a security review, not a transcript dump. The target audience is an engineering leader deciding what must change before launch.
''',
            "attack-anatomy.md": r'''# Attack anatomy: AI red team chain

## Scenario

BrokenPilot is an internal AI agent that retrieves documents, summarizes context, stores memory, and updates tickets. A red team evaluates whether a user can manipulate the system into disclosing unauthorized data or changing a ticket outside their allowed boundary.

## Chain 1: retrieval to disclosure

1. Identify a user with limited tenant access.
2. Query for terms that match restricted documents.
3. Observe whether unauthorized context enters the model response.
4. Enable retrieval authorization.
5. Re-run the test and confirm the restricted context is blocked.

Control tested: retrieval authorization before context construction.

## Chain 2: memory poisoning to tool intent

1. Add a malicious memory instruction.
2. Trigger an agent task related to that instruction.
3. Observe that the agent intent is influenced.
4. Enable memory review or memory isolation.
5. Re-run and confirm the poisoned memory is not active.

Control tested: memory trust and activation.

## Chain 3: manipulated intent to tool execution

1. Cause the model or memory layer to propose a risky action.
2. Target an object outside the user's tenant or role boundary.
3. Observe whether the tool broker checks authorization.
4. Enable tool authorization.
5. Re-run and confirm execution is blocked.

Control tested: independent authorization at the tool boundary.

## Chain 4: model output to downstream sink

1. Cause or retrieve content that includes a benign output-sink marker.
2. Render the model output through the downstream HTML sink.
3. Observe raw versus encoded output.
4. Enable output encoding.
5. Re-run and confirm context-appropriate encoding.

Control tested: insecure output handling.

## What makes a chain useful

A useful attack chain shows the path from entry point to impact, then shows which control breaks the path. A chain that only lists prompts is not enough. The report should name the system boundary that failed.
''',
            "controls-and-remediations.md": r'''# Controls and remediations: AI red team methodology

## Red team control objective

The objective is not to eliminate all possible bad outputs. The objective is to validate whether the system's security boundaries hold under realistic abuse.

## Controls to evaluate

### Retrieval controls

- Tenant, role, and classification filters before context construction.
- Evidence that unauthorized documents never reach the model.
- Tests for both positive and negative access cases.

### Prompt and instruction controls

- Instruction and data separation.
- Untrusted-content handling.
- No reliance on prompt wording as the only boundary.

### Tool controls

- Per-tool authorization.
- Target-object authorization.
- Approval gates for high-impact actions.
- Tool argument validation.
- Audit logging.

### Memory controls

- Memory review before activation.
- Scope isolation by tenant, user, and purpose.
- Expiry and deletion.
- Evidence of what memory influenced a run.

### Output controls

- Context-specific encoding.
- Validation before downstream interpretation.
- Redaction and classification when needed.

### Operational controls

- Reset path for labs and test environments.
- Audit logs for reproduction.
- Kill switches and rollback procedures for production systems.

## Strong remediation language

A strong red team report gives engineering-ready controls:

- Add authorization in the tool broker for target ticket tenant and user role.
- Reject retrieved documents that do not match the active user's tenant and role before context construction.
- Mark memory as pending until reviewed and isolate memory by tenant.
- Encode model output before insertion into HTML sinks.
- Add regression tests for each fixed abuse path.

## Validation after remediation

Every finding should have a validation test. The test should fail in vulnerable mode and pass in controlled mode. If a finding cannot be validated, it is probably not ready for the final report.

## Residual risk

Red team results are samples, not proof of absence. A good report states what was tested, what was not tested, and which risks require monitoring, future testing, or explicit acceptance.
''',
            "common-mistakes.md": r'''# Common mistakes: AI red team methodology

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
''',
            "worked-example.md": r'''# Worked example: Red team finding with defense in depth

## Weak finding

We poisoned the memory and the AI tried to close a beta ticket. This is critical and the agent should have better guardrails.

## Why this is weak

It overstates the issue, uses vague remediation, and fails to distinguish intent from execution. If tool authorization blocked the action, the report should say so.

## Strong finding

**Finding:** Unreviewed global memory can steer agent intent, but independent tool authorization prevents cross-tenant ticket execution.

**Evidence:** A malicious memory entry instructed the agent to close `TCK-2001`. When Alice later asked about the related workflow, the agent attempted to act on that instruction. With tool authorization enabled, the tool broker returned `tool_authorization_denied` because Alice's tenant and the ticket tenant did not match.

**Root cause:** Memory entries can influence planning before review or tenant scoping. However, execution is separately controlled by the tool authorization layer.

**Impact:** If tool authorization were disabled or incomplete, poisoned memory could lead to unauthorized ticket changes. With tool authorization enabled, impact is reduced to manipulated intent and a blocked action attempt.

**Remediation:** Require memory review before activation and isolate memory by tenant, user, and purpose. Keep tool authorization mandatory for every state-changing action. Add audit fields showing which memory entries influenced an agent run.

**Validation:** Add a malicious memory entry and run the scenario. With memory review enabled, the memory should not become active. With memory isolation enabled, cross-tenant memory should not be consumed. With tool authorization enabled, any attempted cross-tenant update should be denied.

**Residual risk:** Tool authorization prevents this execution path, but poisoned memory can still waste operator time, influence summaries, or affect lower-impact decisions. Monitoring and memory review remain necessary.

## Instructor note

This example is the model for mature red team reporting. It shows a weakness, a compensating control, a realistic impact statement, and validation steps.
''',
        },
    },
}

ADDITIONAL_SECTIONS = {'modules/08-secure-mlops-supply-chain/common-mistakes.md': '\n## How to correct these mistakes in class\n\nWhen a student names a missing tool, ask what security property the tool enforces. For example, "use a registry" is not enough. The registry must reject mutable artifacts, missing metadata, unapproved promotion, and digest mismatches. If it does not reject unsafe releases, it is not the boundary.\n\nWhen a student names a missing process, ask what evidence the process creates. "Have a review" is not enough. The review should leave behind approval owner, evaluated artifact digest, dataset identity, rollback target, and the risk decision. A future incident responder should be able to reconstruct the release without interviewing everyone involved.\n\nThe expected correction is concrete: change the pipeline, registry schema, workflow gate, or storage permission so the insecure path fails by default.\n', 'modules/09-privacy-attacks/common-mistakes.md': '\n## How to correct these mistakes in class\n\nWhen a student says "the model leaked private data," push for the exact system path. Was the data retrieved without authorization? Was it summarized from authorized context but shown to the wrong user? Was it stored in logs? Was it inferred from repeated queries? Each path has a different control.\n\nWhen a student proposes output redaction as the main fix, ask whether the model should have seen the data at all. In most cross-tenant cases, the primary fix is authorization before retrieval. Redaction and logging controls are defense in depth, not permission to send restricted data into context.\n\nThe expected correction is a data-flow answer: protect retrieval, output, logs, traces, retention, and support access as one privacy boundary.\n', 'modules/10-adversarial-ml-robustness/common-mistakes.md': '\n## How to correct these mistakes in class\n\nWhen a student celebrates a label flip, ask what decision the model controls. A flipped label is important only because it changes an action: allow, block, escalate, suppress, route, or ignore. The finding should name that action.\n\nWhen a student proposes "train on more examples," ask what happens before retraining works. Good answers add fallback, abstention, review, monitoring, threshold governance, and release criteria. Better training is valuable, but it is not a complete security control by itself.\n\nThe expected correction is an authority answer: decide whether the model is a signal, a prioritizer, or a hard gate, and then design controls that match that authority.\n', 'modules/11-ai-red-team-methodology/common-mistakes.md': '\n## How to correct these mistakes in class\n\nWhen a student submits a transcript, ask for the finding. The transcript is supporting evidence. The finding names the boundary, control failure, impact, remediation, validation, and residual risk.\n\nWhen a student reports only successful attacks, ask what blocked attempts showed. A blocked action may prove that a control works, or that impact is lower than the initial narrative suggests. That nuance is what separates a professional red team report from a collection of screenshots.\n\nThe expected correction is decision-grade reporting: enough evidence for engineering to fix the issue and enough context for leadership to choose launch, delay, or limited pilot.\n', 'modules/09-privacy-attacks/worked-example.md': '\n## What an excellent submission adds\n\nAn excellent submission adds a second observation after the retrieval fix: whether audit logs, traces, or support exports still contain the fake restricted fragment. This turns the lab from a simple authorization exercise into a privacy architecture review.\n\nThe best answer also separates customer-facing impact from internal exposure. Blocking the response to Chris protects one path. It does not automatically prove that developers, support users, or analytics tools cannot see the same data through retained traces.\n', 'modules/10-adversarial-ml-robustness/worked-example.md': '\n## What an excellent submission adds\n\nAn excellent submission includes a product decision. It does not only say that the classifier is brittle. It says whether the classifier can remain in the workflow, whether its authority must be reduced, and what fallback catches uncertain or high-impact cases.\n\nThe best answer also distinguishes model improvement from system improvement. Retraining may improve the model. Abstention, threshold review, monitoring, and fallback change the safety of the whole decision system.\n', 'modules/11-ai-red-team-methodology/controls-and-remediations.md': '\n## Quality bar for red team remediations\n\nA red team remediation should be testable by someone who did not write the report. Avoid language such as "improve guardrails" or "make the agent safer." Instead, name the enforcement point.\n\nGood examples:\n\n- Enforce target-ticket tenant checks in the tool broker before update execution.\n- Reject retrieved documents that do not match the active user\'s tenant and role before context construction.\n- Require memory entries to be approved and scoped before they can influence an agent run.\n- Encode model output before insertion into HTML or other interpreted sinks.\n\nEach remediation should have a paired validation step. If the validation cannot be written, the remediation is probably too vague.\n', 'modules/11-ai-red-team-methodology/worked-example.md': '\n## What an excellent submission adds\n\nAn excellent submission includes both sides of the defense-in-depth story. It explains that memory handling is weak because unreviewed memory can influence intent, and it also explains that tool authorization reduced impact by blocking execution.\n\nThe best reports avoid inflated severity. They say what happened, what did not happen, and what would have been required for worse impact. That makes the recommendation more credible.\n'}

SUPPORT_FILES = {
    "instructor/teaching-modules-08-11-depth-pass.md": r'''# Teaching Modules 08 to 11 after the depth pass

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
''',
    "assessments/modules-08-11-depth-checkpoints.md": r'''# Modules 08 to 11 depth checkpoints

Use these checkpoints during the 40-hour course to verify that students are turning reading into engineering judgment.

## Module 08 checkpoint

Student can explain why a model with good accuracy should not be promoted when artifact identity, dataset provenance, approval, and rollback evidence are missing.

Required submission: one finding from the MLOps evidence pack with evidence, root cause, remediation, validation, and residual risk.

## Module 09 checkpoint

Student can distinguish source-data access control from AI-system privacy controls across retrieval, output, logs, traces, and retention.

Required submission: one cross-tenant privacy finding and one residual-risk note about logs or traces.

## Module 10 checkpoint

Student can explain why a classifier should or should not be used as a hard gate after observing evasion, poisoning, extraction, or threshold tampering.

Required submission: one hard-gate decision memo based on the toy-classifier results.

## Module 11 checkpoint

Student can turn an attack chain into a reproducible finding and can report defense-in-depth when a control blocks impact.

Required submission: one red team finding with reproduction steps and validation after remediation.

## Minimum bar

A checkpoint is complete only if it includes a recommendation. Observations without a decision are notes, not security deliverables.
''',
    "course-templates/depth-reading-response-template.md": r'''# Depth reading response template

Use this template after reading a module deep dive.

## Module

Module number and title:

## Decision

What decision is this module teaching you to make?

## Boundary

What security, privacy, or operational boundary is at stake?

## Evidence

What evidence would you need to make the decision responsibly?

## Weak control

What is a common weak or cosmetic control for this problem?

## Strong control

What control would actually change the security property?

## Validation

How would you test that the control works?

## Residual risk

What risk remains after the control is implemented?

## Lab transfer

Which lab or tabletop exercise demonstrates this issue, and what should you observe or produce?
''',
    "release-notes/v1.1-dev-module-depth-prose-pass-08-11.md": r'''# v1.1-dev module depth prose pass for Modules 08 to 11

This update strengthens the reading material for the four advanced modules that depend most on student judgment:

- Module 08: Secure MLOps and AI supply chain
- Module 09: Privacy attacks and data protection
- Module 10: Adversarial ML and robustness
- Module 11: AI red team methodology

The pass adds or replaces deep-dive, attack-anatomy, controls-and-remediations, common-mistakes, and worked-example pages for each module. The writing is organized around engineering decisions, not attack catalogs.

No MkDocs strict cleanup is included in this package. Release hardening remains a later phase.
''',
}

README_NOTE = """
{start}

## Depth pass for advanced modules

This module now includes a strengthened study path:

- `deep-dive.md` for the core engineering decision;
- `attack-anatomy.md` for the failure path;
- `controls-and-remediations.md` for practical controls;
- `common-mistakes.md` for classroom correction;
- `worked-example.md` for a strong finding or review artifact.

Use these pages with the module lab path and the 40-hour checkpoint materials.

{end}
""".strip()

CLEANUP_NOTE = """
{start}

## Module depth prose pass cleanup

Before public release, review the Modules 08 to 11 depth-pass files for voice consistency with the rest of the course. Keep the decision-driven structure, but remove any temporary apply/check scripts after all content packages stop changing.

{end}
""".strip()


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8", newline="\n")
    print(f"wrote: {path.relative_to(ROOT)}")


def replace_block(text: str, block: str) -> str:
    start = block.splitlines()[0]
    end = block.splitlines()[-1]
    if start in text and end in text:
        before = text.split(start, 1)[0].rstrip()
        after = text.split(end, 1)[1].lstrip()
        return (before + "\n\n" + block + "\n\n" + after).strip() + "\n"
    return text.rstrip() + "\n\n" + block + "\n"


def update_readme(module_slug: str) -> None:
    readme = ROOT / "modules" / module_slug / "README.md"
    if not readme.exists():
        write(readme, f"# {module_slug}\n")
    text = readme.read_text(encoding="utf-8")
    block = README_NOTE.format(start=MARKER_START, end=MARKER_END)
    readme.write_text(replace_block(text, block), encoding="utf-8", newline="\n")
    print(f"updated: {readme.relative_to(ROOT)}")


def main() -> None:
    for slug, module in MODULES.items():
        base = ROOT / "modules" / slug
        for filename, content in module["files"].items():
            write(base / filename, content)
        update_readme(slug)

    for rel, addition in ADDITIONAL_SECTIONS.items():
        target = ROOT / rel
        base_text = target.read_text(encoding="utf-8") if target.exists() else ""
        if addition.strip() not in base_text:
            write(target, base_text.rstrip() + "\n\n" + addition.strip())

    for rel, content in SUPPORT_FILES.items():
        write(ROOT / rel, content)

    cleanup = ROOT / "CLEANUP_BEFORE_RELEASE.md"
    if cleanup.exists():
        text = cleanup.read_text(encoding="utf-8")
    else:
        text = "# Cleanup before release\n"
    block = CLEANUP_NOTE.format(start=MARKER_START, end=MARKER_END)
    cleanup.write_text(replace_block(text, block), encoding="utf-8", newline="\n")
    print(f"updated: {cleanup.relative_to(ROOT)}")

    print("\nApplied module depth prose pass for Modules 08 to 11.")


if __name__ == "__main__":
    main()
