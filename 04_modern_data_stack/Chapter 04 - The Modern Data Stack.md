---
type: chapter
status: stub
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
last_verified:
tags:
  - chapter
---

# Chapter 04 - The Modern Data Stack

> [!story] Previously
> (to write)

**Cloud warehouses, data lakes, Kafka, Airflow, and dbt, and the messy two-tier world they created.**

## The story of this chapter

(to write)

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
