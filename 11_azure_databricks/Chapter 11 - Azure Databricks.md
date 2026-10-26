---
type: chapter
status: written
part: 2
level: 11
section: Azure Databricks
summary: Databricks as a first-party Microsoft service, with its own identity, networking, billing, and integrations.
prev: "[[MosaicML and Open Models]]"
next: "[[Azure Databricks Overview]]"
notes:
  - "[[Azure Databricks Overview]]"
  - "[[First-Party Microsoft Service]]"
  - "[[Creating an Azure Databricks Workspace]]"
  - "[[Managed Resource Group]]"
  - "[[Microsoft Entra ID Integration]]"
  - "[[VNet Injection]]"
  - "[[Secure Cluster Connectivity]]"
  - "[[Azure Private Link]]"
  - "[[ADLS and Access Connectors]]"
  - "[[Azure Key Vault Secret Scopes]]"
  - "[[Azure Data Factory with Databricks]]"
  - "[[Microsoft Fabric and OneLake vs Databricks]]"
  - "[[Power BI on Azure Databricks]]"
  - "[[Azure Billing and Commit Units]]"
  - "[[Azure Monitor and Diagnostic Logs]]"
  - "[[Customer-Managed Keys on Azure]]"
last_verified: 2026-10-25
tags:
  - chapter
---

# Chapter 11 - Azure Databricks

> [!story] Context
> Part 1 ended with [[Chapter 10 - AI and ML|chapter 10]] and [[MosaicML and Open Models]], completing the description of the Databricks platform itself. Part 2 covers how that platform runs on each cloud. This chapter covers Microsoft Azure, where Databricks is a first-party Microsoft service with its own provisioning, identity, networking, billing, and integrations.

**Databricks as a first-party Microsoft service, with its own identity, networking, billing, and integrations.**

## The story of this chapter

### Era

Databricks announced Azure Databricks in November 2017 as a "first party" Microsoft service, built through a year-long joint effort with Microsoft, and the service became generally available on March 22, 2018. Unlike Databricks on AWS and Google Cloud, which are sold by Databricks directly or through a cloud marketplace, Azure Databricks is created as an Azure resource and billed by Microsoft under the customer's Azure subscription terms. See [[Azure Databricks Overview]] and [[First-Party Microsoft Service]].

### Provisioning

A workspace is an Azure resource of type `Microsoft.Databricks/workspaces`, deployed with the Azure portal, Azure CLI, Bicep, ARM templates, or Terraform ([[Creating an Azure Databricks Workspace]]). Premium is the only pricing tier for new workspaces since April 1, 2026, and remaining Standard tier workspaces are upgraded automatically in a phased rollout that starts October 1, 2026. Serverless workspaces run only serverless compute on Databricks-managed default storage. Classic workspaces run cluster VMs in your subscription, inside a [[Managed Resource Group]] protected by a system deny assignment.

### Identity

[[Microsoft Entra ID Integration|Microsoft Entra ID]] is built in. Automatic identity management, on by default for accounts created after August 1, 2025, syncs users, groups (including nested groups), and service principals without a SCIM application. Conditional access policies target the AzureDatabricks application.

### Network

Classic compute can be deployed into a VNet you own with [[VNet Injection]], using two delegated subnets. [[Secure Cluster Connectivity]] removes public IPs from cluster nodes, and Microsoft plans to require it for all classic workspaces. [[Azure Private Link]] adds private endpoints for user access (front-end), cluster-to-control-plane traffic (back-end), and browser authentication. Serverless compute is governed separately by network connectivity configurations.

### Data access and secrets

[[Unity Catalog]] reaches ADLS Gen2 through an Access Connector's managed identity, which needs no stored secret and can pass storage firewalls through resource instance rules ([[ADLS and Access Connectors]]). Remaining credentials can be read from Azure Key Vault through read-only [[Azure Key Vault Secret Scopes]].

### Microsoft integrations

[[Azure Data Factory with Databricks|Azure Data Factory]] runs Lakeflow jobs with the Databricks Job activity. [[Microsoft Fabric and OneLake vs Databricks|Microsoft Fabric]] overlaps with Databricks and integrates through mirrored Unity Catalog catalogs (GA) and read-only OneLake catalog federation. [[Power BI on Azure Databricks|Power BI]] connects with Entra ID SSO and, since October 15, 2026, a generally available ADBC driver, and semantic models can be published from Unity Catalog.

