from __future__ import annotations

from pathlib import Path
import sys

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

REQUIRED = [
    "COURSE_STORYLINE.md",
    "COURSE_VOICE_AND_COHESION_REVIEW.md",
    "modules/MODULE_HANDOFF_MAP.md",
    "instructor/teaching-the-course-narrative.md",
    "instructor/final-voice-cohesion-review-guide.md",
    "labs/LAB_DEBRIEF_LANGUAGE_GUIDE.md",
    "assessments/voice-and-cohesion-review-checklist.md",
    "course-templates/final-voice-cohesion-review-template.md",
    "release-notes/v1.1-dev-final-voice-cohesion-pass.md",
]

NEEDED_PHRASES = [
    "security engineering",
    "trust boundary",
    "validation",
    "residual risk",
    "decision",
]

BAD_PLACEHOLDERS = ["TODO", "TBD", "FIXME", "lorem ipsum"]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def read(path: str) -> str:
    p = ROOT / path
    if not p.exists():
        fail(f"missing {path}")
    return p.read_text(encoding="utf-8")


def main() -> None:
    for path in REQUIRED:
        text = read(path)
        if len(text.split()) < 80:
            fail(f"{path} is too thin")
        lower = text.lower()
        for bad in BAD_PLACEHOLDERS:
            if bad.lower() in lower:
                fail(f"placeholder found in {path}: {bad}")

    storyline = read("COURSE_STORYLINE.md").lower()
    for phrase in NEEDED_PHRASES:
        if phrase not in storyline:
            fail(f"COURSE_STORYLINE.md missing phrase: {phrase}")

    handoff = read("modules/MODULE_HANDOFF_MAP.md")
    for n in range(1, 12):
        if f"{n:02d}" not in handoff:
            fail(f"module handoff missing {n:02d}")

    for slug in MODULES:
        note_path = f"modules/{slug}/cohesion-note.md"
        note = read(note_path)
        lower = note.lower()
        for phrase in ["why this module exists", "handoff", "instructor emphasis", "student exit line"]:
            if phrase not in lower:
                fail(f"{note_path} missing section phrase: {phrase}")
        if len(note.split()) < 140:
            fail(f"{note_path} is too thin")

        readme = ROOT / "modules" / slug / "README.md"
        if readme.exists() and "cohesion-note.md" not in readme.read_text(encoding="utf-8"):
            fail(f"README not linked to cohesion note: {slug}")

    cleanup = ROOT / "CLEANUP_BEFORE_RELEASE.md"
    if cleanup.exists() and "final voice and cohesion cleanup reminder" not in cleanup.read_text(encoding="utf-8").lower():
        fail("CLEANUP_BEFORE_RELEASE.md missing final voice reminder")

    print("Final voice and cohesion checks passed.")


if __name__ == "__main__":
    main()
