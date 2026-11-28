#!/usr/bin/env python3
"""Validate VARTA local links and report SEO architecture issues without changing site files."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://ashubagri.github.io/Varta"


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.meta = {}
        self.title_parts = []
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ("href", "src"):
            value = attrs.get(key)
            if value:
                self.links.append(value.strip())
        if tag.lower() == "meta":
            name = (attrs.get("name") or attrs.get("property") or "").lower()
            if name:
                self.meta[name] = attrs.get("content", "").strip()
        if tag.lower() == "link" and "canonical" in (attrs.get("rel") or "").lower().split():
            self.meta["canonical"] = attrs.get("href", "").strip()
        if tag.lower() == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title_parts.append(data)

    @property
    def title(self):
        return "".join(self.title_parts).strip()


def is_external(value):
    parts = urlsplit(value)
    return bool(parts.scheme) or value.startswith("//") or value.startswith("#")


def resolve_target(source, value):
    parts = urlsplit(value)
    path = unquote(parts.path)
    if not path:
        return None
    # GitHub Pages serves this repository under /Varta/. Strip that deployment
    # prefix before resolving root-relative site assets and links.
    if path == "/Varta":
        path = "/"
    elif path.startswith("/Varta/"):
        path = path[len("/Varta"):]
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
    warnings = []
    parsed = {}
    inbound = {source.resolve(): set() for source in html_files}

    for source in html_files:
        try:
            parser = SiteParser()
            parser.feed(source.read_text(encoding="utf-8"))
            parser.close()
            parsed[source.resolve()] = parser
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
            elif target.suffix.lower() == ".html" and target.resolve() in inbound:
                inbound[target.resolve()].add(source.resolve())

        robots = parser.meta.get("robots", "index,follow").lower()
        if "noindex" not in robots:
            if not parser.title:
                warnings.append(f"{source.relative_to(ROOT)}: indexable page has no <title>.")
            if not parser.meta.get("description"):
                warnings.append(f"{source.relative_to(ROOT)}: indexable page has no meta description.")
            if not parser.meta.get("canonical"):
                warnings.append(f"{source.relative_to(ROOT)}: indexable page has no canonical URL.")

    # Sitemap integrity and coverage. The home page is represented by /, not /index.html.
    sitemap = ROOT / "sitemap.xml"
    sitemap_urls = set()
    if sitemap.exists():
        try:
            root = ET.parse(sitemap).getroot()
            for node in root.iter():
                if node.tag.endswith("loc") and node.text:
                    sitemap_urls.add(node.text.strip().rstrip("/"))
            for url in sorted(sitemap_urls):
                prefix = BASE_URL
                if url == prefix:
                    target = ROOT / "index.html"
                elif url.startswith(prefix + "/"):
                    target = ROOT / url[len(prefix) + 1:]
                else:
                    warnings.append(f"sitemap.xml: URL is outside the VARTA canonical host: {url}")
                    continue
                if not target.exists():
                    errors.append(f"sitemap.xml: URL points to missing file: {url}")
            for source, parser in parsed.items():
                robots = parser.meta.get("robots", "index,follow").lower()
                if "noindex" in robots:
                    continue
                rel = source.relative_to(ROOT).as_posix()
                expected = BASE_URL if rel == "index.html" else f"{BASE_URL}/{rel}"
                if expected.rstrip("/") not in sitemap_urls:
                    warnings.append(f"{rel}: indexable page is missing from sitemap.xml.")
        except Exception as exc:
            errors.append(f"sitemap.xml: could not parse sitemap: {exc}")
    else:
        errors.append("sitemap.xml: file is missing.")

    # Report likely orphaned indexable content; utility/noindex pages are excluded.
    for source, parser in parsed.items():
        if source.name == "index.html" or "noindex" in parser.meta.get("robots", "index,follow").lower():
            continue
        if not inbound.get(source):
            warnings.append(f"{source.relative_to(ROOT)}: no internal HTML page links to this indexable page (possible orphan).")

    if warnings:
        print("VARTA SEO architecture warnings:")
        print("\n".join(f"- {item}" for item in sorted(set(warnings))))
    if errors:
        print("VARTA site checks found errors:")
        print("\n".join(f"- {item}" for item in errors))
        return 1
    print(f"VARTA site checks passed: parsed {len(html_files)} HTML files; all local href/src targets and sitemap URLs exist.")
    print(f"SEO audit: {len(set(warnings))} warning(s); review warnings above, if any.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
