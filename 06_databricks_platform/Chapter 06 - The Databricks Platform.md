---
type: chapter
status: written
part: 1
level: 6
section: Databricks Platform
summary: Databricks arrives. Accounts, workspaces, compute, notebooks, and the tools for building on it.
prev: "[[Predictive Optimization]]"
next: "[[The Founding of Databricks]]"
notes:
  - "[[The Founding of Databricks]]"
  - "[[The Data Intelligence Platform]]"
  - "[[Accounts and Workspaces]]"
  - "[[Control Plane and Compute Plane]]"
  - "[[Databricks Runtime]]"
  - "[[Photon]]"
  - "[[Compute Types]]"
  - "[[All-Purpose Compute]]"
  - "[[Jobs Compute]]"
  - "[[Serverless Compute]]"
  - "[[SQL Warehouses]]"
  - "[[Notebooks]]"
  - "[[Genie Code]]"
  - "[[Git Folders and Workspace Files]]"
  - "[[Declarative Automation Bundles]]"
  - "[[Databricks CLI]]"
  - "[[Databricks SDKs and REST API]]"
  - "[[Databricks Connect]]"
  - "[[DBUs]]"
  - "[[Libraries and Environments]]"
last_verified: 2026-10-25
tags:
  - chapter
---

# Chapter 06 - The Databricks Platform

> [!story] Context
> [[Chapter 05 - The Lakehouse|Chapter 05]] ended with the lakehouse design: open table formats such as [[Delta Lake]] on cheap object storage, maintained with commands like [[OPTIMIZE and VACUUM]], which [[Predictive Optimization]] can run automatically. A design is not a product. This chapter covers the managed platform that Databricks built to run it: accounts, workspaces, compute, and the tools for writing and deploying code.

**Databricks arrives. Accounts, workspaces, compute, notebooks, and the tools for building on it.**

## The story of this chapter

[[The Founding of Databricks|Databricks was founded in 2013]] by the creators of [[Apache Spark]] to run Spark as a managed cloud service, so that teams no longer had to build and operate their own clusters. Over time the company extended that service into what it now calls [[The Data Intelligence Platform]]: the lakehouse plus AI features that use the context of your data.

The platform has a fixed structure. An [[Accounts and Workspaces|account]] represents the company and holds identities, billing, and governance. A workspace is the environment where teams work. Databricks splits each deployment into a [[Control Plane and Compute Plane|control plane]], which Databricks operates, and a compute plane, which runs either in your own cloud account (classic) or in Databricks' serverless environment.

Compute is the largest topic in the chapter, because it drives both performance and cost:

| Compute | Purpose | Note |
|---|---|---|
| Engine | Spark plus Databricks optimizations, versioned with LTS releases | [[Databricks Runtime]], [[Photon]] |
| Interactive clusters | Exploration in notebooks, configured by you | [[All-Purpose Compute]] |
| Job clusters | One cluster per scheduled run, then terminated | [[Jobs Compute]] |
| Serverless | Starts in seconds, managed by Databricks, no cluster settings | [[Serverless Compute]] |
| SQL warehouses | SQL and BI concurrency, in serverless, pro, and classic types | [[SQL Warehouses]] |

[[Compute Types]] gives the decision map. Databricks recommends serverless wherever it is available and classic compute when a workload needs something serverless does not support, such as R, RDD APIs, or init scripts.

The next group of notes covers how code is written. [[Notebooks]] mix Python, SQL, Scala, and R cells with results and Markdown, and are stored as `.ipynb` files by default. [[Genie Code]], renamed Genie Code in March 2026, is the AI agent inside notebooks and editors that writes, runs, and fixes code using Unity Catalog metadata.

The chapter then moves from interactive work to software engineering practice:

1. [[Git Folders and Workspace Files]] (formerly Repos) connect the workspace to GitHub, GitLab, Bitbucket, Azure DevOps, or AWS CodeCommit, and store Python modules beside notebooks.
2. [[Declarative Automation Bundles]] (formerly Databricks Asset Bundles, renamed March 2026) define jobs, pipelines, and apps as YAML in Git and deploy them to each environment with `databricks bundle deploy`.
3. The [[Databricks CLI]] scripts the whole platform from a terminal and authenticates with `databricks auth login`.
4. The [[Databricks SDKs and REST API]] expose the same operations to Python, Java, Go, and JavaScript programs.
5. [[Databricks Connect]], built on [[Spark Connect]], runs DataFrame code from a local IDE on Databricks compute.

Two practical topics close the chapter. [[DBUs]] explain the meter that every compute choice is billed in and how to read it from `system.billing.usage`. [[Libraries and Environments]] explain how to install and pin packages on classic clusters and on serverless environment versions.

