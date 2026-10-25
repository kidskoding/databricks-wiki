---
type: chapter
status: written
part: 1
level: 4
section: The Modern Data Stack
summary: Cloud warehouses, data lakes, Kafka, Airflow, and dbt, and the messy two-tier world they created.
prev: "[[Spark UI]]"
next: "[[Data Warehouses]]"
notes:
  - "[[Data Warehouses]]"
  - "[[Amazon Redshift]]"
  - "[[Snowflake]]"
  - "[[Google BigQuery]]"
  - "[[Data Lakes]]"
  - "[[Object Storage]]"
  - "[[Amazon S3]]"
  - "[[Azure Data Lake Storage]]"
  - "[[Google Cloud Storage]]"
  - "[[Data Swamps]]"
  - "[[Apache Kafka]]"
  - "[[Apache Airflow]]"
  - "[[dbt]]"
  - "[[Fivetran and ELT Tools]]"
  - "[[BI Tools]]"
  - "[[The Two-Tier Architecture Problem]]"
last_verified: 2026-10-25
tags:
  - chapter
---

# Chapter 04 - The Modern Data Stack

> [!story] Context
> [[Chapter 03 - Apache Spark|Chapter 03]] ended with [[Apache Spark]] as a fast, general engine for processing large datasets, inspected through the [[Spark UI]]. This chapter covers the cloud-era systems that surrounded such engines in the 2010s, and the architecture they produced.

**Cloud warehouses, data lakes, Kafka, Airflow, and dbt, and the messy two-tier world they created.**

## The story of this chapter

This chapter covers the period from the mid-2000s to around 2020, when data platforms moved from on-premises hardware to the public cloud. The systems in this chapter came from different vendors and open-source projects. Combined, they became known as the *modern data stack*.

**Cloud data warehouses.** A [[Data Warehouses|data warehouse]] is a database organized for analytical SQL: integrated history, schema-on-write, and fast reads. Before the cloud, warehouses were appliances sized for peak load and paid for whether used or not. AWS announced [[Amazon Redshift]] in November 2012 and made it generally available in February 2013, offering a managed warehouse billed by the hour. [[Snowflake]] separated storage from compute, so independent virtual warehouses could scale and suspend on their own. [[Google BigQuery]], based on Google's internal Dremel system, removed cluster sizing altogether with a serverless model. These products made SQL analytics fast and easy to start, but they store curated data in proprietary formats.

**Data lakes on object storage.** Data that did not fit warehouse tables, such as logs, JSON, images, and raw history, went into [[Data Lakes|data lakes]]: raw files in open formats, with structure applied at read time. Lakes began on [[HDFS]] and moved to cloud [[Object Storage|object storage]]: [[Amazon S3]] (launched in 2006, addressed as `s3://`), [[Azure Data Lake Storage]] (Blob Storage with a hierarchical namespace, addressed as `abfss://`), and [[Google Cloud Storage]] (addressed as `gs://`). Object storage made storing data cheap and durable and separated storage from compute. However, plain files have no transactions, no row-level updates, and no built-in governance. Without catalogs, ownership, and quality controls, many lakes became [[Data Swamps|data swamps]].

**Moving, scheduling, and modeling data.** A set of specialized tools grew around the lake and the warehouse:

| Job | Tool in this chapter | Role |
|---|---|---|
| Stream events between systems | [[Apache Kafka]] | Distributed, replicated log of events |
| Schedule and order pipelines | [[Apache Airflow]] | Python-defined DAGs of tasks |
| Transform data with SQL | [[dbt]] | Version-controlled, tested SQL models |
| Copy data from SaaS and databases | [[Fivetran and ELT Tools]] | Managed, incremental connectors |
| Present results | [[BI Tools]] | Dashboards and reports (Power BI, Tableau, Looker) |

Each tool is good at one job, and each one is another product to license, run, secure, and connect.

**The resulting architecture.** Because lakes lacked reliability and warehouses lacked openness and support for machine learning, most organizations ran both: raw data in the lake, with a curated subset copied into the warehouse for BI. This is [[The Two-Tier Architecture Problem|the two-tier architecture]]. The 2021 lakehouse paper (CIDR 2021) lists its costs: data duplicated across systems, ETL pipelines that can fail or drift, warehouse data that lags behind the lake, machine learning that needs exports from proprietary storage, higher total cost of ownership, and lock-in. Governance is also split, with permissions and lineage configured separately in each system.

**How this connects to Databricks.** Most tools in this chapter still integrate with Databricks. Kafka is a streaming source and sink for Structured Streaming. Airflow triggers Lakeflow Jobs through the Databricks provider. dbt runs on Databricks through the `dbt-databricks` adapter. Fivetran connects through Partner Connect. Power BI and Tableau connect to SQL warehouses. Redshift, Snowflake, and BigQuery can be queried in place through Lakehouse Federation. Each concept note includes an **In Databricks today** callout that describes where its job is handled in Databricks and how the original tool connects.

[[Chapter 05 - The Lakehouse]] describes the alternative to the two-tier design: one copy of data in open table formats on object storage, with warehouse-grade transactions, performance, and governance.

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[Data Warehouses]] | 101 Beginner | A database built for analytics, which is clean, fast, and expensive. |
| 2 | [[Amazon Redshift]] | 201 Practitioner | AWS's cloud data warehouse, launched in 2012. |
| 3 | [[Snowflake]] | 201 Practitioner | The cloud warehouse that separated storage and compute, and Databricks' best-known rival. |
| 4 | [[Google BigQuery]] | 201 Practitioner | Google's serverless warehouse. |
| 5 | [[Data Lakes]] | 101 Beginner | Dumping every file into cheap storage first and figuring it out later. |
| 6 | [[Object Storage]] | 101 Beginner | Cheap, effectively unlimited cloud file storage, which is the floor the lakehouse stands on. |
| 7 | [[Amazon S3]] | 101 Beginner | AWS object storage, the original cloud data lake. |
| 8 | [[Azure Data Lake Storage]] | 101 Beginner | Azure's object storage built for analytics (ADLS Gen2). |
| 9 | [[Google Cloud Storage]] | 101 Beginner | Google Cloud's object storage. |
| 10 | [[Data Swamps]] | 101 Beginner | What a data lake becomes without rules, with no trust, no quality, and no one knowing what is where. |
| 11 | [[Apache Kafka]] | 201 Practitioner | The event-streaming backbone that moves live data between systems. |
| 12 | [[Apache Airflow]] | 201 Practitioner | The open-source scheduler that runs pipelines as DAGs written in Python. |
| 13 | [[dbt]] | 201 Practitioner | SQL transformations with software engineering habits like version control and tests. |
| 14 | [[Fivetran and ELT Tools]] | 201 Practitioner | Managed connectors that copy SaaS and database data into a warehouse. |
| 15 | [[BI Tools]] | 101 Beginner | Power BI, Tableau, Looker, and friends, the charts at the end of every pipeline. |
| 16 | [[The Two-Tier Architecture Problem]] | 101 Beginner | Running a lake and a warehouse side by side means two copies, two bills, stale data, and no AI on warehouse data. |

<!-- GENERATED:reading-order END -->

> [!nextup] Up next
> [[Data Warehouses]]
