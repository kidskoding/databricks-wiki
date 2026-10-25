---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The property of an operation that produces the same result whether it runs once or many times, which makes retries safe."
related:
  - "[[MERGE and Upserts]]"
  - "[[COPY INTO]]"
  - "[[Auto Loader]]"
  - "[[Exactly-Once Processing]]"
  - "[[Lakeflow Jobs]]"
  - "[[ACID Transactions]]"
aliases:
  - "idempotent"
  - "idempotence"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Idempotency

> [!eli5] Summary
> An idempotent operation can be repeated without changing the result after the first run. Running a data load twice does not double the data.

**In data work:** Pipelines fail and are retried, so each step should be safe to rerun. A plain `INSERT` of a day's orders is not idempotent: running it twice duplicates the rows. Idempotent alternatives are key-based upserts, overwriting only the slice being processed, and tracking which inputs have already been loaded. Idempotency is a prerequisite for safe [[Backfill|backfills]] and [[Exactly-Once Processing|exactly-once]] streaming.

**In Databricks:** `MERGE` updates matching rows and inserts new ones by key ([[MERGE and Upserts]]). [[COPY INTO]] is idempotent: it skips files already loaded, even if they were modified, unless `COPY_OPTIONS ('force' = 'true')` is set. [[Auto Loader]] records processed files in its [[Checkpoint|checkpoint]]. `INSERT INTO ... REPLACE WHERE` replaces one predicate range in a single commit. [[Lakeflow Jobs]] retries and repair runs do not make tasks idempotent, so Databricks recommends overwrite or merge over append where duplicates are a concern.

Seen in: [[MERGE and Upserts]], [[COPY INTO]], [[Auto Loader]], [[Exactly-Once Processing]]

## Recall

What does idempotent mean?::Running the operation more than once gives the same result as running it once.
Which COPY INTO option disables idempotency?::force = true in COPY_OPTIONS.

> [!sources]- Sources (last verified: 2026-10-25)
> - [COPY INTO (Azure)](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/delta-copy-into)
> - [Selectively overwrite data with Delta Lake (AWS)](https://docs.databricks.com/aws/en/delta/selective-overwrite)
> - [Troubleshoot and repair job failures (AWS)](https://docs.databricks.com/aws/en/jobs/repair-job-failures)
