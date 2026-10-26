---
type: hub
status: written
summary: Which notes each persona should read, generated from note frontmatter.
related:
  - "[[Chapter 80 - Learning Paths]]"
  - "[[Who Uses Databricks - Roles]]"
  - "[[Path - Absolute Beginner]]"
  - "[[Path - Business Owner]]"
  - "[[Path - Analyst]]"
  - "[[Path - Data Engineer]]"
  - "[[Path - Data Scientist and ML Engineer]]"
  - "[[Path - AI App Developer]]"
  - "[[Path - Platform Admin]]"
  - "[[Path - One-Person Data Team]]"
  - "[[Path - Certification Prep]]"
  - "[[start_here]]"
last_verified: 2026-10-25
tags:
  - hub
---

# Persona Map

> [!eli5] What this page is
> Different people need different parts of this notebook. A shop owner wants to know what it costs and whether it fits. An engineer wants to know how the pipes work. This page sorts every note by the kind of person it helps most, so you can skip what you do not need.

## What a persona is

A **persona** is a reader type: a job you do, not a person you are. Most people wear more than one hat. The one data person at a small business is an analyst, an engineer, and an admin at the same time, so read more than one section if that is you.

Every concept note lists its personas in its frontmatter (`personas:`). The tables below are built from that field by `scripts/build_index.py`, sorted from beginner (`101`) to expert (`401`). A note tagged for a persona is one that persona will get real value from. It is not a ban on everyone else.

| Persona key | Who it is | Guided path |
|---|---|---|
| `everyone` | Anyone new to data, with no background | [[Path - Absolute Beginner]] |
| `owner` | A business owner or executive deciding on Databricks | [[Path - Business Owner]] |
| `analyst` | An analyst or BI developer who lives in Excel, SQL, or Power BI | [[Path - Analyst]] |
| `engineer` | A data engineer who builds ingestion and pipelines | [[Path - Data Engineer]] |
| `scientist` | A data scientist or ML engineer | [[Path - Data Scientist and ML Engineer]] |
| `ai-dev` | An AI or application developer building agents and apps | [[Path - AI App Developer]] |
| `admin` | A platform or cloud admin who sets up accounts, identity, and networking | [[Path - Platform Admin]], then [[Path - Azure Deep Dive\|Azure]], [[Path - AWS Deep Dive\|AWS]], or [[Path - Google Cloud Deep Dive\|Google Cloud]] |
| `security` | A security, privacy, or compliance lead | [[Path - Platform Admin]] |
| `finance` | Finance or FinOps, who watches the bill | [[Path - Business Owner]], then [[Cost Management Basics]] |
| `solo` | The one-person data team at a small business | [[Path - One-Person Data Team]] |

Studying for an exam? [[Path - Certification Prep]] maps the notes to each Databricks certification.

## How to use the map

1. **Pick your row** in the table above. If you are unsure which job you are doing, [[Who Uses Databricks - Roles]] describes each one.
2. **Prefer the guided path** when one exists. A path is a curated, ordered route. The tables below are the complete list, in depth order, and they are better for filling gaps than for a first read.
3. **Read the 101s first:** Each note's `[!eli5]` block is the one-minute answer, and its collapsed "Going deeper" box holds the expert detail.
4. **Follow the graph:** When a note mentions an idea you do not know, its links and `prereqs` take you back to it. The [[Timeline of Data Engineering]] shows where each tool sits in the story.

> [!info] This table is generated
> Do not edit the persona tables by hand. Change a note's `personas:` frontmatter, then run `python3 scripts/build_index.py`, and the tables below rebuild. Notes still marked `status: stub` appear here too, because the plan is fixed even before every note is written.

<!-- GENERATED:persona-map START (scripts/build_index.py) -->

### Anyone new to data

| Depth | Note | Why |
|---|---|---|
| 101 | [[What Databricks Is in Plain English]] | Databricks in one page, with no jargon, for someone who has never heard of it. |
| 101 | [[Who Uses Databricks - Roles]] | The eight job roles that log in to Databricks, what each one does there, and which tools they use. |
| 101 | [[Databricks Free Edition and Trials]] | The free ways to try Databricks (Free Edition and the 14-day trial), what each one includes, and what it leaves out. |
| 101 | [[What Is Data]] | Data as recorded facts, and why businesses keep it. |
| 101 | [[Structured vs Unstructured Data]] | Tables versus documents, images, audio, and logs, and the semi-structured data in between. |
| 101 | [[Files and File Formats]] | What a file format is and why the choice of format decides how fast and cheap data is to use. |
| 101 | [[CSV and JSON]] | The two most common plain-text data formats and their limits at scale. |
| 101 | [[Spreadsheets]] | Why Excel runs the world, and where it breaks. |
| 101 | [[Relational Databases]] | Tables with rules and relationships, managed by software like Postgres, MySQL, and SQL Server. |
| 101 | [[SQL]] | The language for asking databases questions, and why it is still the most important data skill. |
| 101 | [[Servers and the Cloud]] | Computers you rent by the minute from Microsoft, Amazon, or Google. |
| 101 | [[Storage vs Compute]] | The split between where data sits and what crunches it, the most important idea in modern data. |
| 101 | [[Python for Data]] | Why Python and pandas became the default language for data work. |
| 101 | [[APIs]] | How software talks to other software, and how most SaaS data gets pulled out. |
| 101 | [[The Three Vs of Big Data]] | Volume, velocity, and variety, the three ways data got too big for one machine. |
| 101 | [[Scaling Up vs Scaling Out]] | Buying a bigger computer versus using many small ones. |
| 101 | [[The Pain of Hadoop]] | Why Hadoop clusters became slow, expensive, and hard to staff, which set the stage for Spark and the cloud. |
| 101 | [[AMPLab and the Birth of Spark]] | How a Berkeley research lab built Spark in 2009, and how its creators went on to found Databricks. |
| 101 | [[Apache Spark]] | The open-source engine for processing big data in memory across a cluster. |
| 101 | [[Data Warehouses]] | A database built for analytics, which is clean, fast, and expensive. |
| 101 | [[Data Lakes]] | Dumping every file into cheap storage first and figuring it out later. |
| 101 | [[Object Storage]] | Cheap, effectively unlimited cloud file storage, which is the floor the lakehouse stands on. |
| 101 | [[Data Swamps]] | What a data lake becomes without rules, with no trust, no quality, and no one knowing what is where. |
| 101 | [[The Two-Tier Architecture Problem]] | Running a lake and a warehouse side by side means two copies, two bills, stale data, and no AI on warehouse data. |
| 101 | [[The Lakehouse Idea]] | One copy of data in open files on cheap storage, with warehouse-grade reliability and speed. |
| 101 | [[The Founding of Databricks]] | How Spark's creators started a company in 2013 to run Spark in the cloud. |
| 101 | [[The Data Intelligence Platform]] | Databricks' name for the lakehouse plus AI that understands your data (now often called the Data + AI Platform). |
| 101 | [[Accounts and Workspaces]] | The account is the company, and a workspace is a room where teams work. |
| 101 | [[Compute Types]] | The map of Databricks compute, covering all-purpose, jobs, serverless, and SQL warehouses. |
| 101 | [[Serverless Compute]] | Compute that Databricks runs and scales for you, starting in seconds with no clusters to configure. |
| 101 | [[Notebooks]] | Web documents that mix runnable code cells in Python, SQL, Scala, or R with results, charts, and text. |
| 101 | [[Genie Code]] | The built-in AI coding and data agent, renamed from Databricks Assistant to Genie Code in March 2026. |
| 101 | [[Unity Catalog]] | Databricks' governance layer for permissions, discovery, lineage, and auditing across every workspace. |
| 101 | [[Three-Level Namespace]] | catalog.schema.table, the three-part address of every table, view, volume, function, and model. |
| 101 | [[Catalogs Schemas and Tables]] | The securable objects in Unity Catalog (catalogs, schemas, tables, views, volumes, functions, models) and how to organize them. |
| 101 | [[Catalog Explorer]] | The Unity Catalog UI for browsing, searching, and managing data and AI assets and their permissions. |
| 101 | [[Machine Learning Basics]] | Teaching software from examples, covering training, models, features, labels, and predictions, and where each step lives in Databricks. |
| 101 | [[Generative AI and LLMs]] | What large language models are, why they need your business data to be useful, and the Databricks tools for each way of using them. |
| 101 | [[AI Playground]] | A no-code chat UI in the workspace for trying, comparing, and prototyping LLMs and simple tool-calling agents. |
| 101 | [[Azure Databricks Overview]] | What is different when Databricks is sold, billed, and run as a Microsoft Azure service. |
| 101 | [[Databricks on AWS Overview]] | How Databricks runs on AWS, sold by Databricks directly or through AWS Marketplace. |
| 101 | [[Databricks on Google Cloud Overview]] | How Databricks runs on Google Cloud, sold through Google Cloud Marketplace, and what is different there. |
| 101 | [[Path - Absolute Beginner]] | Zero to "I get what Databricks is" in about 20 notes. |

### Business owner or executive

