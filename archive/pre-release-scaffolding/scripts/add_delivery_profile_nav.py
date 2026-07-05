from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MKDOCS = ROOT / "mkdocs.yml"

MODULES = [
    "01-security-engineering-for-ai",
    "02-ml-system-architecture",
    "03-owasp-ml-top-10",
    "04-biml-architectural-risk-analysis",
    "05-llm-application-security",
    "06-rag-security",
    "07-agent-tool-security",
    "08-secure-mlops-supply-chain",
    "09-privacy-attacks",
    "10-adversarial-ml-robustness",
    "11-ai-red-team-methodology",
    "12-capstone-brokenpilot",
]


def insert_after(text: str, needle: str, addition: str) -> str:
    if addition.strip() in text:
        return text
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if needle in line:
            lines.insert(idx + 1, addition)
            return "\n".join(lines) + "\n"
    print(f"warning: did not find nav anchor: {needle}")
    return text


def main() -> int:
    if not MKDOCS.exists():
        print("mkdocs.yml not found")
        return 1

    text = MKDOCS.read_text(encoding="utf-8")

    text = insert_after(
        text,
        '"One-Week Learning Path": start-here/one-week-learning-path.md',
        '      - "40-Hour Course Map": start-here/40-hour-course-map.md',
    )

    for module in MODULES:
        text = insert_after(
            text,
            f'"Overview": modules/{module}/README.md',
            f'          - "Delivery Profile": modules/{module}/delivery-profile.md',
        )

    text = insert_after(
        text,
        '"40-Hour Delivery Plan": instructor/40-hour-delivery-plan.md',
        '      - "40-Hour Module Delivery Profiles": instructor/40-hour-module-delivery-profiles.md',
    )

    text = insert_after(
        text,
        '"40-Hour Assessment Plan": assessments/40-hour-course-assessment-plan.md',
        '      - "40-Hour Deliverables Map": assessments/40-hour-deliverables-map.md',
    )

    MKDOCS.write_text(text, encoding="utf-8", newline="\n")
    print("Updated mkdocs.yml with delivery profile navigation entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
