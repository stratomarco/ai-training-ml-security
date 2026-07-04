# Evidence Map: MLOps Evidence-Pack Model Answer

Use this map to connect observations in the evidence pack to findings, controls, and validation steps.

| Evidence source | Observation | Finding supported | Control expected | Validation |
|---|---|---|---|---|
| `requirements.txt` | Dependencies are not pinned with exact versions and hashes | Dependency provenance is weak | Lockfile with hashes, reviewed base image, dependency scan | Build twice from same lockfile and compare metadata |
| `train.ipynb` | Runtime package installation appears inside the notebook | Training environment is not controlled | No runtime install in production training, approved image digest | Pipeline rejects notebook or job with runtime package installation |
| `train.ipynb` | Fake inline secret appears in notebook text | Secret hygiene is weak | Secret scanning, secret manager, workload identity | Secret scanner flags the notebook before merge or training |
| `metadata/training-run.json` | Dataset hash or schema version is missing | Training data provenance is incomplete | Dataset manifest, schema version, transformation commit | Promotion fails when dataset manifest is missing |
| `registry/model_registry.json` | Artifact URI uses mutable `latest` style reference | Artifact identity is not immutable | Immutable URI, digest, signed manifest | Promotion fails if artifact URI is mutable |
| `registry/model_registry.json` | Recorded and observed hashes do not match | Artifact integrity cannot be proven | Digest verification before promotion | Tampered artifact is blocked |
| `storage/bucket-policy.json` | Shared write access and weak object controls | Artifact storage is mutable | Object lock, least privilege, separated paths | Training role cannot overwrite production artifact |
| `ci/promotion-workflow.yml` | No signature, manifest, approval, or rollback checks | Promotion gate is weak | Policy-as-code promotion gate | Promotion without approval fails |
| `artifacts/model.pkl.README.md` | Pickle artifact placeholder explains executable artifact risk | Artifact format increases impact of tampering | Treat artifact as executable, verify before load, restrict loaders | Loader refuses unsigned or mismatched artifact |

## Review guidance

A student should not cite every line mechanically. The evidence map exists to help them build an argument:

1. What evidence is missing or contradictory?
2. What security property is affected?
3. What decision becomes unsafe because of that gap?
4. What control would change the decision?
5. How would the team validate the control?

The strongest answers use a small number of high-quality findings rather than a long list of disconnected smells.
