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
  - "[[Genie Agents]]"
  - "[[MLflow]]"
  - "[[Feature Engineering and Feature Store]]"
  - "[[Retrieval-Augmented Generation]]"
  - "[[AI Search]]"
  - "[[Lakebase]]"
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
last_verified: 2026-10-25
tags:
  - path
---

# Path - Certification Prep

> [!persona] Who this is for
> **Who:** an engineer, analyst, data scientist, or AI developer preparing for a Databricks certification exam, often a student or someone changing jobs.
> **Goal:** identify which exam fits you, which notes in this vault cover each topic area, and how to practice the hands-on skills the exams test.
> **Outcome:** a study plan for one exam, mapped to notes you can read in order, with a workspace checkpoint for each stage.

> [!warning] Check the exam guide two weeks before your exam
> The exam list, topic areas, and weights below were checked against the official Databricks certification pages and exam guides on 2026-10-25. Databricks updates exam guides without notice, and each guide asks you to re-check it two weeks before your exam date. Exam guides also lag product renames: several still say Genie spaces, Vector Search, Lakehouse Monitoring, or Databricks Asset Bundles. See [[Databricks Product Names and Renames]] and learn both names.

## Before you start

Finish the role path that matches your exam first: [[Path - Data Engineer]], [[Path - Analyst]], [[Path - Data Scientist and ML Engineer]], or [[Path - AI App Developer]]. The exams test hands-on judgment more than definitions, so do every checkpoint in a real workspace. Each exam guide points to [[Databricks Free Edition and Trials|Free Edition]] for hands-on practice.

## The exams at a glance

Databricks lists eight certification exams on its certification page as of 2026-10-25. All are proctored, multiple-choice, delivered online or at a test center, valid for two years, and allow no test aids. Recertification means passing the current version of the exam. The Data Engineer Associate also has a shorter renewal exam. The registration fee is listed on each exam page.

| Exam | Level | Scored questions | Time | Current exam guide | Recommended path |
|---|---|---|---|---|---|
| Data Analyst Associate | Associate | 45 | 90 min | Version current as of October 30, 2025 | [[Path - Analyst]] |
| Data Engineer Associate | Associate | 45 | 90 min | Exam published May 4, 2026; guide updated August 6, 2026 | [[Path - Data Engineer]] Stages 1 to 3 |
| Data Engineer Professional | Professional | 60 | 120 min | Exam published October 9, 2026 | [[Path - Data Engineer]] Stages 4 and 5 |
| Machine Learning Associate | Associate | 48 | 90 min | Exam published March 1, 2025 | [[Path - Data Scientist and ML Engineer]] Stages 1 and 2 |
| Machine Learning Professional | Professional | 59 | 120 min | Exam published September 30, 2025 | [[Path - Data Scientist and ML Engineer]] Stages 3 and 4 |
| Generative AI Engineer Associate | Associate | 45 | 90 min | Exam published March 18, 2026 | [[Path - AI App Developer]] |
| Context Engineer Associate | Associate | 45 | 90 min | Exam published July 29, 2026 | [[Path - AI App Developer]] |
| Associate Developer for Apache Spark | Associate | 45 | 90 min | Exam published October 8, 2026 | [[Path - Data Engineer]] Stage 1 plus Spark rabbit holes |

Exams may also include unscored questions. They are not identified, and extra time is already included in the time limit.

### Accreditations

Accreditations are shorter assessments that earn a badge. The certification page lists:

| Accreditation | Covers | Related path |
|---|---|---|
| Databricks Fundamentals | The lakehouse and the platform basics | [[Path - Absolute Beginner]] |
| Generative AI Fundamentals | LLM concepts for an organization | [[Path - AI App Developer]] |
| AI Agent Fundamentals | AI agent concepts | [[Path - AI App Developer]] |
| AWS, Azure, and GCP Platform Architect | Deployment, security, and cloud integrations on one cloud | [[Path - AWS Deep Dive]], [[Path - Azure Deep Dive]], [[Path - Google Cloud Deep Dive]] |
| Platform Administrator | The final assessment of the Data + AI Platform Administrator learning pathway | [[Path - Platform Admin]] |

