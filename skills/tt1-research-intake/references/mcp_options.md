# MCP Options for Literature Intake

Potential MCP connectors to prioritize:

- OpenAlex API MCP: broad academic metadata, references graph.
- Semantic Scholar MCP: citations, influential papers, related work.
- Crossref MCP: DOI metadata normalization for BibTeX fields.
- arXiv MCP: preprints for robotics, CV, control updates.
- GitHub MCP: implementation repos and issue discussions.

Suggested pipeline:
1. Query by topic.
2. Export top N papers with title/year/DOI/url.
3. Score with source rubric.
4. Promote accepted papers to `Bibliografia.bib` and antecedentes rows.
