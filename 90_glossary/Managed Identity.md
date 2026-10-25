---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "An Azure identity that Azure creates and rotates for a resource, so no passwords or keys are stored."
related:
  - "[[ADLS and Access Connectors]]"
  - "[[Storage Credentials and External Locations]]"
  - "[[Microsoft Entra ID Integration]]"
  - "[[Azure Data Lake Storage]]"
  - "[[Instance Profiles]]"
  - "[[Google Service Accounts]]"
aliases:
  - "Azure managed identity"
  - "MSI"
  - "Managed Service Identity"
  - "system-assigned managed identity"
  - "user-assigned managed identity"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Managed Identity

> [!eli5] Summary
> A managed identity is an identity that Azure creates and maintains for a service, so the service can access other resources without a stored password or key.

**In data work:** In Microsoft Azure, a managed identity is an identity in Microsoft Entra ID that belongs to an Azure resource rather than a person. Azure handles its credentials and rotates them automatically, and you grant it roles (such as Storage Blob Data Contributor) like any other identity. An identity can be system-assigned (created with the resource) or user-assigned (a separate resource you attach). Instead of pasting a storage key into a script, a small firm gives the script's resource an identity and grants it access to one container.

**In Databricks:** Azure Databricks uses a managed identity through the [[ADLS and Access Connectors|Access Connector for Azure Databricks]], a resource that holds the identity. A [[Storage Credentials and External Locations|storage credential]] in [[Unity Catalog]] points at that connector, so Databricks reaches [[Azure Data Lake Storage]] without secrets to rotate. The connector deploys with a system-assigned identity by default, and the docs note that a managed identity, unlike a service principal, can reach storage accounts protected by network rules. The AWS counterpart is an IAM role (see [[Instance Profiles]] and [[Cross-Account IAM Role]]), and on Google Cloud it is a [[Google Service Accounts|service account]].

Seen in: [[ADLS and Access Connectors]], [[Storage Credentials and External Locations]], [[Microsoft Entra ID Integration]]

## Recall

Managed Identity::An Azure-managed identity for a resource with automatic credentials; Azure Databricks uses one via the Access Connector to reach ADLS without keys.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Use Azure managed identities in Unity Catalog to access storage](https://learn.microsoft.com/en-us/azure/databricks/connect/unity-catalog/cloud-storage/azure-managed-identities)
> - [Connect to an ADLS Gen2 external location (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/connect/unity-catalog/cloud-storage/storage-credentials)
