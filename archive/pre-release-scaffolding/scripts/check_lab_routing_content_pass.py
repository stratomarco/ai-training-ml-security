from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULES = [
    "05-llm-application-security",
    "06-rag-security",
    "07-agent-tool-security",
    "08-secure-mlops-supply-chain",
    "09-privacy-attacks",
    "10-adversarial-ml-robustness",
    "11-ai-red-team-methodology",
    "12-capstone-brokenpilot",
]

REQUIRED_FILES = [
    "labs/RUNNABLE_AND_REASONING_LAB_INDEX.md",
    "CLEANUP_BEFORE_RELEASE.md",
    "release-notes/v1.1-dev-lab-routing-content-pass.md",
]

REQUIRED_PHRASES = {
    "labs/RUNNABLE_AND_REASONING_LAB_INDEX.md": [
        "BrokenPilot is the runnable target for LLM, RAG, agent, privacy-leakage, and red-team attack-chain exercises",
        "toy-classifier app is the runnable target for classical ML attacks",
        "MLOps supply-chain exercises are evidence-review labs",
    ],
    "modules/08-secure-mlops-supply-chain/lab-path.md": [
        "intentionally a reasoning and evidence-review module",
        "Do not build a fake pipeline just to make the module runnable",
    ],
    "modules/10-adversarial-ml-robustness/lab-path.md": [
        "toy-classifier app",
        "Do not force classical ML attacks into BrokenPilot",
    ],
    "modules/12-capstone-brokenpilot/lab-path.md": [
        "Assessed runnable scope: Modules 05, 06, 07, 09, and 11",
        "Do not require a finding the app cannot exhibit",
    ],
}

FORBIDDEN_PHRASES = [
    "BrokenPilot covers all twelve modules",
    "BrokenPilot demonstrates all privacy attacks",
    "BrokenPilot demonstrates classical ML attacks",
    "MLOps pipeline runnable target",
]


def require_file(rel: str) -> None:
    path = ROOT / rel
    if not path.exists():
        raise SystemExit(f"missing required file: {rel}")


def require_text(rel: str, phrase: str) -> None:
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    if phrase not in text:
        raise SystemExit(f"missing phrase in {rel}: {phrase}")


def main() -> None:
    for rel in REQUIRED_FILES:
        require_file(rel)

    for module in MODULES:
        require_file(f"modules/{module}/lab-path.md")
        require_file(f"modules/{module}/README.md")
        require_text(f"modules/{module}/README.md", "## Lab routing note")
        require_text(f"modules/{module}/lab-path.md", "## Runnable path")
        require_text(f"modules/{module}/lab-path.md", "## Reasoning path")
        require_text(f"modules/{module}/lab-path.md", "## Graded deliverable")
        require_text(f"modules/{module}/lab-path.md", "## Avoid")

    for rel, phrases in REQUIRED_PHRASES.items():
        for phrase in phrases:
            require_text(rel, phrase)

    searchable = [ROOT / "labs" / "RUNNABLE_AND_REASONING_LAB_INDEX.md"] + [
        ROOT / "modules" / module / "lab-path.md" for module in MODULES
    ]
    for path in searchable:
        text = path.read_text(encoding="utf-8")
        for phrase in FORBIDDEN_PHRASES:
            if phrase in text:
                raise SystemExit(f"forbidden overclaim found in {path.relative_to(ROOT)}: {phrase}")

    print("Lab routing content pass checks passed.")


if __name__ == "__main__":
    main()