| Depth | Note | Why |
|---|---|---|
| 101 | [[What Databricks Is in Plain English]] | Databricks in one page, with no jargon, for someone who has never heard of it. |
| 101 | [[Who Uses Databricks - Roles]] | The eight job roles that log in to Databricks, what each one does there, and which tools they use. |
| 101 | [[Who Uses Databricks - Business Types]] | Kinds of businesses, from e-commerce to clinics to factories, that get real value from Databricks, with example use cases. |
| 101 | [[Signs You Have Outgrown Spreadsheets]] | The warning signs that a business needs a real data platform instead of Excel, Access, or one reporting tool. |
| 101 | [[When Databricks Is Not the Right Fit]] | An honest list of situations where a simpler or cheaper tool is the better choice. |
| 101 | [[How Databricks Pricing Works]] | DBUs, SKUs, serverless versus classic, committed use, and why there are usually two bills. |
| 101 | [[Choosing a Cloud for Databricks]] | How to pick Azure, AWS, or Google Cloud, based mostly on what the business already uses. |
| 101 | [[Your First 30 Days on Databricks]] | A week-by-week plan from sign-up to the first trusted dashboard. |
| 101 | [[The Pain of Hadoop]] | Why Hadoop clusters became slow, expensive, and hard to staff, which set the stage for Spark and the cloud. |
| 101 | [[Data Swamps]] | What a data lake becomes without rules, with no trust, no quality, and no one knowing what is where. |
| 101 | [[BI Tools]] | Power BI, Tableau, Looker, and similar tools that turn tables into dashboards and reports. |
| 101 | [[The Two-Tier Architecture Problem]] | Running a lake and a warehouse side by side means two copies, two bills, stale data, and no AI on warehouse data. |
| 101 | [[The Lakehouse Idea]] | One copy of data in open files on cheap storage, with warehouse-grade reliability and speed. |
| 101 | [[The Founding of Databricks]] | How Spark's creators started a company in 2013 to run Spark in the cloud. |
| 101 | [[The Data Intelligence Platform]] | Databricks' name for the lakehouse plus AI that understands your data (now often called the Data + AI Platform). |
| 101 | [[DBUs]] | The Databricks Unit (DBU), a normalized unit of processing power per hour that Databricks usage is measured and priced in. |
| 101 | [[Databricks SQL]] | Databricks' data warehouse experience, with SQL warehouses, editor, dashboards, and alerts. |
| 101 | [[AI-BI Dashboards]] | Databricks' native dashboards (formerly Lakeview), built on SQL warehouses with AI-assisted authoring and shareable across the account. |
| 101 | [[Genie Agents]] | Genie Agents (formerly Genie spaces) answer plain-English questions about governed data with SQL, tables, and charts. |
| 101 | [[Genie One]] | Genie One (formerly Databricks One), the simplified business-user home for dashboards, Genie Agents, and apps. |
| 101 | [[Generative AI and LLMs]] | What large language models are, why they need your business data to be useful, and the Databricks tools for each way of using them. |
| 101 | [[Agent Bricks]] | Databricks' agent platform, launched in 2025 for building agents from a task description and refocused in 2026 on code-first agents with the Agent Bricks CLI and Agent Runtime. |
| 101 | [[Azure Databricks Overview]] | What is different when Databricks is sold, billed, and run as a Microsoft Azure service. |
| 101 | [[Databricks on AWS Overview]] | How Databricks runs on AWS, sold by Databricks directly or through AWS Marketplace. |
| 101 | [[Databricks on Google Cloud Overview]] | How Databricks runs on Google Cloud, sold through Google Cloud Marketplace, and what is different there. |
| 101 | [[Cost Management Basics]] | Where Databricks spend comes from, how it is metered, and the first five controls to set. |
| 101 | [[Migration Strategy Overview]] | The phases of every migration, from assess and plan to coexist, ingest, convert, validate, switch over, and decommission. |
| 101 | [[Migrating from Excel and Access]] | Moving a spreadsheet-run business into governed tables, with file uploads, Volumes, a first dashboard, and Genie Agents. |
| 101 | [[Migration Checklist]] | A printable, start-to-finish checklist for a small business migration. |
| 101 | [[Path - Business Owner]] | Everything a decision-maker needs, covering fit, cost, risk, and the first 30 days. |
| 201 | [[Databricks vs Alternatives for Small Teams]] | How Databricks compares with Snowflake, BigQuery, Microsoft Fabric, Power BI alone, and plain Postgres for a small team. |
| 201 | [[Estimating Costs for a Small Business]] | A worked, back-of-the-envelope monthly cost estimate for a small company's first workloads. |
| 201 | [[Building a Business Case]] | How to justify Databricks to a boss or a board, covering costs, savings, risks, and a proof of concept. |
| 201 | [[Cloudera and Hortonworks]] | The companies that sold supported Hadoop, and why they merged in 2019. |
| 201 | [[Snowflake]] | The cloud warehouse that separated storage and compute, and Databricks' best-known rival. |
| 201 | [[Serverless Workspaces and Default Storage]] | Workspaces that run only on serverless compute and store data in Databricks-managed default storage, so you supply no cloud storage, credentials, or network. |
| 201 | [[OpenSharing]] | The open protocol, formerly Delta Sharing, for sharing live data and AI assets with anyone, on Databricks or not, without copying. |
| 201 | [[Databricks Marketplace]] | An open marketplace for finding and getting datasets, ML models, and other data products from providers, delivered through OpenSharing. |
| 201 | [[SQL Alerts]] | Databricks SQL alerts run a query on a schedule and send an email, Slack, or Teams message when a value crosses a threshold. |
| 201 | [[Retrieval-Augmented Generation]] | Giving an LLM your documents at question time so it answers from facts, built on Databricks with document parsing, AI Search, and MLflow evaluation. |
| 201 | [[MosaicML and Open Models]] | Databricks' 2023 MosaicML acquisition, the MPT and DBRX open models, and how that technology lives on in hosted models, serving, and AI Runtime. |
| 201 | [[First-Party Microsoft Service]] | Microsoft provisioning, billing, and support, and why Azure Databricks is unusual among Databricks clouds. |
| 201 | [[Microsoft Fabric and OneLake vs Databricks]] | How Microsoft Fabric and Azure Databricks overlap, how to choose between them, and how mirroring and OneLake federation connect them. |
| 201 | [[Azure Billing and Commit Units]] | Pay-as-you-go billing on the Azure invoice, Databricks commit unit (DBCU) prepurchase plans, and Azure and Databricks cost tools. |
| 201 | [[AWS Marketplace and Billing]] | Paying Databricks directly or through AWS Marketplace, and where the EC2, EBS, S3, and networking costs of classic compute appear. |
| 201 | [[Google Cloud Marketplace and Billing]] | Paying for Databricks through a Google Cloud Marketplace subscription on the Google Cloud bill, and where Compute Engine and storage costs appear. |
| 201 | [[Assessing Your Current Data Estate]] | Taking inventory of sources, tables, jobs, reports, users, and costs before moving anything. |
| 201 | [[Running Old and New in Parallel]] | Parallel runs, reconciliation with Lakebridge and SQL, and a safe switch-over and rollback plan. |
| 301 | [[Clean Rooms]] | A governed, serverless environment where up to ten organizations run approved analysis on combined data without seeing each other's raw records. |
| 301 | [[Migrating from Snowflake]] | A Snowflake-to-Databricks playbook covering federation, Iceberg-based coexistence, data unloads, SQL conversion with Lakebridge, and reconciliation. |

### Analyst or BI developer

