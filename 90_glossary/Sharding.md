---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Splitting one database's rows across several independent database servers, each holding a subset called a shard."
related:
  - "[[Partitions]]"
  - "[[NoSQL]]"
  - "[[Scaling Up vs Scaling Out]]"
  - "[[Distributed Systems]]"
  - "[[Data Skew]]"
  - "[[Replication]]"
aliases:
  - "shard"
  - "shards"
  - "horizontal partitioning"
  - "shard key"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Sharding

> [!eli5] Summary
> Sharding splits one big database into several smaller ones on different machines. Each machine holds part of the rows, for example customers A to M on one and N to Z on another.

**In data work:** Sharding is horizontal partitioning across separate database instances. All shards share the same schema, and each holds the rows whose **shard key** falls in its range or hash bucket. It lets an application [[Scaling Up vs Scaling Out|scale out]] writes beyond what one server can handle.
- **Range sharding:** Rows with keys in a range go to one shard. Simple, but popular ranges create hot spots.
- **Hash sharding:** A hash of the key picks the shard. Spreads load evenly but makes range queries touch every shard.

The shard key is the most important choice and is hard to change later. Queries that span shards must be sent to each shard and merged, which is slower. Many [[NoSQL]] databases were designed to shard automatically. Most small businesses never need sharding; one well-sized database handles their transaction volume.

**In Databricks:** You do not shard Delta tables. Data lives in [[Object Storage|object storage]], and Spark splits each query into tasks over [[Partitions|partitions]] at run time, so compute scales out without a fixed shard layout. The same hot-spot problem appears as [[Data Skew|data skew]], where one key holds far more rows than others.

Seen in: [[NoSQL]], [[Distributed Systems]], [[Scaling Up vs Scaling Out]]

## Recall

Sharding::Horizontally partitioning a database's rows across separate database servers by a shard key.
What is the hardest sharding decision to change later?::The shard key.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Data Partitioning Guidance (Microsoft patterns and practices)](https://learn.microsoft.com/en-us/previous-versions/msp-n-p/dn589795(v=pandp.10))
> - [Database Sharding: Concepts and Examples (MongoDB)](https://www.mongodb.com/resources/products/capabilities/database-sharding-explained)
> - [Skew and spill (AWS)](https://docs.databricks.com/aws/en/optimizations/spark-ui-guide/long-spark-stage-page)
