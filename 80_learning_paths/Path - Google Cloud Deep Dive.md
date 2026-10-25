---
type: path
status: written
level: 80
section: Learning Paths
depth: 301
summary: Every Google Cloud-specific rabbit hole in order.
personas:
  - admin
chapter: "[[Chapter 80 - Learning Paths]]"
prev: "[[Path - AWS Deep Dive]]"
next: "[[Path - Certification Prep]]"
evolved_from: []
evolved_into: []
cloud_equivalent:
  - "[[Path - Azure Deep Dive]]"
  - "[[Path - AWS Deep Dive]]"
related:
  - "[[Databricks on Google Cloud Overview]]"
  - "[[Account Setup on Google Cloud]]"
  - "[[Google Cloud Marketplace and Billing]]"
  - "[[Compute on Google Cloud]]"
  - "[[Google Service Accounts]]"
  - "[[GCS Access via Unity Catalog]]"
  - "[[Customer-Managed VPC on Google Cloud]]"
  - "[[Private Service Connect]]"
  - "[[Customer-Managed Keys on Google Cloud]]"
  - "[[BigQuery Integration]]"
  - "[[Unity Catalog]]"
  - "[[Path - Platform Admin]]"
  - "[[Cloud Comparison - Azure vs AWS vs GCP]]"
aliases:
  - GCP Path
  - Google Cloud Path
prereqs:
  - "[[Path - Platform Admin]]"
unlocks: []
clouds:
  - gcp
mastery: new
last_verified: 2026-10-25
tags:
  - path
---

# Path - Google Cloud Deep Dive

> [!persona] Who this is for
> **Who:** a Google Cloud admin, architect, or security lead running Databricks on GCP, and engineers who work alongside BigQuery.
> **Goal:** understand the GCP-specific parts of the platform: subscribing through Google Cloud Marketplace, Compute Engine-based clusters, Google service accounts, GCS access, customer-managed VPCs, Private Service Connect, Cloud KMS keys, and BigQuery.
> **Outcome:** you can deploy a production workspace in your own VPC with Private Service Connect, governed GCS access through service accounts, customer-managed keys, and a clear plan for working alongside BigQuery.

## Before you start

Read [[Path - Platform Admin]] first, or at least its Stages 1 to 3. You need a Google Cloud project with billing, rights to create VPCs, service accounts, GCS buckets, and Cloud KMS keys, and the ability to subscribe to Databricks in Google Cloud Marketplace. Free Edition does not support this path.

## The route

### Stage 1: How Databricks runs on Google Cloud (101 to 201)

**Goal:** learn how subscription and billing work, and where compute runs.

1. [[Databricks on Google Cloud Overview]]: what is different on GCP.
2. [[Account Setup on Google Cloud]]: subscribing through Marketplace and creating the first workspace.
3. [[Google Cloud Marketplace and Billing]] (201): Databricks on the Google Cloud bill.
4. [[Control Plane and Compute Plane]] (201): the split, seen through GCP projects.
5. [[Compute on Google Cloud]] (301): classic clusters on Compute Engine VMs, after the move off GKE.
6. [[Google Cloud Storage]]: where your data lives.

> [!check] Checkpoint
> Subscribe to Databricks from Google Cloud Marketplace in a test project and create a workspace. In the Google Cloud console, find the resources Databricks created (buckets, network, and the VMs once a cluster starts). In Cloud Billing reports, filter by the Databricks marketplace line.

### Stage 2: Identity and data access (201 to 301)

**Goal:** understand the service accounts involved and give Unity Catalog governed GCS access.

1. [[Google Service Accounts]] (301): how Databricks and clusters authenticate to Google Cloud.
2. [[GCS Access via Unity Catalog]] (301): storage credentials backed by Databricks-managed service accounts.
3. [[Storage Credentials and External Locations]] (301): the Unity Catalog objects on top.
4. [[Metastore]] (201): one per region.
5. [[Users Groups and Service Principals]] (201): Databricks identities.
6. [[Single Sign-On]] (201) and [[SCIM Provisioning]] (301): connecting Google Workspace, Okta, or Entra ID.

