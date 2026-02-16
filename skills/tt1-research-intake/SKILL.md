---
name: tt1-research-intake
description: Build and curate related-work evidence for the Rubik CFOP training robot thesis, from search query design to antecedente table rows and BibTeX-ready citations. Use when collecting papers or theses, screening source quality, or updating antecedentes and marco teorico.
---

# TT1 Research Intake Skill

Use this skill to convert scattered references into thesis-ready evidence.

## Workflow

1. Define the target evidence block before searching.
- Mechanical architecture for Rubik robot.
- Control and actuation accuracy.
- Computer vision for cube state recognition.
- Human learning and deliberate practice (CFOP training value).

2. Search with bilingual query sets (ES/EN).
- Use `references/source_queries.md`.
- Prioritize peer-reviewed and thesis repositories.

3. Screen each source quickly.
- Relevance to your subsystem.
- Recency and reproducibility.
- Available metrics and implementation details.

4. Convert accepted sources into two outputs.
- BibTeX entry in `Bibliografia.bib`.
- Antecedente row for `1 Inicial/1.5 Antecedentes.tex`.

5. Use `scripts/build_antecedente_row.py` to create row drafts fast.

## Acceptance criteria

- Each new antecedente includes objective metrics (time, precision, hardware).
- Citation key exists and compiles.
- Source quality rubric satisfied (see references).

## References to load on demand

- `references/source_queries.md`: query packs by topic.
- `references/source_quality_rubric.md`: quality filters.
- `references/mcp_options.md`: MCP ideas for literature intake.
