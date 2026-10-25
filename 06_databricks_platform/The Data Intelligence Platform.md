---
type: concept
status: written
level: 6
section: Databricks Platform
depth: 101
summary: Databricks' name for the lakehouse plus AI that understands your data (now often called the Data + AI Platform).
personas:
  - everyone
  - owner
chapter: "[[Chapter 06 - The Databricks Platform]]"
prev: "[[The Founding of Databricks]]"
next: "[[Accounts and Workspaces]]"
evolved_from:
  - "[[The Lakehouse Idea]]"
  - "[[The Founding of Databricks]]"
evolved_into: []
cloud_equivalent: []
related:
  - "[[Delta Lake]]"
  - "[[Unity Catalog]]"
  - "[[Lakeflow]]"
  - "[[Databricks SQL]]"
  - "[[Genie Agents]]"
  - "[[Genie Code]]"
  - "[[Lakebase]]"
  - "[[Agent Bricks]]"
  - "[[Databricks Apps]]"
  - "[[What Databricks Is in Plain English]]"
  - "[[Microsoft Fabric and OneLake vs Databricks]]"
aliases:
  - Data + AI Platform
  - Databricks Data + AI Platform
  - Databricks Data Intelligence Platform
  - Data intelligence platform
prereqs:
  - "[[The Lakehouse Idea]]"
  - "[[Delta Lake]]"
unlocks:
  - "[[Accounts and Workspaces]]"
  - "[[Unity Catalog]]"
  - "[[Compute Types]]"
clouds:
  - aws
  - azure
  - gcp
mastery: new
last_verified: 2026-10-25
tags:
  - concept
  - flashcards
---

# The Data Intelligence Platform

Mastery: `INPUT[inlineSelect(option(new), option(learning), option(solid)):mastery]`

> [!story] Context
> [[The Founding of Databricks]] covers how Databricks started as hosted Apache Spark and then added open table formats, a governance layer, and AI research. By 2023 the product covered much more than Spark, and Databricks introduced a name for the combined platform.

> [!eli5] Summary
> Databricks is one place where a company stores its data, cleans it, queries it, and builds AI tools on top of it. "Data intelligence" means the system also learns what the data means, so you can ask questions in everyday language and get answers that use your business terms.

> [!renamed] Renamed
> Databricks introduced the name **Data Intelligence Platform** in late 2023. By 2026 the AWS and Azure documentation and databricks.com describe the product as the **Databricks Data + AI Platform**, while some pages (for example, parts of the Google Cloud docs) still say Data Intelligence Platform. No official date for the switch is published. Both names refer to the same product. Before 2023 the usual term was the **Lakehouse Platform**.

> [!analogy]- Analogy: an office building
> | Office building | Databricks |
> |---|---|
> | Foundation and floors | The [[The Lakehouse Idea\|lakehouse]]: open files ([[Delta Lake]] or [[Apache Iceberg]]) in your cloud storage |
> | Front desk and key cards | [[Unity Catalog]]: one list of every asset and one set of access rules |
> | Departments | Workloads: data engineering, SQL and dashboards, machine learning, apps |
> | Office manager who knows the directory | The AI layer, which knows that "rev" means `net_revenue` |

## Background

The lakehouse removes the need to copy data between a lake and a warehouse ([[The Two-Tier Architecture Problem]]). Two problems remain after that:

1. **Data is hard to understand.** A company may have thousands of tables with unclear names, and only a few people know which one is correct.
2. **Generative AI changed expectations.** With large language models ([[LLM]]), users expect to ask questions in plain English. A general chatbot does not know *your* tables, *your* definitions of "active customer", or *your* permissions.

Databricks places an AI layer *inside* the platform, next to the data and the catalog. The layer uses your metadata, lineage, usage history, and permissions to interpret your data. This is the "intelligence" in the name.

## Overview

