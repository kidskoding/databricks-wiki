---
type: path
status: written
level: 80
section: Learning Paths
depth: 201
summary: Ingestion, the lakehouse, pipelines, orchestration, and CI/CD.
personas:
  - engineer
chapter: "[[Chapter 80 - Learning Paths]]"
prev: "[[Path - Analyst]]"
next: "[[Path - Data Scientist and ML Engineer]]"
evolved_from: []
evolved_into: []
cloud_equivalent: []
related:
  - "[[Apache Spark]]"
  - "[[PySpark]]"
  - "[[Delta Lake]]"
  - "[[MERGE and Upserts]]"
  - "[[Medallion Architecture]]"
  - "[[Auto Loader]]"
  - "[[Lakeflow Spark Declarative Pipelines]]"
  - "[[Expectations and Data Quality]]"
  - "[[Lakeflow Jobs]]"
  - "[[Change Data Capture]]"
  - "[[Declarative Automation Bundles]]"
  - "[[CI-CD for Data Pipelines]]"
  - "[[Liquid Clustering]]"
  - "[[Path - Analyst]]"
  - "[[Path - Platform Admin]]"
  - "[[Path - Certification Prep]]"
aliases:
  - DE Path
  - Data Engineering Path
prereqs:
  - "[[Path - Absolute Beginner]]"
unlocks:
  - "[[Path - Certification Prep]]"
  - "[[Path - Platform Admin]]"
clouds:
  - aws
  - azure
  - gcp
mastery: new
last_verified: 2026-10-25
tags:
  - path
---

# Path - Data Engineer

> [!persona] Who this is for
> **Who:** a data engineer, a backend developer moving into data, or an analyst who now owns the pipelines.
> **Goal:** ingest data from files, databases, and SaaS tools; shape it into reliable bronze, silver, and gold tables; run it on a schedule; and deploy it like software.
> **Outcome:** you can build, test, schedule, and deploy a production-grade incremental pipeline, and tune the tables it writes.

## Before you start

You should read SQL fluently and write basic Python. Git basics are useful for Stage 4. Work in [[Databricks Free Edition and Trials|Free Edition]] for Stages 1 to 4; Stage 5 tuning works best on a trial workspace with real data volumes. Install the [[Databricks CLI]] before Stage 4.

## The route

### Stage 1: Spark and the shape of the work (101 to 201)

**Goal:** understand the engine before building on it.

1. [[ETL vs ELT]]: why modern pipelines load first and transform inside the platform.
2. [[Batch vs Streaming]]: the two rhythms of data, and why Databricks treats them alike.
3. [[Apache Spark]]: the engine under everything in this path.
4. [[DataFrames]]: tables in code, the main Spark interface.
5. [[PySpark]]: Spark from Python.
6. [[Lazy Evaluation]] (201): why nothing runs until you ask for a result.
7. [[Transformations and Actions]] (201): the two kinds of operation.
8. [[Partitions]] (201): how data is split so many machines work at once.
9. [[Driver and Executors]] (201): the roles of the machines in a cluster.

> [!check] Checkpoint
> In a notebook, read `samples.nyctaxi.trips` into a DataFrame, filter and aggregate it, and call `.explain()` before calling `display()`. Point to where the plan reads the table and where it aggregates. Count how many cells ran before Spark did any work.

### Stage 2: Lakehouse tables (201)

**Goal:** learn what makes a Delta table reliable and how to change it safely.

1. [[Object Storage]]: the low-cost storage layer under every table.
2. [[Apache Parquet]]: the columnar files inside every Delta table.
3. [[Open Table Formats]]: the metadata layer that turns files into a table.
4. [[Delta Lake]]: Databricks' default table format.
5. [[ACID Transactions]]: why partially written data is never visible.
6. [[Schema Enforcement and Evolution]]: rejecting bad columns and adding new ones.
7. [[MERGE and Upserts]]: the main operation for incremental loads.
8. [[Time Travel]]: reading and restoring old versions.
9. [[Managed vs External Tables]]: who owns the files, and what `DROP` does.
10. [[Volumes]]: governed folders for raw files.
11. [[Medallion Architecture]]: bronze, silver, gold.

> [!check] Checkpoint
> Create a schema and a Volume (`CREATE SCHEMA`, `CREATE VOLUME`), upload two CSV files of customer records to it, and load the first into a Delta table. `MERGE` the second file into it so changed rows update and new rows insert. Run `DESCRIBE HISTORY`, then `RESTORE TABLE ... TO VERSION AS OF` the version before the merge.

### Stage 3: Ingestion, pipelines, and orchestration (201)

**Goal:** build an incremental bronze-to-gold pipeline and schedule it.

1. [[Lakeflow]]: the umbrella for Connect, Pipelines, and Jobs.
2. [[Lakeflow Connect]]: managed connectors for databases and SaaS apps.
3. [[Auto Loader]]: picking up only new files as they land.
4. [[COPY INTO]]: the simple SQL alternative for one-off or small loads.
5. [[Lakeflow Spark Declarative Pipelines]]: declare tables and let Databricks run them (formerly Delta Live Tables).
6. [[Streaming Tables]]: tables that update incrementally as data arrives.
7. [[Materialized Views]]: precomputed gold tables that refresh incrementally.
8. [[Expectations and Data Quality]]: rules that warn, drop, or fail on bad rows.
9. [[Lakeflow Jobs]]: the built-in orchestrator (formerly Workflows).
10. [[Tasks Triggers and Schedules]]: dependencies, retries, and file-arrival triggers.

