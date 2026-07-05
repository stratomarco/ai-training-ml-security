from __future__ import annotations

from pathlib import Path

ROOT = Path.cwd()
MODULES = [
    "01-security-engineering-for-ai",
    "02-ml-system-architecture",
    "03-owasp-ml-top-10",
    "04-biml-architectural-risk-analysis",
]
FILES = [
    "deep-dive.md",
    "attack-anatomy.md",
    "controls-and-remediations.md",
    "common-mistakes.md",
    "worked-example.md",
]
REQUIRED_TERMS = [
    "control",
    "validation",
    "residual risk",
]
FORBIDDEN = [
    "TODO",
    "TBD",
    "placeholder",
    "lorem ipsum",
]


def fail(msg: str) -> None:
    raise SystemExit(f"FAIL: {msg}")


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        fail(f"missing {rel}")
    return path.read_text(encoding="utf-8")


def main() -> None:
    for module in MODULES:
        combined = ""
        for filename in FILES:
            rel = f"modules/{module}/{filename}"
            text = read(rel)
            combined += "\n" + text
            min_words = 150 if filename == "common-mistakes.md" else 250
            if len(text.split()) < min_words:
                fail(f"{rel} is too short for a depth pass")
            lower = text.lower()
            for bad in FORBIDDEN:
                if bad.lower() in lower:
                    fail(f"{rel} contains forbidden placeholder text: {bad}")

        module_lower = combined.lower()
        for term in REQUIRED_TERMS:
            if term not in module_lower:
                fail(f"modules/{module} depth pass does not mention {term}")

        for rel in [
            f"modules/{module}/controls-and-remediations.md",
            f"modules/{module}/worked-example.md",
        ]:
            text = read(rel).lower()
            for term in REQUIRED_TERMS:
                if term not in text:
                    fail(f"{rel} does not mention {term}")

        read(f"modules/{module}/README.md")
        if "depth-prose-pass-01-04" not in read(f"modules/{module}/README.md"):
            fail(f"modules/{module}/README.md missing depth reading path")

    support_files = [
        "instructor/teaching-modules-01-04-depth-pass.md",
        "assessments/modules-01-04-depth-checkpoints.md",
        "course-templates/foundation-risk-review-template.md",
        "release-notes/v1.1-dev-module-depth-prose-pass-01-04.md",
    ]
    for rel in support_files:
        text = read(rel)
        if len(text.split()) < 80:
            fail(f"{rel} is unexpectedly short")

    template = read("course-templates/foundation-risk-review-template.md").lower()
    for section in ["model role", "trust boundaries", "validation", "residual risk", "recommendation"]:
        if section not in template:
            fail(f"foundation template missing {section}")

    print("Module depth prose pass 01 to 04 checks passed.")


if __name__ == "__main__":
    main()
