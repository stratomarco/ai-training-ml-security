from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MKDOCS = ROOT / "mkdocs.yml"
SYNC_SCRIPT = ROOT / "scripts" / "sync_mkdocs_content.py"
WORKFLOW_DIR = ROOT / ".github" / "workflows"

PREFERRED_MODULE_ORDER = [
    "README.md",
    "delivery-profile.md",
    "student-handout.md",
    "slides.md",
    "instructor-notes.md",
    "deep-dive.md",
    "attack-anatomy.md",
    "controls-and-remediations.md",
    "common-mistakes.md",
    "worked-example.md",
    "checklist.md",
    "quiz.md",
    "references.md",
]

PREFERRED_BROKENPILOT_ORDER = [
    "README.md",
    "STANDALONE_CORE_LAB_PATH.md",
    "scenario.md",
    "student-brief.md",
    "architecture.md",
    "data-model.md",
    "tools.md",
    "roles.md",
    "evidence-log-guide.md",
    "remediation-backlog-guide.md",
    "final-presentation-guide.md",
    "grading-rubric.md",
    "capstone-assessment-scope.md",
    "module-mapping.md",
    "secure-reference-architecture.md",
    "implementation-notes.md",
    "instructor-solution.md",
]

EXCLUDE_FROM_NAV = {
    "README.md",
    "modules/module-template.md",
}

SKIP_NAV_PARTS = {
    ".git",
    ".venv",
    ".mkdocs-src",
    "site",
    "__pycache__",
    ".pytest_cache",
    "node_modules",
}


