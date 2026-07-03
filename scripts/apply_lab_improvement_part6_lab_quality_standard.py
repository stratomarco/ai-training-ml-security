from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BLOCKS = {
    "labs/agent-labs/README.md": ("LAB_QUALITY_STANDARD_AGENT_CONSOLIDATION", """
## Runnable path

The runnable agent-security path is BrokenPilot, not this paper folder.

Use these labs for hands-on work:

- `../brokenpilot/prototype-app/TOOL_CALLING_LAB.md`
- `../brokenpilot/prototype-app/MEMORY_POISONING_LAB.md`
- `../brokenpilot/STANDALONE_CORE_LAB_PATH.md`
- `../../modules/07-agent-tool-security/brokenpilot-tool-validation.md`
- `../../modules/07-agent-tool-security/brokenpilot-memory-validation.md`

This folder remains as a scenario and discussion index only. Do not maintain a second paper version of the same agent lab when BrokenPilot can demonstrate the behavior directly.

## Required deliverable

Students should produce a tool permission matrix or approval policy that includes user role, tenant or object scope, permitted action, denied action, approval requirement, audit requirement, and validation request.

The graded artifact is the control design and validation, not the fact that the model can be tricked.
"""),
    "labs/rag-labs/README.md": ("LAB_QUALITY_STANDARD_RAG_CONSOLIDATION", """
## Runnable path

The runnable RAG-security path is BrokenPilot, not this paper folder.

Use these labs for hands-on work:

- `../brokenpilot/prototype-app/LAB_GUIDE.md`
- `../brokenpilot/STANDALONE_CORE_LAB_PATH.md`
- `../../modules/06-rag-security/brokenpilot-standalone-lab.md`

This folder remains as a scenario and discussion index only. Do not maintain a second paper version of the same RAG lab when BrokenPilot can demonstrate retrieval authorization and indirect prompt injection directly.

## Required deliverable

Students should produce a retrieval authorization and source-trust control note covering identity, tenant, document visibility, source trust, instruction/data separation, logging, validation, and residual risk.

The graded artifact is the retrieval control and validation, not the fact that a poisoned document can influence an answer.
"""),
    "labs/README.md": ("LAB_QUALITY_STANDARD_OVERVIEW", """
## Lab quality standard

The course now separates labs into two classes: attack labs, where students observe a failure and a fix, and reasoning labs, where students review artifacts and produce a decision-grade control recommendation.

Use `LAB_QUALITY_STANDARD.md` as the shared standard. Attack labs should be backed by BrokenPilot or the toy-classifier app where possible. Reasoning labs should end in a graded artifact with strong and weak anchors.
"""),
    "labs/privacy-labs/README.md": ("LAB_QUALITY_STANDARD_PRIVACY_ANCHORS", """
## Worked examples

Use the membership inference worked examples to calibrate reasoning-lab grading:

- `worked-examples/strong-membership-inference-risk-review.md`
- `worked-examples/weak-membership-inference-risk-review.md`

The cross-tenant leakage lab is runnable in BrokenPilot. The membership inference and model inversion lab remains a reasoning lab and should be graded on evidence, control design, validation, and residual risk.
"""),
    "labs/adversarial-ml-labs/README.md": ("LAB_QUALITY_STANDARD_ADVERSARIAL_ANCHORS", """
## Worked examples

Use the poisoning and backdoor worked examples to calibrate tabletop grading:

- `worked-examples/strong-poisoning-backdoor-tabletop.md`
- `worked-examples/weak-poisoning-backdoor-tabletop.md`

The evasion lab is backed by the toy-classifier app. The poisoning and backdoor tabletop remains a reasoning lab unless a future runnable target is added.
"""),
    "labs/architecture-risk-review-labs/README.md": ("LAB_QUALITY_STANDARD_ARCHITECTURE_ANCHORS", """
## Worked examples

Use the DocOps architecture review examples to calibrate grading:

- `worked-examples/strong-docops-architecture-risk-review.md`
- `worked-examples/weak-docops-architecture-risk-review.md`

This is a reasoning lab. Students should submit an architecture risk review, not an exploit transcript.
"""),
    "labs/ai-red-team-labs/README.md": ("LAB_QUALITY_STANDARD_REDTEAM_ANCHORS", """
## Worked examples

Use the AI red-team scoping examples to calibrate scope quality:

- `worked-examples/strong-ai-red-team-scope.md`
- `worked-examples/weak-ai-red-team-scope.md`

The attack-chain lab should use BrokenPilot once the class reaches the runnable capstone path. The scoping tabletop remains a reasoning lab.
"""),
    "modules/08-secure-mlops-supply-chain/README.md": ("LAB_MODALITY_MLOPS", """
## Lab modality note

The MLOps supply-chain labs are reasoning labs. They should be graded on review quality, evidence, promotion controls, artifact integrity, validation, and residual risk. The evidence-pack review lab is the concrete artifact path for this module.
"""),
    "modules/09-privacy-attacks/README.md": ("LAB_MODALITY_PRIVACY", """
## Lab modality note

Module 09 has two lab styles: BrokenPilot cross-tenant leakage is runnable and observable; membership inference and model inversion is a reasoning lab and should be graded with strong and weak anchors.
"""),
    "modules/10-adversarial-ml-robustness/README.md": ("LAB_MODALITY_ADVERSARIAL", """
## Lab modality note

Module 10 has two lab styles: evasion and output integrity are observable through the toy-classifier app; poisoning and backdoor analysis may remain tabletop when the learning goal is risk review and release decision quality.
"""),
}


def ensure_block(path: str, marker: str, body: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    text = target.read_text(encoding="utf-8") if target.exists() else f"# {target.parent.name}\n"
    start = f"<!-- {marker}:START -->"
    end = f"<!-- {marker}:END -->"
    managed = f"{start}\n{body.strip()}\n{end}"
    if start in text and end in text:
        text = text.split(start)[0].rstrip() + "\n\n" + managed + "\n\n" + text.split(end, 1)[1].lstrip()
    else:
        text = text.rstrip() + "\n\n" + managed + "\n"
    target.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"updated: {path}")


def main() -> None:
    for path, (marker, body) in BLOCKS.items():
        ensure_block(path, marker, body)
    print("\nApplied lab improvement Part 6 lab quality-standard package.")


if __name__ == "__main__":
    main()
