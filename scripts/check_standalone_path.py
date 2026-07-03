from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "labs/brokenpilot/STANDALONE_CORE_LAB_PATH.md",
    "docs/lab-setup/brokenpilot-standalone-path.md",
    "docs/lab-setup/dvaia-fallback-decision-guide.md",
    "modules/05-llm-application-security/brokenpilot-standalone-lab.md",
    "modules/06-rag-security/brokenpilot-standalone-lab.md",
    "modules/11-ai-red-team-methodology/brokenpilot-standalone-lab.md",
    "instructor/brokenpilot-standalone-facilitation-guide.md",
    "assessments/standalone-hands-on-path-rubric.md",
    "labs/brokenpilot/prototype-app/tests/test_standalone_core_path.py",
]

FORBIDDEN = "\u2014"


def main() -> int:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    if missing:
        print("Missing standalone path files:")
        for path in missing:
            print(f"- {path}")
        return 1

    bad = []
    for rel in REQUIRED:
        path = ROOT / rel
        if path.suffix in {".md", ".py"} and FORBIDDEN in path.read_text(encoding="utf-8"):
            bad.append(rel)

    if bad:
        print("Em dash found in standalone path files:")
        for path in bad:
            print(f"- {path}")
        return 1

    print("Standalone path check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