The Data Intelligence Platform is the name for the whole Databricks platform, not a separate product you install. The official docs describe Databricks as a unified, open platform for data, analytics, and AI, with AI features that tailor it to your data, which integrates with storage and security in your cloud account and manages the cloud infrastructure for you.

The platform has three layers:

| Layer | What it does | Main pieces (notes) |
|---|---|---|
| **Open storage** | Your data, in open formats, in your cloud account | [[Delta Lake]], [[Apache Iceberg]], [[Delta UniForm]], [[Volumes]] |
| **Unified governance** | One catalog, one permission model, lineage, audit | [[Unity Catalog]], [[System Tables]], [[OpenSharing]] |
| **Workloads on shared compute** | The work people run on the data | [[Lakeflow]] (ingest, pipelines, jobs), [[Databricks SQL]], [[AI-BI Dashboards]], [[Genie Agents]], [[Lakebase]], [[Databricks Apps]], Mosaic AI ([[Model Serving]], [[Agent Bricks]]) |

The AI layer spans all three layers. Users interact with it through:

- **[[Genie Code]]**: an AI helper in notebooks and the SQL editor that writes, explains, and fixes code (renamed Genie Code in 2026).
- **[[Genie Agents]]**: a chat interface where business users ask questions about data in plain language.
- **AI-generated documentation**: suggested table and column comments in Unity Catalog.
- **Engine features that tune themselves**: for example, predictive optimization that runs [[OPTIMIZE and VACUUM]] for you, and [[Liquid Clustering]] that picks clustering keys automatically.

## How it works

```mermaid
flowchart TB
  subgraph Users
    A[Analysts] --- E[Engineers] --- S[Scientists] --- B[Business users]
  end
  Users --> AI["AI layer<br/>Genie Code, Genie Agents, AI functions"]
  AI --> W["Workloads<br/>Lakeflow, Databricks SQL, Mosaic AI, Apps, Lakebase"]
  W --> UC["Unity Catalog<br/>catalog, permissions, lineage"]
  UC --> ST["Open storage in your cloud<br/>Delta Lake and Iceberg files"]
```

The platform rests on four design choices:

1. **One copy of the data.** Every workload reads the same tables. An analyst's dashboard and a data scientist's model use the same `sales.orders` table, not two exports.
2. **One governance layer.** The AI features go through Unity Catalog like any other client. Genie Agents and Genie Code see only what the requesting user is allowed to see.
3. **Metadata as input.** Table comments, lineage, popular queries, and certified [[Metric Views]] let the AI give answers that match your business. A well-documented catalog produces better answers.
4. **Managed compute.** You pick a compute type ([[Compute Types]]) and Databricks runs it, increasingly as [[Serverless Compute|serverless]].

The following example calls an [[AI Functions in SQL|AI function]] from SQL:

```sql
-- Classify free-text support tickets without building a model yourself
SELECT ticket_id,
       ai_classify(body, ARRAY('billing', 'shipping', 'product defect')) AS topic
FROM support.tickets.raw
LIMIT 10;
```

## Small-business considerations

> [!smallbiz] Small-business considerations
> For a small company, the platform replaces several separate tools:
> - Your data lands in one place (often your own cloud storage).
> - The same tables feed your [[Dashboard|dashboards]], your spreadsheets via [[BI Tools]], and any AI experiments.
> - Business users can try [[Genie Agents]] to ask questions directly, if someone first documents the key tables.
>
> Most small teams use a fraction of the platform. Start with SQL, a few pipelines, and dashboards. Billing is usage-based in [[DBUs]]. See [[How Databricks Pricing Works]] for the official meter, not prices quoted in blog posts.

## Cloud differences

> [!azure]- Azure Databricks
> Same platform and the same layers. On Azure, it also integrates with Microsoft services: [[Microsoft Entra ID Integration|Entra ID]] for identity, [[Azure Data Lake Storage|ADLS Gen2]] for storage, and [[Power BI on Azure Databricks|Power BI]] for reports. For how it compares with Microsoft's own analytics suite, see [[Microsoft Fabric and OneLake vs Databricks]].

