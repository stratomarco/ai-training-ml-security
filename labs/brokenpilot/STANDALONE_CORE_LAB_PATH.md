# BrokenPilot Standalone Core Lab Path

BrokenPilot is the course-owned core hands-on target for the one-week course. DVAIA remains an optional external reference lab.

This path covers the executable parts of Modules 05, 06, 07, 09, 11, and 12. Module 08 uses a static MLOps evidence pack. Modules 03 and 10 use the separate toy classifier for classical ML attacks.

## When to use this path

Use this path when:

- DVAIA is unavailable, broken, slow, blocked by corporate network controls, or not approved for installation.
- The instructor wants one deterministic local target for the whole cohort.
- Students are working offline or in a restricted environment.
- The course needs repeatable evidence for practice and optional feedback.

Use DVAIA as an optional extension when it is available and time permits.

## Required local target

Start BrokenPilot from the repository root.

Windows PowerShell:

```powershell
cd labs\brokenpilot\prototype-app
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest
python run_lab.py --profile vulnerable
```

macOS or Linux:

```bash
cd labs/brokenpilot/prototype-app
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
pytest
python run_lab.py --profile vulnerable
```

Open:

```text
http://127.0.0.1:8010
```

## Required evidence

Each student team must collect evidence for four runnable behaviors:

| Area | Endpoint | Required evidence |
|---|---|---|
| Prompt injection handling | `POST /chat` | vulnerable output and controlled output |
| Retrieval authorization | `POST /retrieve` | cross-tenant retrieval before and after authz |
| Tool confused deputy | `POST /tools/update-ticket` | cross-tenant update before and after tool authz |
| Memory poisoning | `POST /memory/add`, `POST /agent/run` | poisoned intent and independent tool-authz block |

The evidence does not need to be polished during the lab. It must be clear enough to support a final finding later.

## Control toggles

BrokenPilot controls are set by the named `run_lab.py --profile` launcher. The `vulnerable` profile is intentionally unsafe for fake local data. Stop the server before changing profiles and verify `GET /controls` after restart.

| Toggle | Required in standalone path | Teaching point |
|---|---:|---|
| `ENABLE_PROMPT_INJECTION_FILTER` | yes | deterministic stand-in for instruction/data separation |
| `ENABLE_RETRIEVAL_AUTHZ` | yes | retrieval is an authorization boundary |
| `ENABLE_TOOL_AUTHZ` | yes | tool authorization must be independent of model intent |
| `ENABLE_TOOL_APPROVAL` | optional | workflow-ending actions need approval gates |
| `ENABLE_MEMORY_REVIEW` | yes | memory writes need trust and review policy |
| `ENABLE_MEMORY_ISOLATION` | yes | memory must not become global executable policy |

## Important honesty note about prompt-injection filtering

The BrokenPilot prompt-injection control uses deterministic marker detection to make the lab repeatable. This is not a production control. A real attacker can avoid exact markers, encode instructions, split instructions across documents, or hide instructions in normal-looking support text.

The architectural teaching point is not signature matching. The real control objective is:

- treat retrieved content as data, not authority;
- keep system instructions outside retrieved text;
- reduce the privileges of generated output;
- enforce authorization and policy outside the model;
- log and review suspicious retrieval and answer behavior.

Students should explicitly say this in their findings.

## Module mapping

| Module | BrokenPilot activity | Assessment output |
|---|---|---|
| 05 LLM Application Security | direct/indirect injection and output handling | one finding with mitigation limits |
| 06 RAG Security | retrieval authorization and indirect injection | evidence log and control recommendation |
| 07 Agent and Tool Security | tool authz, approval, memory poisoning | tool permission matrix or finding |
| 09 Privacy Attacks | cross-tenant retrieval of fake sensitive fragments | privacy finding and residual logging risk |
| 11 AI Red Team Methodology | mini red-team sprint over the same target | rewritten strong finding |
| 12 BrokenPilot Capstone | end-to-end review | final report and presentation |

## Instructor success criteria

A successful standalone run has these properties:

- every team can start the app locally or through Docker;
- every team can reproduce at least two vulnerable behaviors;
- every team can demonstrate at least one control changing the result;
- no team is asked to reproduce a vulnerability the runnable target cannot exhibit;
- the final report separates demonstrated findings from tabletop risks.
