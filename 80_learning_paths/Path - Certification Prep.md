---
type: path
status: written
level: 80
section: Learning Paths
depth: 301
summary: Which Databricks certifications exist and which notes map to each exam.
personas:
  - engineer
  - analyst
  - scientist
chapter: "[[Chapter 80 - Learning Paths]]"
prev: "[[Path - Google Cloud Deep Dive]]"
next: "[[start_here]]"
evolved_from: []
evolved_into: []
cloud_equivalent: []
related:
  - "[[Unity Catalog]]"
  - "[[Delta Lake]]"
  - "[[Apache Spark]]"
  - "[[Lakeflow Spark Declarative Pipelines]]"
  - "[[Lakeflow Jobs]]"
  - "[[Auto Loader]]"
  - "[[Databricks SQL]]"
  - "[[AI-BI Dashboards]]"
  - "[[MLflow]]"
  - "[[Feature Engineering and Feature Store]]"
  - "[[Retrieval-Augmented Generation]]"
  - "[[AI Search]]"
  - "[[Declarative Automation Bundles]]"
  - "[[Path - Data Engineer]]"
  - "[[Path - Analyst]]"
  - "[[Path - Data Scientist and ML Engineer]]"
  - "[[Path - AI App Developer]]"
  - "[[Path - Platform Admin]]"
aliases:
  - Databricks Certifications
  - Exam Prep
prereqs:
  - "[[Path - Absolute Beginner]]"
unlocks: []
clouds:
  - aws
  - azure
  - gcp
mastery: new
last_verified:
tags:
  - path
---

# Path - Certification Prep

> [!persona] Who this is for
> **Who:** an engineer, analyst, data scientist, or AI developer preparing for a Databricks certification exam, often a student or someone changing jobs.
> **Goal:** identify which exam fits you, which notes in this vault cover each topic area, and how to practice the hands-on skills the exams test.
> **Outcome:** a study plan for one exam, mapped to notes you can read in order, with a workspace checkpoint for each stage.

> [!warning] Check the exam list before you study
> Databricks revises its exams and exam guides often, and has renamed many of the products they cover (see [[Databricks Product Names and Renames]]). The exam list and topic areas below reflect the vault author's knowledge as of mid-2026 and **were not re-verified against the official certification pages for this edition**. Before you book an exam, open the official Databricks certification page (on Databricks Academy), download the current exam guide for your exam, and compare its topic list with the tables here.

## Before you start

Finish the role path that matches your exam first: [[Path - Data Engineer]], [[Path - Analyst]], [[Path - Data Scientist and ML Engineer]], or [[Path - AI App Developer]]. The exams test hands-on judgment more than definitions, so do every checkpoint in a real workspace. [[Databricks Free Edition and Trials|Free Edition]] covers most associate-level practice.

## The exams at a glance

These are the certifications Databricks has offered in recent years, listed from the author's knowledge and **not confirmed** against the official pages for this edition. Exam names, levels, and recommended experience may have changed.

| Exam | Level | Recommended path | Core notes |
|---|---|---|---|
| Data Engineer Associate | Associate | [[Path - Data Engineer]] Stages 1 to 3 | [[Delta Lake]], [[Auto Loader]], [[Lakeflow Spark Declarative Pipelines]], [[Lakeflow Jobs]], [[Unity Catalog]] |
| Data Engineer Professional | Professional | [[Path - Data Engineer]] Stages 4 and 5 | [[Change Data Capture]], [[Structured Streaming on Databricks]], [[Declarative Automation Bundles]], [[Liquid Clustering]] |
| Data Analyst Associate | Associate | [[Path - Analyst]] | [[Databricks SQL]], [[SQL Warehouses]], [[AI-BI Dashboards]], [[Genie Agents]] |
| Machine Learning Associate | Associate | [[Path - Data Scientist and ML Engineer]] Stages 1 and 2 | [[MLflow]], [[Experiment Tracking]], [[AutoML]], [[MLlib]] |
| Machine Learning Professional | Professional | [[Path - Data Scientist and ML Engineer]] Stages 3 and 4 | [[Feature Engineering and Feature Store]], [[Models in Unity Catalog]], [[Model Serving]], [[Data Quality Monitoring]] |
| Generative AI Engineer Associate | Associate | [[Path - AI App Developer]] | [[Retrieval-Augmented Generation]], [[AI Search]], [[Mosaic AI Agent Framework]], [[Agent Evaluation and Tracing]] |
| Associate Developer for Apache Spark | Associate | [[Path - Data Engineer]] Stage 1 plus Spark rabbit holes | [[DataFrames]], [[Spark SQL]], [[Partitions]], [[Shuffles]] |

