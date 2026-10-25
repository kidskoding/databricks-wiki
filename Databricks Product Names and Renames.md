---
type: hub
status: written
summary: Current product names, old names, and when they changed. Check here before trusting any name.
related:
  - "[[Genie Code]]"
  - "[[Genie Agents]]"
  - "[[Genie One]]"
  - "[[Declarative Automation Bundles]]"
  - "[[Lakeflow Spark Declarative Pipelines]]"
  - "[[Lakeflow Jobs]]"
  - "[[OpenSharing]]"
  - "[[AI Search]]"
  - "[[Unity Gateway]]"
  - "[[AI Runtime]]"
  - "[[Data Quality Monitoring]]"
  - "[[AI-BI Dashboards]]"
  - "[[The Data Intelligence Platform]]"
  - "[[Agent Bricks]]"
  - "[[Microsoft Entra ID Integration]]"
  - "[[Timeline of Data Engineering]]"
  - "[[Open Source vs Databricks - Who Replaced What]]"
last_verified: 2026-10-25
tags:
  - hub
---

# Databricks Product Names and Renames

This page lists every product rename recorded in the vault: the current name, the former names, when the change happened, and the official source. It is the vault's reference for names.

> [!eli5] What this page is
> Databricks often gives its products new names. Old web pages, videos, and screenshots still use the old names, which is confusing. This page lists each product's name today and the names it had before, so you can tell when two names mean the same thing.

## How to use this page