> [!aws]- Databricks on AWS
> Same platform. Storage is [[Amazon S3]]. AWS is usually first to receive new features.

> [!gcp]- Databricks on Google Cloud
> Same platform. Storage is [[Google Cloud Storage]]. Some docs pages on this cloud still use the "Data Intelligence Platform" name. A few AI and serverless features reach Google Cloud later than the other two clouds, so check the feature's availability page.

## Advanced topics

> [!deepdive]- Advanced topics (301–401)
> - **Marketing name, not an architecture.** "Data Intelligence Platform" and "Data + AI Platform" are product-family names. Nothing in the API or CLI is called that. When you read docs, follow the concrete product names (Unity Catalog, Lakeflow, Databricks SQL, Mosaic AI).
> - **Where the intelligence lives.** Most AI features are served from the [[Control Plane and Compute Plane|control plane]] or serverless compute, and some use partner-hosted models. Admins can switch off partner-powered AI features at the account and workspace level, which also disables some [[Genie Code]] capabilities.
> - **Semantics are the bottleneck.** The quality of Genie answers depends on table comments, primary and foreign keys, example queries, and [[Metric Views]]. The 2026 Unity Catalog additions (business glossary terms, domains) push in the same direction. See [[Semantic Layer]].
> - **Scope of the platform.** The well-architected framework's "scope" page is a good map of which capabilities belong to which persona and which are optional.

## Common misconceptions

> [!confusion] "Data intelligence" is not one AI product
> It is the name for the whole platform with AI features built in. The individual AI products are [[Genie Code]], [[Genie Agents]], AI functions, and Mosaic AI.

> [!confusion] Lakehouse vs Data Intelligence Platform
> The [[The Lakehouse Idea|lakehouse]] is the architecture (open tables that work as both lake and warehouse). The Data Intelligence Platform is Databricks' product built on that architecture, plus governance and AI.

## Recall

What does Databricks mean by "data intelligence"?::An AI layer built into the platform that uses your metadata, lineage, usage, and permissions to understand your specific data.
What name was the platform called before "Data Intelligence Platform"?::The Databricks Lakehouse Platform.
What name do the AWS and Azure docs use for the platform in 2026?::The Databricks Data + AI Platform.
What are the three layers of the platform?::Open storage (Delta/Iceberg), unified governance (Unity Catalog), and workloads on managed compute.
Why does a well-documented catalog make Genie better?::Genie uses table comments, keys, example queries, and metric definitions to translate business questions into correct SQL.
Do AI features bypass Unity Catalog permissions?::No. They act as the asking user and only see what that user can see.

## Next steps

> [!path] Learning path
> **Needs first:** [[The Lakehouse Idea]], [[Delta Lake]]
> **Unlocks next:** [[Accounts and Workspaces]], [[Unity Catalog]], [[Compute Types]]

> [!nextup] Next
> [[Accounts and Workspaces]] covers the two containers a company gets when it signs up for Databricks.

> [!sources]- Sources (last verified: 2026-10-25)
> - [What is Databricks? (AWS)](https://docs.databricks.com/aws/en/introduction)
> - [What is Azure Databricks?](https://learn.microsoft.com/en-us/azure/databricks/introduction/)
> - [The scope of the Databricks platform](https://docs.databricks.com/aws/en/lakehouse-architecture/scope)
> - [Databricks AI/BI (AWS)](https://docs.databricks.com/aws/en/ai-bi)
> - [Databricks Data + AI Platform product page](https://www.databricks.com/product/data-intelligence-platform)
> - [What is a data intelligence platform (Databricks blog)](https://www.databricks.com/blog/what-is-a-data-intelligence-platform)
> - [Data guides (Google Cloud docs)](https://docs.databricks.com/gcp/en/guides/)
