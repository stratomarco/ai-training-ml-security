from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

START = "<!-- lab-routing-content-pass:start -->"
END = "<!-- lab-routing-content-pass:end -->"

MODULES = {
    "05-llm-application-security": {
        "title": "Module 05 Lab Path: LLM Application Security",
        "summary": "Module 05 uses BrokenPilot for direct prompt injection, indirect prompt injection, and insecure output handling. DVAIA remains an optional external comparison lab, not a survival dependency.",
        "runnable": [
            "BrokenPilot direct prompt injection lab",
            "BrokenPilot insecure output handling lab",
            "BrokenPilot standalone Module 05 lab",
        ],
        "reasoning": [
            "Explain why prompt wording is not a security boundary",
            "Map the same root cause across user input, retrieved content, and downstream output sinks",
        ],
        "deliverable": "A Module 05 control note that identifies the trust boundary, shows the vulnerable and controlled behavior, recommends an architectural control, and states residual risk.",
        "keep": [
            "Direct injection through user input",
            "Indirect injection through retrieved content",
            "Output handling through a downstream HTML sink",
        ],
        "avoid": [
            "Do not imply marker detection is a production control",
            "Do not grade students only on making the model misbehave",
        ],
    },
    "06-rag-security": {
        "title": "Module 06 Lab Path: RAG Security",
        "summary": "Module 06 uses BrokenPilot as the primary runnable RAG target. The core learning path is retrieval authorization, source trust, and indirect prompt injection through retrieved documents.",
        "runnable": [
            "BrokenPilot retrieval authorization toggle",
            "BrokenPilot indirect prompt injection through retrieved documents",
            "BrokenPilot standalone Module 06 lab",
        ],
        "reasoning": [
            "Design metadata filters and authorization checks before retrieval results enter the model context",
            "Explain why vector similarity is not authorization",
        ],
        "deliverable": "A retrieval security design note with tenant filters, role/user checks, logging expectations, validation tests, and residual risk.",
        "keep": [
            "Observable cross-tenant retrieval failure and fix",
            "Source trust and context construction discussion",
        ],
        "avoid": [
            "Do not maintain a second paper-only RAG path that duplicates BrokenPilot",
            "Do not present prompt instructions as a substitute for retrieval authorization",
        ],
    },
    "07-agent-tool-security": {
        "title": "Module 07 Lab Path: Agent and Tool Security",
        "summary": "Module 07 remains the reference lab standard. BrokenPilot demonstrates the tool confused-deputy problem, tool authorization, approval gates, audit logging, and defense in depth with memory poisoning.",
        "runnable": [
            "BrokenPilot tool authorization lab",
            "BrokenPilot memory poisoning lab",
            "BrokenPilot tool approval and audit behavior",
        ],
        "reasoning": [
            "Separate model intent from system authorization",
            "Design a tool broker that enforces target-object authorization",
        ],
        "deliverable": "A tool permission matrix or tool-control design with authorization rules, approval rules, audit fields, and validation steps.",
        "keep": [
            "Memory poisoning can steer intent while tool authorization still blocks unsafe execution",
            "The model may propose; the system must decide and enforce",
        ],
        "avoid": [
            "Do not split the module across duplicate paper agent labs",
            "Do not grade only the exploit path",
        ],
    },
    "08-secure-mlops-supply-chain": {
        "title": "Module 08 Lab Path: Secure MLOps and AI Supply Chain",
        "summary": "Module 08 is intentionally a reasoning and evidence-review module. It should not be forced into BrokenPilot. Students inspect realistic supply-chain evidence and produce a concrete promotion-control review.",
        "runnable": [],
        "reasoning": [
            "MLOps evidence-pack review lab",
            "Broken ML pipeline tabletop",
            "Model artifact provenance and promotion-gate review",
        ],
        "deliverable": "An MLOps supply-chain review memo with evidence, risk rating, required controls, validation checks, and a launch/pilot/delay recommendation.",
        "keep": [
            "Artifact integrity",
            "Dependency pinning and lockfiles",
            "Dataset provenance",
            "Promotion gates and rollback",
        ],
        "avoid": [
            "Do not build a fake pipeline just to make the module runnable",
            "Do not reduce supply-chain review to package scanning only",
        ],
    },
    "09-privacy-attacks": {
        "title": "Module 09 Lab Path: Privacy Attacks and Data Protection",
        "summary": "Module 09 combines a runnable BrokenPilot privacy leakage lab with reasoning labs for privacy attacks that should not be forced into a toy web app.",
        "runnable": [
            "BrokenPilot cross-tenant privacy leakage lab",
            "Retrieval authorization toggle for restricted and confidential documents",
        ],
        "reasoning": [
            "Membership inference and model inversion tabletop",
            "Privacy-control residual risk review",
        ],
        "deliverable": "A privacy leakage review with evidence, impacted data class, violated boundary, remediation, validation, and residual logging/privacy risk.",
        "keep": [
            "Cross-tenant fake secret leakage is observable",
            "Retrieval authorization changes the privacy property",
            "Defense-in-depth discussion: retrieval fixed, logs and downstream sinks still matter",
        ],
        "avoid": [
            "Do not claim the BrokenPilot lab demonstrates all privacy attacks",
            "Do not use real personal data or real secrets",
        ],
    },
    "10-adversarial-ml-robustness": {
        "title": "Module 10 Lab Path: Adversarial ML and Robustness",
        "summary": "Module 10 uses the toy-classifier app for observable classical ML attacks. BrokenPilot is not the right target for model evasion, poisoning, extraction, or threshold integrity.",
        "runnable": [
            "Toy-classifier evasion lab",
            "Toy-classifier poisoning lab",
            "Toy-classifier extraction boundary approximation",
            "Toy-classifier output integrity threshold tampering",
        ],
        "reasoning": [
            "Poisoning and backdoor tabletop",
            "Robustness review and hard-gate decision analysis",
        ],
        "deliverable": "A robustness review explaining whether the classifier can safely act as a hard authorization gate, what fallback is required, and how the control should be validated.",
        "keep": [
            "Accuracy is evidence, not a complete risk argument",
            "Frame evasion around the engineering decision, not the trick",
        ],
        "avoid": [
            "Do not force classical ML attacks into BrokenPilot",
            "Do not teach bypass strings as transferable real-world evasion guidance",
        ],
    },
    "11-ai-red-team-methodology": {
        "title": "Module 11 Lab Path: AI Red Team Methodology",
        "summary": "Module 11 uses BrokenPilot for an observable attack-chain path and uses tabletop exercises for scoping, rules of engagement, reporting, and stakeholder communication.",
        "runnable": [
            "BrokenPilot attack-chain lab",
            "BrokenPilot standalone Module 11 lab",
            "Finding rewrite exercise based on BrokenPilot evidence",
        ],
        "reasoning": [
            "AI red-team scoping tabletop",
            "Rules of engagement and test-plan quality review",
        ],
        "deliverable": "A red-team finding or scope package with evidence, root cause, impact, control, validation, residual risk, and clear leadership summary.",
        "keep": [
            "Evidence quality over bug count",
            "Scope, safety, and authorization are part of the assessment",
        ],
        "avoid": [
            "Do not let students treat red teaming as unbounded poking",
            "Do not grade only novelty or exploit count",
        ],
    },
    "12-capstone-brokenpilot": {
        "title": "Module 12 Lab Path: BrokenPilot Capstone",
        "summary": "Module 12 uses BrokenPilot as the capstone target for LLM, RAG, agent, privacy leakage, and red-team reporting. MLOps and adversarial ML material may appear as supporting reasoning evidence, not as BrokenPilot vulnerabilities.",
        "runnable": [
            "BrokenPilot final capstone review",
            "Tool confused-deputy path",
            "RAG leakage and indirect injection path",
            "Memory poisoning path",
            "Privacy leakage path",
        ],
        "reasoning": [
            "Final report risk prioritization",
            "Residual risk and remediation backlog",
            "Executive recommendation",
        ],
        "deliverable": "A final BrokenPilot report and presentation with validated findings, remediation backlog, residual risk, and a leadership-ready recommendation.",
        "keep": [
            "Assessed runnable scope: Modules 05, 06, 07, 09, and 11",
            "Supporting tabletop scope: Modules 08 and 10",
        ],
        "avoid": [
            "Do not require a finding the app cannot exhibit",
            "Do not overclaim BrokenPilot as a target for all twelve modules",
        ],
    },
}

