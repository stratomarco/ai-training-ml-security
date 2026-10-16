# Student-style course validation, 15 October 2026

## Decision

The required 40-hour learning path is technically runnable and produces coherent security decisions on the tested Windows host. This was an accelerated maintainer-run walkthrough with sample written submissions, not a timed 40-hour delivery or an independent first-time learner pilot. Keep BrokenPilot, the toy classifier, and the Module 08 evidence review as the required path. The AIGoat setup and media issues recorded below were resolved for two optional MCP labs on Windows in the [16 October follow-up](../aigoat-adoption-evaluation.md); independent learner validation remains open.

## Environment and method

- Course checkout: `dev`, starting from commit `67da24b` on 15 October 2026.
- Host: Windows with Docker Desktop, Python 3.14, and Ubuntu WSL. The toy classifier and BrokenPilot suite were run using Python 3.12 containers.
- BrokenPilot core: documented Docker Compose route, published only on `127.0.0.1:8010`, healthy container, browser UI and direct loopback API requests.
- BrokenPilot Qwen extension: local Ollama container published on `127.0.0.1:11434`, exact `qwen3:4b-instruct-2507-q4_K_M` model, digest `0edcdef34593eac1aa2be9c7d06c432dcf81945adca5eca2f27662c18f168ba0`; Python launcher on `127.0.0.1:8010`.
- AIGoat extension: fresh WSL checkout of pinned v2.0 commit `e1c538badb93c6c1c2307096ab5d709a9ee0fe55`, isolated Docker project and volumes, loopback-only published ports, upstream UI interactions. See [adoption evaluation](../aigoat-adoption-evaluation.md).
- Static Module 08 notebook was read as evidence, never executed. No real systems or credentials were used.

## Completion matrix

| Course area | Student action | Observed result |
|---|---|---|
| 01 to 02, foundations and lifecycle | Completed DocAssist threat model and LoanAssist lifecycle DFD, assets, eight attack paths, controls, residual risk. | Written decisions cover identity, retrieval, training, feedback, provider, logs, and registry boundaries. Reasoning exercise, not runnable proof. |
| 03, OWASP ML | Reviewed phishing scenario and ran all four toy classifier scripts. | Evasion changed 0.903 to 0.360 and flipped label; four poisoned labels changed 0.838 to 0.136; extraction agreement 9/10 after 90 synthetic queries; threshold change reclassified the same 0.838 score. Seven tests passed. |
| 04, architecture | Completed DocOps review with assets, boundaries, unsafe assumptions, abuse cases, risks, requirements, and residual risk. | Design analysis only. |
| 05 to 06, LLM and RAG | Ran direct injection, indirect injection, raw output, cross-tenant retrieval, and Eve ticket to Alice agent chain in vulnerable and controlled settings. | Vulnerable markers and state change reproduced. All-controls blocked direct/indirect mock instruction behavior, excluded the unauthorized chunk, and encoded the output marker. The mock marker filter is not a production control. |
| 07, agents | Ran direct cross-tenant ticket update, same-tenant approval, and cross-tenant memory poisoning; wrote an OpsAgent control design. | Vulnerable cross-tenant update succeeded; all-controls returned HTTP 403. Same-tenant closure needed approval. Unreviewed memory was inactive under controls. BrokenPilot Python 3.12 suite: 37 passed. |
| 08, MLOps | Read all static evidence-pack artifacts, blocked promotion, completed separate TriageRanker design decision and executive memo, ran offline gate. | Approved/tampered/unapproved decisions were allow/deny/deny with exit codes 0/1/1. Five gate unit tests passed. The notebook was not executed and no pickle was loaded. |
| 09, privacy | Completed PeopleAssist assessment and membership inference/inversion tabletop; used BrokenPilot cross-tenant retrieval evidence. | Separates observed fake-data retrieval leakage from untested model privacy hypotheses. |
| 10, robustness | Completed PhishGuard test plan and used toy classifier observations. | Recommends advisory classification, analyst fallback, monitoring, and rollback. No real email system tested. |
| 11, red team | Completed scope, three paths, evidence requirements, and a rewritten tool-authorization finding. | Finding cites actor, target, vulnerable and controlled outcomes, acceptance test, and residual risk. |
| 12, capstone | Completed a BrokenPilot threat model and report with six prioritized findings, backlog, secure reference flow, residual risk, and a launch recommendation. | Recommends delaying write-enabled deployment. Wider paper-design components are labeled as untested design scope. |
| Optional Qwen | Ran live model chat and agent proposals with the exact course model. | Vulnerable chat produced a refusal that repeated a fake credential fragment. App-side retrieval authorization excluded Beta document `DOC-003` for Alice and Alpha document `DOC-002` for Eve; Eve's answer lacked the Alpha fragment. Model declined a retrieved ticket instruction, so no injection success is claimed. A same-tenant update proposal was blocked without separate authorization fields and executed with matching fields. |
| Optional AIGoat | Completed MCP03-2 and MCP07-1 at vulnerable and defended levels in the upstream UI. | Tool pin and process credential scoping comparisons matched the source and earlier API pilot. Upstream UI accepted the submissions. |

