# Databricks Brain: Obsidian vault conventions

A second brain for Databricks, written by a Databricks student fellow (UIUC). It teaches Databricks bottom-up to someone with no background. It will also be shown publicly in a blog post, so every note must read well and look polished.

## Structure

- **The vault is one story, told in chronological order.** Each chapter covers an era or problem, the tools that solved it, and the new pain that led to the next chapter. Pre-Databricks history (Hadoop, Spark, Kafka, Airflow, lakes and warehouses) comes first. Databricks arrives in chapter 06 as the answer to that history.
- `start_here.md` is the home dashboard and table of contents. It links to the chapter notes.
- Each folder holds one chapter note (`Chapter NN - Title.md`, `type: chapter`) that lists its concept notes in reading order. Those lists define the planned note names.
- Every planned concept note already exists as a stub (`status: stub`). Writing a note means filling in the stub, keeping its frontmatter links and setting `status: written`.
- Folders are named `nn_name` (lowercase, underscores, no spaces or `&`, so they are easy to `cd` into) and numbered in story order (`01_foundations` → `14_admin_security_and_cost`). Keep this format for any new folder. `01`–`10` are Part 1 (the story); `11`–`14` are Part 2 (the clouds). Azure Databricks is a full chapter, not a footnote: it is a first-party Microsoft service with its own identity, networking, billing, and integrations.
- Hub notes at the root (`Timeline of Data Engineering.md`, `Open Source vs Databricks - Who Replaced What.md`) tie the story together.
- `90_glossary/` holds one short plain-English note per jargon term.
- `_templates/Concept.md` is the note template. Every concept note follows its section order.

## Graph links (frontmatter)

The graph view is a core feature, so links live in frontmatter properties as well as in the text:

- `chapter`: the chapter note. `prev` / `next`: reading order within the story.
- `evolved_from` / `evolved_into`: history threads across chapters (MapReduce → Apache Spark, Apache Hive → Unity Catalog).
- `cloud_equivalent`: the same idea on another cloud (VNet Injection ↔ Customer-Managed VPC).
- `related`: any other strong connection.
- Every note opens with a `[!story]` "Previously" callout and ends with a `[!nextup]` hand-off to its `next` note. Notes about pre-Databricks tools add a `[!bridge]` callout saying where that job lives in Databricks today.
- Graph color groups (by folder) live in `.obsidian/graph.json`.

## Writing rules

- **Research every note.** Check facts against official docs before writing: `docs.databricks.com/{aws,gcp}/en/...` and `learn.microsoft.com/en-us/azure/databricks/...`. Databricks renames products often (Delta Live Tables → Lakeflow Declarative Pipelines, Workflows → Lakeflow Jobs, Delta Sharing → OpenSharing in June 2026). Never write product names from memory without checking.
- List sources in the collapsed `[!sources]` callout and set `last_verified` in frontmatter to the date you checked.
- **Plain English first.** The `[!eli5]` block uses no jargon. Every jargon word elsewhere links to its note or glossary entry.
- Give per-cloud differences in the `[!azure]`, `[!aws]`, `[!gcp]` callouts. Skip a cloud only if nothing differs, and say so.
- Keep flashcards (`Question::Answer`) in the `## Recall` section, outside callouts, so the Spaced Repetition plugin parses them.
- Escape pipes in wiki links inside tables: `[[Note\|alias]]`.
- Frontmatter `level` is the folder number, `section` is the human-readable section name (for example `Unity Catalog & Governance`). The dashboard groups by these.
- `Unity Catalog.md` in `07_unity_catalog_and_governance/` is the reference example for tone, depth, and format.

## Styling

Custom callouts (`story`, `nextup`, `bridge`, `eli5`, `analogy`, `azure`, `aws`, `gcp`, `confusion`, `recall`, `path`, `sources`) are defined in `.obsidian/snippets/databricks-brain.css`. Add new callout types there, not inline.