### Retired exams

The Databricks Certified Hadoop Migration Architect exam is no longer available as of August 1, 2024.

## The route

### Stage 1: Shared core for every exam (101 to 201)

**Goal:** learn the platform basics that appear on every exam.

1. [[The Data Intelligence Platform]]: how Databricks describes its own platform. Exam guides call it the Databricks Data + AI Platform or the Databricks Intelligence Platform.
2. [[Accounts and Workspaces]]: account versus workspace.
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

**Goal:** cover the topic areas of one associate exam. Each table lists the exam's own sections and weights, with the vault notes that cover them.

#### Data Engineer Associate

Code is in SQL where possible, otherwise Python.

| Topic area | Weight | Vault notes |
|---|---|---|
| Databricks Intelligence Platform | 6% | [[The Data Intelligence Platform]], [[Compute Types]], [[Serverless Compute]] |
| Data Ingestion and Loading | 21% | [[Auto Loader]], [[COPY INTO]], [[Lakeflow Connect]], [[Volumes]] |
| Data Transformation and Modeling | 22% | [[PySpark]], [[DataFrames]], [[Materialized Views]], [[Streaming Tables]], [[Expectations and Data Quality]], [[MERGE and Upserts]] |
| Working with Lakeflow Jobs | 16% | [[Lakeflow Jobs]], [[Tasks Triggers and Schedules]] |
| Implementing CI/CD | 10% | [[Git Folders and Workspace Files]], [[Declarative Automation Bundles]], [[Databricks CLI]] |
| Troubleshooting, Monitoring, and Optimization | 10% | [[Spark UI]], [[Liquid Clustering]], [[Data Skew]], [[Spill]] |
| Governance and Security | 15% | [[Managed vs External Tables]], [[Privileges and Grants]], [[Row Filters and Column Masks]], [[Attribute-Based Access Control]] |

#### Data Analyst Associate

The exam uses ANSI SQL. The exam guide does not list weights; the weights below come from the exam page.

| Topic area | Weight | Vault notes |
|---|---|---|
| Understanding of Databricks Data + AI Platform | 11% | [[The Data Intelligence Platform]], [[Catalogs Schemas and Tables]], [[Databricks Marketplace]] |
| Managing Data | 8% | [[Unity Catalog]], [[Data Lineage]] |
| Importing Data | 5% | [[Auto Loader]], [[OpenSharing]], [[Databricks Marketplace]] |
| Executing queries using Databricks SQL and Databricks SQL Warehouses | 20% | [[Databricks SQL]], [[SQL Warehouses]], [[SQL Editor]], [[Genie Code]], [[Lakehouse Federation]], [[Materialized Views]] |
| Analyzing Queries | 15% | [[Photon]], [[Query Performance and Caching]], [[Time Travel]], [[Liquid Clustering]] |
| Creating Dashboards and Visualizations in Databricks | 16% | [[AI-BI Dashboards]], [[SQL Alerts]] |
| Developing, Sharing, and Maintaining AI/BI Genie spaces | 12% | [[Genie Agents]] (formerly Genie spaces) |
| Data Modeling with Databricks SQL | 5% | [[Star Schema]], [[Slowly Changing Dimensions]] |
| Securing Data | 8% | [[Privileges and Grants]], [[Row Filters and Column Masks]] |

#### Machine Learning Associate

ML code is in Python; other data code may be in SQL.

| Topic area | Weight | Vault notes |
|---|---|---|
| Databricks Machine Learning | 38% | [[MLflow]], [[Experiment Tracking]], [[AutoML]], [[Feature Engineering and Feature Store]] |
| ML Workflows | 19% | [[Machine Learning Basics]], [[PySpark]], [[DataFrames]] |
| Model Development | 31% | [[MLlib]], [[Experiment Tracking]] |
| Model Deployment | 12% | [[Models in Unity Catalog]], [[Model Serving]] |

