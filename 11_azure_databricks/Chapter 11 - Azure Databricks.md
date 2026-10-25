---
type: chapter
status: stub
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
last_verified:
tags:
  - chapter
---

# Chapter 11 - Azure Databricks

> [!story] Previously
> (to write)

**Databricks as a first-party Microsoft service, with its own identity, networking, billing, and integrations.**

## The story of this chapter

(to write)

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

> [!nextup] Up next
> [[Azure Databricks Overview]]
