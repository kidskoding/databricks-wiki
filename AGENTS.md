# AGENTS.md: how an AI agent should use this vault

This repository is **Databricks Brain**, an Obsidian vault that teaches Databricks from zero to expert. It is meant to be read by people *and* by agents. This file tells an agent how to find things, how to answer from the vault, and how to add to it safely. Writing style rules live in `CLAUDE.md`. Read both before you edit anything.

## 1. The shape of the vault

| Folder | Part | What is in it |
|---|---|---|
| `00_is_databricks_for_you/` | 0, front door | Who uses Databricks, cost, fit, first 30 days. Written for business readers. |
| `01_foundations/` → `05_lakehouse/` | 1, the story | History before Databricks: data basics, Hadoop, Spark, warehouses and lakes, the lakehouse. |
| `06_databricks_platform/` → `10_ai_and_ml/` | 1, the story | The Databricks platform itself. |
| `11_azure_databricks/`, `12_databricks_on_aws/`, `13_databricks_on_gcp/` | 2, the clouds | Per-cloud identity, networking, storage, keys, billing. |
| `14_admin_security_and_cost/` | 2 | Cloud-neutral administration, security, FinOps. |
| `15_migrating_to_databricks/` | 3, moving in | Migration playbooks by source system. |
| `80_learning_paths/` | 4 | Ordered routes through the vault, one per persona. |
| `90_glossary/` | | One short note per jargon term. |
| root | | `start_here.md` (home), hub notes (timeline, who-replaced-what, cloud comparison, renames, persona map). |
| `_meta/` | | `manifest.yaml` (blueprint), `vault_index.json` (generated graph), `Vault Progress.base`. |
| `_templates/` | | `Concept.md`, `Glossary.md`, `Path.md`. |
| `scripts/` | | `scaffold.py` (create stubs from the manifest), `build_index.py` (rebuild the index and check links). |

Each content folder has one chapter note, `Chapter NN - Title.md`, which lists its notes in reading order.

## 2. Finding things fast

1. **`llms.txt`**: one line per note (title, path, depth, summary), in reading order. Read this first.
2. **`_meta/vault_index.json`**: every note (`nodes`) with `type`, `status`, `depth`, `section`, `summary`, `personas`, `aliases`, `clouds`, `links_out`, plus every typed frontmatter edge (`edges`).
3. **Frontmatter on each note**: it holds the same data. The notes themselves are the source of truth, and the index is rebuilt from them.
4. **Names**: a wiki link `[[Title]]` resolves to the file `Title.md` anywhere in the vault. Old or alternative names (for example `Delta Live Tables`, `Databricks Asset Bundles`) are listed in a note's `aliases`. Search aliases when a name is not found, and check `Databricks Product Names and Renames.md`.

### Edge types (frontmatter keys)

| Key | Meaning | Example |
|---|---|---|
| `chapter` | The chapter this note belongs to | `Delta Lake` → `Chapter 05 - The Lakehouse` |
| `prev` / `next` | Reading order through the whole story | `Delta Lake` → `Delta Transaction Log` |
| `evolved_from` / `evolved_into` | History: this replaced or grew out of that | `MapReduce` → `Apache Spark` |
| `cloud_equivalent` | The same idea on another cloud | `VNet Injection` ↔ `Customer-Managed VPC on AWS` |
| `related` | Other strong connection | |
| `prereqs` / `unlocks` | Learning dependencies | |
| `notes` | (chapter notes only) member notes in order | |

### Other frontmatter

- `type`: `concept`, `chapter`, `path`, `glossary`, `hub`.
- `status`: `stub` (planned, not written yet; do **not** answer from a stub's body) or `written`.
- `depth`: `101` beginner, `201` practitioner, `301` advanced, `401` expert.
- `personas`: `everyone`, `owner`, `analyst`, `engineer`, `scientist`, `ai-dev`, `admin`, `security`, `finance`, `solo` (one-person data team). The definitions are in `_meta/manifest.yaml`.
- `clouds`: which clouds the note's content applies to.
- `last_verified`: the date the facts were last checked against official docs. Databricks changes fast, so treat anything older than about six months as possibly stale.

## 3. Answering a question from the vault

1. Find candidate notes via `llms.txt` or the `summary` and `aliases` fields.
2. Read the note. Its `[!eli5]` block is the beginner answer, the main sections are the practitioner answer, and `[!deepdive]` is the expert answer. Match the depth to the person asking.
3. For "how is this different on Azure / AWS / GCP", read the note's `[!azure]` / `[!aws]` / `[!gcp]` callouts, then follow `cloud_equivalent` edges.
4. For "what came before / what replaced it", follow `evolved_from` / `evolved_into`.
5. For "where do I start" questions from a role, use the matching note in `80_learning_paths/`.
6. Cite the note (and its `[!sources]` links) in your answer. If `status: stub` or `last_verified` is old, say so, and check the official docs before stating product facts.

## 4. Writing or editing notes

1. Every planned note already exists as a stub. **Fill the stub in place.** Keep its filename and frontmatter links, then set `status: written` and `last_verified: YYYY-MM-DD`.
2. Follow the section order of the matching template in `_templates/`. `07_unity_catalog_and_governance/Unity Catalog.md` is the reference for tone, depth, and format.
3. **Research before writing, using official Databricks sources only:** `docs.databricks.com/aws/en/...`, `docs.databricks.com/gcp/en/...`, `learn.microsoft.com/en-us/azure/databricks/...`, and `databricks.com` (staff blog posts, `databricks.com/glossary`, product pages). No third-party blogs, Wikipedia, forums, or other vendors' sites. If those sources cannot confirm a fact, leave it out. List the sources in `[!sources]`.
4. **Only link to notes that exist.** Every `[[link]]` must match a filename. If a jargon term has no note, link the nearest existing note or glossary entry, or add the term to `glossary:` in `_meta/manifest.yaml` and run `python3 scripts/scaffold.py` to create its stub.
5. Add edges generously but truthfully, and add them in both directions where it makes sense (`evolved_from` here, `evolved_into` there).
6. To add a new note, add it to `_meta/manifest.yaml` under the right chapter, then run `python3 scripts/scaffold.py`. The script creates the stub and refreshes the chapter's reading-order table. Fix `prev`/`next` on the neighbours by hand if you inserted it mid-chapter.
7. After editing, run `python3 scripts/build_index.py`. It rebuilds `llms.txt`, `_meta/vault_index.json`, and the Persona Map, and it exits non-zero if any link is unresolved. Commit the regenerated files with your change.

## 5. Things to never do

- Never write a Databricks product name from memory. The renames are real and recent (see the renames hub).
- Never put flashcards (`Question::Answer`) inside a callout. They go in `## Recall`.
- Never use a bare `|` inside a wiki link in a table. Write `[[Note\|alias]]`.
- Never invent prices. Link to the official pricing page and explain how the meter works instead.
