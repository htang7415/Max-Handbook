#!/usr/bin/env python3
"""Audit module README files for the engineering module shape.

Usage:
  python scripts/audit_module_readmes.py <README-or-module-path> [...]
  python scripts/audit_module_readmes.py --track software-engineering
  python scripts/audit_module_readmes.py  # defaults to software-engineering
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


REQUIRED_SECTIONS = [
    "Concept",
    "Use When",
    "First Principles",
    "Workflow",
    "Minimal Code Mental Model",
    "Failure Modes",
    "Function",
    "Run tests",
]

SECTION_PATTERN = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


def is_alias_readme(markdown: str) -> bool:
    if not markdown.startswith("---\n"):
        return False
    end = markdown.find("\n---\n", 4)
    if end == -1:
        return False
    frontmatter = markdown[4:end]
    return any(
        line.strip().startswith(("aliasOf:", "alias_of:"))
        for line in frontmatter.splitlines()
    )


def readme_path(path: Path) -> Path:
    if path.is_dir():
        return path / "README.md"
    return path


def discover_readmes(repo_root: Path, track: str | None, paths: list[str]) -> list[Path]:
    if paths:
        return sorted({readme_path(Path(path)) for path in paths})

    base = repo_root / "modules"
    if track:
        base = base / track
    return sorted(base.glob("**/README.md"))


def missing_sections(path: Path) -> list[str]:
    markdown = path.read_text(encoding="utf-8")
    if is_alias_readme(markdown):
        return []
    sections = {match.group(1).strip() for match in SECTION_PATTERN.finditer(markdown)}
    return [section for section in REQUIRED_SECTIONS if section not in sections]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check module README files for required engineering sections."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="README files or module directories. Defaults to all module READMEs.",
    )
    parser.add_argument(
        "--track",
        default="software-engineering",
        help="Limit default discovery to one track. Defaults to software-engineering.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    readmes = discover_readmes(repo_root, args.track, args.paths)
    failures: list[tuple[Path, list[str]]] = []

    for path in readmes:
        if not path.exists():
            failures.append((path, ["README.md not found"]))
            continue
        missing = missing_sections(path)
        if missing:
            failures.append((path, missing))

    if failures:
        for path, missing in failures:
            rel_path = path.relative_to(repo_root) if path.is_absolute() else path
            print(f"{rel_path}: missing {', '.join(missing)}")
        print(f"\n{len(failures)} README file(s) need updates.")
        return 1

    print(f"Checked {len(readmes)} README file(s); all match the engineering module shape.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
