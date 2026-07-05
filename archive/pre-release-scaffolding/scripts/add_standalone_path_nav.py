from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MKDOCS = ROOT / "mkdocs.yml"

ENTRIES = [
    ('      - "BrokenPilot Standalone Path": lab-setup/brokenpilot-standalone-path.md\n', '      - "DVAIA Setup": lab-setup/dvaia.md\n'),
    ('      - "DVAIA Fallback Decision Guide": lab-setup/dvaia-fallback-decision-guide.md\n', '      - "DVAIA Setup": lab-setup/dvaia.md\n'),
    ('          - "BrokenPilot Standalone Lab": modules/05-llm-application-security/brokenpilot-standalone-lab.md\n', '          - "Exercise": modules/05-llm-application-security/exercise-llm-application-security-review.md\n'),
    ('          - "BrokenPilot Standalone Lab": modules/06-rag-security/brokenpilot-standalone-lab.md\n', '          - "Exercise": modules/06-rag-security/exercise-rag-threat-model.md\n'),
    ('          - "BrokenPilot Standalone Lab": modules/11-ai-red-team-methodology/brokenpilot-standalone-lab.md\n', '          - "Finding Rewrite Exercise": modules/11-ai-red-team-methodology/exercise-finding-rewrite.md\n'),
    ('      - "BrokenPilot Standalone Core Path": labs/brokenpilot/STANDALONE_CORE_LAB_PATH.md\n', '      - "BrokenPilot Capstone": labs/brokenpilot/README.md\n'),
    ('      - "BrokenPilot Standalone Facilitation Guide": instructor/brokenpilot-standalone-facilitation-guide.md\n', '      - "Finding Rewrite Facilitation Guide": instructor/finding-rewrite-facilitation-guide.md\n'),
    ('      - "Standalone Hands-On Path Rubric": assessments/standalone-hands-on-path-rubric.md\n', '      - "Finding Rewrite Exercise": assessments/finding-rewrite-exercise.md\n'),
]


def insert_after(text: str, entry: str, anchor: str) -> str:
    if entry.strip() in text:
        return text
    if anchor not in text:
        print(f"anchor not found, skipped: {anchor.strip()}")
        return text
    return text.replace(anchor, anchor + entry, 1)


def main() -> int:
    if not MKDOCS.exists():
        print("mkdocs.yml not found")
        return 1

    text = MKDOCS.read_text(encoding="utf-8")
    updated = text
    for entry, anchor in ENTRIES:
        updated = insert_after(updated, entry, anchor)

    if updated != text:
        MKDOCS.write_text(updated, encoding="utf-8", newline="\n")
        print("mkdocs.yml updated with standalone path entries.")
    else:
        print("mkdocs.yml already contains standalone path entries or anchors were missing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