> [!check] Checkpoint
> Create a pipeline in the Lakeflow Pipelines editor with three datasets: a streaming table that reads your Volume with Auto Loader (`read_files` in SQL or `cloudFiles` in Python), a silver streaming table with an expectation such as `CONSTRAINT valid_id EXPECT (customer_id IS NOT NULL) ON VIOLATION DROP ROW`, and a gold materialized view. Run it, drop a new file into the Volume, and run it again. Then wrap it in a job with a second task that runs a SQL query after the pipeline succeeds.

### Stage 4: Production practices (201 to 301)

**Goal:** handle change data, keep history, and ship pipelines through Git and CI.

1. [[Change Data Capture]] (301): copying only what changed, with AUTO CDC.
2. [[Slowly Changing Dimensions]] (301): type 1 versus type 2 history.
3. [[Structured Streaming on Databricks]] (301): Kafka sources, checkpoints, and real-time mode.
4. [[Secrets Management]] (201): keeping credentials out of code.
5. [[Git Folders and Workspace Files]] (201): your repo inside the workspace.
6. [[Databricks CLI]] (201): scripting the platform.
7. [[Declarative Automation Bundles]] (301): jobs and pipelines as YAML in Git (formerly Databricks Asset Bundles).
8. [[Testing Data Pipelines]] (301): unit tests, data tests, and expectations.
9. [[CI-CD for Data Pipelines]] (301): dev, staging, and prod with automated deploys.

> [!check] Checkpoint
> Change your silver table to an AUTO CDC flow that keeps SCD type 2 history (`STORED AS SCD TYPE 2`), and confirm `__START_AT` and `__END_AT` columns appear. Then, on your laptop, run `databricks bundle init`, add your pipeline and job to the bundle, and run `databricks bundle validate` and `databricks bundle deploy -t dev`. Commit the bundle to a Git repo.

### Stage 5: Tuning and internals (301 to 401)

**Goal:** make tables and queries fast and cost-efficient at scale.

1. [[Liquid Clustering]] (301): the layout that replaced partitioning and Z-ordering for most tables.
2. [[OPTIMIZE and VACUUM]] (301): compaction, cleanup, and Predictive Optimization.
3. [[Change Data Feed]] (301): row-level change logs for downstream consumers.
4. [[Delta Transaction Log]] (301): how `_delta_log` provides transactions.
5. [[Deletion Vectors]] (401): marking rows deleted instead of rewriting files.
6. [[Shuffles]] (301): the most expensive operation in Spark.
7. [[Adaptive Query Execution]] (301): Spark re-planning mid-query.
8. [[Photon]] (301): the C++ engine behind fast SQL.
9. [[Query Performance and Caching]] (301): reading a query profile.

> [!check] Checkpoint
> Create a copy of a large sample table with `CREATE TABLE ... CLUSTER BY (col) AS SELECT ...`, run `OPTIMIZE`, and compare `DESCRIBE DETAIL` (file count, size) before and after. Run the same filtered query against the original and the clustered copy and compare the "files read" numbers in each query profile.

## Rabbit holes

- **History of the role:** [[MapReduce]], [[Apache Hadoop]], [[Apache Hive]], [[Hive Metastore]], [[Apache Kafka]], [[Apache Airflow]], [[dbt]], [[Fivetran and ELT Tools]]. The hub [[Open Source vs Databricks - Who Replaced What]] maps each to its Databricks successor.
- **Other table formats:** [[Apache Iceberg]], [[Apache Hudi]], [[Delta UniForm]].
- **Spark internals:** [[RDDs]], [[Catalyst Optimizer]], [[Tungsten]], [[Jobs Stages and Tasks]], [[Spark UI]], [[Spark Connect]].
- **Low-code and SQL-first:** [[Lakeflow Designer]] and [[dbt on Databricks]].
- **Migrations:** [[Migrating from SQL Server]], [[Migrating from Hadoop]], [[Migrating ETL Tools]], [[Lakebridge]].
- **Cloud storage access:** [[ADLS and Access Connectors]], [[S3 Access via Unity Catalog]], [[GCS Access via Unity Catalog]], and the full [[Path - Azure Deep Dive]], [[Path - AWS Deep Dive]], or [[Path - Google Cloud Deep Dive]].
- **Azure orchestration:** [[Azure Data Factory with Databricks]].

## You are done when

- You can explain lazy evaluation, partitions, and shuffles with an example.
- You can load, merge, time-travel, and restore a Delta table.
- You have built an incremental pipeline with Auto Loader, expectations, and a gold materialized view.
- You can schedule it as a multi-task job with retries and a trigger.
- You can handle CDC with SCD type 2 history.
- You deploy pipelines from Git with a bundle, not through the UI.
- You can tune a slow table with liquid clustering and read a query profile.

> [!nextup] Next
> [[Path - Data Scientist and ML Engineer]] covers building models on the tables data engineers produce.

> [!sources]- Sources (last verified: 2026-10-25)
> - Route assembled on 2026-10-25 from the vault index (`llms.txt`) and the `engineer` persona tags in `_meta/manifest.yaml`. Product names follow the vault's renames hub ([[Databricks Product Names and Renames]]). Official documentation links live in each linked note's `[!sources]` callout.
> - Checkpoint commands (`MERGE`, `RESTORE`, `CLUSTER BY`, `OPTIMIZE`, `databricks bundle ...`) are standard Databricks SQL and CLI commands; exact Free Edition limits on pipelines and jobs were not re-checked for this path. See [[Databricks Free Edition and Trials]].