LAB_INDEX = """# Runnable and Reasoning Lab Index

This index keeps the course honest about what students can run and what they should review as a reasoning exercise.

BrokenPilot is the runnable target for LLM, RAG, agent, privacy-leakage, and red-team attack-chain exercises. The toy-classifier app is the runnable target for classical ML attacks. MLOps supply-chain exercises are evidence-review labs. Some privacy and red-team exercises are tabletop by design.

| Area | Primary lab modality | Main target | Graded artifact |
|---|---|---|---|
| Module 05 LLM application security | Runnable attack lab | BrokenPilot | LLM control note |
| Module 06 RAG security | Runnable attack lab | BrokenPilot | Retrieval authorization design |
| Module 07 agent and tool security | Runnable attack lab | BrokenPilot | Tool permission matrix |
| Module 08 MLOps supply chain | Reasoning evidence review | Static evidence pack | Supply-chain review memo |
| Module 09 privacy attacks | Mixed | BrokenPilot plus tabletop | Privacy leakage review |
| Module 10 adversarial ML | Runnable toy ML plus tabletop | Toy classifier | Robustness review |
| Module 11 AI red team | Mixed | BrokenPilot plus tabletop | Red-team finding or scope package |
| Module 12 capstone | Runnable capstone | BrokenPilot | Final report and presentation |

## Delivery rule

Each lab must clearly say whether it is an attack lab or a reasoning lab.

Attack labs must show observable vulnerable behavior and observable controlled behavior. Reasoning labs must end in a concrete artifact with evidence, recommendation, validation, and residual risk.

## Do not force-fit targets

BrokenPilot should not be extended to represent classical ML model attacks or a full MLOps pipeline. That would create the wrong mental model. Use the toy-classifier app for model behavior and the evidence pack for MLOps review.
"""

