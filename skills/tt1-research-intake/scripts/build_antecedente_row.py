#!/usr/bin/env python3
import argparse


def esc(text: str) -> str:
    return (
        text.replace("\\", "\\\\textbackslash{}")
        .replace("&", "\\\\&")
        .replace("%", "\\\\%")
        .replace("_", "\\\\_")
        .replace("#", "\\\\#")
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a LaTeX antecedentes table row")
    parser.add_argument("--no", required=True, help="Row number")
    parser.add_argument("--name", required=True, help="Project/paper name")
    parser.add_argument("--description", required=True, help="Short description")
    parser.add_argument("--features", required=True, help="Semicolon-separated feature bullets")
    parser.add_argument("--country", required=True)
    parser.add_argument("--org", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--cite", required=True, help="BibTeX key")
    args = parser.parse_args()

    features = [f.strip() for f in args.features.split(";") if f.strip()]
    feature_block = "\n".join([f"    -{esc(item)}\\\\" for item in features])

    print("\\centering " + esc(args.no) + " & \\centering " + esc(args.name) + " &")
    print("\\parbox{45mm}{" + esc(args.description) + "} &")
    print("\\parbox{40mm}{")
    print(feature_block)
    print(" } &")
    print("\\centering " + esc(args.country) + " & \\centering " + esc(args.org))
    print(" & \\centering " + esc(args.type) + ". & \\quad[\\cite{" + esc(args.cite) + "}] \\\\")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
