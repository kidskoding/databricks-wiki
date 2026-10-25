---
type: path
status: written
level: 80
section: Learning Paths
depth: 301
summary: Every Azure-specific rabbit hole in order.
personas:
  - admin
chapter: "[[Chapter 80 - Learning Paths]]"
prev: "[[Path - One-Person Data Team]]"
next: "[[Path - AWS Deep Dive]]"
evolved_from: []
evolved_into: []
cloud_equivalent:
  - "[[Path - AWS Deep Dive]]"
  - "[[Path - Google Cloud Deep Dive]]"
related:
  - "[[Azure Databricks Overview]]"
  - "[[First-Party Microsoft Service]]"
  - "[[Creating an Azure Databricks Workspace]]"
  - "[[Managed Resource Group]]"
  - "[[Microsoft Entra ID Integration]]"
  - "[[ADLS and Access Connectors]]"
  - "[[VNet Injection]]"
  - "[[Secure Cluster Connectivity]]"
  - "[[Azure Private Link]]"
  - "[[Azure Key Vault Secret Scopes]]"
  - "[[Azure Monitor and Diagnostic Logs]]"
  - "[[Customer-Managed Keys on Azure]]"
  - "[[Power BI on Azure Databricks]]"
  - "[[Unity Catalog]]"
  - "[[Path - Platform Admin]]"
  - "[[Cloud Comparison - Azure vs AWS vs GCP]]"
aliases:
  - Azure Path
  - Azure Databricks Path
prereqs:
  - "[[Path - Platform Admin]]"
unlocks: []
clouds:
  - azure
mastery: new
last_verified: 2026-10-25
tags:
  - path
---

# Path - Azure Deep Dive

> [!persona] Who this is for
> **Who:** an Azure admin, cloud architect, or security lead who runs, or is about to run, Azure Databricks. Also the analyst or engineer in a Microsoft environment who needs to know what differs on Azure.
> **Goal:** understand the Azure-specific parts of the platform: the first-party service model, the managed resource group, Entra ID, ADLS access, VNet injection, Private Link, Key Vault, Azure Monitor, and Power BI.
> **Outcome:** you can deploy a production-ready Azure Databricks workspace with private networking, Entra-based identity, governed ADLS access, customer-managed keys, and logs flowing into Azure Monitor.

## Before you start

Read [[Path - Platform Admin]] first, or at least its Stages 1 to 3; this path assumes you know the cloud-neutral ideas. You need an Azure subscription where you can create resource groups, virtual networks, storage accounts, and Key Vaults, and Entra ID rights to create groups and app registrations. Free Edition does not support this path.

## The route

### Stage 1: Azure Databricks differences (101 to 201)

**Goal:** learn what Microsoft runs, what you own, and how billing works.

1. [[Azure Databricks Overview]]: what changes when Microsoft sells and runs Databricks.
2. [[First-Party Microsoft Service]] (201): Microsoft support, the Azure portal, and Azure billing.
3. [[Creating an Azure Databricks Workspace]]: tier, region, networking, and resource group choices.
4. [[Managed Resource Group]] (201): the locked group that holds Databricks' VMs, disks, and storage.
5. [[Azure Data Lake Storage]]: ADLS Gen2, where your data lives.
6. [[Azure Billing and Commit Units]] (201): pay-as-you-go, pre-purchase, and Azure Cost Management.
7. [[Control Plane and Compute Plane]] (201): the split, seen through Azure resources.

> [!check] Checkpoint
> In the Azure portal, create a Premium-tier Azure Databricks workspace in a test resource group. Open its managed resource group and list what is inside (storage account, network, and later VMs). Try to delete one resource and note the deny assignment that blocks the deletion. In Azure Cost Management, filter by the workspace's resources.

### Stage 2: Identity and data access (201 to 301)

**Goal:** bring in Entra ID identities and give Unity Catalog governed access to ADLS.

1. [[Microsoft Entra ID Integration]] (201): sign-in, automatic identity management, and service principals.
2. [[Users Groups and Service Principals]] (201): the Databricks side of those identities.
3. [[SCIM Provisioning]] (301): when you still need SCIM, and when automatic identity management covers it.
4. [[Metastore]] (201): one per region, and how Azure workspaces attach.
5. [[ADLS and Access Connectors]] (301): the managed identity Unity Catalog uses to reach ADLS.
6. [[Storage Credentials and External Locations]] (301): the Unity Catalog objects built on that connector.
7. [[Managed Identity]]: the glossary entry for Azure's password-free identities.
8. [[Azure Key Vault Secret Scopes]] (301): Key Vault as the backing store for secrets.
9. [[Secrets Management]] (201): secret scopes in general.

