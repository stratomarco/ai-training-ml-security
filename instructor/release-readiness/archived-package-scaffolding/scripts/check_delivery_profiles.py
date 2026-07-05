from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
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

REQUIRED_PHRASES = [
    "## Live-course role",
    "## Core content to keep",
    "## Compressed path",
    "## Lab or exercise path",
    "## Self-study path",
    "## Safe cuts",
    "## Instructor checks",
]


def main() -> int:
    failures: list[str] = []

    for module in MODULES:
        path = ROOT / "modules" / module / "delivery-profile.md"
        if not path.exists():
            failures.append(f"missing: {path.relative_to(ROOT)}")
            continue

        text = path.read_text(encoding="utf-8")
        for phrase in REQUIRED_PHRASES:
            if phrase not in text:
                failures.append(f"{path.relative_to(ROOT)} missing section: {phrase}")

    for path in [
        ROOT / "instructor" / "40-hour-module-delivery-profiles.md",
        ROOT / "docs" / "start-here" / "40-hour-course-map.md",
        ROOT / "assessments" / "40-hour-deliverables-map.md",
    ]:
        if not path.exists():
            failures.append(f"missing: {path.relative_to(ROOT)}")

    if failures:
        print("Delivery profile check failed.")
        for item in failures:
            print(f"- {item}")
        return 1

    print("Delivery profile check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