Databricks has also offered shorter **accreditations** (unconfirmed for this edition: earlier examples included fundamentals and platform-architect badges). They are a suitable first step and map to [[Path - Absolute Beginner]] and [[Path - Platform Admin]]. Check the official page for which badges are current.

## The route

### Stage 1: Shared core for every exam (101 to 201)

**Goal:** learn the platform basics that appear on every exam.

1. [[The Data Intelligence Platform]]: how Databricks describes its own platform, which exam questions reflect.
2. [[Accounts and Workspaces]]: account versus workspace, a common question.
3. [[Control Plane and Compute Plane]] (201): what runs where.
4. [[Compute Types]]: all-purpose, jobs, serverless, and SQL warehouses, and when to pick each.
5. [[Delta Lake]]: the table format that most questions assume.
6. [[Time Travel]] (201): `VERSION AS OF`, `RESTORE`, and `DESCRIBE HISTORY`.
7. [[Unity Catalog]]: governance appears on every exam.
8. [[Three-Level Namespace]]: `catalog.schema.table`.
9. [[Privileges and Grants]] (201): which privileges a user needs to query a table.
10. [[Medallion Architecture]]: bronze, silver, gold.

> [!check] Checkpoint
> Without notes, in a Free Edition workspace: create a schema and a Delta table, insert rows, update some, run `DESCRIBE HISTORY`, query an older version, and `RESTORE` it. Then write the exact `GRANT` statements a new analyst would need to `SELECT` from that table. Check your answer against [[Privileges and Grants]].

### Stage 2: Your associate exam (201)

**Goal:** cover the topic areas of one associate exam. Choose the list for your exam.

**Data Engineer Associate.** *Unconfirmed:* earlier exam guides grouped topics roughly as the platform, development and ingestion, data processing and transformation, productionizing pipelines, and governance.

1. [[Auto Loader]]: incremental file ingestion, a frequent topic.
2. [[COPY INTO]]: the simpler loader, and when it is sufficient.
3. [[Lakeflow Connect]]: managed connectors.
4. [[Lakeflow Spark Declarative Pipelines]]: declarative pipelines (formerly Delta Live Tables, and older exam material may still use that name).
5. [[Streaming Tables]] and [[Materialized Views]]: the two pipeline dataset types.
6. [[Expectations and Data Quality]]: warn, drop, or fail.
7. [[MERGE and Upserts]]: incremental updates in SQL.
8. [[Lakeflow Jobs]] and [[Tasks Triggers and Schedules]]: orchestration (formerly Workflows).
9. [[Volumes]] and [[Managed vs External Tables]]: storage questions.
10. [[OpenSharing]] and [[Lakehouse Federation]]: sharing and federation (OpenSharing was formerly Delta Sharing).

**Data Analyst Associate.** *Unconfirmed:* earlier exam guides grouped topics roughly as Databricks SQL, data management, SQL queries, visualization and dashboards, and analytics applications.

