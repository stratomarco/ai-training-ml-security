from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FAILURES: list[str] = []


def require(path: str, text: str | None = None) -> None:
    p = ROOT / path
    if not p.exists():
        FAILURES.append(f"missing required file: {path}")
        return
    if text is not None:
        content = p.read_text(encoding="utf-8")
        if text not in content:
            FAILURES.append(f"{path} missing expected text: {text}")


def forbid(path: str) -> None:
    if (ROOT / path).exists():
        FAILURES.append(f"student-facing/pre-release file should have been archived: {path}")


def main() -> None:
    require("PUBLISHED_COURSE_VIEW.md", "Student-facing by default")
    require("instructor/release-readiness/README.md", "Release readiness archive")
    require("instructor/release-readiness/archived-pre-release-docs/README.md", "Archived pre-release documents")
    require("CLEANUP_BEFORE_RELEASE.md", "Release cleanup phase 2 status")

    # These are the common pre-release documents that should no longer sit at repo root
    # after this cleanup phase. They may not all exist in every checkout.
    for path in [
        "COURSE_CONTENT_AUDIT.md",
        "COURSE_DRY_RUN_PLAN_40H.md",
        "COURSE_FLOW_REVIEW.md",
        "COURSE_COMPLETION_SCORECARD.md",
        "COURSE_VOICE_AND_COHESION_REVIEW.md",
        "ROUND3_CONTENT_QUALITY_FIXES.md",
        "RELEASE_CLEANUP_PHASE1_REPORT.md",
        "README_PACKAGE.md",
    ]:
        forbid(path)

    # Final lab readiness review belongs with release/instructor readiness material,
    # not in the student lab root.
    forbid("labs/FINAL_LAB_READINESS_REVIEW.md")
    forbid("instructor/FINAL_LAB_READINESS_REVIEW.md")

    # Legacy duplicate lab folders should be clearly marked as optional or BrokenPilot-primary.
    legacy_checks = [
        ("labs/agent-labs/README.md", "BrokenPilot is the primary runnable path"),
        ("labs/rag-labs/README.md", "BrokenPilot is the primary runnable path"),
        ("labs/dvaia-guides/README.md", "optional appendix material"),
    ]
    for path, text in legacy_checks:
        if (ROOT / path).exists():
            require(path, text)

    if FAILURES:
        print("Release cleanup phase 2 check failed:")
        for failure in FAILURES:
            print(f"- {failure}")
        raise SystemExit(1)

    print("Release cleanup phase 2 checks passed.")


if __name__ == "__main__":
    main()
