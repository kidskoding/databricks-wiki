# Databricks Brain: Obsidian vault conventions

A second brain for Databricks, written by a Databricks student fellow (UIUC). It teaches Databricks bottom-up to someone with no background, all the way to expert depth. The core audience includes small businesses (mom-and-pop shops, small teams, the one data person) who are considering a move to Databricks. It will also be shown publicly in a blog post, so every note must read well and look polished. Agents read it too: see `AGENTS.md` for how the vault is navigated, indexed, and extended.

## Structure

- **The vault is one story, told in chronological order:** Each chapter covers an era or problem, the tools that solved it, and the new pain that led to the next chapter. Pre-Databricks history (Hadoop, Spark, Kafka, Airflow, lakes and warehouses) comes first. Databricks arrives in chapter 06 as the answer to that history.
- `start_here.md` is the home dashboard and table of contents. It links to the chapter notes.
- Each folder holds one chapter note (`Chapter NN - Title.md`, `type: chapter`) that lists its concept notes in reading order. Those lists define the planned note names.
- `_meta/manifest.yaml` is the blueprint: every chapter and planned note, with its depth, summary, personas, and key edges. `python3 scripts/scaffold.py` creates any missing stubs from it.
- Every planned note already exists as a stub (`status: stub`). Writing a note means filling in the stub, keeping its frontmatter links and setting `status: written`.
- Folders are named `nn_name` (lowercase, underscores, no spaces or `&`, so they are easy to `cd` into) and numbered in story order. Keep this format for any new folder.
  - `00_is_databricks_for_you` is Part 0, the front door for business readers.
  - `01`–`10` are Part 1 (the story).
  - `11`–`14` are Part 2 (the clouds and administration). Azure Databricks is a full chapter, not a footnote: it is a first-party Microsoft service with its own identity, networking, billing, and integrations.
  - `15_migrating_to_databricks` is Part 3 (moving in).
  - `80_learning_paths` holds one path note per persona (`type: path`, from `_templates/Path.md`).
- Hub notes at the root (`Timeline of Data Engineering.md`, `Open Source vs Databricks - Who Replaced What.md`, `Cloud Comparison - Azure vs AWS vs GCP.md`, `Databricks Product Names and Renames.md`, `Persona Map.md`) tie the story together.
- After any edit, run `python3 scripts/build_index.py` (it needs PyYAML; without it, run `uv run --with pyyaml python3 scripts/build_index.py`). It regenerates `llms.txt`, `_meta/vault_index.json`, and the Persona Map table, and it fails on unresolved links. Commit the regenerated files.
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

- **Research every note against trusted primary sources:** In order of preference:
  1. Official Databricks documentation: `docs.databricks.com/{aws,gcp}/en/...` and `learn.microsoft.com/en-us/azure/databricks/...`, including release notes.
  2. Other Databricks-published material: `databricks.com` (engineering and product blog posts by Databricks staff, `databricks.com/glossary`, research papers, product and pricing pages).
  3. Other trusted primary sources: official open-source project docs (`spark.apache.org`, `delta.io`, `iceberg.apache.org`, `mlflow.org`, `kafka.apache.org`, `airflow.apache.org`, `unitycatalog.io`), official cloud provider docs (`learn.microsoft.com`, `docs.aws.amazon.com`, `cloud.google.com`), other vendors' own docs when describing their product, and peer-reviewed papers (CIDR, VLDB, OSDI, NSDI, SIGMOD).

  Do not use or cite content farms, SEO blogs, Medium posts, Wikipedia, forums, or AI-generated summaries. If a trusted source cannot confirm a fact, leave it out or mark it unconfirmed. Databricks renames products often (Delta Live Tables → Lakeflow Spark Declarative Pipelines, Workflows → Lakeflow Jobs, Databricks Asset Bundles → Declarative Automation Bundles, Delta Sharing → OpenSharing). Never write product names from memory without checking.
- List sources in the collapsed `[!sources]` callout and set `last_verified` in frontmatter to the date you checked.
- **Write like developer documentation:** The notes read like professional reference docs in the style of the Cloudflare, Vercel, and Databricks docs, not like a blog or a chat:
  - **Never use em dashes (U+2014):** Use a period, comma, colon, or parentheses instead. Do not substitute a spaced en dash or double hyphen. `scripts/build_index.py` fails on any em dash.
  - Open each page with one sentence that says what the thing is. Follow with short sections a reader can scan, and put procedures in numbered steps with one action per step.
  - Neutral, precise, declarative. Present tense, active voice, second person for instructions ("Run `OPTIMIZE`...").
  - Short paragraphs, one idea each. Lead with the definition, then the details.
  - No hype, rhetorical questions, jokes, exclamation marks, filler ("simply", "just", "magic", "game-changer"), or narrative scene-setting.
  - Use the exact product names, UI labels, SQL keywords, and API names. Put code identifiers in backticks.
  - Prefer tables for reference data (options, limits, comparisons) and numbered lists for procedures.
  - Structure with real headings, not bold run-in labels. A topic that gets its own paragraph is a `###` subheading. A short labelled item is a bullet with a colon: `- **Label:** text`. Never write `**Label.** text`; `scripts/build_index.py` fails on it (fix with `scripts/fix_bold_leads.py`).
  - Code samples are minimal, runnable, labeled with a language, and commented only where needed.
  - State status explicitly: Public Preview, GA, deprecated, with the date checked.
- **Plain language first:** The `[!eli5]` Summary block states what the thing is and why it matters in two or three sentences without jargon. It is still written professionally. Every jargon word elsewhere links to its note or glossary entry.
- Analogies are optional. Use one only when it genuinely clarifies the idea, and keep it brief and factual.
- Give per-cloud differences in the `[!azure]`, `[!aws]`, `[!gcp]` callouts. Skip a cloud only if nothing differs, and say so.
- Keep flashcards (`Question::Answer`) in the `## Recall` section, outside callouts, so the Spaced Repetition plugin parses them.
- Escape pipes in wiki links inside tables: `[[Note\|alias]]`.
- `depth` sets how advanced a note is: `101` beginner, `201` practitioner, `301` advanced, `401` expert. Every note still opens in plain English. Expert material goes in the collapsed `[!deepdive]-` box so beginners can skip it.
- `summary` is one plain-English line, which agents and `llms.txt` use. `personas` lists who the note is for (keys in the manifest).
- Every concept note has a `[!smallbiz]` callout: what it means for a 5–50 person company, when to care, and when to skip.
- When a product was renamed, add a `[!renamed]` callout near the top with the old names, and list them in `aliases`.
- Never state prices. Explain the meter and link to the official pricing page.
- Frontmatter `level` is the folder number, `section` is the human-readable section name (for example `Unity Catalog & Governance`). The dashboard groups by these.
- `Unity Catalog.md` in `07_unity_catalog_and_governance/` is the reference example for tone, depth, and format.
- Standard concept-note headings, in order: `Background`, `Overview`, `How it works`, `Small-business considerations` (the `[!smallbiz]` callout), `Cloud differences`, `Advanced topics`, `Common misconceptions`, `Recall`, `Next steps`.

## Styling

Custom callouts (`story`, `nextup`, `bridge`, `eli5`, `analogy`, `azure`, `aws`, `gcp`, `confusion`, `recall`, `path`, `sources`, `smallbiz`, `deepdive`, `persona`, `check`, `renamed`) are defined in `.obsidian/snippets/databricks-brain.css`. Add new callout types there, not inline.