| Depth | Note | Why |
|---|---|---|
| 101 | [[Signs You Have Outgrown Spreadsheets]] | The warning signs that a business needs a real data platform instead of Excel, Access, or one reporting tool. |
| 101 | [[Spreadsheets]] | Why Excel runs the world, and where it breaks. |
| 101 | [[SQL]] | The language for asking databases questions, and why it is still the most important data skill. |
| 101 | [[Primary and Foreign Keys]] | How rows get IDs and how tables point at each other. |
| 101 | [[ETL vs ELT]] | Extract, transform, load, and why the order flipped in the cloud. |
| 101 | [[DataFrames]] | Tables in code, with named columns and types, the main way people use Spark today. |
| 101 | [[Spark SQL]] | Running SQL on Spark, the bridge from Hive to Databricks SQL. |
| 101 | [[Data Warehouses]] | A database built for analytics, which is clean, fast, and expensive. |
| 101 | [[BI Tools]] | Power BI, Tableau, Looker, and similar tools that turn tables into dashboards and reports. |
| 101 | [[Delta Lake]] | Databricks' open-source table format and the default for every table on the platform. |
| 101 | [[Medallion Architecture]] | Bronze (raw), silver (cleaned), and gold (business-ready) layers of tables. |
| 101 | [[SQL Warehouses]] | Compute built for SQL queries, dashboards, and BI tools, in serverless, pro, and classic types. |
| 101 | [[Genie Code]] | The built-in AI coding and data agent, renamed from Databricks Assistant to Genie Code in March 2026. |
| 101 | [[Three-Level Namespace]] | catalog.schema.table, the three-part address of every table, view, volume, function, and model. |
| 101 | [[Catalogs Schemas and Tables]] | The securable objects in Unity Catalog (catalogs, schemas, tables, views, volumes, functions, models) and how to organize them. |
| 101 | [[Catalog Explorer]] | The Unity Catalog UI for browsing, searching, and managing data and AI assets and their permissions. |
| 101 | [[Lakeflow Designer]] | A no-code, drag-and-drop pipeline builder with AI help. |
| 101 | [[Databricks SQL]] | Databricks' data warehouse experience, with SQL warehouses, editor, dashboards, and alerts. |
| 101 | [[SQL Editor]] | Writing, running, and sharing queries in the browser. |
| 101 | [[AI-BI Dashboards]] | Databricks' native dashboards (formerly Lakeview), built on SQL warehouses with AI-assisted authoring and shareable across the account. |
| 101 | [[Genie Agents]] | Genie Agents (formerly Genie spaces) answer plain-English questions about governed data with SQL, tables, and charts. |
| 101 | [[Genie One]] | Genie One (formerly Databricks One), the simplified business-user home for dashboards, Genie Agents, and apps. |
| 101 | [[AutoML]] | Letting Databricks train and compare models for you and hand back notebooks, now removed from Databricks Runtime 18.0 ML onward. |
| 101 | [[AI Playground]] | A no-code chat UI in the workspace for trying, comparing, and prototyping LLMs and simple tool-calling agents. |
| 101 | [[Migrating from Excel and Access]] | Moving a spreadsheet-run business into governed tables, with file uploads, Volumes, a first dashboard, and Genie Agents. |
| 101 | [[Path - Analyst]] | From Excel and SQL to Databricks SQL, dashboards, Genie Agents, and Power BI. |
| 201 | [[Databricks vs Alternatives for Small Teams]] | How Databricks compares with Snowflake, BigQuery, Microsoft Fabric, Power BI alone, and plain Postgres for a small team. |
| 201 | [[OLTP vs OLAP]] | Systems that run the business versus systems that analyze it. |
| 201 | [[Data Modeling Basics]] | Deciding which tables to have and how they connect, covering normalization, entities, and grain. |
| 201 | [[Star Schema]] | Fact and dimension tables, the classic shape for analytics. |
| 201 | [[Apache Hive]] | SQL on Hadoop, which made big data queryable by analysts. |
| 201 | [[Columnar Storage]] | Storing data column by column so analytics reads only what it needs. |
| 201 | [[Amazon Redshift]] | AWS's cloud data warehouse, previewed in 2012 and generally available in 2013. |
| 201 | [[Snowflake]] | The cloud warehouse that separated storage and compute, and Databricks' best-known rival. |
| 201 | [[Google BigQuery]] | Google's serverless warehouse, where you run SQL without sizing or managing any servers. |
| 201 | [[dbt]] | SQL transformations with software engineering habits like version control and tests. |
| 201 | [[Time Travel]] | Querying a table as it was yesterday, and undoing mistakes. |
| 201 | [[Data Lineage]] | An automatic, column-level map of where every table and column came from and where it goes, captured by Unity Catalog at runtime. |
| 201 | [[Lakehouse Federation]] | Querying Postgres, SQL Server, Snowflake, BigQuery, and other databases and catalogs in place through Unity Catalog, without copying. |
| 201 | [[Databricks Marketplace]] | An open marketplace for finding and getting datasets, ML models, and other data products from providers, delivered through OpenSharing. |
| 201 | [[Unity Catalog Functions]] | SQL and Python functions registered in Unity Catalog, governed and reusable across queries, policies, agents, and tools. |
| 201 | [[COPY INTO]] | The simple SQL command for loading files into a table once. |
| 201 | [[Materialized Views]] | Precomputed query results that refresh incrementally. |
| 201 | [[dbt on Databricks]] | Running dbt projects against Databricks SQL, and as job tasks. |
| 201 | [[SQL Alerts]] | Databricks SQL alerts run a query on a schedule and send an email, Slack, or Teams message when a value crosses a threshold. |
| 201 | [[Connecting Power BI]] | Live and import connections from Power BI to Databricks, and publishing from Unity Catalog. |
| 201 | [[Connecting Tableau and Other BI Tools]] | Tableau, Looker, Sigma, Excel, and anything with JDBC or ODBC. |
| 201 | [[AI Functions in SQL]] | Calling LLMs from plain SQL to classify, summarize, extract, and translate. |
| 201 | [[VARIANT Data Type]] | The VARIANT data type stores JSON-like semi-structured data in an efficient binary form that you query with path expressions. |
| 201 | [[Microsoft Fabric and OneLake vs Databricks]] | How Microsoft Fabric and Azure Databricks overlap, how to choose between them, and how mirroring and OneLake federation connect them. |
| 201 | [[Power BI on Azure Databricks]] | Entra single sign-on from Power BI, the ADBC driver, publishing semantic models from Unity Catalog, and DirectQuery guidance. |
| 201 | [[BigQuery Integration]] | Reading and writing BigQuery with the Spark connector, and querying it in place through Lakehouse Federation. |
| 201 | [[Migrating BI Reports]] | Repointing Power BI and Tableau reports to Databricks SQL warehouses, or rebuilding them as AI/BI dashboards and Genie agents. |
| 301 | [[Slowly Changing Dimensions]] | SCD type 1 and type 2, which decide whether to keep history when a customer moves. |
| 301 | [[Query Performance and Caching]] | Query profiles, result and disk caches, and why a query is slow. |
| 301 | [[Metric Views]] | Defining a business metric once in Unity Catalog so every tool computes it the same way. |
| 301 | [[SQL Scripting and Stored Procedures]] | Variables, control flow, error handling, and reusable stored procedures in Databricks SQL, for porting procedural warehouse logic. |
| 301 | [[Path - Certification Prep]] | Which Databricks certifications exist and which notes map to each exam. |

### Data engineer

