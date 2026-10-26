---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "One customer's isolated instance of a shared cloud service; in Azure, a Microsoft Entra ID tenant is an organization's directory of users, groups, and apps."
related:
  - "[[Microsoft Entra ID Integration]]"
  - "[[Accounts and Workspaces]]"
  - "[[Resource Group]]"
  - "[[Identity Provider]]"
  - "[[SaaS PaaS and IaaS]]"
  - "[[Azure Databricks Overview]]"
aliases:
  - "Entra tenant"
  - "Azure AD tenant"
  - "directory"
  - "multi-tenant"
  - "tenant ID"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Tenant

> [!eli5] Summary
> A tenant is one organization's private space inside a service that many organizations share. In Microsoft's cloud, it is the company's directory of people and apps.

**In data work:** The word has two common meanings.
- **Multi-tenancy:** A [[SaaS PaaS and IaaS|SaaS]] provider runs one platform for many customers (tenants) and isolates each customer's data and configuration. Single-tenant means a customer gets dedicated infrastructure.
- **Identity tenant:** In Microsoft Azure, a Microsoft Entra ID tenant is the directory that holds an organization's users, groups, service principals, and app registrations. Every Azure subscription trusts exactly one tenant. A small business that uses Microsoft 365 already has one.

**In Databricks:** On Azure, the tenant decides who can sign in.
- **Users:** You can add any user who belongs to the Microsoft Entra ID tenant of your Azure Databricks workspace.
- **Groups:** Groups from the tenant can be synced to the Azure Databricks account automatically (automatic identity management) or through a [[SCIM]] connector.
- **Service principals:** Microsoft Entra service principals from the tenant can authenticate to Azure Databricks.

See [[Microsoft Entra ID Integration]]. On AWS and Google Cloud, there is no equivalent cloud-level tenant for Databricks sign-in; you connect your [[Identity Provider|identity provider]] to the Databricks account with [[Single Sign-On|SSO]] instead (see [[Accounts and Workspaces]]).

Seen in: [[Microsoft Entra ID Integration]], [[Azure Databricks Overview]], [[Accounts and Workspaces]]

## Recall

Tenant (Azure)::A Microsoft Entra ID directory holding an organization's users, groups, and apps; Azure Databricks users come from it.
Multi-tenant::One service instance shared by many customers, with each customer's data isolated.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Manage users (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/admin/users-groups/users)
> - [Groups (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/admin/users-groups/groups)
> - [Authenticate with Microsoft Entra service principals (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/auth/azure-sp)
> - [Automatic identity management (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/admin/users-groups/automatic-identity-management/)