The full sample written work was saved locally as `student-walkthrough-2026-10-15.md` beside this checkout, with SHA-256 `c0dd38f2bec18997c88b37cb8f2968fa9348835f2c853f81a74410aac0c55107`. It is intentionally not committed to the student-facing course so the exercises do not become answer-copying tasks. Another maintainer should not assume that local file exists in their checkout.

## Meaningful delivery findings

1. **AIGoat was not ready as a required install in this run.** Its native Windows checkout failed on seven quoted product-image filenames. A full WSL checkout still needed a separate safe Compose configuration and removal of backend bind mounts because this Docker Desktop installation lacked the Ubuntu integration socket. Even after a healthy build, those seven images returned 404 in the browser. The two selected MCP exercises worked. The next day's [contained Windows setup](../../labs/aigoat-guides/windows-mcp-setup.md) preserved and served all images, but this remains optional pending an independent learner pilot.
2. **Qwen output must be inspected, not scored by refusal wording.** The live answer repeated a fake credential fragment while saying it would not reveal it. The Qwen lab guide already instructs students to check the full answer. The local model's refusal of Eve's ticket instruction was one model observation and did not validate a deterministic application control. The code-enforced retrieval and explicit-intent comparisons gave the stronger boundary evidence.
3. **Python 3.12 needs a clear fallback on current Windows machines.** The toy classifier's pinned scikit-learn version does not install cleanly under this host's Python 3.14; the documented Docker Desktop alternative now runs the full toy lab with Python 3.12. BrokenPilot's Docker route worked. A separate local Python 3.14 virtual environment failed during `ensurepip` on this host, so the optional Qwen run used an isolated dependency folder. This host-specific failure should be retested with an ordinary Python 3.12 installation before attributing it to the course.
4. **The published one-week route needed clearer entry points.** The homepage now links directly to the 40-hour course map and workbook. The workbook links each day's modules and lab entry points, and the generated navigation retains the `40-Hour` label. In the locally built site, the workbook opened from the homepage and its Module 01 and BrokenPilot links reached the intended pages in the browser. The strict site build also passed.

## Release checks

The complete `scripts/run_final_release_gate.py` passed in a clean Python 3.12 container after installing the root, BrokenPilot, then toy-classifier dependencies in the same sequence as CI. That gate includes repository checks, generated navigation, strict MkDocs build, 37 BrokenPilot tests, seven toy-classifier tests, and five artifact-promotion tests. An earlier attempt using the checkout's documentation-only Python 3.14 environment stopped at missing pytest; that was an incomplete local environment, not a failing course test. The successful container run is the relevant gate result.

## Limits and next gate

This was one host, one accelerated operator, and one pinned upstream AIGoat version. Cold AIGoat dependency/model download timing was not measured because Docker reused cached layers. macOS/Linux learner setup, classroom timing, accessibility beyond the exercised browser flows, and independent learner comprehension remain unverified. The course's optional quizzes, external DVAIA comparison, and every additional self-study reading were outside this required-path run. A real pilot should use at least one new student and one instructor, record setup time and support interventions, have them complete the 40-hour path without answer access, and compare their findings with the evidence criteria. Do not describe this run as proof of that human learning outcome.
