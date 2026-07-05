from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / ".mkdocs-src"
MKDOCS = ROOT / "mkdocs.yml"

PREFERRED_MODULE_FILES = [
    "README.md",
    "student-reading-guide.md",
    "cohesion-note.md",
    "lab-path.md",
    "delivery-profile.md",
    "deep-dive.md",
    "attack-anatomy.md",
    "controls-and-remediations.md",
    "common-mistakes.md",
    "worked-example.md",
    "exercise-deliverable-anchor.md",
    "exercise.md",
    "student-handout.md",
    "instructor-notes.md",
    "quiz.md",
    "references.md",
]

TOP_LEVEL_START = [
    "index.md",
    "syllabus.md",
    "course-map.md",
    "glossary.md",
    "PUBLISHED_COURSE_VIEW.md",
]

TOP_LEVEL_PROJECT = [
    "README.md",
    "VERSION.md",
    "CHANGELOG.md",
    "ROADMAP.md",
    "COURSE_RELEASE_MANIFEST.md",
    "USAGE_AND_LICENSING_GUIDE.md",
    "RELEASE_TAGGING_GUIDE.md",
    "references.md",
    "CONTRIBUTING.md",
    "LICENSE.md",
    "LICENSE-CONTENT.md",
    "LICENSE-CODE.md",
    "COMMERCIAL-LICENSE.md",
]

ROOT_EXCLUDE_PATTERNS = [
    re.compile(r"^CLEANUP_BEFORE_RELEASE\.md$"),
    re.compile(r"^RELEASE_CHECKLIST\.md$"),
    re.compile(r"^QUALITY_IMPROVEMENT_PLAN\.md$"),
    re.compile(r"^QUALITY_GATE_BASELINE\.md$"),
    re.compile(r"^RELEASE_CANDIDATE_CHECKLIST\.md$"),
    re.compile(r"^VALIDATION_BASELINE\.md$"),
    re.compile(r"^STYLE_AND_VOICE_.*\.md$"),
    re.compile(r"^FINAL_.*\.md$"),
    re.compile(r"^VOICE_POLISH_.*\.md$"),
    re.compile(r"^GENERATED_SCAFFOLDING_.*\.md$"),
    re.compile(r"^COURSE_CONTENT_AUDIT\.md$"),
    re.compile(r"^COURSE_FLOW_REVIEW\.md$"),
    re.compile(r"^COURSE_DRY_RUN_PLAN_40H\.md$"),
    re.compile(r"^COURSE_COMPLETION_SCORECARD\.md$"),
]

EXCLUDE_PATH_CONTAINS = [
    "/archive/",
    "/archived-",
    "/release-readiness/",
    "/__pycache__/",
    "/.pytest_cache/",
]

EXCLUDE_EXACT = {
    "modules/module-template.md",
}


def rel(path: Path) -> str:
    return path.relative_to(DOCS).as_posix()


def title_from_name(name: str) -> str:
    stem = Path(name).stem
    stem = stem.replace("README", "Overview")
    stem = re.sub(r"^\d+[-_]", "", stem)
    stem = stem.replace("-", " ").replace("_", " ")
    replacements = {
        "llm": "LLM",
        "rag": "RAG",
        "ml": "ML",
        "ai": "AI",
        "owasp": "OWASP",
        "biml": "BIML",
        "dvaia": "DVAIA",
        "mkdocs": "MkDocs",
        "ci": "CI",
        "mlo ps": "MLOps",
        "mlops": "MLOps",
    }
    words = []
    for word in stem.split():
        lower = word.lower()
        words.append(replacements.get(lower, word.capitalize()))
    return " ".join(words)


def should_exclude(path: str) -> bool:
    if path in EXCLUDE_EXACT:
        return True
    norm = "/" + path
    if any(part in norm for part in EXCLUDE_PATH_CONTAINS):
        return True
    if "/" not in path:
        return any(pattern.match(path) for pattern in ROOT_EXCLUDE_PATTERNS)
    return False


