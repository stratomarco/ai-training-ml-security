from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "labs/brokenpilot/worked-examples/current-complete-final-report.md",
    "labs/brokenpilot/worked-examples/current-final-report-evidence-map.md",
    "labs/brokenpilot/worked-examples/current-final-report-review-guide.md",
    "course-templates/current-brokenpilot-final-report-template.md",
    "assessments/brokenpilot-current-final-report-rubric.md",
    "modules/12-capstone-brokenpilot/final-report-current-path.md",
    "labs/brokenpilot/CAPSTONE_FINAL_REPORT_CURRENT_PATH.md",
    "instructor/current-brokenpilot-capstone-debrief-guide.md",
    "release-notes/v1.1-dev-current-brokenpilot-final-report.md",
]

REPORT_TERMS = [
    "Direct prompt injection",
    "Model output reaches an HTML sink",
    "Cross-tenant retrieval",
    "Tool confused deputy",
    "Memory poisoning",
    "Remediation backlog",
    "Launch recommendation",
    "Residual risk",
]

EVIDENCE_TERMS = [
    "DIRECT_PROMPT_INJECTION_FOLLOWED",
    "OUTPUT_SINK_TRIGGERED",
    "DOC-002",
    "DOC-006",
    "TCK-2001",
    "MEMORY_INSTRUCTION",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def read(path: str) -> str:
    p = ROOT / path
    require(p.exists(), f"missing {path}")
    text = p.read_text(encoding="utf-8")
    require("TODO" not in text, f"placeholder TODO found in {path}")
    require("TBD" not in text, f"placeholder TBD found in {path}")
    return text


def main() -> None:
    for path in REQUIRED:
        text = read(path)
        min_words = 30 if path.startswith("release-notes/") else 80
        require(len(text.split()) >= min_words, f"{path} is too thin")

    report = read("labs/brokenpilot/worked-examples/current-complete-final-report.md")
    for term in REPORT_TERMS:
        require(term in report, f"report missing term: {term}")
    for term in EVIDENCE_TERMS:
        require(term in report, f"report missing evidence marker: {term}")

    rubric = read("assessments/brokenpilot-current-final-report-rubric.md")
    for term in ["Evidence", "Root cause", "Remediation", "Defense in depth", "Launch decision"]:
        require(term in rubric, f"rubric missing category: {term}")

    template = read("course-templates/current-brokenpilot-final-report-template.md")
    for term in ["Evidence", "Root cause", "Strong control", "Weak control", "Validation", "Residual risk"]:
        require(term in template, f"template missing section: {term}")

    module_path = read("modules/12-capstone-brokenpilot/final-report-current-path.md")
    require("toy-classifier" in module_path, "module path must preserve BrokenPilot/toy-classifier scope split")
    require("MLOps evidence-pack" in module_path, "module path must preserve Module 08 evidence-pack scope")

    print("Current BrokenPilot final report checks passed.")


if __name__ == "__main__":
    main()