| Depth | Note | Why |
|---|---|---|
| 101 | [[Your First 30 Days on Databricks]] | A week-by-week plan from sign-up to the first trusted dashboard. |
| 101 | [[Primary and Foreign Keys]] | How rows get IDs and how tables point at each other. |
| 101 | [[Python for Data]] | Why Python and pandas became the default language for data work. |
| 101 | [[APIs]] | How software talks to other software, and how most SaaS data gets pulled out. |
| 101 | [[ETL vs ELT]] | Extract, transform, load, and why the order flipped in the cloud. |
| 101 | [[Batch vs Streaming]] | Processing data in scheduled chunks versus continuously as it arrives. |
| 101 | [[Scaling Up vs Scaling Out]] | Buying a bigger computer versus using many small ones. |
| 101 | [[Apache Hadoop]] | The open-source system that let ordinary companies store and process huge data on cheap machines. |
| 101 | [[Apache Spark]] | The open-source engine for processing big data in memory across a cluster. |
| 101 | [[DataFrames]] | Tables in code, with named columns and types, the main way people use Spark today. |
| 101 | [[Spark SQL]] | Running SQL on Spark, the bridge from Hive to Databricks SQL. |
| 101 | [[PySpark]] | Spark from Python, the interface most data teams use. |
| 101 | [[Data Lakes]] | Dumping every file into cheap storage first and figuring it out later. |
| 101 | [[Object Storage]] | Cheap, effectively unlimited cloud file storage, which is the floor the lakehouse stands on. |
| 101 | [[Amazon S3]] | AWS object storage, launched in 2006, the original cloud data lake. |
| 101 | [[Azure Data Lake Storage]] | Azure's object storage built for analytics, Blob Storage with a hierarchical namespace (formerly ADLS Gen2). |
| 101 | [[Google Cloud Storage]] | Google Cloud's object storage, addressed as gs://bucket/path. |
| 101 | [[Delta Lake]] | Databricks' open-source table format and the default for every table on the platform. |
| 101 | [[Medallion Architecture]] | Bronze (raw), silver (cleaned), and gold (business-ready) layers of tables. |
| 101 | [[Notebooks]] | Web documents that mix runnable code cells in Python, SQL, Scala, or R with results, charts, and text. |
| 101 | [[Genie Code]] | The built-in AI coding and data agent, renamed from Databricks Assistant to Genie Code in March 2026. |
| 101 | [[Three-Level Namespace]] | catalog.schema.table, the three-part address of every table, view, volume, function, and model. |
| 101 | [[Lakeflow]] | Databricks' umbrella for ingestion (Connect), transformation (Pipelines), and orchestration (Jobs). |
| 101 | [[Lakeflow Connect]] | Managed connectors for Salesforce, SQL Server, Google Analytics, and other common sources. |
| 101 | [[Lakeflow Jobs]] | Databricks' built-in orchestrator for scheduled multi-task workflows (formerly Workflows). |
| 101 | [[Migration Strategy Overview]] | The phases of every migration, from assess and plan to coexist, ingest, convert, validate, switch over, and decommission. |
| 101 | [[Migration Checklist]] | A printable, start-to-finish checklist for a small business migration. |
| 201 | [[OLTP vs OLAP]] | Systems that run the business versus systems that analyze it. |
| 201 | [[Data Modeling Basics]] | Deciding which tables to have and how they connect, covering normalization, entities, and grain. |
| 201 | [[Star Schema]] | Fact and dimension tables, the classic shape for analytics. |
| 201 | [[Distributed Systems]] | Many computers acting as one, and the new failure modes that come with it. |
| 201 | [[Google File System and MapReduce Papers]] | The 2003 and 2004 Google papers that started the big data era. |
| 201 | [[HDFS]] | Hadoop's distributed file system, which splits files into replicated blocks across many machines. |
| 201 | [[MapReduce]] | Hadoop's map-then-reduce processing model, which was powerful, slow, and painful to write. |
| 201 | [[Apache Hive]] | SQL on Hadoop, which made big data queryable by analysts. |
| 201 | [[Hive Metastore]] | The table directory Hive introduced, which Spark and early Databricks inherited. |
| 201 | [[Cloudera and Hortonworks]] | The companies that sold supported Hadoop, and why they merged in 2019. |
| 201 | [[Columnar Storage]] | Storing data column by column so analytics reads only what it needs. |
| 201 | [[Apache Parquet]] | The open columnar file format underneath Delta Lake, Iceberg, and most of the lakehouse. |
| 201 | [[Lazy Evaluation]] | Why Spark plans the whole job before running any of it. |
| 201 | [[Transformations and Actions]] | The two kinds of Spark operations, ones that describe work and ones that trigger it. |
| 201 | [[Driver and Executors]] | The boss process and the worker processes in every Spark cluster. |
| 201 | [[Partitions]] | How Spark slices data so many machines can work on it at once. |
| 201 | [[Structured Streaming]] | Spark's engine for treating a live stream like a table that keeps growing. |
| 201 | [[Spark UI]] | The built-in web interface for seeing what a Spark application did and why it was slow. |
| 201 | [[Pandas API on Spark]] | The pandas API on Spark (pyspark.pandas, formerly Koalas) runs pandas-style code on Spark so it scales past one machine's memory. |
| 201 | [[Amazon Redshift]] | AWS's cloud data warehouse, previewed in 2012 and generally available in 2013. |
| 201 | [[Snowflake]] | The cloud warehouse that separated storage and compute, and Databricks' best-known rival. |
| 201 | [[Google BigQuery]] | Google's serverless warehouse, where you run SQL without sizing or managing any servers. |
| 201 | [[Apache Kafka]] | The event-streaming backbone that moves live data between systems. |
| 201 | [[Apache Airflow]] | The open-source scheduler that runs pipelines as DAGs written in Python. |
| 201 | [[dbt]] | SQL transformations with software engineering habits like version control and tests. |
| 201 | [[Fivetran and ELT Tools]] | Managed connectors that copy SaaS and database data into a warehouse or lakehouse. |
| 201 | [[ACID Transactions]] | The four guarantees that stop half-written, conflicting, or lost data. |
| 201 | [[Open Table Formats]] | A metadata layer over Parquet files that turns a folder into a real table. |
| 201 | [[Time Travel]] | Querying a table as it was yesterday, and undoing mistakes. |
| 201 | [[Schema Enforcement and Evolution]] | Rejecting bad columns, and safely adding new ones. |
| 201 | [[MERGE and Upserts]] | Insert-or-update in one statement, the workhorse of incremental pipelines. |
| 201 | [[Apache Iceberg]] | The Netflix-born table format, Delta's main rival, now first-class in Unity Catalog. |
| 201 | [[Predictive Optimization]] | Databricks automatically running OPTIMIZE, VACUUM, and statistics collection on Unity Catalog managed tables. |
| 201 | [[Databricks Runtime]] | The tuned Spark plus libraries image every classic cluster boots, and its LTS versions. |
| 201 | [[All-Purpose Compute]] | Interactive clusters for notebooks and exploration, which you create, share, and must remember to stop. |
| 201 | [[Jobs Compute]] | Clusters that spin up for one scheduled job and then disappear, at a lower price. |
| 201 | [[Git Folders and Workspace Files]] | Git folders sync workspace code with GitHub, GitLab, Bitbucket, Azure DevOps, or CodeCommit; workspace files store code beside notebooks. |
| 201 | [[Databricks CLI]] | The `databricks` command-line tool for scripting workspaces and accounts, authenticating, and deploying bundles. |
| 201 | [[Libraries and Environments]] | How to install Python, JAR, and R packages and pin dependencies with notebook-scoped libraries, compute-scoped libraries, and serverless environments. |
| 201 | [[dbutils and Widgets]] | The Databricks Utilities (dbutils) library for files, secrets, notebook chaining, and job task values, and widgets for notebook parameters. |
| 201 | [[DBFS]] | The legacy Databricks File System (DBFS root and mounts), why it is deprecated, and how Unity Catalog volumes, external locations, and workspace files replace it. |
| 201 | [[Managed vs External Tables]] | Who owns the files, and what happens when you drop a table. Managed is the default and recommended choice. |
| 201 | [[Volumes]] | Governed folders for non-table files like CSVs, images, PDFs, and model artifacts, addressed as /Volumes/catalog/schema/volume. |
| 201 | [[Data Lineage]] | An automatic, column-level map of where every table and column came from and where it goes, captured by Unity Catalog at runtime. |
| 201 | [[Lakehouse Federation]] | Querying Postgres, SQL Server, Snowflake, BigQuery, and other databases and catalogs in place through Unity Catalog, without copying. |
| 201 | [[OpenSharing]] | The open protocol, formerly Delta Sharing, for sharing live data and AI assets with anyone, on Databricks or not, without copying. |
| 201 | [[Unity Catalog Functions]] | SQL and Python functions registered in Unity Catalog, governed and reusable across queries, policies, agents, and tools. |
| 201 | [[Auto Loader]] | Incrementally ingesting new files as they land in cloud storage. |
| 201 | [[COPY INTO]] | The simple SQL command for loading files into a table once. |
| 201 | [[Lakeflow Spark Declarative Pipelines]] | Declaring the tables you want and letting Databricks run, retry, and track the pipeline (formerly Delta Live Tables). |
| 201 | [[Streaming Tables]] | Tables that keep themselves up to date from a stream or growing source. |
| 201 | [[Materialized Views]] | Precomputed query results that refresh incrementally. |
| 201 | [[Expectations and Data Quality]] | Rules on your data that warn, drop, or stop the pipeline when broken. |
| 201 | [[Tasks Triggers and Schedules]] | Task types, dependencies, file-arrival and table-update triggers, and retries. |
| 201 | [[dbt on Databricks]] | Running dbt projects against Databricks SQL, and as job tasks. |
| 201 | [[Partner Connect]] | Guided connections to Fivetran, dbt, Power BI, Tableau, Sigma, and other partners that provision the warehouse, service principal, and token for you. |
| 201 | [[VARIANT Data Type]] | The VARIANT data type stores JSON-like semi-structured data in an efficient binary form that you query with path expressions. |
| 201 | [[Azure Data Factory with Databricks]] | Calling Azure Databricks from Azure Data Factory pipelines with the Job and Notebook activities, and when to use Lakeflow Jobs instead. |
| 201 | [[BigQuery Integration]] | Reading and writing BigQuery with the Spark connector, and querying it in place through Lakehouse Federation. |
| 201 | [[Secrets Management]] | Keeping passwords and keys out of notebooks with secret scopes, and the newer secrets in Unity Catalog. |
| 201 | [[Assessing Your Current Data Estate]] | Taking inventory of sources, tables, jobs, reports, users, and costs before moving anything. |
| 201 | [[Migrating from SQL Server]] | Moving off an on-premises or Azure SQL Server, using federation first, Lakeflow Connect replication after, and Lakebridge for T-SQL. |
| 201 | [[Migrating from Postgres and MySQL]] | Moving app-database analytics from PostgreSQL or MySQL into the lakehouse without slowing the app down. |
| 201 | [[Running Old and New in Parallel]] | Parallel runs, reconciliation with Lakebridge and SQL, and a safe switch-over and rollback plan. |
| 201 | [[Path - Data Engineer]] | Ingestion, the lakehouse, pipelines, orchestration, and CI/CD. |
| 301 | [[YARN]] | Hadoop's resource manager, which decides which job gets which machines. |
| 301 | [[Apache HBase]] | A fast key-value database on top of HDFS, modeled after Google Bigtable. |
| 301 | [[Apache ORC]] | Hive's columnar format, Parquet's sibling and rival. |
| 301 | [[RDDs]] | Resilient distributed datasets, Spark's original low-level building block. |
| 301 | [[Catalyst Optimizer]] | The query planner that rewrites your SQL and DataFrame code into a faster plan. |
| 301 | [[Shuffles]] | Moving data between machines, the most expensive thing Spark does. |
| 301 | [[Jobs Stages and Tasks]] | How Spark breaks one query into jobs, stages, and tasks you can see in the Spark UI. |
| 301 | [[Adaptive Query Execution]] | Spark re-planning a query during execution based on runtime statistics. |
| 301 | [[Spark Connect]] | The client-server protocol that lets thin clients run Spark DataFrame code on a remote Spark server. |
| 301 | [[The Lakehouse Paper]] | The 2021 CIDR paper that named and argued for the lakehouse. |
| 301 | [[Delta Transaction Log]] | The _delta_log folder of JSON commits that makes Delta Lake transactional. |
| 301 | [[Apache Hudi]] | The Uber-born table format focused on upserts and incremental processing. |
| 301 | [[Delta UniForm]] | Writing Delta tables that Iceberg readers can also read. |
| 301 | [[Liquid Clustering]] | Self-organizing data layout that replaced partitioning and Z-ordering for most tables. |
| 301 | [[Change Data Feed]] | A row-level log of what changed in a Delta table, for downstream incremental processing. |
| 301 | [[OPTIMIZE and VACUUM]] | Compacting small files and deleting old ones, and Predictive Optimization doing it for you. |
| 301 | [[Photon]] | Databricks' C++ query engine that speeds up SQL and DataFrame work. |
| 301 | [[Declarative Automation Bundles]] | Infrastructure as code for jobs, pipelines, and apps, defined as YAML in Git and deployed with `databricks bundle` (formerly Databricks Asset Bundles). |
| 301 | [[Databricks SDKs and REST API]] | Programmatic control of Databricks through the REST API and the official SDKs for Python, Java, Go, and JavaScript (plus an R SDK from Databricks Labs). |
| 301 | [[Databricks Connect]] | A client library, built on Spark Connect, that runs Spark code from your local IDE on Databricks clusters or serverless compute. |
| 301 | [[Instance Pools]] | Sets of idle, ready-to-use cloud VMs that classic clusters draw from to cut start and autoscaling time. |
| 301 | [[Init Scripts]] | Shell scripts that run on each classic cluster node at startup, the cluster-scoped and global types, and where to store them safely. |
| 301 | [[Hive Metastore Migration to Unity Catalog]] | Upgrading older workspaces from the legacy Hive metastore to Unity Catalog with federation, SYNC, CLONE, and the UCX utilities. |
| 301 | [[Service Credentials]] | Unity Catalog objects that let code reach cloud services other than storage, such as queues or secret stores, without handling keys. |
| 301 | [[Change Data Capture]] | Copying only what changed in a source database, with AUTO CDC. |
| 301 | [[Slowly Changing Dimensions]] | SCD type 1 and type 2, which decide whether to keep history when a customer moves. |
| 301 | [[Structured Streaming on Databricks]] | Running Spark streams on Databricks, covering Kafka sources, checkpoints, and real-time mode. |
| 301 | [[CI-CD for Data Pipelines]] | Dev, staging, and prod, with tests and automated deployment for data code. |
| 301 | [[Testing Data Pipelines]] | Unit tests, data tests, and expectations for code that moves data. |
| 301 | [[Query Performance and Caching]] | Query profiles, result and disk caches, and why a query is slow. |
| 301 | [[Metric Views]] | Defining a business metric once in Unity Catalog so every tool computes it the same way. |
| 301 | [[Lakebase]] | A managed Postgres database (OLTP) inside the lakehouse, for apps and agents, generally available since January 22, 2026. |
| 301 | [[SQL Scripting and Stored Procedures]] | Variables, control flow, error handling, and reusable stored procedures in Databricks SQL, for porting procedural warehouse logic. |
| 301 | [[Data Quality Monitoring]] | Watching tables and model inputs for freshness, completeness, and drift with anomaly detection and data profiling (formerly Lakehouse Monitoring). |
| 301 | [[ADLS and Access Connectors]] | How Unity Catalog reaches ADLS Gen2 through an Access Connector's managed identity, including storage behind firewalls. |
| 301 | [[Azure Key Vault Secret Scopes]] | Using Azure Key Vault as the read-only backing store for a Databricks secret scope, with its permission model and limits. |
| 301 | [[Instance Profiles]] | The legacy way clusters got S3 access by attaching an IAM role to EC2 nodes, and why Unity Catalog replaced it. |
| 301 | [[S3 Access via Unity Catalog]] | Storage credentials backed by self-assuming IAM roles, plus external locations, for governed S3 access. |
| 301 | [[GCS Access via Unity Catalog]] | Storage credentials backed by Databricks-generated Google service accounts, plus external locations, for governed GCS access. |
| 301 | [[Authentication - Tokens and OAuth]] | Personal access tokens versus OAuth (U2M, M2M, and token federation) for scripts, tools, and automation. |
| 301 | [[Migrating from Snowflake]] | A Snowflake-to-Databricks playbook covering federation, Iceberg-based coexistence, data unloads, SQL conversion with Lakebridge, and reconciliation. |
| 301 | [[Migrating from Amazon Redshift]] | A Redshift-to-Databricks playbook covering federation, UNLOAD to S3 as Parquet, SQL conversion with Lakebridge, and switch-over. |
| 301 | [[Migrating from Google BigQuery]] | A BigQuery-to-Databricks playbook covering Storage API federation, EXPORT DATA to Cloud Storage, SQL conversion, and reconciliation. |
| 301 | [[Migrating from Hadoop]] | Moving HDFS data, Hive tables, Spark jobs, and Oozie workflows off an on-premises Hadoop cluster into Databricks. |
| 301 | [[Migrating ETL Tools]] | Converting SSIS, DataStage, Informatica, Talend, Airflow, and stored procedures into Databricks notebooks, SQL, pipelines, and jobs. |
| 301 | [[Lakebridge]] | Databricks' free migration toolkit for profiling, SQL conversion, and data reconciliation. |
| 301 | [[Path - Certification Prep]] | Which Databricks certifications exist and which notes map to each exam. |
| 401 | [[Tungsten]] | Spark's memory-management and code-generation engine work, the precursor to Photon. |
| 401 | [[Deletion Vectors]] | Marking rows deleted instead of rewriting whole files. |
| 401 | [[Hive Metastore Federation for AWS Glue]] | Governing and reading tables registered in the AWS Glue Data Catalog from Unity Catalog through catalog federation. |

