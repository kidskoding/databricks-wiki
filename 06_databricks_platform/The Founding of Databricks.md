---
type: concept
status: written
level: 6
section: Databricks Platform
depth: 101
summary: How Spark's creators started a company in 2013 to run Spark in the cloud.
personas:
  - everyone
  - owner
chapter: "[[Chapter 06 - The Databricks Platform]]"
prev: "[[Chapter 06 - The Databricks Platform]]"
next: "[[The Data Intelligence Platform]]"
evolved_from:
  - "[[AMPLab and the Birth of Spark]]"
  - "[[The Pain of Hadoop]]"
evolved_into:
  - "[[The Data Intelligence Platform]]"
cloud_equivalent: []
related:
  - "[[Apache Spark]]"
  - "[[Apache Software Foundation]]"
  - "[[Delta Lake]]"
  - "[[MLflow]]"
  - "[[The Lakehouse Paper]]"
  - "[[Azure Databricks Overview]]"
  - "[[Databricks on Google Cloud Overview]]"
  - "[[MosaicML and Open Models]]"
  - "[[Open Source]]"
  - "[[Timeline of Data Engineering]]"
aliases:
  - Databricks history
  - History of Databricks
prereqs:
  - "[[AMPLab and the Birth of Spark]]"
  - "[[Apache Spark]]"
unlocks:
  - "[[The Data Intelligence Platform]]"
  - "[[Accounts and Workspaces]]"
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

# The Founding of Databricks

Mastery: `INPUT[inlineSelect(option(new), option(learning), option(solid)):mastery]`

> [!story] Context
> [[Chapter 05 - The Lakehouse|Chapter 05]] covers a fast engine ([[Apache Spark]]), inexpensive storage ([[Data Lakes]]), and a design for reliable tables on top of it ([[Delta Lake]]). Running all of it still requires a team of cluster specialists. Databricks, Inc. was founded to provide these tools as a managed service.

> [!eli5] Summary
> A group of university researchers built a fast tool for processing large amounts of data and released it for free. Companies adopted it but found it hard to set up and operate. In 2013 the same researchers founded Databricks, a company that runs the tool for customers on rented computers in the cloud.

> [!analogy]- Analogy: the recipe and the restaurant
> | Restaurant | Databricks |
> |---|---|
> | Free published recipe | [[Apache Spark]] |
> | Cooking at home with your own equipment | Running Spark yourself on [[Apache Hadoop\|Hadoop]] clusters |
> | Restaurant run by the recipe's authors, with extra dishes | Databricks, with service-only features |
> | New recipes added to the free cookbook | New open-source projects ([[Delta Lake]], [[MLflow]]) |

## Background

By 2013, [[Apache Spark]] was a prominent project in big data. It came out of UC Berkeley's AMPLab (see [[AMPLab and the Birth of Spark]]) and ran many jobs far faster than [[MapReduce]] because it kept data in memory.

Using Spark in practice still involved the problems described in [[The Pain of Hadoop]]:

- You had to buy or rent servers, install Hadoop and Spark, tune memory settings, and patch them.
- Clusters sat idle and cost money at night, or were too small at month end.
- Data scientists, engineers, and analysts used different tools and passed files around.
- The commercial Hadoop vendors ([[Cloudera and Hortonworks]]) sold software for your own data center, not a service in the cloud.

The cloud ([[Servers and the Cloud]]) made a different model possible: rent computers by the minute, start a [[Cluster|cluster]] when needed, and discard it afterward. The Spark creators founded Databricks to make that model easy to use.

## Overview

Databricks, Inc. was founded in **2013** by the team that started the Spark research project at UC Berkeley. It is headquartered in San Francisco. The seven co-founders and their titles, as listed on the Databricks founders page in October 2026:

| Co-founder | Title (October 2026) |
|---|---|
| **Ali Ghodsi** | Co-founder and Chief Executive Officer. CEO since January 2016. |
| **Ion Stoica** | Co-founder and Executive Chair. The company's first CEO, until January 2016. |
| **Matei Zaharia** | Co-founder and CTO. Lead author of the first Spark papers (HotCloud 2010, NSDI 2012). |
| **Reynold Xin** | Co-founder and Chief Architect. |
| **Patrick Wendell** | Co-founder and VP of Engineering. |
| **Andy Konwinski** | Co-founder. |
| **Arsalan Tavakoli-Shiraji** | Co-founder and SVP of Field Engineering. |

The company's model has two parts:

1. **Keep the core open:** The same year it was founded, the team donated Spark to the [[Apache Software Foundation]]. Spark became a top-level Apache project on February 27, 2014. Later projects followed the same pattern: [[MLflow]] (2018), [[Delta Lake]] (2019), and [[Unity Catalog]] (open-sourced in 2024).
2. **Sell the service, not the software:** Databricks does not sell a box to install. It sells a managed cloud platform that runs open engines on the customer's cloud account, plus features that exist only in the service (like [[Photon]] and serverless compute).

## How it works

