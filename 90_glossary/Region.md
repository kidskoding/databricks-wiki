---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A geographic area where a cloud provider runs its data centers, such as East US or Frankfurt."
related:
  - "[[Availability Zone]]"
  - "[[Accounts and Workspaces]]"
  - "[[Metastore]]"
  - "[[Disaster Recovery]]"
  - "[[Egress]]"
  - "[[Choosing a Cloud for Databricks]]"
aliases:
  - "cloud region"
  - "Azure region"
  - "AWS region"
  - "GCP region"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Region

> [!eli5] Summary
> A region is a geographic area where a cloud provider operates data centers. The region you choose affects speed, available services, cost, and where data is legally stored.

**In data work:** Cloud providers group data centers into regions (for example `eastus2` on Azure, `us-east-1` on AWS, `europe-west3` on Google Cloud). Each region contains several [[Availability Zone|availability zones]]. You choose a region for each resource, and the choice affects speed for users, which services are available, legal data residency, and cost, since moving data between regions incurs [[Egress|egress]] charges. A Canadian clinic might pick a Canadian region to keep patient data in the country.

**In Databricks:** Every Databricks workspace lives in one cloud region, and its storage should be in the same region to avoid slow, costly cross-region traffic. [[Unity Catalog]] allows one [[Metastore|metastore]] per region, shared by the workspaces in that region; to reach data in another region's metastore, Databricks recommends Databricks-to-Databricks [[OpenSharing]]. Feature availability (serverless, some AI models) varies by region, so check before choosing. [[Disaster Recovery]] plans often pair a primary region with a secondary one.

Seen in: [[Accounts and Workspaces]], [[Metastore]], [[Disaster Recovery]], [[Choosing a Cloud for Databricks]]

## Recall

Region::A geographic group of cloud data centers; a Databricks workspace runs in one region, with one Unity Catalog metastore per region.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Phase 3: Design Unity Catalog architecture (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/lakehouse-architecture/deployment-guide/unity-catalog)
> - [Phase 3: Design Unity Catalog architecture (Google Cloud)](https://docs.databricks.com/gcp/en/lakehouse-architecture/deployment-guide/unity-catalog)
