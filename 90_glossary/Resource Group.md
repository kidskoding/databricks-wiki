---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "An Azure container that holds related resources, such as a Databricks workspace, so you can manage, secure, and bill them together."
related:
  - "[[Managed Resource Group]]"
  - "[[Creating an Azure Databricks Workspace]]"
  - "[[Azure Databricks Overview]]"
  - "[[Tenant]]"
  - "[[Tagging for Chargeback]]"
  - "[[Azure Billing and Commit Units]]"
aliases:
  - "Azure resource group"
  - "resource groups"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Resource Group

> [!eli5] Summary
> A resource group is a labeled folder in Azure for related cloud resources. You can grant access, apply tags, track cost, or delete everything in it together.

**In data work:** Every Azure resource belongs to exactly one resource group inside a subscription. Teams group resources by application, environment, or lifecycle, for example `rg-analytics-prod` and `rg-analytics-dev`. Azure role-based access control and tags can be applied at the resource group level and are inherited by the resources inside it, which makes it a natural unit for permissions and cost reports. Deleting a resource group deletes everything in it.

**In Databricks:** An Azure Databricks workspace involves two resource groups.
- **Your resource group:** Holds the workspace resource itself, and often its VNet, storage, and Key Vault. You choose it when [[Creating an Azure Databricks Workspace|creating the workspace]].
- **The [[Managed Resource Group|managed resource group]]:** Holds the infrastructure Azure Databricks manages for classic compute, such as the workspace storage account, virtual machines, and (for a managed VNet) a NAT gateway. It is set by the `managedResourceGroupId` property, and you cannot modify its contents. Serverless compute mode workspaces do not use one.

A small business can use one resource group per environment and tag it for cost tracking (see [[Tagging for Chargeback]]). AWS and Google Cloud organize resources differently: AWS uses accounts and tags, and Google Cloud uses projects.

Seen in: [[Managed Resource Group]], [[Creating an Azure Databricks Workspace]], [[Azure Databricks Overview]]

## Recall

Resource group::An Azure container for related resources that share access control, tags, and lifecycle.
Which resource group holds the infrastructure Azure Databricks manages for a workspace?::The managed resource group.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Microsoft.Databricks/workspaces: Bicep, ARM template, and Terraform AzAPI reference](https://learn.microsoft.com/en-us/azure/templates/microsoft.databricks/workspaces)
> - [az databricks workspace (Azure CLI)](https://learn.microsoft.com/en-us/cli/azure/databricks/workspace?view=azure-cli-latest)
> - [Deploy a workspace using the Azure portal](https://learn.microsoft.com/en-us/azure/databricks/admin/workspace/create-workspace)
> - [Enable secure cluster connectivity (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/security/network/classic/secure-cluster-connectivity)
