#!/usr/bin/env python3
import pathlib
import re
import sys
from typing import List, Set, Tuple

CITE_RE = re.compile(r"\\cite[a-zA-Z*]*\s*(?:\[[^\]]*\]\s*)?(?:\[[^\]]*\]\s*)?\{([^}]*)\}")
BIB_RE = re.compile(r"^\s*@\w+\{\s*([^,\s]+)")
MANUAL_CITE_RE = re.compile(r"(?<![\\#A-Za-z])\[\d+(?:\s*-\s*\d+)?\]")


def collect_tex_keys(root: pathlib.Path) -> Tuple[Set[str], List[Tuple[pathlib.Path, int, str]]]:
    keys: Set[str] = set()
    manual_cites: List[Tuple[pathlib.Path, int, str]] = []
    for tex in root.rglob("*.tex"):
        if "Constructor" in tex.parts:
            continue
        text = tex.read_text(encoding="utf-8", errors="ignore")
        for match in CITE_RE.finditer(text):
            raw = match.group(1)
            for key in raw.split(","):
                key = key.strip()
                if key:
                    keys.add(key)
        for line_no, line in enumerate(text.splitlines(), start=1):
            if MANUAL_CITE_RE.search(line):
                manual_cites.append((tex, line_no, line.strip()))
    return keys, manual_cites


def collect_bib_keys(bib_file: pathlib.Path) -> Set[str]:
    keys: Set[str] = set()
    for line in bib_file.read_text(encoding="utf-8", errors="ignore").splitlines():
        m = BIB_RE.match(line)
        if m:
            keys.add(m.group(1).strip())
    return keys


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: citation_audit.py <root_dir> <bib_file>")
        return 2

    root = pathlib.Path(sys.argv[1]).resolve()
    bib = pathlib.Path(sys.argv[2]).resolve()

    if not root.exists():
        print(f"ERROR: root dir not found: {root}")
        return 2
    if not bib.exists():
        print(f"ERROR: bib file not found: {bib}")
        return 2

    tex_keys, manual_cites = collect_tex_keys(root)
    bib_keys = collect_bib_keys(bib)

    missing = sorted(tex_keys - bib_keys)
    unused = sorted(bib_keys - tex_keys)

    print(f"Cited keys: {len(tex_keys)}")
    print(f"Bib keys: {len(bib_keys)}")

    if missing:
        print("\nMissing keys in BibTeX:")
        for key in missing:
            print(f"- {key}")

    if unused:
        print("\nUnused BibTeX keys:")
        for key in unused:
            print(f"- {key}")

    if manual_cites:
        print("\nManual numeric citations found (replace with \\cite{...}):")
        for file_path, line_no, line in manual_cites:
            print(f"- {file_path}:{line_no}: {line}")

    return 1 if missing or manual_cites else 0


if __name__ == "__main__":
    raise SystemExit(main())
