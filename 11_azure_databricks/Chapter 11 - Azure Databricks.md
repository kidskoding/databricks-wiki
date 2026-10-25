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

**Era.** Databricks announced Azure Databricks in November 2017 as a "first party" Microsoft service, built through a year-long joint effort with Microsoft, and the service became generally available on March 22, 2018. Unlike Databricks on AWS and Google Cloud, which are sold by Databricks directly or through a cloud marketplace, Azure Databricks is created as an Azure resource and billed by Microsoft under the customer's Azure subscription terms. See [[Azure Databricks Overview]] and [[First-Party Microsoft Service]].

**Provisioning.** A workspace is an Azure resource of type `Microsoft.Databricks/workspaces`, deployed with the Azure portal, Azure CLI, Bicep, ARM templates, or Terraform ([[Creating an Azure Databricks Workspace]]). Premium is the only pricing tier for new workspaces since April 1, 2026, and remaining Standard tier workspaces were scheduled for automatic upgrade on October 1, 2026. Serverless workspaces run only serverless compute on Databricks-managed default storage. Classic workspaces run cluster VMs in your subscription, inside a [[Managed Resource Group]] protected by a system deny assignment.

**Identity.** [[Microsoft Entra ID Integration|Microsoft Entra ID]] is built in. Automatic identity management, on by default for accounts created after August 1, 2025, syncs users, groups (including nested groups), and service principals without a SCIM application. Conditional access policies target the AzureDatabricks application.

**Network.** Classic compute can be deployed into a VNet you own with [[VNet Injection]], using two delegated subnets. [[Secure Cluster Connectivity]] removes public IPs from cluster nodes, and Microsoft plans to require it for all classic workspaces. [[Azure Private Link]] adds private endpoints for user access (front-end), cluster-to-control-plane traffic (back-end), and browser authentication. Serverless compute is governed separately by network connectivity configurations.

**Data access and secrets.** [[Unity Catalog]] reaches ADLS Gen2 through an Access Connector's managed identity, which needs no stored secret and can pass storage firewalls through resource instance rules ([[ADLS and Access Connectors]]). Remaining credentials can be read from Azure Key Vault through read-only [[Azure Key Vault Secret Scopes]].

**Microsoft integrations.** [[Azure Data Factory with Databricks|Azure Data Factory]] runs Lakeflow jobs with the Databricks Job activity. [[Microsoft Fabric and OneLake vs Databricks|Microsoft Fabric]] overlaps with Databricks and integrates through mirrored Unity Catalog catalogs (GA) and read-only OneLake catalog federation. [[Power BI on Azure Databricks|Power BI]] connects with Entra ID SSO and, since October 15, 2026, a generally available ADBC driver, and semantic models can be published from Unity Catalog.

**Operations.** Usage is metered in DBUs on the Azure invoice and can be prepaid with one- or three-year Databricks commit units ([[Azure Billing and Commit Units]]). Diagnostic settings send audit events to Azure Monitor, while the `system.access.audit` table covers account-level events too ([[Azure Monitor and Diagnostic Logs]]). [[Customer-Managed Keys on Azure]] encrypt managed services, workspace storage, and managed disks with Key Vault or Managed HSM keys.

**Next.** [[Chapter 12 - Databricks on AWS]] covers the same concepts on Amazon Web Services, and the [[Cloud Comparison - Azure vs AWS vs GCP]] hub compares all three side by side.

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[Azure Databricks Overview]] | 101 Beginner | What is different when Databricks is sold and run by Microsoft. |
| 2 | [[First-Party Microsoft Service]] | 201 Practitioner | Microsoft support, the Azure portal, Azure billing, and why Azure Databricks is unusual among Databricks clouds. |
| 3 | [[Creating an Azure Databricks Workspace]] | 101 Beginner | Step by step in the Azure portal, covering pricing tier, region, networking, and resource group. |
| 4 | [[Managed Resource Group]] | 201 Practitioner | The locked resource group Azure creates to hold Databricks' VMs, disks, and storage. |
| 5 | [[Microsoft Entra ID Integration]] | 201 Practitioner | Sign-in, automatic identity management, and service principals with Microsoft Entra ID. |
| 6 | [[VNet Injection]] | 301 Advanced | Deploying Databricks compute into your own Azure virtual network. |
| 7 | [[Secure Cluster Connectivity]] | 301 Advanced | No public IPs on cluster nodes, with all control traffic going outbound. |
| 8 | [[Azure Private Link]] | 401 Expert | Private connections to the workspace and control plane without the public internet. |
| 9 | [[ADLS and Access Connectors]] | 301 Advanced | How Unity Catalog reaches ADLS Gen2 through a managed identity. |
| 10 | [[Azure Key Vault Secret Scopes]] | 301 Advanced | Using Azure Key Vault as the backing store for Databricks secrets. |
| 11 | [[Azure Data Factory with Databricks]] | 201 Practitioner | Calling Databricks from ADF pipelines, and when to use Lakeflow instead. |
| 12 | [[Microsoft Fabric and OneLake vs Databricks]] | 201 Practitioner | How Fabric and Azure Databricks overlap, compete, and integrate. |
| 13 | [[Power BI on Azure Databricks]] | 201 Practitioner | Entra single sign-on into Power BI, publishing to the Power BI service, and DirectQuery tips. |
| 14 | [[Azure Billing and Commit Units]] | 201 Practitioner | Pay-as-you-go on the Azure bill, pre-purchase plans, and Azure cost tools. |
| 15 | [[Azure Monitor and Diagnostic Logs]] | 301 Advanced | Sending Databricks logs to Log Analytics, Storage, or Event Hubs. |
| 16 | [[Customer-Managed Keys on Azure]] | 401 Expert | Encrypting managed services and storage with your own Key Vault keys. |

<!-- GENERATED:reading-order END -->

> [!nextup] Next
> [[Azure Databricks Overview]] covers what is different when Databricks is sold, billed, and run as a Microsoft Azure service.