CLEANUP_BACKLOG = """# Final Cleanup Backlog

Do not work this list until the course content and labs are stable.

## Repository cleanup

- Remove temporary apply scripts that were only used to patch development packages.
- Keep durable check scripts that protect important claims, such as runnable lab tests and repository structure checks.
- Remove generated folders from version control if they are present, especially `.mkdocs-src/`, `site/`, caches, virtual environments, and model artifacts generated during toy-classifier runs.
- Review release notes and development notes for duplication.

## Editorial cleanup

- Normalize voice across modules so the material reads like a coherent instructor-authored course.
- Replace repetitive phrasing and generic summary language.
- Keep the style direct, concrete, and engineering-focused.
- Avoid over-polished generated phrasing, but do not remove useful precision.
- Keep attribution and licensing accurate.

## Website cleanup

- Finish MkDocs navigation only after content stops moving.
- Decide which support files belong in navigation and which should be intentionally excluded.
- Then switch to strict build and CI gates.

## Lab cleanup

- Ensure every runnable lab has deterministic tests.
- Ensure every reasoning lab has strong and weak anchors.
- Ensure every graded artifact has a rubric.
- Ensure no lab references data or scripts that are not shipped.
"""

RELEASE_NOTE = """# v1.1-dev lab routing content pass

This development package aligns Modules 05 through 12 with the correct lab modality and target.

It does not touch MkDocs strict navigation. Website cleanup remains an end-game task after content and labs stabilize.

## Added

- A runnable and reasoning lab index.
- A per-module lab path file for Modules 05 through 12.
- README routing notes for Modules 05 through 12.
- A final cleanup backlog to defer repository and editorial cleanup until content is complete.

## Purpose

The course now tells students exactly what to run, what to review, and what deliverable is graded for each advanced module. This prevents BrokenPilot from being overclaimed as a universal target and keeps the lab modalities aligned with the review guidance.
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"wrote: {path.relative_to(ROOT)}")


def bullet(items: list[str]) -> str:
    if not items:
        return "- Not applicable for this module."
    return "\n".join(f"- {item}" for item in items)


def module_doc(slug: str, data: dict[str, object]) -> str:
    return f"""# {data['title']}

## Role in the 40-hour course

{data['summary']}

## Runnable path

{bullet(data['runnable'])}

## Reasoning path

{bullet(data['reasoning'])}

## Graded deliverable

{data['deliverable']}

## Keep central

{bullet(data['keep'])}

## Avoid

{bullet(data['avoid'])}

## Instructor note

Use this file as the first stop when deciding what to run live, what to assign as self-study, and what to grade. If a lab cannot produce observable vulnerable and controlled behavior, treat it as a reasoning lab and grade the artifact instead of pretending it is runnable.
"""


def routing_block(slug: str, data: dict[str, object]) -> str:
    return f"""{START}

## Lab routing note

{data['summary']}

Primary graded deliverable: {data['deliverable']}

See `lab-path.md` in this module and `labs/RUNNABLE_AND_REASONING_LAB_INDEX.md` for the full lab modality map.

{END}"""


def upsert_block(path: Path, block: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        text = path.read_text(encoding="utf-8")
    else:
        text = f"# {path.parent.name}\n"

    if START in text and END in text:
        before = text.split(START)[0].rstrip()
        after = text.split(END, 1)[1].lstrip()
        new_text = before + "\n\n" + block + "\n\n" + after
    else:
        new_text = text.rstrip() + "\n\n" + block + "\n"

    path.write_text(new_text.rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"updated: {path.relative_to(ROOT)}")


def main() -> None:
    write(ROOT / "labs" / "RUNNABLE_AND_REASONING_LAB_INDEX.md", LAB_INDEX)
    write(ROOT / "CLEANUP_BEFORE_RELEASE.md", CLEANUP_BACKLOG)
    write(ROOT / "release-notes" / "v1.1-dev-lab-routing-content-pass.md", RELEASE_NOTE)

    for slug, data in MODULES.items():
        module_dir = ROOT / "modules" / slug
        write(module_dir / "lab-path.md", module_doc(slug, data))
        upsert_block(module_dir / "README.md", routing_block(slug, data))

    print("\nApplied lab routing content pass.")


if __name__ == "__main__":
    main()
