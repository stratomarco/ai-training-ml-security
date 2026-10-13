# Offline artifact-promotion gate

This small Module 08 lab makes one promotion decision observable. It uses fake JSON weight files, synthetic metadata, and Python's standard library. The gate hashes artifact bytes and compares them with a separate trusted approval policy. It never deserializes or executes a model.

## Run the three cases

Use Python 3.10 or newer from this directory. No package install or network connection is needed.

```text
python promotion_gate.py
python promotion_gate.py --artifact fixtures/tampered-v1.weights.json --manifest fixtures/approved-v1.manifest.json
python promotion_gate.py --artifact fixtures/unapproved-v2.weights.json --manifest fixtures/unapproved-v2.manifest.json
```

Expected decisions:

| Candidate | Expected decision | Why |
|---|---|---|
| Approved v1 | `allow` | Artifact digest and release evidence match the protected policy |
| Tampered v1 | `deny` | The bytes differ from both the manifest and approved digest |
| Unapproved v2 | `deny` | Its manifest matches its bytes, but the revision, digest, source, and dataset lack approval |

The CLI exits `0` on allow, `1` on deny, and `2` if its trusted policy is invalid. This makes a denied promotion visible to an automated pipeline.

## Student investigation

1. Run each case and compare `manifest_matches_artifact` with `artifact_digest_is_approved`.
2. Explain why an attacker who can replace both an artifact and its untrusted manifest could make the first check pass.
3. Identify which system must protect `trusted_policy.json` in a real deployment. What would happen if an attacker could edit it?
4. Decide which additional evidence you would require before deployment: trusted signer identity, source and dataset provenance, safe format, scanning results, evaluation, and approval.
5. Describe what a signature proves and what it cannot prove about the model's behavior or safety.

The checked-in policy represents an approval record held outside the attacker's control. Because this is an offline training repository, students can inspect or edit every file; the exercise does not claim to protect its own policy from the computer's owner.

## Scope and next step

This is an integrity and approval gate, not a digital-signature implementation. A production workflow would verify a signature or provenance attestation against a separately trusted identity before loading an artifact. Format controls and static scanners are useful additional signals, but a clean scan is not proof of safety. A later optional lab may demonstrate Cosign or another signature verifier after the offline trust-root and cross-platform setup are validated.

The fake `json-weights-v1` files are never parsed as models. No pickle, checkpoint loader, Hugging Face token, cloud account, or live model is required.