The ML Associate guide predates the AutoML change: AutoML is removed from Databricks Runtime 18.0 ML. Read [[AutoML]] for both the exam view and the current state.

#### Generative AI Engineer Associate

ML code is in Python.

| Topic area | Weight | Vault notes |
|---|---|---|
| Design Applications | 14% | [[Generative AI and LLMs]], [[Prompt]], [[Agent Bricks]] |
| Data Preparation | 14% | [[Retrieval-Augmented Generation]], [[Embedding]], [[Delta Lake]] |
| Application Development | 30% | [[Mosaic AI Agent Framework]], [[Foundation Model APIs]], [[Unity Gateway]], [[Genie Agents]] |
| Assembling and Deploying Apps | 22% | [[AI Search]] (the guide says Vector Search), [[Model Serving]], [[Models in Unity Catalog]], [[AI Functions in SQL]] |
| Governance | 8% | [[Unity Catalog]], [[Unity Gateway]] |
| Evaluation and Monitoring | 12% | [[Agent Evaluation and Tracing]], [[MLflow]] |

#### Context Engineer Associate

The newest exam (published July 29, 2026). It tests what an agent receives at inference time: instructions, retrieved knowledge, memory, tools, and compacted history. Code is in Python.

| Topic area | Weight | Vault notes |
|---|---|---|
| Foundations of Context Engineering | 16% | [[AI Agent]], [[Generative AI and LLMs]], [[Token]] |
| System Prompt and Instruction Design | 9% | [[Prompt]], [[Genie Agents]], [[Experiment Tracking]] |
| Knowledge Retrieval and Genie Configuration | 20% | [[AI Search]], [[Retrieval-Augmented Generation]], [[Embedding]], [[Genie Agents]], [[Unity Catalog]] |
| Memory Architecture with Lakebase and MLflow | 18% | [[Lakebase]], [[MLflow]], [[Agent Evaluation and Tracing]] |
| Tool Design, MCP, and Agent Context | 13% | [[Agent Bricks]], [[Unity Gateway]], [[Mosaic AI Agent Framework]] |
| Context Compression and Compaction | 11% | [[Agent Evaluation and Tracing]] (traces); no dedicated vault note |
| Multi-Agent and Long-Horizon Task Design | 13% | [[Agent Bricks]], [[Mosaic AI Agent Framework]] |

#### Associate Developer for Apache Spark

Code is in Python.

| Topic area | Weight | Vault notes |
|---|---|---|
| Apache Spark Architecture and Components | 20% | [[Apache Spark]], [[Driver and Executors]], [[Jobs Stages and Tasks]], [[Lazy Evaluation]], [[Transformations and Actions]], [[Partitions]], [[Shuffles]] |
| Using Spark SQL | 20% | [[Spark SQL]] |
| Developing Apache Spark DataFrame/DataSet API Applications | 30% | [[DataFrames]], [[PySpark]], [[UDF]], [[Broadcast Join]] |
| Troubleshooting and Tuning Apache Spark DataFrame API Applications | 10% | [[Adaptive Query Execution]], [[Spark UI]], [[Data Skew]] |
| Structured Streaming | 10% | [[Structured Streaming]], [[Watermark]], [[Checkpoint]] |
| Using Spark Connect to deploy applications | 5% | [[Spark Connect]] |
| Using Pandas API on Apache Spark | 5% | [[Pandas]], [[Python for Data]] |

> [!check] Checkpoint
> Do the hands-on task for your exam in a workspace, without looking anything up:
> - **Data Engineer:** a pipeline that ingests files from a Volume with Auto Loader into bronze, applies one expectation in silver, builds a gold materialized view, and runs as a scheduled job.
> - **Data Analyst:** a dashboard with a filter and three visuals on a gold table, a Genie agent (formerly Genie space) on it, and an alert.
> - **ML:** three tracked runs in MLflow, the best one registered in Unity Catalog with an alias and loaded by alias.
> - **Generative AI:** an AI Search index on a chunk table, queried by a simple RAG chain, with one evaluation run logged to MLflow.
> - **Context Engineer:** a Genie agent with instructions, sample questions, and trusted SQL; then an agent that keeps conversation state in Lakebase across two sessions, with its traces logged to MLflow.
> - **Spark Developer:** a notebook that reads a sample table, does a join and a window function, writes the result partitioned or clustered, and shows `.explain()` before and after a `repartition`.

