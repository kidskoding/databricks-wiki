---
name: databricks-brain
description: Answer Databricks questions and do Databricks work (SQL, Unity Catalog, Lakeflow pipelines and jobs, bundles, compute, AI/BI, Model Serving, Agent Bricks, Azure/AWS/GCP setup, cost, migration) from this repo's verified knowledge graph instead of memory. Use whenever a task touches the Databricks platform, a Databricks product name, or a small-business data platform decision.
---

# Databricks Brain

This repo is a verified knowledge graph of the Databricks platform as of October 2026: 487 notes and 7,000+ typed links, from beginner to expert, across Azure, AWS, and Google Cloud. Use it before your own memory. Databricks renames products often, and your training data is out of date.

## Workflow

1. **Load the briefing once per task.** Read `_meta/primer.md`, or call the `databricks_primer` MCP tool. It holds current product names, decision guides, defaults and limits, cloud differences, snippets, and gotchas.
2. **Translate names first.** Before you write any product name, resolve it: `python3 scripts/brain.py resolve "<name>"` or the `databricks_resolve` tool. If a user says "Delta Live Tables", "Workflows", "Vector Search", or "Databricks Assistant", answer with the current name and mention the old one once.
3. **Pull context for each question:** `python3 scripts/brain.py context "<question>"` or `databricks_context`. It returns the relevant notes' summaries and best-matching sections within a word budget.
4. **Drill in when you need detail:**

   | Need | CLI | MCP tool |
   |---|---|---|
   | One note at a chosen depth | `brain.py note "<title>" --level summary\|standard\|full` | `databricks_note` |
   | One section | `brain.py note "<title>" --section "How it works"` | `databricks_note` |
   | Ranked search, optionally per cloud | `brain.py search "<query>" --cloud aws` | `databricks_search` |
   | Azure vs AWS vs GCP | `brain.py cloud "<title>"` | `databricks_cloud` |
   | Related, prereqs, unlocks | `brain.py neighbors "<title>"` | `databricks_neighbors` |
   | What it replaced, what replaced it | `brain.py history "<title>"` | `databricks_history` |
   | Learning route for a role | `brain.py path analyst` | `databricks_path` |

   Add `--json` for machine-readable output.
5. **Answer at the asker's depth.** A note's `Summary` is the beginner answer, the main sections are the practitioner answer, and `Advanced topics` is the expert answer.
6. **Cite and check freshness.** Name the notes you used. Treat anything listed in the primer's status watchlist, or with an old `last_verified` date, as possibly changed. Check the note's sources before you rely on it for production decisions.

## Rules

- Never state prices. Explain the meter (DBUs plus cloud costs) and point to the official pricing page.
- Prefer the vault's verified snippets over code you write from memory, and adapt names to the user's catalog and schema.
- If the vault does not cover something, say so, and use only official Databricks docs or other primary sources (see `CLAUDE.md`).
- To edit the vault itself, follow `AGENTS.md` and `CLAUDE.md`, then run `python3 scripts/build_index.py`.