### Data scientist or ML engineer

| Depth | Note | Why |
|---|---|---|
| 101 | [[Python for Data]] | Why Python and pandas became the default language for data work. |
| 101 | [[DataFrames]] | Tables in code, with named columns and types, the main way people use Spark today. |
| 101 | [[PySpark]] | Spark from Python, the interface most data teams use. |
| 101 | [[Notebooks]] | Web documents that mix runnable code cells in Python, SQL, Scala, or R with results, charts, and text. |
| 101 | [[Machine Learning Basics]] | Teaching software from examples, covering training, models, features, labels, and predictions, and where each step lives in Databricks. |
| 101 | [[MLflow]] | The open-source platform for tracking, packaging, evaluating, tracing, and deploying ML models and GenAI agents, managed on Databricks. |
| 101 | [[AutoML]] | Letting Databricks train and compare models for you and hand back notebooks, now removed from Databricks Runtime 18.0 ML onward. |
| 201 | [[Lazy Evaluation]] | Why Spark plans the whole job before running any of it. |
| 201 | [[Transformations and Actions]] | The two kinds of Spark operations, ones that describe work and ones that trigger it. |
| 201 | [[MLlib]] | Spark's built-in library for distributed machine learning on DataFrames. |
| 201 | [[Pandas API on Spark]] | The pandas API on Spark (pyspark.pandas, formerly Koalas) runs pandas-style code on Spark so it scales past one machine's memory. |
| 201 | [[Databricks Runtime]] | The tuned Spark plus libraries image every classic cluster boots, and its LTS versions. |
| 201 | [[All-Purpose Compute]] | Interactive clusters for notebooks and exploration, which you create, share, and must remember to stop. |
| 201 | [[Libraries and Environments]] | How to install Python, JAR, and R packages and pin dependencies with notebook-scoped libraries, compute-scoped libraries, and serverless environments. |
| 201 | [[dbutils and Widgets]] | The Databricks Utilities (dbutils) library for files, secrets, notebook chaining, and job task values, and widgets for notebook parameters. |
| 201 | [[Volumes]] | Governed folders for non-table files like CSVs, images, PDFs, and model artifacts, addressed as /Volumes/catalog/schema/volume. |
| 201 | [[Experiment Tracking]] | Logging every training run's parameters, metrics, and artifacts in MLflow experiments, so results can be compared and reproduced. |
| 201 | [[Models in Unity Catalog]] | Versioning, aliasing, and governing ML models as Unity Catalog objects, the default MLflow registry since MLflow 3. |
| 201 | [[Model Serving]] | Turning a registered model into a live, autoscaling REST endpoint on serverless CPU or GPU compute. |
| 201 | [[Path - Data Scientist and ML Engineer]] | Notebooks, Spark, MLflow, the feature store, and serving. |
| 301 | [[Feature Engineering and Feature Store]] | Reusable, governed model inputs in Unity Catalog, kept consistent between training and serving, with Lakebase-backed online stores. |
| 301 | [[Data Quality Monitoring]] | Watching tables and model inputs for freshness, completeness, and drift with anomaly detection and data profiling (formerly Lakehouse Monitoring). |
| 301 | [[AI Runtime]] | GPU clusters on Databricks Runtime ML and AI Runtime serverless GPUs (A10 and H100) for deep learning, fine-tuning, and LLM work. |
| 301 | [[Path - Certification Prep]] | Which Databricks certifications exist and which notes map to each exam. |
| 401 | [[Fine-Tuning]] | Further training a foundation model on your own examples, when not to bother, and how to do it on AI Runtime now that Foundation Model Fine-tuning is end of life. |

### AI or application developer

| Depth | Note | Why |
|---|---|---|
| 101 | [[Generative AI and LLMs]] | What large language models are, why they need your business data to be useful, and the Databricks tools for each way of using them. |
| 101 | [[MLflow]] | The open-source platform for tracking, packaging, evaluating, tracing, and deploying ML models and GenAI agents, managed on Databricks. |
| 101 | [[Agent Bricks]] | Databricks' agent platform, launched in 2025 for building agents from a task description and refocused in 2026 on code-first agents with the Agent Bricks CLI and Agent Runtime. |
| 101 | [[AI Playground]] | A no-code chat UI in the workspace for trying, comparing, and prototyping LLMs and simple tool-calling agents. |
| 201 | [[Unity Catalog Functions]] | SQL and Python functions registered in Unity Catalog, governed and reusable across queries, policies, agents, and tools. |
| 201 | [[AI Functions in SQL]] | Calling LLMs from plain SQL to classify, summarize, extract, and translate. |
| 201 | [[Databricks Apps]] | Hosting internal web apps in Streamlit, Dash, React, and others right next to your data. |
| 201 | [[Model Serving]] | Turning a registered model into a live, autoscaling REST endpoint on serverless CPU or GPU compute. |
| 201 | [[Foundation Model APIs]] | Pay-per-token and provisioned-throughput access to Databricks-hosted open and partner LLMs, through an OpenAI-compatible API. |
| 201 | [[AI Search]] | Databricks AI Search (formerly Vector Search) finds text or images by meaning, the retrieval half of RAG, with indexes synced from Delta tables. |
| 201 | [[Retrieval-Augmented Generation]] | Giving an LLM your documents at question time so it answers from facts, built on Databricks with document parsing, AI Search, and MLflow evaluation. |
| 201 | [[MosaicML and Open Models]] | Databricks' 2023 MosaicML acquisition, the MPT and DBRX open models, and how that technology lives on in hosted models, serving, and AI Runtime. |
| 201 | [[Path - AI App Developer]] | LLMs, RAG, AI Search, agents, Databricks Apps, and Lakebase. |
| 301 | [[Spark Connect]] | The client-server protocol that lets thin clients run Spark DataFrame code on a remote Spark server. |
| 301 | [[Databricks SDKs and REST API]] | Programmatic control of Databricks through the REST API and the official SDKs for Python, Java, Go, and JavaScript (plus an R SDK from Databricks Labs). |
| 301 | [[Databricks Connect]] | A client library, built on Spark Connect, that runs Spark code from your local IDE on Databricks clusters or serverless compute. |
| 301 | [[Lakebase]] | A managed Postgres database (OLTP) inside the lakehouse, for apps and agents, generally available since January 22, 2026. |
| 301 | [[Unity Gateway]] | Unity Gateway (formerly AI Gateway) governs, rate-limits, logs, and guards every model and MCP call, including calls to external providers. |
| 301 | [[Mosaic AI Agent Framework]] | The earlier code-first agent tooling (ResponsesAgent, MLflow AgentServer on Databricks Apps, Model Serving deployment), now legacy and mapped to Agent Bricks. |
| 301 | [[Agent Evaluation and Tracing]] | Measuring agent and RAG quality in MLflow 3 with traces, LLM judges, custom scorers, human feedback, and production monitoring. |
| 301 | [[Managed MCP Servers]] | Databricks-hosted Model Context Protocol servers that give AI agents governed access to Genie, SQL, AI Search indexes, and Unity Catalog functions. |
| 401 | [[Fine-Tuning]] | Further training a foundation model on your own examples, when not to bother, and how to do it on AI Runtime now that Foundation Model Fine-tuning is end of life. |