1. [[Databricks SQL]] and [[SQL Warehouses]]: the analyst workbench and its compute.
2. [[SQL Editor]]: writing and sharing queries.
3. [[Catalogs Schemas and Tables]]: data management.
4. [[AI-BI Dashboards]]: dashboards, filters, and sharing.
5. [[Genie Agents]]: natural-language analytics.
6. [[SQL Alerts]]: alerting on results.
7. [[Connecting Power BI]] and [[Partner Connect]]: BI tool integration.
8. [[Star Schema]] and [[Slowly Changing Dimensions]]: modeling concepts.

**Machine Learning Associate.** *Unconfirmed:* earlier exam guides grouped topics roughly as Databricks ML tooling, data preparation, model development, and deployment.

1. [[Machine Learning Basics]]: the vocabulary.
2. [[Notebooks]] and [[Libraries and Environments]]: the ML working environment.
3. [[PySpark]] and [[DataFrames]]: data preparation at scale.
4. [[MLflow]] and [[Experiment Tracking]]: logging and comparing runs.
5. [[AutoML]]: baselines.
6. [[MLlib]]: distributed training.
7. [[Models in Unity Catalog]]: registering and aliasing.
8. [[Feature Engineering and Feature Store]]: feature tables.

**Generative AI Engineer Associate.** *Unconfirmed:* earlier exam guides grouped topics roughly as designing applications, data preparation, application development, assembling and deploying, governance, and evaluation and monitoring.

1. [[Generative AI and LLMs]]: core concepts.
2. [[Retrieval-Augmented Generation]]: the main design pattern.
3. [[AI Search]]: indexes and retrieval.
4. [[Foundation Model APIs]]: choosing and calling models.
5. [[Mosaic AI Agent Framework]]: building agents and chains.
6. [[Model Serving]]: deploying them.
7. [[Agent Evaluation and Tracing]]: judges, metrics, and traces.
8. [[Unity Gateway]]: guardrails and governance.

**Associate Developer for Apache Spark.** *Unconfirmed:* earlier exam guides grouped topics roughly as Spark architecture, the DataFrame API, Spark SQL, and Structured Streaming basics.

1. [[Apache Spark]] and [[Driver and Executors]]: architecture.
2. [[Lazy Evaluation]] and [[Transformations and Actions]]: the execution model.
3. [[DataFrames]], [[PySpark]], and [[Spark SQL]]: the API.
4. [[Partitions]] and [[Shuffles]]: performance basics.
5. [[Adaptive Query Execution]]: runtime re-planning.
6. [[Structured Streaming]]: streams as growing tables.
7. [[Spark Connect]]: the client-server model.

> [!check] Checkpoint
> Do the hands-on task for your exam in a workspace, without looking anything up:
> - **Data Engineer:** a pipeline that ingests files from a Volume with Auto Loader into bronze, applies one expectation in silver, builds a gold materialized view, and runs as a scheduled job.
> - **Data Analyst:** a dashboard with a filter and three visuals on a gold table, a Genie agent (formerly Genie space) on it, and an alert.
> - **ML:** three tracked runs in MLflow, the best one registered in Unity Catalog with an alias and loaded by alias.
> - **Generative AI:** an AI Search index on a chunk table, queried by a simple RAG chain, with one evaluation run logged to MLflow.
> - **Spark Developer:** a notebook that reads a sample table, does a join and a window function, writes the result partitioned or clustered, and shows `.explain()` before and after a `repartition`.

### Stage 3: Your professional exam (301 to 401)

**Goal:** cover the production depth that professional exams add.

**Data Engineer Professional.** *Unconfirmed:* earlier exam guides grouped topics roughly as data processing, modeling, security and governance, monitoring and logging, testing, and deployment.