Each stage of the company's history addresses a problem described in chapters 02 to 05:

```mermaid
timeline
  title Databricks, from lab to platform
  2009 : Spark starts at Berkeley AMPLab
  2013 : Databricks founded : Spark donated to Apache
  2014 : Databricks Cloud shown at Spark Summit
  2015 : Platform generally available
  2016 : Ali Ghodsi becomes CEO
  2018 : Azure Databricks GA : MLflow open-sourced
  2019 : Delta Lake open-sourced
  2020 : Lakehouse idea published
  2021 : Databricks on Google Cloud
  2023 : MosaicML joins : Data Intelligence Platform
  2024 : Unity Catalog open-sourced
```

Key milestones:

- **A hosted notebook on AWS (2014–2015):** The first product was "Databricks Cloud", unveiled at Spark Summit in June 2014 and generally available in June 2015: a web page with notebooks attached to Spark clusters that Databricks started and stopped for you on Amazon Web Services. This is the seed of today's [[Notebooks]] and [[All-Purpose Compute]].
- **Azure as a first-party service (2018):** Microsoft and Databricks built **Azure Databricks** together. It became generally available on March 22, 2018. It is sold and billed by Microsoft and appears in the Azure portal like any other Azure service. See [[Azure Databricks Overview]] and [[First-Party Microsoft Service]].
- **The lakehouse (2020):** In January 2020 Databricks published the blog post "What is a Lakehouse?". Customers had long copied data from lakes into warehouses ([[The Two-Tier Architecture Problem]]). Databricks proposed that one open table format could serve both purposes. See [[The Lakehouse Idea]] and [[The Lakehouse Paper]].
- **Google Cloud (2021):** Databricks launched on Google Cloud in February 2021 and became generally available there in May 2021. The same platform now runs on all three major clouds. See [[Databricks on Google Cloud Overview]].
- **The AI turn (2023 onward):** Databricks completed its acquisition of MosaicML in July 2023 to train and serve large models ([[MosaicML and Open Models]]) and, from November 2023, began calling its product the [[The Data Intelligence Platform|Data Intelligence Platform]].

## Small-business considerations

> [!smallbiz] Small-business considerations
> The founding model has two practical consequences for a 10-person company:
> - **Open formats lower your risk:** Because Delta Lake, Spark, and MLflow are open source, your data sits in your own cloud storage in open files. If you leave Databricks, the files stay readable. This reduces [[Vendor Lock-In]].
> - **You are buying operations, not software:** Databricks exists because running Spark yourself is hard. If you only have a few gigabytes in spreadsheets, you may not need it yet. See [[When Databricks Is Not the Right Fit]] and [[Databricks vs Alternatives for Small Teams]].

## Cloud differences

> [!azure]- Azure Databricks
> Azure Databricks became generally available in March 2018. It is a [[First-Party Microsoft Service|first-party Microsoft service]]: you create it in the Azure portal, Microsoft bills it on your Azure invoice, and support runs through Microsoft. See [[Azure Databricks Overview]].

> [!aws]- Databricks on AWS
> AWS was the original cloud. Databricks on AWS is sold by Databricks directly or through AWS Marketplace. See [[Databricks on AWS Overview]].

> [!gcp]- Databricks on Google Cloud
> The newest of the three, launched in February 2021 (generally available in May 2021) and sold directly or through Google Cloud Marketplace. See [[Databricks on Google Cloud Overview]].

## Advanced topics

> [!deepdive]- Advanced topics (301–401)
> - **The open-core pattern:** Databricks open-sources the engine or format and competes on the managed service: performance (Photon, Predictive I/O), operations (serverless), and governance (the hosted Unity Catalog). When you evaluate a feature, check whether it is in the open project or only in the service.
> - **Research DNA:** Many core features started as papers: Spark's RDDs (NSDI 2012), Spark SQL (SIGMOD 2015), the lakehouse paper, and [[Photon]] (SIGMOD 2022). Reading them explains design choices the docs take for granted.
> - **Acquisitions shape the product map:** The MosaicML acquisition closed in July 2023 and became much of Mosaic AI. Tabular, the company founded by the original creators of [[Apache Iceberg]], was acquired in June 2024, which is why Databricks now treats Iceberg and Delta as peers (see [[Delta UniForm]]). Databricks agreed to acquire the serverless Postgres company Neon in May 2025, and [[Lakebase]] is built on Neon technology.
> - **Founders' roles:** On January 11, 2016, Ion Stoica moved from CEO to Executive Chairman, Ali Ghodsi (then VP of Engineering and Product) became CEO, and Patrick Wendell became VP of Engineering. Titles change over time; the founders page on databricks.com is the current reference.

## Common misconceptions

> [!confusion] Databricks is not Apache Spark
> **Spark** is a free, open-source engine owned by the Apache Software Foundation. **Databricks** is a company and a paid cloud platform that runs Spark (and much more). Databricks employees write a large share of Spark's code, but Spark does not belong to Databricks.