### Stage 3: Your professional exam (301 to 401)

**Goal:** cover the production depth that professional exams add.

#### Data Engineer Professional

Code is in Python and SQL. The exam guide dated October 9, 2026 lists 60 scored questions in nine sections. The summary on the exam page still showed the previous outline (59 questions, ten sections) on 2026-10-25, so follow the guide.

| Topic area | Weight | Vault notes |
|---|---|---|
| Developing Code for Data Processing using Python and SQL | 23% | [[Declarative Automation Bundles]], [[Lakeflow Spark Declarative Pipelines]], [[Streaming Tables]], [[Materialized Views]], [[Change Data Capture]], [[Slowly Changing Dimensions]], [[Lakeflow Jobs]], [[Serverless Compute]], [[Testing Data Pipelines]], [[Structured Streaming on Databricks]] |
| Data Ingestion & Acquisition | 12% | [[Auto Loader]], [[Lakeflow Connect]], [[OpenSharing]], [[Clean Rooms]], [[Lakehouse Federation]] |
| Data Manipulation | 12% | [[Spark SQL]], [[PySpark]], [[AI Functions in SQL]], [[Expectations and Data Quality]] |
| Monitoring and Alerting | 10% | [[System Tables]], [[SQL Alerts]], [[Lakeflow Jobs]] |
| Cost & Performance Optimization | 15% | [[Liquid Clustering]], [[Deletion Vectors]], [[OPTIMIZE and VACUUM]], [[Caching]], [[Change Data Feed]], [[Query Performance and Caching]] |
| Ensuring Data Security and Compliance | 8% | [[Privileges and Grants]], [[Attribute-Based Access Control]], [[Row Filters and Column Masks]], [[PII]], [[GDPR]] |
| Data Governance | 5% | [[Unity Catalog]], [[Privileges and Grants]] |
| Debugging and Deploying | 10% | [[Spark UI]], [[System Tables]], [[Declarative Automation Bundles]], [[Git Folders and Workspace Files]], [[CI-CD for Data Pipelines]] |
| Data Modeling | 5% | [[Liquid Clustering]], [[Star Schema]], [[Materialized Views]], [[Metric Views]] |

#### Machine Learning Professional

The guide still uses the older names Databricks Asset Bundles and Lakehouse Monitoring.

| Topic area | Weight | Vault notes |
|---|---|---|
| Model Development | 44% | [[MLlib]], [[MLflow]], [[Experiment Tracking]], [[Feature Engineering and Feature Store]], [[AI Runtime]] |
| ML Ops | 44% | [[Models in Unity Catalog]], [[Declarative Automation Bundles]], [[Lakeflow Jobs]], [[Data Quality Monitoring]] (formerly Lakehouse Monitoring), [[Drift]] |
| Model Deployment | 12% | [[Model Serving]], [[Models in Unity Catalog]] |

> [!check] Checkpoint
> **Data Engineer Professional:** convert your associate pipeline to AUTO CDC with SCD type 2, deploy it with a bundle to `dev` and `prod` targets, and add a row filter to the gold table. **ML Professional:** add a feature table to your model, deploy it to a serving endpoint (on a workspace that allows it), schedule batch scoring, and set up a monitor on the inference table.

### Stage 4: Exam week (201 to 301)

**Goal:** close knowledge gaps and become familiar with the question style.

1. [[Databricks Product Names and Renames]]: exam guides and older prep material use old product names, so learn both.
2. [[Open Source vs Databricks - Who Replaced What]]: "which feature replaced X" questions.
3. [[Compute Types]] and [[Serverless Compute]]: compute-choice scenario questions.
4. [[Cost Optimization Checklist]]: "most cost-effective option" questions.
5. [[Compute Policies]]: admin-flavored questions on engineering exams.
6. Your exam's Recall sections: review the `## Recall` flashcards in every note on your list with the Spaced Repetition plugin.

