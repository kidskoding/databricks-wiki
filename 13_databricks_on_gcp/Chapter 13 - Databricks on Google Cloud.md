---
type: chapter
status: written
part: 2
level: 13
section: Databricks on Google Cloud
summary: Databricks on GCP, covering Google service accounts, Private Service Connect, GCS, and BigQuery.
prev: "[[Databricks on AWS GovCloud]]"
next: "[[Databricks on Google Cloud Overview]]"
notes:
  - "[[Databricks on Google Cloud Overview]]"
  - "[[Account Setup on Google Cloud]]"
  - "[[Compute on Google Cloud]]"
  - "[[Customer-Managed VPC on Google Cloud]]"
  - "[[Private Service Connect]]"
  - "[[Google Service Accounts]]"
  - "[[GCS Access via Unity Catalog]]"
  - "[[BigQuery Integration]]"
  - "[[Google Cloud Marketplace and Billing]]"
  - "[[Customer-Managed Keys on Google Cloud]]"
last_verified: 2026-10-25
tags:
  - chapter
---

# Chapter 13 - Databricks on Google Cloud

> [!story] Context
> [[Chapter 12 - Databricks on AWS]] ended with [[Databricks on AWS GovCloud]], completing the AWS deployment model. This chapter covers Google Cloud, where Databricks is bought through Google Cloud Marketplace and acts in your project through Google service accounts.

**Databricks on GCP, covering Google service accounts, Private Service Connect, GCS, and BigQuery.**

## The story of this chapter

**Era.** Databricks launched on Google Cloud in February 2021, the newest of its three clouds. It is sold through Google Cloud Marketplace: a subscription links the Databricks account to one Cloud Billing account, and workspaces are created at `accounts.gcp.databricks.com`. See [[Databricks on Google Cloud Overview]] and [[Account Setup on Google Cloud]].

**Workspaces.** Serverless workspaces use serverless compute and Databricks-managed default storage, and create no billable resources in your project. Classic workspaces run compute in a Google Cloud project you choose, with two GCS buckets for workspace system data. Workspace configuration cannot be changed after creation, so region, network, and keys are decided up front.

**Compute.** At launch, Databricks on Google Cloud was built on Google Kubernetes Engine (GKE). Current documentation describes classic compute as Compute Engine VMs in the workspace VPC, and the GKE-specific network settings are deprecated ([[Compute on Google Cloud]]). Machine types, preemptible VMs, local SSDs, and the cluster's service account are set with `gcp_attributes`.

**Network.** A [[Customer-Managed VPC on Google Cloud]] uses one subnet per workspace, supports Shared VPC host and service projects, and is the recommended choice for new classic workspaces; Databricks plans to deprecate creation with a Databricks-managed VPC. [[Private Service Connect]] adds private front-end and back-end endpoints (a workspace endpoint and an SCC relay endpoint) on the Enterprise plan. Public access stays allowed on PSC workspaces until you restrict it. Serverless compute reaches Cloud Storage and BigQuery through Private Google Access.

**Identity and data access.** All Google Cloud access goes through [[Google Service Accounts]]: a workspace service account that manages Compute Engine resources, the `databricks-compute` account that cluster VMs run as by default, and optional custom accounts. For governed data, Unity Catalog storage credentials use a service account that Databricks generates, which you grant bucket roles ([[GCS Access via Unity Catalog]]). [[BigQuery Integration]] offers read-only Lakehouse Federation through the BigQuery Storage API and a Spark connector for reads and writes.

**Cost and keys.** Databricks usage appears on the Google Cloud bill through the Marketplace subscription, next to Compute Engine, storage, and networking charges for classic compute; cloud credits do not apply to serverless usage ([[Google Cloud Marketplace and Billing]]). [[Customer-Managed Keys on Google Cloud]] encrypt managed services, the workspace buckets, and compute disks with Cloud KMS keys, attached at workspace creation on the Enterprise tier.

**Next.** [[Chapter 14 - Admin Security and Cost]] covers the administration tasks that apply on every cloud: identity, network security, encryption, compliance, cost, and automation.

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[Databricks on Google Cloud Overview]] | 101 Beginner | How Databricks runs on Google Cloud and what is different there. |
| 2 | [[Account Setup on Google Cloud]] | 101 Beginner | Subscribing through Google Cloud Marketplace and creating the first workspace. |
| 3 | [[Compute on Google Cloud]] | 301 Advanced | How classic clusters run on Compute Engine VMs (after the move off GKE). |
| 4 | [[Customer-Managed VPC on Google Cloud]] | 301 Advanced | Bringing your own VPC and subnets for Databricks compute. |
| 5 | [[Private Service Connect]] | 401 Expert | Private connectivity between your VPC and Databricks on Google Cloud. |
| 6 | [[Google Service Accounts]] | 301 Advanced | How Databricks and clusters authenticate to Google Cloud resources. |
| 7 | [[GCS Access via Unity Catalog]] | 301 Advanced | Storage credentials backed by Google service accounts for governed GCS access. |
| 8 | [[BigQuery Integration]] | 201 Practitioner | Reading and writing BigQuery from Databricks, and federation. |
| 9 | [[Google Cloud Marketplace and Billing]] | 201 Practitioner | Paying for Databricks through the Google Cloud bill. |
| 10 | [[Customer-Managed Keys on Google Cloud]] | 401 Expert | Encrypting with Cloud KMS keys you control. |

<!-- GENERATED:reading-order END -->

> [!nextup] Up next
> [[Databricks on Google Cloud Overview]]