def md_files() -> list[str]:
    if not DOCS.exists():
        raise SystemExit("Missing .mkdocs-src. Run scripts/sync_mkdocs_content.py first.")
    return sorted(rel(p) for p in DOCS.rglob("*.md"))


def add_if_exists(nav_paths: set[str], path: str, title: str | None = None):
    if (DOCS / path).exists() and not should_exclude(path):
        nav_paths.add(path)
        return {title or title_from_name(path): path}
    return None


def section_from_paths(title: str, paths: list[str], nav_paths: set[str]):
    items = []
    for path in paths:
        entry = add_if_exists(nav_paths, path)
        if entry:
            items.append(entry)
    if items:
        return {title: items}
    return None


def directory_section(title: str, directory: str, nav_paths: set[str], preferred: list[str] | None = None):
    base = DOCS / directory
    if not base.exists():
        return None

    files = [p for p in base.rglob("*.md") if not should_exclude(rel(p))]
    if not files:
        return None

    items = []
    preferred = preferred or ["README.md"]

    # First include directory README if present.
    for fname in preferred:
        p = base / fname
        if p.exists() and p.is_file() and not should_exclude(rel(p)):
            rp = rel(p)
            nav_paths.add(rp)
            items.append({title_from_name(fname): rp})

    # Then include subdirectories as nested sections.
    for sub in sorted([p for p in base.iterdir() if p.is_dir()], key=lambda x: x.name):
        sub_files = sorted([p for p in sub.rglob("*.md") if not should_exclude(rel(p))])
        if not sub_files:
            continue
        sub_items = []

        readme = sub / "README.md"
        if readme.exists() and not should_exclude(rel(readme)):
            rp = rel(readme)
            nav_paths.add(rp)
            sub_items.append({"Overview": rp})

        for p in sub_files:
            rp = rel(p)
            if rp in nav_paths:
                continue
            nav_paths.add(rp)
            sub_items.append({title_from_name(p.name): rp})

        if sub_items:
            items.append({title_from_name(sub.name): sub_items})

    # Include remaining direct files.
    direct = sorted([p for p in base.glob("*.md") if not should_exclude(rel(p))])
    for p in direct:
        rp = rel(p)
        if rp in nav_paths:
            continue
        nav_paths.add(rp)
        items.append({title_from_name(p.name): rp})

    return {title: items} if items else None


def modules_section(nav_paths: set[str]):
    root = DOCS / "modules"
    if not root.exists():
        return None
    items = []

    for module_dir in sorted([p for p in root.iterdir() if p.is_dir()], key=lambda p: p.name):
        module_items = []

        for fname in PREFERRED_MODULE_FILES:
            p = module_dir / fname
            if p.exists() and not should_exclude(rel(p)):
                rp = rel(p)
                nav_paths.add(rp)
                module_items.append({title_from_name(fname): rp})

        for p in sorted(module_dir.glob("*.md")):
            rp = rel(p)
            if rp in nav_paths or should_exclude(rp):
                continue
            nav_paths.add(rp)
            module_items.append({title_from_name(p.name): rp})

        if module_items:
            items.append({title_from_name(module_dir.name): module_items})

    return {"Modules": items} if items else None


def top_level_section(nav_paths: set[str]):
    items = []
    for path in TOP_LEVEL_START:
        entry = add_if_exists(nav_paths, path, "Home" if path == "index.md" else None)
        if entry:
            items.append(entry)

    start = DOCS / "start-here"
    if start.exists():
        start_items = []
        for p in sorted(start.glob("*.md")):
            rp = rel(p)
            if rp in nav_paths or should_exclude(rp):
                continue
            nav_paths.add(rp)
            start_items.append({title_from_name(p.name): rp})
        if start_items:
            items.append({"Start Here": start_items})

    return {"Start Here": items} if items else None