### Platform or cloud admin

| Depth | Note | Why |
|---|---|---|
| 101 | [[Choosing a Cloud for Databricks]] | How to pick Azure, AWS, or Google Cloud, based mostly on what the business already uses. |
| 101 | [[Amazon S3]] | AWS object storage, launched in 2006, the original cloud data lake. |
| 101 | [[Azure Data Lake Storage]] | Azure's object storage built for analytics, Blob Storage with a hierarchical namespace (formerly ADLS Gen2). |
| 101 | [[Google Cloud Storage]] | Google Cloud's object storage, addressed as gs://bucket/path. |
| 101 | [[Accounts and Workspaces]] | The account is the company, and a workspace is a room where teams work. |
| 101 | [[Compute Types]] | The map of Databricks compute, covering all-purpose, jobs, serverless, and SQL warehouses. |
| 101 | [[SQL Warehouses]] | Compute built for SQL queries, dashboards, and BI tools, in serverless, pro, and classic types. |
| 101 | [[DBUs]] | The Databricks Unit (DBU), a normalized unit of processing power per hour that Databricks usage is measured and priced in. |
| 101 | [[Unity Catalog]] | Databricks' governance layer for permissions, discovery, lineage, and auditing across every workspace. |
| 101 | [[Catalog Explorer]] | The Unity Catalog UI for browsing, searching, and managing data and AI assets and their permissions. |
| 101 | [[Azure Databricks Overview]] | What is different when Databricks is sold, billed, and run as a Microsoft Azure service. |
| 101 | [[Creating an Azure Databricks Workspace]] | Step by step in the Azure portal, CLI, or Bicep, covering pricing tier, workspace type, region, networking, and resource group. |
| 101 | [[Databricks on AWS Overview]] | How Databricks runs on AWS, sold by Databricks directly or through AWS Marketplace. |
| 101 | [[Account Setup on AWS]] | Signing up, then creating a serverless workspace or a classic workspace with Quickstart, manual setup, or Terraform. |
| 101 | [[Databricks on Google Cloud Overview]] | How Databricks runs on Google Cloud, sold through Google Cloud Marketplace, and what is different there. |
| 101 | [[Account Setup on Google Cloud]] | Subscribing through Google Cloud Marketplace, activating the account, and creating the first serverless or classic workspace. |
| 101 | [[Cost Management Basics]] | Where Databricks spend comes from, how it is metered, and the first five controls to set. |
| 201 | [[Hive Metastore]] | The table directory Hive introduced, which Spark and early Databricks inherited. |
| 201 | [[Driver and Executors]] | The boss process and the worker processes in every Spark cluster. |
| 201 | [[Open Table Formats]] | A metadata layer over Parquet files that turns a folder into a real table. |
| 201 | [[Apache Iceberg]] | The Netflix-born table format, Delta's main rival, now first-class in Unity Catalog. |
| 201 | [[Predictive Optimization]] | Databricks automatically running OPTIMIZE, VACUUM, and statistics collection on Unity Catalog managed tables. |
| 201 | [[Control Plane and Compute Plane]] | What Databricks runs for you, versus what runs in your cloud account or in serverless. |
| 201 | [[Databricks CLI]] | The `databricks` command-line tool for scripting workspaces and accounts, authenticating, and deploying bundles. |
| 201 | [[Serverless Workspaces and Default Storage]] | Workspaces that run only on serverless compute and store data in Databricks-managed default storage, so you supply no cloud storage, credentials, or network. |
| 201 | [[DBFS]] | The legacy Databricks File System (DBFS root and mounts), why it is deprecated, and how Unity Catalog volumes, external locations, and workspace files replace it. |
| 201 | [[Metastore]] | The top-level Unity Catalog container, one per region, that holds every catalog, credential, share, and connection. |
| 201 | [[Managed vs External Tables]] | Who owns the files, and what happens when you drop a table. Managed is the default and recommended choice. |
| 201 | [[Privileges and Grants]] | GRANT and REVOKE on securable objects, how privileges inherit down the tree, and how ownership and MANAGE work. |
| 201 | [[System Tables]] | Databricks' own operational data (billing, audit, lineage, compute, jobs, queries) as queryable tables in the system catalog. |
| 201 | [[Governed Tags]] | Account-level tag definitions with controlled values and assignment permissions, used for discovery, classification, and ABAC policies. |
| 201 | [[Models in Unity Catalog]] | Versioning, aliasing, and governing ML models as Unity Catalog objects, the default MLflow registry since MLflow 3. |
| 201 | [[First-Party Microsoft Service]] | Microsoft provisioning, billing, and support, and why Azure Databricks is unusual among Databricks clouds. |
| 201 | [[Managed Resource Group]] | The locked resource group Azure creates to hold a classic workspace's VMs, disks, network resources, and workspace storage account. |
| 201 | [[Microsoft Entra ID Integration]] | Sign-in, automatic identity management, SCIM, conditional access, tokens, and service principals with Microsoft Entra ID. |
| 201 | [[Microsoft Fabric and OneLake vs Databricks]] | How Microsoft Fabric and Azure Databricks overlap, how to choose between them, and how mirroring and OneLake federation connect them. |
| 201 | [[Workspace Storage Bucket]] | The S3 bucket a classic AWS workspace uses for its own system data, and why production data belongs elsewhere. |
| 201 | [[Account Console]] | The account-level admin site for workspaces, users, metastores, and billing. |
| 201 | [[Users Groups and Service Principals]] | The three kinds of identity, and why groups should own everything. |
| 201 | [[Single Sign-On]] | Logging in with your company identity provider, configured once for the account and every workspace. |
| 201 | [[Admin Roles]] | Account admins, workspace admins, metastore admins, and the narrower feature roles, and who can do what. |
| 201 | [[Compute Policies]] | Guardrails on what classic compute people can create, written as JSON rules (formerly cluster policies). |
| 201 | [[Budgets and Usage Dashboards]] | Budget alerts in the account console and the built-in usage dashboards built on system.billing tables. |
| 201 | [[Tagging for Chargeback]] | Tagging compute, warehouses, pools, and serverless usage so every DBU maps to a team or project. |
| 201 | [[Cost Optimization Checklist]] | A practical checklist covering auto-termination, serverless, spot instances, sizing, Photon, pools, and data layout. |
| 301 | [[YARN]] | Hadoop's resource manager, which decides which job gets which machines. |
| 301 | [[Delta UniForm]] | Writing Delta tables that Iceberg readers can also read. |
| 301 | [[OPTIMIZE and VACUUM]] | Compacting small files and deleting old ones, and Predictive Optimization doing it for you. |
| 301 | [[Photon]] | Databricks' C++ query engine that speeds up SQL and DataFrame work. |
| 301 | [[Declarative Automation Bundles]] | Infrastructure as code for jobs, pipelines, and apps, defined as YAML in Git and deployed with `databricks bundle` (formerly Databricks Asset Bundles). |
| 301 | [[Databricks SDKs and REST API]] | Programmatic control of Databricks through the REST API and the official SDKs for Python, Java, Go, and JavaScript (plus an R SDK from Databricks Labs). |
| 301 | [[Instance Pools]] | Sets of idle, ready-to-use cloud VMs that classic clusters draw from to cut start and autoscaling time. |
| 301 | [[Init Scripts]] | Shell scripts that run on each classic cluster node at startup, the cluster-scoped and global types, and where to store them safely. |
| 301 | [[Storage Credentials and External Locations]] | How Unity Catalog is allowed to reach your cloud storage, with credentials held by the catalog instead of by clusters. |
| 301 | [[Row Filters and Column Masks]] | SQL functions attached to a table that show each person only the rows and column values they are allowed to see. |
| 301 | [[Attribute-Based Access Control]] | Policies driven by governed tags, set once on a catalog or schema, that filter rows and mask columns on every matching table. |
| 301 | [[Audit Logs]] | A record of who did what and when across the account, queryable as system.access.audit or delivered to your own storage. |
| 301 | [[Hive Metastore Migration to Unity Catalog]] | Upgrading older workspaces from the legacy Hive metastore to Unity Catalog with federation, SYNC, CLONE, and the UCX utilities. |
| 301 | [[Service Credentials]] | Unity Catalog objects that let code reach cloud services other than storage, such as queues or secret stores, without handling keys. |
| 301 | [[Lakeguard]] | The isolation technology that lets many users share standard and serverless compute while Unity Catalog enforces fine-grained access. |
| 301 | [[CI-CD for Data Pipelines]] | Dev, staging, and prod, with tests and automated deployment for data code. |
| 301 | [[Unity Gateway]] | Unity Gateway (formerly AI Gateway) governs, rate-limits, logs, and guards every model and MCP call, including calls to external providers. |
| 301 | [[AI Runtime]] | GPU clusters on Databricks Runtime ML and AI Runtime serverless GPUs (A10 and H100) for deep learning, fine-tuning, and LLM work. |
| 301 | [[VNet Injection]] | Deploying Azure Databricks classic compute into your own Azure virtual network, with subnet sizing, delegation, NSG rules, and egress. |
| 301 | [[Secure Cluster Connectivity]] | No public IPs on classic cluster nodes, with all control traffic initiated outbound to a relay, and the egress options that go with it. |
| 301 | [[ADLS and Access Connectors]] | How Unity Catalog reaches ADLS Gen2 through an Access Connector's managed identity, including storage behind firewalls. |
| 301 | [[Azure Key Vault Secret Scopes]] | Using Azure Key Vault as the read-only backing store for a Databricks secret scope, with its permission model and limits. |
| 301 | [[Azure Monitor and Diagnostic Logs]] | Sending Azure Databricks diagnostic (audit) logs to Log Analytics, Storage, or Event Hubs, and when to use the audit log system table instead. |
| 301 | [[Cross-Account IAM Role]] | The IAM role that lets the Databricks control plane launch and manage EC2 instances in your AWS account. |
| 301 | [[Customer-Managed VPC on AWS]] | Running classic compute in a VPC you create and control, with subnet, security group, and egress requirements. |
| 301 | [[Instance Profiles]] | The legacy way clusters got S3 access by attaching an IAM role to EC2 nodes, and why Unity Catalog replaced it. |
| 301 | [[S3 Access via Unity Catalog]] | Storage credentials backed by self-assuming IAM roles, plus external locations, for governed S3 access. |
| 301 | [[EC2 Instance Types and Graviton]] | Picking EC2 node types, fleet types, spot instances, and Arm-based Graviton for classic compute price and performance. |
| 301 | [[Compute on Google Cloud]] | How classic clusters run on Compute Engine VMs (after the move off GKE), with machine types, preemptible VMs, and gcp_attributes. |
| 301 | [[Customer-Managed VPC on Google Cloud]] | Bringing your own VPC and subnet (standalone or Shared VPC) for Databricks classic compute on Google Cloud. |
| 301 | [[Google Service Accounts]] | The workspace, compute, custom, and Unity Catalog service accounts that let Databricks and clusters authenticate to Google Cloud. |
| 301 | [[GCS Access via Unity Catalog]] | Storage credentials backed by Databricks-generated Google service accounts, plus external locations, for governed GCS access. |
| 301 | [[SCIM Provisioning]] | Syncing users and groups automatically from Entra ID, Okta, or another IdP. |
| 301 | [[Authentication - Tokens and OAuth]] | Personal access tokens versus OAuth (U2M, M2M, and token federation) for scripts, tools, and automation. |
| 301 | [[Network Security Overview]] | The map of front-end, back-end (classic), and serverless network controls on every cloud. |
| 301 | [[IP Access Lists]] | Allowing workspace and account console access only from known networks. |
| 301 | [[Terraform Provider]] | Managing Databricks accounts, workspaces, identities, policies, and permissions as code with the databricks/databricks Terraform provider. |
| 301 | [[Migrating from Hadoop]] | Moving HDFS data, Hive tables, Spark jobs, and Oozie workflows off an on-premises Hadoop cluster into Databricks. |
| 301 | [[Path - Platform Admin]] | Accounts, identity, Unity Catalog, networking, and cost controls on your cloud. |
| 301 | [[Path - Azure Deep Dive]] | Every Azure-specific rabbit hole in order. |
| 301 | [[Path - AWS Deep Dive]] | Every AWS-specific rabbit hole in order. |
| 301 | [[Path - Google Cloud Deep Dive]] | Every Google Cloud-specific rabbit hole in order. |
| 401 | [[Azure Private Link]] | Private endpoints for inbound (front-end), classic compute (back-end), and serverless connections to Azure Databricks without the public internet. |
| 401 | [[AWS PrivateLink]] | Private front-end and back-end connectivity between your VPCs and Databricks using VPC interface endpoints. |
| 401 | [[Hive Metastore Federation for AWS Glue]] | Governing and reading tables registered in the AWS Glue Data Catalog from Unity Catalog through catalog federation. |
| 401 | [[Databricks on AWS GovCloud]] | The separate Databricks environment in AWS GovCloud (US) for FedRAMP High, DoD IL5, and other US public-sector workloads. |
| 401 | [[Private Service Connect]] | Private front-end and back-end connectivity between your VPCs and Databricks on Google Cloud using PSC endpoints. |
| 401 | [[Serverless Network Security]] | Network connectivity configurations, private endpoints, and network policies (serverless egress control) for serverless compute. |
| 401 | [[Disaster Recovery]] | Backups, multi-region strategies, managed disaster recovery, and what Databricks does and does not protect. |

