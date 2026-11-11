#!/usr/bin/env python3
"""Check VARTA HTML files and local href/src targets without changing site files."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ("href", "src") and value:
                self.links.append(value.strip())

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)


def is_external(value):
    parts = urlsplit(value)
    return bool(parts.scheme) or value.startswith("//") or value.startswith("#")


def resolve_target(source, value):
    parts = urlsplit(value)
    path = unquote(parts.path)
    if not path:
        return None
    target = ROOT / path.lstrip("/") if path.startswith("/") else source.parent / path
    target = target.resolve()
    try:
        target.relative_to(ROOT.resolve())
    except ValueError:
        return None
    if target.is_dir():
        target = target / "index.html"
    return target


def main():
    html_files = sorted(ROOT.rglob("*.html"))
    errors = []
    for source in html_files:
        try:
            parser = SiteParser()
            parser.feed(source.read_text(encoding="utf-8"))
            parser.close()
        except Exception as exc:
            errors.append(f"{source.relative_to(ROOT)}: HTML parsing failed: {exc}")
            continue
        for value in parser.links:
            if is_external(value):
                continue
            target = resolve_target(source, value)
            if target is None:
                errors.append(f"{source.relative_to(ROOT)}: unsafe or invalid local path: {value}")
            elif not target.exists():
                errors.append(f"{source.relative_to(ROOT)}: missing local target: {value}")
    if errors:
        print("VARTA site checks found issues:")
        print("\n".join(f"- {item}" for item in errors))
        return 1
    print(f"VARTA site checks passed: parsed {len(html_files)} HTML files; all local href/src targets exist.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
