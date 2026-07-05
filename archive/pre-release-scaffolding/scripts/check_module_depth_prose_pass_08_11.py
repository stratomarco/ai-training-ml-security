from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULES = [
    "08-secure-mlops-supply-chain",
    "09-privacy-attacks",
    "10-adversarial-ml-robustness",
    "11-ai-red-team-methodology",
]
FILES = [
    "deep-dive.md",
    "attack-anatomy.md",
    "controls-and-remediations.md",
    "common-mistakes.md",
    "worked-example.md",
]
REQUIRED_SUPPORT = [
    "instructor/teaching-modules-08-11-depth-pass.md",
    "assessments/modules-08-11-depth-checkpoints.md",
    "course-templates/depth-reading-response-template.md",
    "release-notes/v1.1-dev-module-depth-prose-pass-08-11.md",
]
REQUIRED_PHRASES = {
    "08-secure-mlops-supply-chain/deep-dive.md": ["model artifact", "provenance", "rollback"],
    "08-secure-mlops-supply-chain/controls-and-remediations.md": ["artifact digest", "promotion", "Validation"],
    "09-privacy-attacks/deep-dive.md": ["retrieval", "logs", "traces"],
    "09-privacy-attacks/worked-example.md": ["FAKE-ALPHA-PAYMENT-TOKEN-DO-NOT-USE", "Residual risk"],
    "10-adversarial-ml-robustness/deep-dive.md": ["hard decision gate", "toy-classifier", "fallback"],
    "10-adversarial-ml-robustness/worked-example.md": ["hard gate", "threshold", "Residual risk"],
    "11-ai-red-team-methodology/deep-dive.md": ["launch", "evidence", "scope"],
    "11-ai-red-team-methodology/worked-example.md": ["defense in depth", "tool_authorization_denied", "Residual risk"],
}

BAD_STRINGS = ["TODO", "TBD", "lorem ipsum", "as an AI", "I apologize"]


def words(text: str) -> int:
    return len([w for w in text.replace("/", " ").split() if w.strip()])


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    for module in MODULES:
        base = ROOT / "modules" / module
        if not base.exists():
            fail(f"missing module directory: {base.relative_to(ROOT)}")
        for filename in FILES:
            path = base / filename
            if not path.exists():
                fail(f"missing file: {path.relative_to(ROOT)}")
            text = path.read_text(encoding="utf-8")
            minimum = {
                "deep-dive.md": 450,
                "attack-anatomy.md": 300,
                "controls-and-remediations.md": 400,
                "common-mistakes.md": 275,
                "worked-example.md": 350,
            }[filename]
            if words(text) < minimum:
                fail(f"file too thin: {path.relative_to(ROOT)} has {words(text)} words, expected at least {minimum}")
            for bad in BAD_STRINGS:
                if bad.lower() in text.lower():
                    fail(f"bad placeholder/generic phrase {bad!r} in {path.relative_to(ROOT)}")
            for phrase in ["Validation", "Residual risk"]:
                if filename in {"controls-and-remediations.md", "worked-example.md"} and phrase not in text:
                    fail(f"{path.relative_to(ROOT)} missing {phrase}")
        readme = base / "README.md"
        if not readme.exists() or "Depth pass for advanced modules" not in readme.read_text(encoding="utf-8"):
            fail(f"README not updated for {module}")

    for rel, phrases in REQUIRED_PHRASES.items():
        path = ROOT / "modules" / rel
        if not path.exists():
            fail(f"missing required phrase file: {rel}")
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                fail(f"{rel} missing phrase: {phrase}")

    support_minimums = {
        "instructor/teaching-modules-08-11-depth-pass.md": 180,
        "assessments/modules-08-11-depth-checkpoints.md": 140,
        "course-templates/depth-reading-response-template.md": 70,
        "release-notes/v1.1-dev-module-depth-prose-pass-08-11.md": 60,
    }
    for rel in REQUIRED_SUPPORT:
        path = ROOT / rel
        if not path.exists():
            fail(f"missing support file: {rel}")
        text = path.read_text(encoding="utf-8")
        minimum = support_minimums[rel]
        if words(text) < minimum:
            fail(f"support file too thin: {rel} has {words(text)} words, expected at least {minimum}")

    cleanup = ROOT / "CLEANUP_BEFORE_RELEASE.md"
    if not cleanup.exists() or "Module depth prose pass cleanup" not in cleanup.read_text(encoding="utf-8"):
        fail("cleanup reminder missing")

    # Style preference only: warn, do not fail, if old long dash appears.
    em_dash_hits = []
    for path in ROOT.rglob("*.md"):
        if any(part in {".git", ".venv", "site", ".mkdocs-src"} for part in path.parts):
            continue
        if "—" in path.read_text(encoding="utf-8"):
            em_dash_hits.append(path.relative_to(ROOT).as_posix())
    if em_dash_hits:
        print("WARN: em dash found in files. Style preference only, not a failure.")
        for hit in em_dash_hits[:10]:
            print(f"  {hit}")

    print("Module depth prose pass checks passed.")


if __name__ == "__main__":
    main()
