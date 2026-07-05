from __future__ import annotations

from pathlib import Path

ROOT = Path.cwd()

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

REQUIRED_HEADINGS = [
    "## What this module is really about",
    "## Question to keep in mind",
    "## Decisions students must learn to make",
    "## Lab or exercise connection",
    "## What a strong submission looks like",
    "## Common misreadings to avoid",
    "## Exit ticket",
]

REQUIRED_FILES = [
    "docs/start-here/student-reading-flow.md",
    "CONTENT_QUALITY_EDITING_GUIDE.md",
    "labs/READING_TO_LAB_TRANSFER_CHECKLIST.md",
    "instructor/teaching-from-reading-guides.md",
    "course-templates/module-reading-notes-template.md",
    "release-notes/v1.1-dev-content-quality-reading-flow-pass.md",
]

BANNED_PHRASES = [
    "as an ai language model",
    "delve into",
    "rapidly evolving landscape",
]


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def main() -> None:
    for rel in REQUIRED_FILES:
        text = read(ROOT / rel)
        if len(text.strip()) < 200:
            fail(f"file is too thin: {rel}")

    for slug in MODULES:
        guide = ROOT / "modules" / slug / "student-reading-guide.md"
        text = read(guide)
        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                fail(f"{guide.relative_to(ROOT)} missing heading: {heading}")
        if "security" not in text.lower():
            fail(f"{guide.relative_to(ROOT)} does not appear to discuss security")
        if "lab" not in text.lower() and "exercise" not in text.lower():
            fail(f"{guide.relative_to(ROOT)} does not connect to a lab or exercise")
        if "root cause" not in text.lower() and slug in {
            "05-llm-application-security",
            "06-rag-security",
            "07-agent-tool-security",
            "11-ai-red-team-methodology",
            "12-capstone-brokenpilot",
        }:
            fail(f"{guide.relative_to(ROOT)} should mention root cause")

        readme = ROOT / "modules" / slug / "README.md"
        readme_text = read(readme)
        if "student-reading-guide.md" not in readme_text:
            fail(f"{readme.relative_to(ROOT)} does not link the reading guide")

    combined = "\n".join(
        path.read_text(encoding="utf-8", errors="ignore").lower()
        for path in [ROOT / rel for rel in REQUIRED_FILES]
        + [ROOT / "modules" / slug / "student-reading-guide.md" for slug in MODULES]
        if path.exists()
    )
    for phrase in BANNED_PHRASES:
        if phrase in combined:
            fail(f"generated-sounding banned phrase present: {phrase}")

    cleanup = read(ROOT / "CLEANUP_BEFORE_RELEASE.md")
    if "Content voice cleanup reminder" not in cleanup:
        fail("cleanup reminder missing content voice section")

    print("Content-quality reading-flow checks passed.")


if __name__ == "__main__":
    main()
