"""Check that every published course page edits a real source file."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
EDIT_PREFIX = "https://github.com/stratomarco/ai-training-ml-security/edit/main/"


class EditLinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        href = dict(attrs).get("href")
        if href and href.startswith(EDIT_PREFIX):
            self.links.append(href)


def main() -> None:
    errors: list[str] = []
    checked = 0
    for page in SITE.rglob("*.html"):
        if page == SITE / "404.html":
            continue
        html = page.read_text(encoding="utf-8")
        if 'name="generator" content="mkdocs-' not in html:
            continue  # A copied application UI, not a MkDocs content page.

        parser = EditLinkParser()
        parser.feed(html)
        if len(parser.links) != 1:
            errors.append(f"{page.relative_to(SITE)}: expected one edit link, found {len(parser.links)}")
            continue

        source = (ROOT / unquote(parser.links[0][len(EDIT_PREFIX):])).resolve()
        if not source.is_relative_to(ROOT.resolve()) or not source.is_file():
            errors.append(f"{page.relative_to(SITE)}: edit link has no repository source")
        checked += 1

    if checked == 0:
        errors.append("No MkDocs content pages were checked")
    if errors:
        raise SystemExit("MkDocs edit-link check failed:\n" + "\n".join(errors))
    print(f"MkDocs edit-link check passed for {checked} pages.")


if __name__ == "__main__":
    main()