At the end of this chapter, you can create compute, write and version code, deploy it, and predict its cost. The platform does not yet answer who may read which table, where a value came from, or how data is shared. [[Chapter 07 - Unity Catalog and Governance]] covers the governance layer that answers those questions.

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[The Founding of Databricks]] | 101 Beginner | How Spark's creators started a company in 2013 to run Spark in the cloud. |
| 2 | [[The Data Intelligence Platform]] | 101 Beginner | Databricks' name for the lakehouse plus AI that understands your data (now often called the Data + AI Platform). |
| 3 | [[Accounts and Workspaces]] | 101 Beginner | The account is the company, and a workspace is a room where teams work. |
| 4 | [[Control Plane and Compute Plane]] | 201 Practitioner | What Databricks runs for you, versus what runs in your cloud account or in serverless. |
| 5 | [[Databricks Runtime]] | 201 Practitioner | The tuned Spark plus libraries image every classic cluster boots, and its LTS versions. |
| 6 | [[Photon]] | 301 Advanced | Databricks' C++ query engine that speeds up SQL and DataFrame work. |
| 7 | [[Compute Types]] | 101 Beginner | The map of Databricks compute, covering all-purpose, jobs, serverless, and SQL warehouses. |
| 8 | [[All-Purpose Compute]] | 201 Practitioner | Interactive clusters for notebooks and exploration, which you create, share, and must remember to stop. |
| 9 | [[Jobs Compute]] | 201 Practitioner | Clusters that spin up for one scheduled job and then disappear, at a lower price. |
| 10 | [[Serverless Compute]] | 101 Beginner | Compute that Databricks runs and scales for you, starting in seconds with no clusters to configure. |
| 11 | [[SQL Warehouses]] | 101 Beginner | Compute built for SQL queries, dashboards, and BI tools, in serverless, pro, and classic types. |
| 12 | [[Notebooks]] | 101 Beginner | Web documents that mix runnable code cells in Python, SQL, Scala, or R with results, charts, and text. |
| 13 | [[Genie Code]] | 101 Beginner | The built-in AI coding and data agent, renamed from Databricks Assistant to Genie Code in March 2026. |
| 14 | [[Git Folders and Workspace Files]] | 201 Practitioner | Git folders sync workspace code with GitHub, GitLab, Bitbucket, Azure DevOps, or CodeCommit; workspace files store code beside notebooks. |
| 15 | [[Declarative Automation Bundles]] | 301 Advanced | Infrastructure as code for jobs, pipelines, and apps, defined as YAML in Git and deployed with `databricks bundle` (formerly Databricks Asset Bundles). |
| 16 | [[Databricks CLI]] | 201 Practitioner | The `databricks` command-line tool for scripting workspaces and accounts, authenticating, and deploying bundles. |
| 17 | [[Databricks SDKs and REST API]] | 301 Advanced | Programmatic control of Databricks through the REST API and the official SDKs for Python, Java, Go, and JavaScript (plus an R SDK from Databricks Labs). |
| 18 | [[Databricks Connect]] | 301 Advanced | A client library, built on Spark Connect, that runs Spark code from your local IDE on Databricks clusters or serverless compute. |
| 19 | [[DBUs]] | 101 Beginner | The Databricks Unit (DBU), a normalized unit of processing power per hour that Databricks usage is measured and priced in. |
| 20 | [[Libraries and Environments]] | 201 Practitioner | How to install Python, JAR, and R packages and pin dependencies with notebook-scoped libraries, compute-scoped libraries, and serverless environments. |
| 21 | [[Serverless Workspaces and Default Storage]] | 201 Practitioner | Workspaces that run only on serverless compute and store data in Databricks-managed storage, with no cloud setup. |
| 22 | [[dbutils and Widgets]] | 201 Practitioner | The notebook utility library for files, secrets, and job values, and widgets for notebook parameters. |
| 23 | [[Instance Pools]] | 301 Advanced | Pre-warmed idle VMs that cut classic cluster start time. |
| 24 | [[Init Scripts]] | 301 Advanced | Shell scripts that run on each classic cluster node at startup, and where to store them safely. |
| 25 | [[DBFS]] | 201 Practitioner | The legacy Databricks File System and mounts, and why Unity Catalog volumes replace them. |

<!-- GENERATED:reading-order END -->

> [!nextup] Next
> [[The Founding of Databricks]] covers how the creators of Spark started the company. After the last note in this chapter, continue to [[Chapter 07 - Unity Catalog and Governance]].