> [!confusion] Databricks is more than hosted Spark
> It started that way. The platform now includes SQL warehouses, governance, pipelines, dashboards, a Postgres database, and AI tools. Many users never write Spark code at all.

## Recall

When was Databricks founded?::2013.
Where did the Databricks founders work before starting the company?::UC Berkeley's AMPLab, where Apache Spark was created.
Name the seven Databricks co-founders.::Ali Ghodsi, Andy Konwinski, Arsalan Tavakoli-Shiraji, Ion Stoica, Matei Zaharia, Patrick Wendell, and Reynold Xin.
When and where did the Spark research project start?::At the UC Berkeley AMPLab in 2009. It was open-sourced in early 2010.
What did the founders do with Spark the year Databricks was founded?::Donated it to the Apache Software Foundation.
What was Databricks' first product?::A hosted notebook service ("Databricks Cloud") that ran Spark clusters on AWS for you.
Which three open-source projects did Databricks create after Spark?::MLflow (2018), Delta Lake (2019), and the open-source Unity Catalog (2024).
In what year did Azure Databricks become generally available?::2018.

## Next steps

> [!path] Learning path
> **Needs first:** [[AMPLab and the Birth of Spark]], [[Apache Spark]]
> **Unlocks next:** [[The Data Intelligence Platform]], [[Accounts and Workspaces]]

> [!nextup] Next
> [[The Data Intelligence Platform]] describes what the platform includes today and what Databricks means by "data intelligence".

> [!sources]- Sources (last verified: 2026-10-25)
> - [What is Databricks? (AWS)](https://docs.databricks.com/aws/en/introduction)
> - [What is Azure Databricks?](https://learn.microsoft.com/en-us/azure/databricks/introduction/)
> - [What is a data intelligence platform (Databricks blog)](https://www.databricks.com/blog/what-is-a-data-intelligence-platform)
> - [About Databricks](https://www.databricks.com/company/about-us)
> - [Databricks founders](https://www.databricks.com/company/founders)
> - [Databricks announces changes in leadership team (January 11, 2016)](https://www.databricks.com/company/newsroom/press-releases/databricks-announces-changes-leadership-team-align-rapid-growth)
> - [Databricks unveils Apache Spark-based cloud platform (June 30, 2014)](https://www.databricks.com/blog/2014/06/30/databricks-unveils-spark-based-cloud-platform.html)
> - [Databricks is now generally available (June 15, 2015)](https://www.databricks.com/blog/2015/06/15/databricks-is-now-generally-available.html)
> - [Apache Spark history](https://spark.apache.org/history.html)
> - [Spark becomes top-level Apache project (February 27, 2014)](https://spark.apache.org/news/spark-becomes-tlp.html)
> - [Apache Spark research papers](https://spark.apache.org/research.html)
> - [Databricks delivers Microsoft Azure Databricks (March 22, 2018)](https://www.databricks.com/company/newsroom/press-releases/databricks-delivers-microsoft-azure-databricks-addressing-customer-demand)
> - [Introducing MLflow (June 5, 2018)](https://www.databricks.com/blog/2018/06/05/introducing-mlflow-an-open-source-machine-learning-platform.html)
> - [Databricks open sources Delta Lake (April 24, 2019)](https://www.databricks.com/company/newsroom/press-releases/databricks-open-sources-delta-lake-for-data-lake-reliability)
> - [What is a Lakehouse? (January 30, 2020)](https://www.databricks.com/blog/2020/01/30/what-is-a-data-lakehouse.html)
> - [Lakehouse research paper](https://www.databricks.com/research/lakehouse-a-new-generation-of-open-platforms-that-unify-data-warehousing-and-advanced-analytics)
> - [Announcing the launch of Databricks on Google Cloud (February 17, 2021)](https://www.databricks.com/blog/2021/02/17/announcing-the-launch-of-databricks-on-google-cloud.html)
> - [Databricks on Google Cloud now generally available (May 4, 2021)](https://www.databricks.com/blog/2021/05/04/databricks-on-google-cloud-now-generally-available.html)
> - [Databricks completes acquisition of MosaicML (July 19, 2023)](https://www.databricks.com/company/newsroom/press-releases/databricks-completes-acquisition-mosaicml)
> - [Databricks + Tabular (completed June 2024)](https://www.databricks.com/blog/databricks-tabular)
> - [Databricks open sources Unity Catalog (June 12, 2024)](https://www.databricks.com/company/newsroom/press-releases/databricks-open-sources-unity-catalog-creating-industrys-only-open)
> - [Databricks agrees to acquire Neon (May 14, 2025)](https://www.databricks.com/company/newsroom/press-releases/databricks-agrees-acquire-neon-help-developers-deliver-ai-systems)
> - [Databricks launches Lakebase (June 11, 2025)](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-lakebase-new-class-operational-database-ai-apps)
> - [Photon: A Fast Query Engine for Lakehouse Systems (SIGMOD 2022, ACM)](https://dl.acm.org/doi/10.1145/3514221.3526054)