1. [[Change Data Capture]] (301): AUTO CDC and change feeds.
2. [[Slowly Changing Dimensions]] (301): type 1 and type 2.
3. [[Change Data Feed]] (301): row-level changes downstream.
4. [[Structured Streaming on Databricks]] (301): checkpoints, watermarks, and Kafka.
5. [[Liquid Clustering]] and [[OPTIMIZE and VACUUM]] (301): layout and maintenance.
6. [[Row Filters and Column Masks]] (301): fine-grained security.
7. [[System Tables]] and [[Audit Logs]]: monitoring and logging.
8. [[Testing Data Pipelines]] (301): tests for data code.
9. [[Declarative Automation Bundles]] and [[CI-CD for Data Pipelines]] (301): deployment.
10. [[Spark UI]] and [[Query Performance and Caching]]: diagnosing slow jobs.

**Machine Learning Professional.** *Unconfirmed:* earlier exam guides grouped topics roughly as experimentation, model lifecycle management, deployment, and monitoring.

1. [[Feature Engineering and Feature Store]] (301): online and offline features.
2. [[Models in Unity Catalog]]: lifecycle with aliases.
3. [[Model Serving]]: real-time endpoints.
4. [[Lakeflow Jobs]]: batch inference and retraining.
5. [[Data Quality Monitoring]] (301): drift and inference monitoring.
6. [[Declarative Automation Bundles]] (301): MLOps deployment.
7. [[AI Runtime]] (301): scaling training.
8. [[Agent Evaluation and Tracing]] (301): evaluation for LLM-based models.

> [!check] Checkpoint
> **Data Engineer Professional:** convert your associate pipeline to AUTO CDC with SCD type 2, deploy it with a bundle to `dev` and `prod` targets, and add a row filter to the gold table. **ML Professional:** add a feature table to your model, deploy it to a serving endpoint (on a workspace that allows it), schedule batch scoring, and set up a monitor on the inference table.

### Stage 4: Exam week (201 to 301)

**Goal:** close knowledge gaps and become familiar with the question style.

1. [[Databricks Product Names and Renames]]: older exam prep material uses old product names, so learn both.
2. [[Open Source vs Databricks - Who Replaced What]]: "which feature replaced X" questions.
3. [[Compute Types]] and [[Serverless Compute]]: compute-choice scenario questions.
4. [[Cost Optimization Checklist]]: "most cost-effective option" questions.
5. [[Compute Policies]]: admin-flavored questions on engineering exams.
6. Your exam's Recall sections: review the `## Recall` flashcards in every note on your list with the Spaced Repetition plugin.

> [!check] Checkpoint
> Take the official practice exam or sample questions for your certification, if Databricks offers them. For every question you miss, find the vault note that covers it and add a flashcard to that note's Recall section in your own copy of the vault.

## Rabbit holes

- **Admin and architecture badges:** [[Path - Platform Admin]], then [[Path - Azure Deep Dive]], [[Path - AWS Deep Dive]], or [[Path - Google Cloud Deep Dive]] for your cloud.
- **History questions:** [[AMPLab and the Birth of Spark]], [[The Lakehouse Paper]], [[Timeline of Data Engineering]].
- **Spark internals for the Spark exam:** [[Catalyst Optimizer]], [[Tungsten]], [[Jobs Stages and Tasks]], [[RDDs]].
- **Table formats:** [[Apache Iceberg]], [[Delta UniForm]], [[Deletion Vectors]].

## You are done when

- You have confirmed your exam's current name and topic list on the official certification page.
- You can do the Stage 2 (or Stage 3) checkpoint for your exam from memory.
- You know the current and old names of every product on your exam.
- You have reviewed the Recall flashcards for every note on your list.
- You consistently pass the official practice questions.

> [!nextup] Next
> This is the last path. Return to [[start_here]] to choose another path, or read the story from the beginning.

> [!sources]- Sources (not verified for this edition)
> - The exam list and topic areas above come from the author's knowledge as of mid-2026. They could not be checked against the official Databricks certification pages when this note was written (October 2026), so `last_verified` is left blank on purpose. Verify them on the official Databricks certification page and in each exam's current exam guide before studying.
> - Note-to-topic mappings were built on 2026-10-25 from the vault index (`llms.txt`). Product facts and official documentation links live in each linked note's `[!sources]` callout.