> [!check] Checkpoint
> Create an Access Connector for Azure Databricks, grant its managed identity **Storage Blob Data Contributor** on an ADLS Gen2 container, and register it in Unity Catalog as a storage credential. Then run `CREATE EXTERNAL LOCATION raw_zone URL 'abfss://<container>@<account>.dfs.core.windows.net/raw' WITH (STORAGE CREDENTIAL <name>);` and `LIST 'abfss://...'` from a notebook. Create a Key Vault-backed secret scope and read one secret.

### Stage 3: Private networking (301 to 401)

**Goal:** keep cluster traffic off the public internet and restrict front-end access.

1. [[Network Security Overview]] (301): the map of front-end, back-end, and serverless controls.
2. [[VNet Injection]] (301): Databricks compute in your own virtual network.
3. [[Secure Cluster Connectivity]] (301): no public IPs on nodes, outbound-only control traffic.
4. [[Azure Private Link]] (401): private front-end and back-end connections.
5. [[Serverless Network Security]] (401): network connectivity configurations and private endpoints for serverless.
6. [[IP Access Lists]] (301): restrict who can reach the workspace.
7. [[VPC and VNet]] and [[Subnet]]: the glossary entries behind all of the above.

> [!check] Checkpoint
> Deploy a second workspace with VNet injection into a VNet you created, with two delegated subnets and secure cluster connectivity (no public IP) enabled. Start a cluster and confirm in the Azure portal that its VMs have no public IP addresses. Sketch, on paper, where Private Link endpoints would go for front-end and back-end traffic.

### Stage 4: Operate, encrypt, and integrate (201 to 401)

**Goal:** log, encrypt, and connect Azure Databricks to the rest of the Microsoft estate.

1. [[Azure Monitor and Diagnostic Logs]] (301): diagnostic settings to Log Analytics, Storage, or Event Hubs.
2. [[Audit Logs]] (301): the Databricks-side audit trail.
3. [[System Tables]] (201): audit and billing as SQL.
4. [[Encryption]] (301): what is encrypted by default.
5. [[Customer-Managed Keys on Azure]] (401): your own Key Vault keys for managed services and storage.
6. [[Compliance Security Profile]] (401): hardened settings for regulated workloads.
7. [[Power BI on Azure Databricks]] (201): Entra single sign-on and publishing to the Power BI service.
8. [[Azure Data Factory with Databricks]] (201): calling Databricks from ADF, and when to use Lakeflow instead.
9. [[Microsoft Fabric and OneLake vs Databricks]] (201): where Fabric overlaps, competes, and integrates.
10. [[Disaster Recovery]] (401): paired regions and what you must plan yourself.

> [!check] Checkpoint
> Add a diagnostic setting on the workspace that sends logs to a Log Analytics workspace, run a few notebook commands, and query the resulting tables in Log Analytics. Compare one event with the same event in `system.access.audit`. Publish a dataset from Unity Catalog to the Power BI service (or connect Power BI Desktop with Entra sign-in) and confirm row-level permissions still apply.

## Rabbit holes

- **The same ideas elsewhere:** [[Path - AWS Deep Dive]], [[Path - Google Cloud Deep Dive]], and [[Cloud Comparison - Azure vs AWS vs GCP]].
- **Automation:** [[Terraform Provider]] for workspaces, networks, and grants; [[Declarative Automation Bundles]] for jobs and pipelines.
- **Migrating a Microsoft estate:** [[Migrating from SQL Server]], [[Migrating ETL Tools]] (SSIS), [[Migrating BI Reports]].
- **Governance extras:** [[Row Filters and Column Masks]], [[Attribute-Based Access Control]], [[Data Classification]].
- **Cost:** [[Compute Policies]], [[Budgets and Usage Dashboards]], [[Tagging for Chargeback]].

## You are done when

- You can explain what the first-party model means for support, billing, and the portal.
- You can list what is in the managed resource group and explain why you cannot change it.
- Identities come from Entra ID, and automation uses Entra service principals.
- Unity Catalog reaches ADLS through an Access Connector, not keys.
- Your production workspace uses VNet injection, secure cluster connectivity, and a Private Link design.
- Logs reach Azure Monitor, keys can be customer-managed, and Power BI works with single sign-on.

> [!nextup] Next
> [[Path - AWS Deep Dive]] covers the same topics for Databricks on AWS.

> [!sources]- Sources (last verified: 2026-10-25)
> - Route assembled on 2026-10-25 from chapter 11 (Azure Databricks), chapter 14, and chapter 07 of the vault index (`llms.txt`). Product facts and official Microsoft Learn links live in each linked note's `[!sources]` callout; [[Unity Catalog]] cites the Access Connector documentation.
> - Role names, subnet requirements, and portal steps in the checkpoints were not re-checked for this path; confirm them in [[ADLS and Access Connectors]] and [[VNet Injection]] before deploying.