> [!check] Checkpoint
> Work through the sample questions in your exam guide. For every question you miss, find the vault note that covers it and add a flashcard to that note's Recall section in your own copy of the vault.

## Rabbit holes

- **Admin and architecture accreditations:** [[Path - Platform Admin]], then [[Path - Azure Deep Dive]], [[Path - AWS Deep Dive]], or [[Path - Google Cloud Deep Dive]] for your cloud.
- **History questions:** [[AMPLab and the Birth of Spark]], [[The Lakehouse Paper]], [[Timeline of Data Engineering]].
- **Spark internals for the Spark exam:** [[Catalyst Optimizer]], [[Tungsten]], [[Jobs Stages and Tasks]], [[RDDs]].
- **Table formats:** [[Apache Iceberg]], [[Delta UniForm]], [[Deletion Vectors]].

## You are done when

- You have downloaded the current exam guide for your exam and compared its outline with the table above.
- You can do the Stage 2 (or Stage 3) checkpoint for your exam from memory.
- You know the current and old names of every product on your exam.
- You have reviewed the Recall flashcards for every note on your list.
- You answer the sample questions in your exam guide correctly and can explain why each wrong option is wrong.

> [!nextup] Next
> This is the last path. Return to [[start_here]] to choose another path, or read the story from the beginning.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Databricks Certification and Badging](https://www.databricks.com/learn/certification): exam list, accreditations, and the Hadoop Migration Architect retirement.
> - [Data Analyst Associate](https://www.databricks.com/learn/certification/data-analyst-associate) and [exam guide (October 2025)](https://www.databricks.com/sites/default/files/2025-10/databricks-certified-data-analyst-associate-oct-2025.pdf)
> - [Data Engineer Associate](https://www.databricks.com/learn/certification/data-engineer-associate) and [exam guide (August 2026)](https://www.databricks.com/sites/default/files/2026-10/Databricks-Certified-Data-Engineer-Associate-Exam-Guide-August-2026.pdf)
> - [Data Engineer Professional](https://www.databricks.com/learn/certification/data-engineer-professional) and [exam guide (October 9, 2026)](https://www.databricks.com/sites/default/files/2026-10/Databricks-Certified-Data-Engineer-Professional-Exam-Guide-9-Oct-2026.pdf)
> - [Machine Learning Associate](https://www.databricks.com/learn/certification/machine-learning-associate) and [exam guide](https://www.databricks.com/sites/default/files/2026-10/Databricks-Certified-Machine-Learning-Associate-Exam-Guide-August-2026.pdf)
> - [Machine Learning Professional](https://www.databricks.com/learn/certification/machine-learning-professional) and [exam guide](https://www.databricks.com/sites/default/files/2026-10/databricks-certified-machine-learning-professional-exam-guide-august.pdf)
> - [Generative AI Engineer Associate](https://www.databricks.com/learn/certification/genai-engineer-associate) and [exam guide](https://www.databricks.com/sites/default/files/2026-10/databricks-certified-gen-ai-associate-exam-guide-august-2026.pdf)
> - [Context Engineer Associate](https://www.databricks.com/learn/certification/context-engineer-associate) and [exam guide](https://www.databricks.com/sites/default/files/2026-10/Databricks-Certified-Context-Engineer-Associate-Exam-Guide-August-2026.pdf)
> - [Associate Developer for Apache Spark](https://www.databricks.com/learn/certification/apache-spark-developer-associate) and [exam guide](https://www.databricks.com/sites/default/files/2026-10/databricks-certified-associate-developer-apache-spark-exam-guide-august-2026.pdf)
> - Note-to-topic mappings were built on 2026-10-25 from the exam outlines and the vault index (`llms.txt`). Product facts and documentation links live in each linked note's `[!sources]` callout.
