from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def ok(message: str) -> None:
    print(f"OK: {message}")


def file_contains(path: Path, needle: str) -> bool:
    return path.exists() and needle in path.read_text(encoding="utf-8", errors="ignore")


def main() -> None:
    mkdocs = ROOT / "mkdocs.yml"
    if not mkdocs.exists():
        fail("mkdocs.yml is missing")
    text = mkdocs.read_text(encoding="utf-8", errors="ignore")
    if "course-templates/" not in text and "templates/" not in text:
        fail("mkdocs.yml does not include a templates navigation section")
    for required in ["labs/brokenpilot/", "not_in_nav:"]:
        if required not in text:
            fail(f"mkdocs.yml does not include expected navigation/config text: {required}")
    if list((ROOT / "modules").glob("*/delivery-profile.md")) and "delivery-profile.md" not in text:
        fail("delivery profiles exist but are not present in mkdocs.yml navigation")
    ok("mkdocs.yml includes templates, labs, delivery profiles when present, and not_in_nav")

    workflows = list((ROOT / ".github" / "workflows").glob("*.yml")) + list((ROOT / ".github" / "workflows").glob("*.yaml"))
    if not workflows:
        fail("no GitHub workflow files found")
    if not any(file_contains(path, "mkdocs build --strict") for path in workflows):
        fail("no workflow uses mkdocs build --strict")
    ok("a workflow uses mkdocs build --strict")

    if not any(file_contains(path, "pytest") and "brokenpilot" in path.read_text(encoding="utf-8", errors="ignore").lower() for path in workflows):
        fail("no workflow appears to run BrokenPilot pytest")
    ok("a workflow runs BrokenPilot pytest")

    print("\nRound 2 release-readiness checks passed.")


if __name__ == "__main__":
    main()
