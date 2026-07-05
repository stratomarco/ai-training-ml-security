
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "STYLE_AND_VOICE_FINAL_PASS.md",
    "VOICE_POLISH_PASS_REPORT.md",
    "instructor/release-readiness/student-facing-cleanup-checklist.md",
    "instructor/release-readiness/final-human-editor-pass.md",
    "scripts/report_voice_polish_hotspots.py",
]


def main() -> None:
    missing = [rel for rel in REQUIRED if not (ROOT / rel).exists()]
    if missing:
        print("Release cleanup phase 5 check failed:")
        for rel in missing:
            print(f"- missing: {rel}")
        raise SystemExit(1)

    guide = (ROOT / "STYLE_AND_VOICE_FINAL_PASS.md").read_text(encoding="utf-8")
    for phrase in ["Preserve the security argument", "Do not overclaim", "What good final prose looks like"]:
        if phrase not in guide:
            raise SystemExit(f"Release cleanup phase 5 check failed: style guide missing {phrase!r}")

    print("Release cleanup phase 5 checks passed.")


if __name__ == "__main__":
    main()
