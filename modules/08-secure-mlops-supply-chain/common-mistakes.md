# Common mistakes: Secure MLOps and AI supply chain

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

## How to correct these mistakes in class

When a student names a missing tool, ask what security property the tool enforces. For example, "use a registry" is not enough. The registry must reject mutable artifacts, missing metadata, unapproved promotion, and digest mismatches. If it does not reject unsafe releases, it is not the boundary.

When a student names a missing process, ask what evidence the process creates. "Have a review" is not enough. The review should leave behind approval owner, evaluated artifact digest, dataset identity, rollback target, and the risk decision. A future incident responder should be able to reconstruct the release without interviewing everyone involved.

The expected correction is concrete: change the pipeline, registry schema, workflow gate, or storage permission so the insecure path fails by default.