### Security, privacy, or compliance lead

| Depth | Note | Why |
|---|---|---|
| 101 | [[Unity Catalog]] | Databricks' governance layer for permissions, discovery, lineage, and auditing across every workspace. |
| 201 | [[Control Plane and Compute Plane]] | What Databricks runs for you, versus what runs in your cloud account or in serverless. |
| 201 | [[Privileges and Grants]] | GRANT and REVOKE on securable objects, how privileges inherit down the tree, and how ownership and MANAGE work. |
| 201 | [[Data Lineage]] | An automatic, column-level map of where every table and column came from and where it goes, captured by Unity Catalog at runtime. |
| 201 | [[System Tables]] | Databricks' own operational data (billing, audit, lineage, compute, jobs, queries) as queryable tables in the system catalog. |
| 201 | [[Governed Tags]] | Account-level tag definitions with controlled values and assignment permissions, used for discovery, classification, and ABAC policies. |
| 201 | [[Microsoft Entra ID Integration]] | Sign-in, automatic identity management, SCIM, conditional access, tokens, and service principals with Microsoft Entra ID. |
| 201 | [[Users Groups and Service Principals]] | The three kinds of identity, and why groups should own everything. |
| 201 | [[Single Sign-On]] | Logging in with your company identity provider, configured once for the account and every workspace. |
| 201 | [[Secrets Management]] | Keeping passwords and keys out of notebooks with secret scopes, and the newer secrets in Unity Catalog. |
| 301 | [[Storage Credentials and External Locations]] | How Unity Catalog is allowed to reach your cloud storage, with credentials held by the catalog instead of by clusters. |
| 301 | [[Row Filters and Column Masks]] | SQL functions attached to a table that show each person only the rows and column values they are allowed to see. |
| 301 | [[Attribute-Based Access Control]] | Policies driven by governed tags, set once on a catalog or schema, that filter rows and mask columns on every matching table. |
| 301 | [[Audit Logs]] | A record of who did what and when across the account, queryable as system.access.audit or delivered to your own storage. |
| 301 | [[Clean Rooms]] | A governed, serverless environment where up to ten organizations run approved analysis on combined data without seeing each other's raw records. |
| 301 | [[Data Classification]] | A Unity Catalog feature that scans catalogs for sensitive data such as PII and can tag matching columns automatically. |
| 301 | [[Lakeguard]] | The isolation technology that lets many users share standard and serverless compute while Unity Catalog enforces fine-grained access. |
| 301 | [[Unity Gateway]] | Unity Gateway (formerly AI Gateway) governs, rate-limits, logs, and guards every model and MCP call, including calls to external providers. |
| 301 | [[VNet Injection]] | Deploying Azure Databricks classic compute into your own Azure virtual network, with subnet sizing, delegation, NSG rules, and egress. |
| 301 | [[Secure Cluster Connectivity]] | No public IPs on classic cluster nodes, with all control traffic initiated outbound to a relay, and the egress options that go with it. |
| 301 | [[Azure Key Vault Secret Scopes]] | Using Azure Key Vault as the read-only backing store for a Databricks secret scope, with its permission model and limits. |
| 301 | [[Azure Monitor and Diagnostic Logs]] | Sending Azure Databricks diagnostic (audit) logs to Log Analytics, Storage, or Event Hubs, and when to use the audit log system table instead. |
| 301 | [[Cross-Account IAM Role]] | The IAM role that lets the Databricks control plane launch and manage EC2 instances in your AWS account. |
| 301 | [[Customer-Managed VPC on AWS]] | Running classic compute in a VPC you create and control, with subnet, security group, and egress requirements. |
| 301 | [[Customer-Managed VPC on Google Cloud]] | Bringing your own VPC and subnet (standalone or Shared VPC) for Databricks classic compute on Google Cloud. |
| 301 | [[Google Service Accounts]] | The workspace, compute, custom, and Unity Catalog service accounts that let Databricks and clusters authenticate to Google Cloud. |
| 301 | [[Authentication - Tokens and OAuth]] | Personal access tokens versus OAuth (U2M, M2M, and token federation) for scripts, tools, and automation. |
| 301 | [[Network Security Overview]] | The map of front-end, back-end (classic), and serverless network controls on every cloud. |
| 301 | [[IP Access Lists]] | Allowing workspace and account console access only from known networks. |
| 301 | [[Encryption]] | Encryption at rest and in transit on Databricks, and where customer-managed keys apply. |
| 301 | [[Path - Platform Admin]] | Accounts, identity, Unity Catalog, networking, and cost controls on your cloud. |
| 401 | [[Azure Private Link]] | Private endpoints for inbound (front-end), classic compute (back-end), and serverless connections to Azure Databricks without the public internet. |
| 401 | [[Customer-Managed Keys on Azure]] | Encrypting Azure Databricks managed services, workspace storage (DBFS root), and managed disks with your own Azure Key Vault or Managed HSM keys. |
| 401 | [[AWS PrivateLink]] | Private front-end and back-end connectivity between your VPCs and Databricks using VPC interface endpoints. |
| 401 | [[Customer-Managed Keys on AWS]] | Encrypting managed services, the workspace storage bucket, and EBS volumes with AWS KMS keys you control. |
| 401 | [[Databricks on AWS GovCloud]] | The separate Databricks environment in AWS GovCloud (US) for FedRAMP High, DoD IL5, and other US public-sector workloads. |
| 401 | [[Private Service Connect]] | Private front-end and back-end connectivity between your VPCs and Databricks on Google Cloud using PSC endpoints. |
| 401 | [[Customer-Managed Keys on Google Cloud]] | Encrypting managed services, workspace GCS buckets, and Compute Engine disks with Cloud KMS keys you control, set at workspace creation. |
| 401 | [[Serverless Network Security]] | Network connectivity configurations, private endpoints, and network policies (serverless egress control) for serverless compute. |
| 401 | [[Compliance Security Profile]] | A workspace setting that applies hardened images, monitoring agents, and other controls required for HIPAA, PCI-DSS, FedRAMP, and other standards. |
| 401 | [[Disaster Recovery]] | Backups, multi-region strategies, managed disaster recovery, and what Databricks does and does not protect. |