1. Find the name you have in the **Former names** column, or search this page for it.
2. Use the **Current name** in new work, and open the linked note for details.
3. Expect old names in some places after a rename. API paths, CLI commands, Python packages, and doc URLs often keep the old wording. See [[#What still uses an old name]].

A date in **Changed** comes from official release notes, a Databricks blog post, or the vendor's own announcement, checked on 2026-10-25. **Date not published** means no official source gives a date for the rename. Databricks also edits old release notes to use current names, so the earliest page that shows a new name is not evidence of the rename date. A rename is often announced on one date and reaches each cloud's docs later, so docs for Azure, AWS, and Google Cloud can disagree for a few weeks.

## Databricks product renames

| Current name | Former names | Changed | Note link | Source |
|---|---|---|---|---|
| **Genie Code** | Databricks Assistant, Databricks AI Assistant | March 11, 2026 | [[Genie Code]] | [Introducing Genie Code (Databricks blog)](https://www.databricks.com/blog/introducing-genie-code) |
| **Declarative Automation Bundles** | Databricks Asset Bundles (DABs) | March 16, 2026 | [[Declarative Automation Bundles]] | [Bundles release notes (AWS)](https://docs.databricks.com/aws/en/release-notes/dev-tools/bundles) |
| **Genie One** | Databricks One, then Genie | Genie: April 2026. Genie One: June 2026 ([[Migrating BI Reports]] gives June 9, 2026) | [[Genie One]] | [AI/BI and Genie One release notes 2026 (AWS)](https://docs.databricks.com/aws/en/ai-bi/release-notes/2026) |
| **Genie Agents** | Genie spaces, AI/BI Genie | July 2026 (platform release notes dated July 8, AI/BI release notes dated July 9) | [[Genie Agents]] | [July 2026 release notes (AWS)](https://docs.databricks.com/aws/en/release-notes/product/2026/july) |
| **Unity Gateway** | AI Gateway, Mosaic AI Gateway; interim name Unity AI Gateway | Announced April 15, 2026; GA August 4, 2026 | [[Unity Gateway]] | [Unity Gateway release notes (AWS)](https://docs.databricks.com/aws/en/release-notes/unity-gateway/) |
| **Databricks AI Search** | Mosaic AI Vector Search, Databricks Vector Search | June 1, 2026 | [[AI Search]] | [June 2026 release notes (AWS)](https://docs.databricks.com/aws/en/release-notes/product/2026/june) |
| **OpenSharing** | Delta Sharing | Announced June 10, 2026 | [[OpenSharing]] | [Databricks announces OpenSharing (press release)](https://www.databricks.com/company/newsroom/press-releases/databricks-announces-opensharing) |
| **AI Runtime** | Serverless GPU compute (now part of AI Runtime) | AI Runtime entered Public Preview on March 19, 2026. Rename date not published | [[AI Runtime]] | [AI Runtime (AWS)](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/) |
| **Lakeflow Spark Declarative Pipelines** (short form: Lakeflow pipelines) | Delta Live Tables (DLT), then Lakeflow Declarative Pipelines | Lakeflow Declarative Pipelines: June 2025. Current name: November 2025 | [[Lakeflow Spark Declarative Pipelines]] | [What happened to Delta Live Tables (DLT)? (AWS)](https://docs.databricks.com/aws/en/ldp/concepts/where-is-dlt) |
| **AUTO CDC** (`AUTO CDC INTO`, `create_auto_cdc_flow()`) | APPLY CHANGES (`APPLY CHANGES INTO`, `apply_changes()`) | June 11, 2025 | [[Change Data Capture]] | [The AUTO CDC APIs (AWS)](https://docs.databricks.com/aws/en/ldp/cdc) |
| **Lakeflow Jobs** | Databricks Workflows, and before that Databricks Jobs | June 11, 2025 (release notes: "Databricks Jobs is now Lakeflow Jobs") | [[Lakeflow Jobs]] | [Lakeflow Jobs (AWS)](https://docs.databricks.com/aws/en/jobs/) |
| **AI/BI dashboards** (shown as Dashboards) | Lakeview dashboards | April 18, 2024: Lakeview dashboards GA and renamed Dashboards in the UI. AI/BI Dashboards announced June 12, 2024 | [[AI-BI Dashboards]] | [Dashboards (AWS)](https://docs.databricks.com/aws/en/dashboards/) |
| **Databricks Data + AI Platform** | Data Intelligence Platform; before that, Lakehouse Platform | Data Intelligence Platform introduced November 15, 2023. Data + AI Platform: date not published | [[The Data Intelligence Platform]] | [Databricks Data + AI Platform product page](https://www.databricks.com/product/data-intelligence-platform) |
| **Data quality monitoring** (data profiling and anomaly detection) | Lakehouse Monitoring (now the data profiling part) | Date not published | [[Data Quality Monitoring]] | [Data quality monitoring (AWS)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/) |
| **MLflow 3 GenAI evaluation** and **production monitoring** | Mosaic AI Agent Evaluation; Lakehouse Monitoring for generative AI | MLflow 3.0 GA on Databricks June 10, 2025. Rename date not published | [[Agent Evaluation and Tracing]] | [Migrate to MLflow 3 from Agent Evaluation (AWS)](https://docs.databricks.com/aws/en/mlflow3/genai/agent-eval-migration) |
| **Supervisor Agent** (now legacy) | Multi-Agent Supervisor | February 5, 2026 | [[Agent Bricks]] | [What is Agent Bricks? (AWS)](https://docs.databricks.com/aws/en/agents/concepts) |
| **Databricks Free Edition** | Databricks Community Edition (replaced, not renamed) | Announced June 11, 2025; Community Edition retired in 2025 | [[Databricks Free Edition and Trials]] | [Introducing Databricks Free Edition (Databricks blog)](https://www.databricks.com/blog/introducing-databricks-free-edition) |
| **Lakebridge** | Remorph (Databricks Labs project) | Announced June 12, 2025. The Remorph lineage is inferred from the repository, not stated on an official page | [[Lakebridge]] | [Introducing Lakebridge (Databricks blog)](https://www.databricks.com/blog/introducing-lakebridge-free-open-data-migration-databricks-sql) |
| **Compute policies** | Cluster policies | Date not published | [[Compute Policies]] | [Create and manage compute policies (AWS)](https://docs.databricks.com/aws/en/admin/clusters/policies) |
| **Serverless usage policies** | Serverless budget policies, budget policies | Budget policies to serverless budget policies: March 19, 2025. Serverless usage policies: date not published | [[Tagging for Chargeback]] | [Attribute usage with serverless usage policies (AWS)](https://docs.databricks.com/aws/en/admin/usage/budget-policies) |
| **Git folders** | Repos, Databricks Repos | March 21, 2024 | [[Git Folders and Workspace Files]] | [Databricks Git folders concepts (Google Cloud)](https://docs.databricks.com/gcp/en/repos/git-folders-concepts) |
| **SQL warehouses** | SQL endpoints | June 23, 2022 | [[SQL Warehouses]] | [SQL warehouse types (AWS)](https://docs.databricks.com/aws/en/compute/sql-warehouse/warehouse-types) |
| **Compute plane** | Data plane | Date not published | [[Control Plane and Compute Plane]] | [High-level architecture (AWS)](https://docs.databricks.com/aws/en/getting-started/high-level-architecture) |
| **Disk cache** | Delta cache, DBIO cache | Date not published | [[Caching]], [[Query Performance and Caching]] | [Optimize performance with caching (Azure)](https://learn.microsoft.com/en-us/azure/databricks/optimizations/disk-cache) |
| **pandas API on Spark** (`pyspark.pandas`) | Koalas | Apache Spark 3.2.0, released October 13, 2021 | [[Pandas]], [[Python for Data]] | [Pandas API on Spark (AWS)](https://docs.databricks.com/aws/en/pandas/pandas-on-spark) |

## Retired, legacy, and replaced products

These products were not renamed. They were retired or moved to legacy status, and another product took over their job.

| Current name | Former names | Changed | Note link | Source |
|---|---|---|---|---|
| **AI Runtime** for training and fine-tuning | Foundation Model Fine-tuning, Mosaic AI Model Training (end of life; the `databricks_genai` package and fine-tuning UI are no longer available) | End-of-life date not published | [[Fine-Tuning]] | [Foundation Model Fine-tuning (EoL) (AWS)](https://docs.databricks.com/aws/en/large-language-models/foundation-model-training/) |
| No single replacement; **serverless forecasting** (Public Preview) covers forecasting | AutoML (removed in Databricks Runtime 18.0 ML; still in 16.4 LTS ML) | Databricks Runtime 18.0 ML: Beta December 9, 2025; GA January 15, 2026 | [[AutoML]] | [Databricks Runtime 18.0 for Machine Learning (GCP)](https://docs.databricks.com/gcp/en/release-notes/runtime/18.0ml) |
| **Genie Agents** (no-code) and **Agent Bricks CLI** with **Agent Runtime** (code-first) | Knowledge Assistant and Supervisor Agent (legacy); Supervisor API (end of life) | Legacy: October 12, 2026. Supervisor API end of life: September 30, 2026 | [[Agent Bricks]] | [October 2026 release notes (AWS)](https://docs.databricks.com/aws/en/release-notes/product/2026/october) |
| **Agent Runtime** with `DurableAgentServer` | MLflow AgentServer, LongRunningAgentServer, agents deployed to Model Serving (legacy) | As of the October 2026 release notes | [[Mosaic AI Agent Framework]] | [October 2026 release notes (AWS)](https://docs.databricks.com/aws/en/release-notes/product/2026/october) |
| **Unity Gateway model provider services** | External model endpoints on Model Serving (legacy) | External model providers in Unity Gateway released July 17, 2026 | [[Unity Gateway]] | [Tutorial: Create external model endpoints (legacy) (AWS)](https://docs.databricks.com/aws/en/machine-learning/foundation-models/external-models-tutorial) |
| **AI/BI dashboards** | Databricks SQL dashboards, now legacy dashboards (end of life) | Support ended April 10, 2025; no longer accessible from January 12, 2026 | [[AI-BI Dashboards]] | [Clone a legacy dashboard to an AI/BI dashboard (AWS)](https://docs.databricks.com/aws/en/dashboards/clone-legacy-to-aibi) |
| **Databricks SQL alerts** (current) | Legacy alerts; `alerts-legacy` CLI command group (deprecated) | New alerts: Beta May 22, 2025; Public Preview November 14, 2025; GA May 14, 2026 | [[SQL Alerts]] | [What are legacy alerts? (AWS)](https://docs.databricks.com/aws/en/sql/user/alerts/legacy) |
| **Databricks CLI** (0.205.0 and above) | Legacy Databricks CLI (0.18 and below, archived) | New CLI: Public Preview June 21, 2023; GA May 21, 2026 | [[Databricks CLI]] | [Legacy Databricks CLI (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/archive/dev-tools/cli/) |
| **Models in Unity Catalog** | Workspace Model Registry (legacy); stages replaced by aliases | Models in Unity Catalog GA October 17, 2023 | [[Models in Unity Catalog]] | [Workspace Model Registry (legacy) (AWS)](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/workspace-model-registry) |

## Cloud provider and partner renames

These names belong to Microsoft, Google, and partner companies, but they appear throughout Databricks docs.

| Current name | Former names | Changed | Note link | Source |
|---|---|---|---|---|
| **Microsoft Entra ID** | Azure Active Directory, Azure AD, AAD | Announced July 11, 2023; rollout from August 15, 2023 | [[Microsoft Entra ID Integration]] | [New name for Azure Active Directory (Microsoft Learn)](https://learn.microsoft.com/en-us/entra/fundamentals/new-name) |
| **Azure Data Lake Storage** | Azure Data Lake Storage Gen2 (ADLS Gen2). Gen1 is retired | Date not published | [[Azure Data Lake Storage]] | [Azure Data Lake Storage overview (Microsoft Learn)](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) |
| **Managed Service for Apache Spark** | Dataproc | April 3, 2026 | [[Apache Hadoop]] | [Managed Service for Apache Spark (Google Cloud)](https://cloud.google.com/products/managed-service-for-apache-spark) |
| **Google Cloud Lakehouse** | BigLake | April 20, 2026 | [[Migrating from Google BigQuery]] | [Enable Google Cloud Lakehouse catalog federation (GCP)](https://docs.databricks.com/gcp/en/query-federation/google-cloud-lakehouse) |
| **dbt platform** | dbt Cloud | May 28, 2025 (dbt Launch Showcase) | [[dbt]], [[dbt on Databricks]] | [dbt platform task for jobs (AWS)](https://docs.databricks.com/aws/en/jobs/tasks/dbt-platform) |
| **Fivetran + dbt Labs** (company) | Fivetran; dbt Labs | Merger announced October 13, 2025; completed June 1, 2026 | [[Fivetran and ELT Tools]], [[dbt]] | [Fivetran + dbt Labs complete merger (dbt Labs)](https://www.getdbt.com/blog/fivetran-dbt-labs-complete-merger-to-create-the-data-infrastructure-for-trusted-ai-agents) |
| **Cloudera** (company) | Cloudera and Hortonworks | Merger announced October 3, 2018; completed January 2019 | [[Cloudera and Hortonworks]] | [Cloudera and Hortonworks merger announcement (SEC)](https://www.sec.gov/Archives/edgar/data/0001610532/000162828018012255/cldr8-k10318ex991.htm) |

## What still uses an old name

A rename usually changes the product name in the UI and docs first. These places keep the old wording, according to the notes:

| Product | Where the old name survives |
|---|---|
| [[Declarative Automation Bundles]] | The `databricks bundle` command and `databricks.yml` files are unchanged. |
| [[Lakeflow Spark Declarative Pipelines]] | Old code with `import dlt` keeps working. New code uses `from pyspark import pipelines as dp`. The open-source core is Apache Spark Declarative Pipelines, part of Spark from version 4.1. |
| [[Change Data Capture]] | `APPLY CHANGES` code still runs. |
| [[Lakeflow Jobs]] | The jobs system tables moved from the `workflow` schema to `lakeflow`, with identical content. |
| [[Git Folders and Workspace Files]] | The REST API (`/api/2.0/repos`) and the `databricks repos` CLI command group. |
| [[AI-BI Dashboards]] | The dashboard REST API path `/api/2.0/lakeview/dashboards`. |
| [[AI Search]] | The SQL function `vector_search()`, some UI labels, doc URLs (`/vector-search/`), and the REST API path. The current Python SDK uses `AISearchClient`. |
| [[Unity Gateway]] | Doc URLs still contain `ai-gateway`. |
| [[OpenSharing]] | Some pages still say Delta Sharing. Doc pages moved from `/delta-sharing/` to `/opensharing/`. |
| [[AI Runtime]] | The deprecated `serverless_gpu` package is replaced by `databricks-sdk-air` from GPU environment version 6. The arguments `gpus` and `gpu_type` become `num_accelerators` and `accelerator_type`. |
| [[Data Quality Monitoring]] | Some doc URLs contain `lakehouse-monitoring`. |
| [[Compute Policies]] | The Terraform resource `databricks_cluster_policy` and parts of the API. |
| [[Tagging for Chargeback]] | Some Google Cloud and older Azure pages still say serverless budget policies. |
| [[Lakebridge]] | The Python package `databricks-labs-remorph` and the `.databricks/labs/remorph-transpilers/` folder. |
| [[Microsoft Entra ID Integration]] | Older Databricks pages, APIs, and error messages, for example "AAD token". |
| [[Genie Code]] | Older docs, blog posts, and admin settings may say Assistant. |

> [!confusion] Genie Code, Genie Agents, and Genie One are three different products
> | Product | Former name | Audience | Job |
> |---|---|---|---|
> | [[Genie Code]] | Databricks Assistant | Engineers, analysts, data scientists | Writes, runs, and fixes code in notebooks and editors |
> | [[Genie Agents]] | Genie spaces | Business users | Answers plain-English questions over curated data |
> | [[Genie One]] | Databricks One | Business users | The simplified home for dashboards, Genie Agents, and apps |

## Vault note titles

Notes are titled with the current product name, and every former name is listed in the note's `aliases`, so a search for an old name finds the right note. The note [[Hive Metastore Federation for AWS Glue]] also carries the alias "AWS Glue and Lake Formation Federation". When a product is renamed, update its note title, its `aliases`, its `[!renamed]` callout, and this page.

## Next steps

- See where each rename falls in history in [[Timeline of Data Engineering]].
- See which Databricks product took over each open-source tool in [[Open Source vs Databricks - Who Replaced What]].

> [!sources]- Sources (last verified: 2026-10-25)
> Every row restates a `[!renamed]` callout, an alias, or a fact from the linked note. Each row's Source column cites the official page that note relies on. Dates in **Changed** were checked on 2026-10-25 against the sources below. Additional sources:
> - [March 2026 release notes (AWS)](https://docs.databricks.com/aws/en/release-notes/product/2026/march)
> - [Genie Code (AWS)](https://docs.databricks.com/aws/en/genie-code/)
> - [Declarative Automation Bundles feature release notes (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/release-notes/dev-tools/bundles)
> - [Use Genie One (AWS)](https://docs.databricks.com/aws/en/genie-one)
> - [Genie Agents (AWS)](https://docs.databricks.com/aws/en/genie-agents)
> - [Unity Gateway: governance layer for agentic AI (Databricks blog)](https://www.databricks.com/blog/ai-gateway-governance-layer-agentic-ai)
> - [Databricks AI Search (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/ai-search/ai-search)
> - [What is the OpenSharing Databricks-to-Databricks protocol? (AWS)](https://docs.databricks.com/aws/en/opensharing/share-data-databricks)
> - [Serverless GPU environment version 6 (AWS)](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/six-gpu)
> - [What happened to Delta Live Tables (DLT)? (Azure)](https://learn.microsoft.com/en-us/azure/databricks/ldp/concepts/where-is-dlt)
> - [Jobs system table reference (AWS)](https://docs.databricks.com/aws/en/admin/system-tables/jobs)
> - [Databricks SQL release notes 2024 (AWS)](https://docs.databricks.com/aws/en/sql/release-notes/2024)
> - [What is a data intelligence platform (Databricks blog)](https://www.databricks.com/blog/what-is-a-data-intelligence-platform)
> - [Data quality monitoring (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/data-quality-monitoring/)
> - [Migrate Community Edition workspaces to Free Edition (AWS)](https://docs.databricks.com/aws/en/getting-started/ce-migration)
> - [Lakebridge repository (Databricks Labs, GitHub)](https://github.com/databrickslabs/lakebridge)
> - [Use tags to attribute and track usage (GCP)](https://docs.databricks.com/gcp/en/admin/account-settings/usage-detail-tags)
> - [Azure Databricks Git folders concepts (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/repos/git-folders-concepts)
> - [Pandas API on Apache Spark 3.2 (Databricks blog)](https://www.databricks.com/blog/2021/10/04/pandas-api-on-upcoming-apache-spark-3-2.html)
> - [alerts-legacy command group (deprecated) (AWS)](https://docs.databricks.com/aws/en/dev-tools/cli/reference/alerts-legacy-commands)
> - [Migrate workflows and models to Unity Catalog (AWS)](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/migrate-to-uc)
> - [Databricks Runtime 16.4 LTS for Machine Learning (AWS)](https://docs.databricks.com/aws/en/release-notes/runtime/16.4lts-ml)
> - [Supervisor API (deprecated) (AWS)](https://docs.databricks.com/aws/en/agents/agent-bricks/supervisor-api)
> - [Guidelines for migrating ADLS Gen1 to Gen2 (Microsoft Learn)](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-migrate-gen1-to-gen2)
> - [Databricks SQL release notes 2022: SQL endpoint renamed SQL warehouse, June 23, 2022 (AWS)](https://docs.databricks.com/aws/en/sql/release-notes/2022)
> - [Databricks SQL release notes 2024: Lakeview dashboards GA and renamed Dashboards, April 18, 2024 (AWS)](https://docs.databricks.com/aws/en/sql/release-notes/2024)
> - [Introducing AI/BI (Databricks blog, June 12, 2024)](https://www.databricks.com/blog/introducing-aibi-intelligent-analytics-real-world-data)
> - [June 2023 release notes: new Databricks CLI in Public Preview, June 21, 2023 (AWS)](https://docs.databricks.com/aws/en/release-notes/product/2023/june)
> - [October 2023 release notes: Models in Unity Catalog GA, October 17, 2023 (AWS)](https://docs.databricks.com/aws/en/release-notes/product/2023/october)
> - [March 2024 release notes: Databricks Repos changed to Git folders, March 21, 2024 (AWS)](https://docs.databricks.com/aws/en/release-notes/product/2024/march)
> - [March 2025 release notes: budget policies renamed serverless budget policies, March 19, 2025 (AWS)](https://docs.databricks.com/aws/en/release-notes/product/2025/march)
> - [May 2025 release notes: new SQL alerts in Beta, May 22, 2025 (AWS)](https://docs.databricks.com/aws/en/release-notes/product/2025/may)
> - [June 2025 release notes: AUTO CDC APIs replace APPLY CHANGES and Databricks Jobs is now Lakeflow Jobs, June 11, 2025; MLflow 3.0 GA, June 10, 2025 (AWS)](https://docs.databricks.com/aws/en/release-notes/product/2025/june)
> - [November 2025 release notes: SQL alerts Public Preview, November 14, 2025 (AWS)](https://docs.databricks.com/aws/en/release-notes/product/2025/november)
> - [December 2025 release notes: Databricks Runtime 18.0 ML Beta, December 9, 2025 (AWS)](https://docs.databricks.com/aws/en/release-notes/product/2025/december)
> - [January 2026 release notes: Databricks Runtime 18.0 GA, January 15, 2026 (AWS)](https://docs.databricks.com/aws/en/release-notes/product/2026/january)
> - [February 2026 release notes: Multi-Agent Supervisor is now Supervisor Agent, February 5, 2026 (AWS)](https://docs.databricks.com/aws/en/release-notes/product/2026/february)
> - [May 2026 release notes: SQL alerts GA, May 14, 2026; Databricks CLI GA, May 21, 2026 (AWS)](https://docs.databricks.com/aws/en/release-notes/product/2026/may)
> - [July 2026 release notes: external model providers in Unity Gateway, July 17, 2026 (AWS)](https://docs.databricks.com/aws/en/release-notes/product/2026/july)
> - [Optimize performance with caching: Delta cache renamed to disk cache (AWS)](https://docs.databricks.com/aws/en/optimizations/disk-cache)
> - [Spark 3.2.0 released, October 13, 2021 (Apache Spark news)](https://spark.apache.org/news/index.html) and [Spark 3.2.0 release notes: Pandas API on Spark](https://spark.apache.org/releases/spark-release-3-2-0.html)
> - [Managed Service for Apache Spark release notes: announcement of April 3, 2026 (Google Cloud)](https://docs.cloud.google.com/managed-spark/docs/release-notes)
> - [What is borderless Lakehouse?: "As of April 20th, 2026, BigLake is now called Lakehouse" (Google Cloud)](https://docs.cloud.google.com/lakehouse/docs/introduction)
> - [Updated names for dbt platform and features (dbt Labs)](https://www.getdbt.com/blog/updated-names-for-dbt-platform-and-features) and [2025 dbt platform release notes: dbt Launch Showcase, May 28, 2025](https://docs.getdbt.com/docs/dbt-versions/2025-release-notes)
