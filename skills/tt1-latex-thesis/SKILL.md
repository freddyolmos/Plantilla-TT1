---
name: tt1-latex-thesis
description: Draft, revise, and maintain a UPIITA TT1/TT2 thesis in LaTeX with compile-safe structure, consistent chapter flow, and citation hygiene. Use when writing chapter content, adding tables or figures, fixing LaTeX errors, or validating references in Plantilla-TT1.
---

# TT1 LaTeX Thesis Skill

Use this skill to keep thesis progress stable while writing quickly.

## Workflow

1. Compile baseline before editing.

```bash
latexmk -pdf -interaction=nonstopmode main.tex
```

2. Edit one section at a time and keep chapter traceability.
- Problem -> objective -> requirements -> architecture -> implementation -> validation -> conclusions.
- Keep explicit links between requirements (R#) and validation evidence.

3. For figures and tables, always include:
- clear caption,
- label (`\\label{...}`),
- in-text reference (`Figura~\\ref{...}`, `Tabla~\\ref{...}`).

4. Use only BibTeX keys for citations (`\\cite{key}`), never manual numeric citations like `[1]` in body text.

5. Run health checks after meaningful changes:

```bash
skills/tt1-latex-thesis/scripts/check_latex_health.sh .
python3 skills/tt1-latex-thesis/scripts/citation_audit.py . Bibliografia.bib
```

## Key rules for this repository

- Main entry point is `main.tex`.
- Bibliography source of truth is `Bibliografia.bib`.
- Keep chapter files small and modular under numbered folders.
- Prefer deterministic edits over broad rewrites.

## References to load on demand

- `references/section_map.md`: chapter-to-file map and expected content.
- `references/content_checklists.md`: ready-to-use checklist per chapter.