def project_section(nav_paths: set[str]):
    items = []
    for path in TOP_LEVEL_PROJECT:
        entry = add_if_exists(nav_paths, path)
        if entry:
            items.append(entry)

    # Include safe top-level docs that are not already in start/project and not excluded.
    for p in sorted(DOCS.glob("*.md")):
        rp = rel(p)
        if rp in nav_paths or should_exclude(rp):
            continue
        nav_paths.add(rp)
        items.append({title_from_name(p.name): rp})

    return {"Project": items} if items else None


def yaml_quote(text: str) -> str:
    escaped = text.replace('"', '\\"')
    return f'"{escaped}"'


def dump_nav_item(item, indent: int = 0) -> list[str]:
    pad = " " * indent
    lines: list[str] = []
    if isinstance(item, dict):
        for key, value in item.items():
            if isinstance(value, str):
                lines.append(f"{pad}- {yaml_quote(key)}: {value}")
            elif isinstance(value, list):
                lines.append(f"{pad}- {yaml_quote(key)}:")
                for child in value:
                    lines.extend(dump_nav_item(child, indent + 4))
    return lines


def remove_top_level_block(text: str, key: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(rf"^{re.escape(key)}\s*:", line):
            i += 1
            while i < len(lines):
                nxt = lines[i]
                if nxt and not nxt.startswith((" ", "\t")) and re.match(r"^[A-Za-z0-9_-]+\s*:", nxt):
                    break
                i += 1
            continue
        out.append(line)
        i += 1
    return "\n".join(out).rstrip() + "\n"


def ensure_docs_dir(text: str) -> str:
    if re.search(r"^docs_dir\s*:", text, flags=re.M):
        return re.sub(r"^docs_dir\s*:.*$", "docs_dir: .mkdocs-src", text, flags=re.M)
    lines = text.splitlines()
    insert_at = 1 if lines else 0
    for idx, line in enumerate(lines):
        if line.startswith("site_name:"):
            insert_at = idx + 1
            break
    lines.insert(insert_at, "docs_dir: .mkdocs-src")
    return "\n".join(lines).rstrip() + "\n"


def write_mkdocs(nav: list[dict], excluded: list[str]) -> None:
    text = MKDOCS.read_text(encoding="utf-8") if MKDOCS.exists() else "site_name: AI Training - ML Security\n"
    for block in ["nav", "not_in_nav"]:
        text = remove_top_level_block(text, block)
    text = ensure_docs_dir(text)

    # Keep validation config if present, but avoid forcing omitted-files warnings while we use not_in_nav.
    text = remove_top_level_block(text, "validation")

    not_in_nav_lines = ["not_in_nav: |"]
    for path in excluded:
        not_in_nav_lines.append(f"  /{path}")

    nav_lines = ["nav:"]
    for item in nav:
        nav_lines.extend(dump_nav_item(item, 2))

    final = text.rstrip() + "\n\n" + "\n".join(not_in_nav_lines) + "\n\n" + "\n".join(nav_lines) + "\n"
    MKDOCS.write_text(final, encoding="utf-8", newline="\n")


def main() -> None:
    all_files = md_files()
    nav_paths: set[str] = set()
    nav: list[dict] = []

    for section in [
        top_level_section(nav_paths),
        modules_section(nav_paths),
        directory_section("Labs", "labs", nav_paths),
        directory_section("Course Templates", "course-templates", nav_paths),
        directory_section("Assessments", "assessments", nav_paths),
        directory_section("Instructor", "instructor", nav_paths),
        directory_section("Releases", "releases", nav_paths),
        directory_section("Release Notes", "release-notes", nav_paths),
        project_section(nav_paths),
    ]:
        if section:
            nav.append(section)

    excluded = sorted(path for path in all_files if path not in nav_paths)

    write_mkdocs(nav, excluded)

    print(f"Generated MkDocs nav entries for {len(nav_paths)} pages.")
    print(f"Declared {len(excluded)} intentional non-nav pages.")


if __name__ == "__main__":
    main()
