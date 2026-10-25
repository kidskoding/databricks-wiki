---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Keeping copies of data in more than one place so it survives failures or is closer to users."
related:
  - "[[Disaster Recovery]]"
  - "[[Fault Tolerance]]"
  - "[[Object Storage]]"
  - "[[Change Data Capture]]"
  - "[[Lakeflow Connect]]"
  - "[[Availability Zone]]"
aliases:
  - "data replication"
  - "replica"
  - "geo-replication"
  - "GRS"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Replication

> [!eli5] Summary
> Replication is keeping synchronized copies of data in more than one place, so the data survives a failure or is closer to the people using it.

**In data work:** Replication copies data to other disks, machines, zones, or regions and keeps those copies in sync. Synchronous replication waits for every copy before confirming a write (safer, slower); asynchronous replication confirms first and copies after (faster, may lose the last few seconds). Cloud [[Object Storage|object storage]] replicates within a region automatically, and you can pay for cross-region (geo) replication. [[HDFS]] stored three copies of each block by default. Replication of a database into an analytics platform is a related idea, usually done with [[Change Data Capture]].

**In Databricks:** Databricks relies on your cloud storage's built-in replication for durability. For [[Disaster Recovery]], teams copy Delta tables to a second region with deep clone (Databricks has written about clones for exactly this) or storage replication, and keep code in Git so workspaces can be recreated. [[Lakeflow Connect]] replicates data from operational databases and SaaS apps into the lakehouse. Replication protects against hardware failure but not against bad writes, which is where [[Time Travel]] helps.

Seen in: [[Disaster Recovery]], [[Fault Tolerance]], [[HDFS]]

## Recall

Replication::Keeping synced copies of data in several places for durability or speed; it guards against hardware loss, not bad writes.

> [!sources]- Sources (last verified: 2026-10-25)
> - [What is HDFS? (Databricks glossary)](https://www.databricks.com/glossary/hadoop-distributed-file-system-hdfs)
> - [Delta Clones Simplify Disaster Recovery (Databricks blog)](https://www.databricks.com/blog/2021/04/20/attack-of-the-delta-clones-against-disaster-recovery-availability-complexity.html)
> - [Disaster recovery (AWS)](https://docs.databricks.com/aws/en/admin/disaster-recovery)