def rel_posix(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def file_title(path: Path) -> str:
    try:
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            stripped = line.strip()
            if stripped.startswith("# "):
                return stripped[2:].strip().replace('"', "'")
    except OSError:
        pass

    name = path.stem
    replacements = {
        "README": "Overview",
        "ml": "ML",
        "llm": "LLM",
        "rag": "RAG",
        "ai": "AI",
        "dvaia": "DVAIA",
        "biml": "BIML",
        "mlops": "MLOps",
        "owasp": "OWASP",
        "nist": "NIST",
        "brokenpilot": "BrokenPilot",
    }
    parts = re.split(r"[-_]+", name)
    titled = []
    for part in parts:
        titled.append(replacements.get(part.lower(), part.capitalize()))
    return " ".join(titled)


def sort_markdown(files: list[Path], preferred: list[str] | None = None) -> list[Path]:
    preferred = preferred or []
    order = {name: index for index, name in enumerate(preferred)}
    return sorted(
        files,
        key=lambda p: (
            order.get(p.name, 1000),
            p.parent.as_posix().lower(),
            p.name.lower(),
        ),
    )


def markdown_files_under(base: Path) -> list[Path]:
    if not base.exists():
        return []
    files = []
    for path in base.rglob("*.md"):
        rel_parts = set(path.relative_to(ROOT).parts)
        if rel_parts & SKIP_NAV_PARTS:
            continue
        if rel_posix(path) in EXCLUDE_FROM_NAV:
            continue
        files.append(path)
    return files


def nav_item(path: Path, indent: int = 6) -> str:
    rel = rel_posix(path)
    return " " * indent + f'- "{file_title(path)}": {rel}'


def section(title: str, lines: list[str]) -> list[str]:
    if not lines:
        return []
    return [f"  - {title}:"] + lines


def simple_file_items(paths: list[Path], indent: int = 6) -> list[str]:
    return [nav_item(path, indent) for path in paths if path.exists()]


def build_start_here() -> list[str]:
    items: list[Path] = []
    for candidate in [
        ROOT / "docs" / "index.md",
        ROOT / "docs" / "start-here" / "one-week-learning-path.md",
        ROOT / "docs" / "start-here" / "40-hour-course-map.md",
        ROOT / "docs" / "start-here" / "cross-platform-setup.md",
        ROOT / "docs" / "lab-setup" / "brokenpilot-standalone-path.md",
        ROOT / "docs" / "lab-setup" / "dvaia.md",
        ROOT / "docs" / "lab-setup" / "dvaia-validation.md",
        ROOT / "docs" / "lab-setup" / "dvaia-fallback-decision-guide.md",
    ]:
        if candidate.exists():
            items.append(candidate)

    # Convert docs/* to final site paths by writing path relative to docs source.
    lines = []
    for path in items:
        if path.parts[-2:] == ("docs", "index.md"):
            lines.append('      - "Course Home": index.md')
        elif "docs" in path.parts:
            rel = path.relative_to(ROOT / "docs").as_posix()
            lines.append(f'      - "{file_title(path)}": {rel}')
    return section("Start Here", lines)


def build_course_docs() -> list[str]:
    candidates = [
        "syllabus.md",
        "references.md",
        "VERSION.md",
        "ROADMAP.md",
        "CHANGELOG.md",
    ]
    return section("Course", simple_file_items([ROOT / item for item in candidates]))


def build_modules() -> list[str]:
    modules_dir = ROOT / "modules"
    if not modules_dir.exists():
        return []
    lines: list[str] = []
    for module_dir in sorted([p for p in modules_dir.iterdir() if p.is_dir()]):
        if not re.match(r"^\d{2}-", module_dir.name):
            continue
        files = sort_markdown(list(module_dir.glob("*.md")), PREFERRED_MODULE_ORDER)
        if not files:
            continue
        title = file_title(module_dir / "README.md") if (module_dir / "README.md").exists() else module_dir.name
        lines.append(f'      - "{title}":')
        for path in files:
            lines.append(nav_item(path, 10))
    return section("Modules", lines)


def build_templates() -> list[str]:
    base = ROOT / "course-templates"
    if not base.exists():
        base = ROOT / "templates"
    files = sort_markdown(list(base.glob("*.md"))) if base.exists() else []
    return section("Templates", simple_file_items(files))


def build_labs() -> list[str]:
    labs_dir = ROOT / "labs"
    if not labs_dir.exists():
        return []
    lines: list[str] = []
    overview = labs_dir / "README.md"
    if overview.exists():
        lines.append(nav_item(overview))

    for lab_dir in sorted([p for p in labs_dir.iterdir() if p.is_dir()]):
        files = markdown_files_under(lab_dir)
        if not files:
            continue
        preferred = PREFERRED_BROKENPILOT_ORDER if lab_dir.name == "brokenpilot" else ["README.md"]
        files = sort_markdown(files, preferred)
        title = file_title(lab_dir / "README.md") if (lab_dir / "README.md").exists() else file_title(lab_dir)
        lines.append(f'      - "{title}":')
        for path in files:
            lines.append(nav_item(path, 10))
    return section("Labs", lines)


def build_directory_section(title: str, dirname: str) -> list[str]:
    base = ROOT / dirname
    files = sort_markdown(markdown_files_under(base), ["README.md"])
    return section(title, simple_file_items(files))


def build_lab_setup() -> list[str]:
    base = ROOT / "docs" / "lab-setup"
    if not base.exists():
        return []
    files = sort_markdown(list(base.glob("*.md")), ["README.md"])
    lines = []
    for path in files:
        rel = path.relative_to(ROOT / "docs").as_posix()
        lines.append(f'      - "{file_title(path)}": {rel}')
    return section("Lab Setup", lines)


def build_release_notes() -> list[str]:
    base = ROOT / "release-notes"
    files = sort_markdown(markdown_files_under(base))
    return section("Release Notes", simple_file_items(files))


def build_project_docs() -> list[str]:
    candidates = [
        "SOURCE_OF_TRUTH.md",
        "CONTENT_STRATEGY.md",
        "QUALITY_IMPROVEMENT_PLAN.md",
        "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md",
        "LICENSE.md",
        "LICENSE-CONTENT.md",
        "LICENSE-CODE.md",
        "COMMERCIAL-LICENSE.md",
    ]
    return section("Project Meta", simple_file_items([ROOT / item for item in candidates]))


def generate_nav() -> str:
    lines = ["nav:"]
    for block in [
        build_start_here(),
        build_course_docs(),
        build_modules(),
        build_templates(),
        build_labs(),
        build_lab_setup(),
        build_directory_section("Assessments", "assessments"),
        build_directory_section("Instructor", "instructor"),
        build_release_notes(),
        build_project_docs(),
    ]:
        lines.extend(block)
    return "\n".join(lines) + "\n"


def replace_top_level_block(text: str, key: str, replacement: str) -> str:
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.match(rf"^{re.escape(key)}:\s*$", line):
            start = i
            break
    if start is None:
        return text.rstrip() + "\n\n" + replacement

    end = len(lines)
    for j in range(start + 1, len(lines)):
        line = lines[j]
        if line and not line.startswith((" ", "\t")) and re.match(r"^[A-Za-z0-9_-]+:", line):
            end = j
            break
    new_lines = lines[:start] + replacement.rstrip().splitlines() + lines[end:]
    return "\n".join(new_lines).rstrip() + "\n"


def ensure_block_before_theme(text: str, block_key: str, block: str) -> str:
    text = replace_top_level_block(text, block_key, block)
    return text


def patch_mkdocs() -> None:
    if not MKDOCS.exists():
        raise SystemExit("mkdocs.yml not found. Run this script from the repository root.")
    text = MKDOCS.read_text(encoding="utf-8")
    text = replace_top_level_block(text, "nav", generate_nav())
    text = replace_top_level_block(
        text,
        "not_in_nav",
        "not_in_nav: |\n  /README.md\n  /modules/module-template.md\n",
    )
    text = replace_top_level_block(
        text,
        "validation",
        "validation:\n  nav:\n    omitted_files: warn\n",
    )
    MKDOCS.write_text(text, encoding="utf-8", newline="\n")
    print("updated: mkdocs.yml navigation, not_in_nav, and nav validation")


def patch_sync_script() -> None:
    if not SYNC_SCRIPT.exists():
        print("skip: scripts/sync_mkdocs_content.py not found")
        return
    text = SYNC_SCRIPT.read_text(encoding="utf-8")
    # Ensure course-templates is copied if the repository has it.
    if "course-templates" not in text and (ROOT / "course-templates").exists():
        text = text.replace('"templates",', '"templates",\n    "course-templates",')
    # Avoid copying root README.md into the MkDocs source root. docs/index.md is the homepage.
    text = re.sub(r'\n\s*["\']README\.md["\'],', "", text)
    SYNC_SCRIPT.write_text(text, encoding="utf-8", newline="\n")
    print("updated: scripts/sync_mkdocs_content.py")


def patch_deploy_workflows() -> None:
    if not WORKFLOW_DIR.exists():
        print("skip: .github/workflows not found")
        return
    for path in list(WORKFLOW_DIR.glob("*.yml")) + list(WORKFLOW_DIR.glob("*.yaml")):
        text = path.read_text(encoding="utf-8")
        original = text
        # Make MkDocs builds strict unless already strict.
        text = re.sub(r"(?<!#)(mkdocs\s+build)(?!\s+--strict)", r"\1 --strict", text)
        if text != original:
            path.write_text(text, encoding="utf-8", newline="\n")
            print(f"updated: {path.relative_to(ROOT)} uses mkdocs build --strict")


def main() -> None:
    patch_sync_script()
    patch_mkdocs()
    patch_deploy_workflows()
    print("\nRound 2 release-readiness patch applied.")
    print("Next: python scripts/sync_mkdocs_content.py && mkdocs build --strict")


if __name__ == "__main__":
    main()