> [!check] Checkpoint
> Create a storage credential in Catalog Explorer; Databricks shows the service account email it generated. Grant that service account access to one GCS bucket in IAM (for example **Storage Legacy Bucket Reader** and **Storage Object Admin**, as the linked note specifies), then create an external location on `gs://<bucket>/raw` and run `LIST 'gs://<bucket>/raw'`.

### Stage 3: Private networking (301 to 401)

**Goal:** run compute in your VPC and reach Databricks privately.

1. [[Network Security Overview]] (301): the full map of controls.
2. [[Customer-Managed VPC on Google Cloud]] (301): your own VPC and subnets for Databricks compute.
3. [[Private Service Connect]] (401): private front-end and back-end connectivity.
4. [[Serverless Network Security]] (401): connectivity and egress controls for serverless.
5. [[IP Access Lists]] (301): restricting front-end access.
6. [[VPC and VNet]] and [[Subnet]]: the related glossary entries.

> [!check] Checkpoint
> Create a VPC with a subnet sized for your cluster count, register it as a network configuration in the account console, and deploy a workspace into it. Start a cluster and confirm its VMs have only private IPs. Sketch where the Private Service Connect endpoints for the workspace front end and the back-end relay would go.

### Stage 4: Keys, BigQuery, and operations (201 to 401)

**Goal:** manage your own keys, work with BigQuery, and operate the platform securely.

1. [[Encryption]] (301): defaults, and where your keys fit.
2. [[Customer-Managed Keys on Google Cloud]] (401): Cloud KMS keys you control.
3. [[BigQuery Integration]] (201): reading, writing, and federating BigQuery.
4. [[Google BigQuery]] (201): the warehouse you are integrating with or moving from.
5. [[Lakehouse Federation]] (201): querying BigQuery in place from Unity Catalog.
6. [[Migrating from Google BigQuery]] (301): exports to GCS and SQL conversion.
7. [[Audit Logs]] (301): the audit trail on GCP.
8. [[Terraform Provider]] (301): automating workspaces, networks, and grants.
9. [[Disaster Recovery]] (401): multi-region plans on Google Cloud.

> [!check] Checkpoint
> Create a BigQuery connection in Unity Catalog and a foreign catalog on it, then query one BigQuery table from the SQL Editor and join it with a Delta table. Check the query profile to see what was pushed down to BigQuery. Write down which Cloud KMS keys you would create for managed services and for workspace storage.

## Rabbit holes

- **The same ideas elsewhere:** [[Path - Azure Deep Dive]], [[Path - AWS Deep Dive]], and [[Cloud Comparison - Azure vs AWS vs GCP]].
- **Regulated workloads:** [[Compliance Security Profile]]. Check that note for which standards are available on Google Cloud, since support differs by cloud.
- **Containers history:** [[Kubernetes]], to understand what the move off GKE changed.
- **Cost:** [[Compute Policies]], [[Budgets and Usage Dashboards]], [[Cost Optimization Checklist]].
- **Automation:** [[Declarative Automation Bundles]] and [[Databricks SDKs and REST API]].

## You are done when

- You can explain how the Marketplace subscription, billing, and workspace creation fit together.
- You know which Google service accounts Databricks uses and what each can reach.
- Unity Catalog reaches GCS through storage credentials, not keys in notebooks.
- Production compute runs in your own VPC, with a Private Service Connect design.
- You can query BigQuery from Databricks and decide between federation and migration.
- You know which Cloud KMS keys protect what.

> [!nextup] Next
> [[Path - Certification Prep]] maps Databricks certifications to the notes in this vault.

> [!sources]- Sources (last verified: 2026-10-25)
> - Route assembled on 2026-10-25 from chapter 13 (Databricks on Google Cloud), chapter 14, and chapter 07 of the vault index (`llms.txt`). Product facts and official documentation links live in each linked note's `[!sources]` callout; [[Unity Catalog]] cites the GCS external location documentation.
> - Exact IAM roles, subnet sizing, and BigQuery federation details in the checkpoints were not re-checked for this path; confirm them in [[GCS Access via Unity Catalog]], [[Customer-Managed VPC on Google Cloud]], and [[BigQuery Integration]].