### Finance or FinOps

| Depth | Note | Why |
|---|---|---|
| 101 | [[When Databricks Is Not the Right Fit]] | An honest list of situations where a simpler or cheaper tool is the better choice. |
| 101 | [[How Databricks Pricing Works]] | DBUs, SKUs, serverless versus classic, committed use, and why there are usually two bills. |
| 101 | [[Serverless Compute]] | Compute that Databricks runs and scales for you, starting in seconds with no clusters to configure. |
| 101 | [[DBUs]] | The Databricks Unit (DBU), a normalized unit of processing power per hour that Databricks usage is measured and priced in. |
| 101 | [[Cost Management Basics]] | Where Databricks spend comes from, how it is metered, and the first five controls to set. |
| 201 | [[Estimating Costs for a Small Business]] | A worked, back-of-the-envelope monthly cost estimate for a small company's first workloads. |
| 201 | [[Building a Business Case]] | How to justify Databricks to a boss or a board, covering costs, savings, risks, and a proof of concept. |
| 201 | [[Jobs Compute]] | Clusters that spin up for one scheduled job and then disappear, at a lower price. |
| 201 | [[System Tables]] | Databricks' own operational data (billing, audit, lineage, compute, jobs, queries) as queryable tables in the system catalog. |
| 201 | [[First-Party Microsoft Service]] | Microsoft provisioning, billing, and support, and why Azure Databricks is unusual among Databricks clouds. |
| 201 | [[Azure Billing and Commit Units]] | Pay-as-you-go billing on the Azure invoice, Databricks commit unit (DBCU) prepurchase plans, and Azure and Databricks cost tools. |
| 201 | [[AWS Marketplace and Billing]] | Paying Databricks directly or through AWS Marketplace, and where the EC2, EBS, S3, and networking costs of classic compute appear. |
| 201 | [[Google Cloud Marketplace and Billing]] | Paying for Databricks through a Google Cloud Marketplace subscription on the Google Cloud bill, and where Compute Engine and storage costs appear. |
| 201 | [[Compute Policies]] | Guardrails on what classic compute people can create, written as JSON rules (formerly cluster policies). |
| 201 | [[Budgets and Usage Dashboards]] | Budget alerts in the account console and the built-in usage dashboards built on system.billing tables. |
| 201 | [[Tagging for Chargeback]] | Tagging compute, warehouses, pools, and serverless usage so every DBU maps to a team or project. |
| 201 | [[Cost Optimization Checklist]] | A practical checklist covering auto-termination, serverless, spot instances, sizing, Photon, pools, and data layout. |
| 301 | [[Instance Pools]] | Sets of idle, ready-to-use cloud VMs that classic clusters draw from to cut start and autoscaling time. |
| 301 | [[EC2 Instance Types and Graviton]] | Picking EC2 node types, fleet types, spot instances, and Arm-based Graviton for classic compute price and performance. |

### One-person data team at a small business

| Depth | Note | Why |
|---|---|---|
| 101 | [[Who Uses Databricks - Business Types]] | Kinds of businesses, from e-commerce to clinics to factories, that get real value from Databricks, with example use cases. |
| 101 | [[Signs You Have Outgrown Spreadsheets]] | The warning signs that a business needs a real data platform instead of Excel, Access, or one reporting tool. |
| 101 | [[When Databricks Is Not the Right Fit]] | An honest list of situations where a simpler or cheaper tool is the better choice. |
| 101 | [[How Databricks Pricing Works]] | DBUs, SKUs, serverless versus classic, committed use, and why there are usually two bills. |
| 101 | [[Databricks Free Edition and Trials]] | The free ways to try Databricks (Free Edition and the 14-day trial), what each one includes, and what it leaves out. |
| 101 | [[Choosing a Cloud for Databricks]] | How to pick Azure, AWS, or Google Cloud, based mostly on what the business already uses. |
| 101 | [[Your First 30 Days on Databricks]] | A week-by-week plan from sign-up to the first trusted dashboard. |
| 101 | [[Medallion Architecture]] | Bronze (raw), silver (cleaned), and gold (business-ready) layers of tables. |
| 101 | [[Compute Types]] | The map of Databricks compute, covering all-purpose, jobs, serverless, and SQL warehouses. |
| 101 | [[Serverless Compute]] | Compute that Databricks runs and scales for you, starting in seconds with no clusters to configure. |
| 101 | [[Lakeflow]] | Databricks' umbrella for ingestion (Connect), transformation (Pipelines), and orchestration (Jobs). |
| 101 | [[Lakeflow Connect]] | Managed connectors for Salesforce, SQL Server, Google Analytics, and other common sources. |
| 101 | [[Lakeflow Jobs]] | Databricks' built-in orchestrator for scheduled multi-task workflows (formerly Workflows). |
| 101 | [[Lakeflow Designer]] | A no-code, drag-and-drop pipeline builder with AI help. |
| 101 | [[AutoML]] | Letting Databricks train and compare models for you and hand back notebooks, now removed from Databricks Runtime 18.0 ML onward. |
| 101 | [[Agent Bricks]] | Databricks' agent platform, launched in 2025 for building agents from a task description and refocused in 2026 on code-first agents with the Agent Bricks CLI and Agent Runtime. |
| 101 | [[Creating an Azure Databricks Workspace]] | Step by step in the Azure portal, CLI, or Bicep, covering pricing tier, workspace type, region, networking, and resource group. |
| 101 | [[Account Setup on AWS]] | Signing up, then creating a serverless workspace or a classic workspace with Quickstart, manual setup, or Terraform. |
| 101 | [[Account Setup on Google Cloud]] | Subscribing through Google Cloud Marketplace, activating the account, and creating the first serverless or classic workspace. |
| 101 | [[Cost Management Basics]] | Where Databricks spend comes from, how it is metered, and the first five controls to set. |
| 101 | [[Migration Strategy Overview]] | The phases of every migration, from assess and plan to coexist, ingest, convert, validate, switch over, and decommission. |
| 101 | [[Migrating from Excel and Access]] | Moving a spreadsheet-run business into governed tables, with file uploads, Volumes, a first dashboard, and Genie Agents. |
| 101 | [[Migration Checklist]] | A printable, start-to-finish checklist for a small business migration. |
| 101 | [[Path - One-Person Data Team]] | The shortest route for a small business with one data person doing every job. |
| 201 | [[Databricks vs Alternatives for Small Teams]] | How Databricks compares with Snowflake, BigQuery, Microsoft Fabric, Power BI alone, and plain Postgres for a small team. |
| 201 | [[Estimating Costs for a Small Business]] | A worked, back-of-the-envelope monthly cost estimate for a small company's first workloads. |
| 201 | [[Fivetran and ELT Tools]] | Managed connectors that copy SaaS and database data into a warehouse or lakehouse. |
| 201 | [[Predictive Optimization]] | Databricks automatically running OPTIMIZE, VACUUM, and statistics collection on Unity Catalog managed tables. |
| 201 | [[Serverless Workspaces and Default Storage]] | Workspaces that run only on serverless compute and store data in Databricks-managed default storage, so you supply no cloud storage, credentials, or network. |
| 201 | [[Lakehouse Federation]] | Querying Postgres, SQL Server, Snowflake, BigQuery, and other databases and catalogs in place through Unity Catalog, without copying. |
| 201 | [[Partner Connect]] | Guided connections to Fivetran, dbt, Power BI, Tableau, Sigma, and other partners that provision the warehouse, service principal, and token for you. |
| 201 | [[Databricks Apps]] | Hosting internal web apps in Streamlit, Dash, React, and others right next to your data. |
| 201 | [[Cost Optimization Checklist]] | A practical checklist covering auto-termination, serverless, spot instances, sizing, Photon, pools, and data layout. |
| 201 | [[Assessing Your Current Data Estate]] | Taking inventory of sources, tables, jobs, reports, users, and costs before moving anything. |
| 201 | [[Migrating from SQL Server]] | Moving off an on-premises or Azure SQL Server, using federation first, Lakeflow Connect replication after, and Lakebridge for T-SQL. |
| 201 | [[Migrating from Postgres and MySQL]] | Moving app-database analytics from PostgreSQL or MySQL into the lakehouse without slowing the app down. |

<!-- GENERATED:persona-map END -->

> [!sources]- Sources (last verified: 2026-10-25)
> - Persona definitions: `_meta/manifest.yaml` (`personas:`) in this vault.
> - Table generator: `scripts/build_index.py` (`write_persona_map`) in this vault.
> - Each note's own `[!sources]` callout holds the official documentation behind it.