### Operations

Usage is metered in DBUs on the Azure invoice and can be prepaid with one- or three-year Databricks commit units ([[Azure Billing and Commit Units]]). Diagnostic settings send audit events to Azure Monitor, while the `system.access.audit` table covers account-level events too ([[Azure Monitor and Diagnostic Logs]]). [[Customer-Managed Keys on Azure]] encrypt managed services, workspace storage, and managed disks with Key Vault or Managed HSM keys.

### Next

[[Chapter 12 - Databricks on AWS]] covers the same concepts on Amazon Web Services, and the [[Cloud Comparison - Azure vs AWS vs GCP]] hub compares all three side by side.

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[Azure Databricks Overview]] | 101 Beginner | What is different when Databricks is sold, billed, and run as a Microsoft Azure service. |
| 2 | [[First-Party Microsoft Service]] | 201 Practitioner | Microsoft provisioning, billing, and support, and why Azure Databricks is unusual among Databricks clouds. |
| 3 | [[Creating an Azure Databricks Workspace]] | 101 Beginner | Step by step in the Azure portal, CLI, or Bicep, covering pricing tier, workspace type, region, networking, and resource group. |
| 4 | [[Managed Resource Group]] | 201 Practitioner | The locked resource group Azure creates to hold a classic workspace's VMs, disks, network resources, and workspace storage account. |
| 5 | [[Microsoft Entra ID Integration]] | 201 Practitioner | Sign-in, automatic identity management, SCIM, conditional access, tokens, and service principals with Microsoft Entra ID. |
| 6 | [[VNet Injection]] | 301 Advanced | Deploying Azure Databricks classic compute into your own Azure virtual network, with subnet sizing, delegation, NSG rules, and egress. |
| 7 | [[Secure Cluster Connectivity]] | 301 Advanced | No public IPs on classic cluster nodes, with all control traffic initiated outbound to a relay, and the egress options that go with it. |
| 8 | [[Azure Private Link]] | 401 Expert | Private endpoints for inbound (front-end), classic compute (back-end), and serverless connections to Azure Databricks without the public internet. |
| 9 | [[ADLS and Access Connectors]] | 301 Advanced | How Unity Catalog reaches ADLS Gen2 through an Access Connector's managed identity, including storage behind firewalls. |
| 10 | [[Azure Key Vault Secret Scopes]] | 301 Advanced | Using Azure Key Vault as the read-only backing store for a Databricks secret scope, with its permission model and limits. |
| 11 | [[Azure Data Factory with Databricks]] | 201 Practitioner | Calling Azure Databricks from Azure Data Factory pipelines with the Job and Notebook activities, and when to use Lakeflow Jobs instead. |
| 12 | [[Microsoft Fabric and OneLake vs Databricks]] | 201 Practitioner | How Microsoft Fabric and Azure Databricks overlap, how to choose between them, and how mirroring and OneLake federation connect them. |
| 13 | [[Power BI on Azure Databricks]] | 201 Practitioner | Entra single sign-on from Power BI, the ADBC driver, publishing semantic models from Unity Catalog, and DirectQuery guidance. |
| 14 | [[Azure Billing and Commit Units]] | 201 Practitioner | Pay-as-you-go billing on the Azure invoice, Databricks commit unit (DBCU) prepurchase plans, and Azure and Databricks cost tools. |
| 15 | [[Azure Monitor and Diagnostic Logs]] | 301 Advanced | Sending Azure Databricks diagnostic (audit) logs to Log Analytics, Storage, or Event Hubs, and when to use the audit log system table instead. |
| 16 | [[Customer-Managed Keys on Azure]] | 401 Expert | Encrypting Azure Databricks managed services, workspace storage (DBFS root), and managed disks with your own Azure Key Vault or Managed HSM keys. |

<!-- GENERATED:reading-order END -->

> [!nextup] Next
> [[Azure Databricks Overview]] covers what is different when Databricks is sold, billed, and run as a Microsoft Azure service.
