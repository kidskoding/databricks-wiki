---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The service that stores an organization's user accounts and groups and authenticates sign-ins for other applications."
related:
  - "[[Single Sign-On]]"
  - "[[SCIM Provisioning]]"
  - "[[Microsoft Entra ID Integration]]"
  - "[[Users Groups and Service Principals]]"
  - "[[Authentication - Tokens and OAuth]]"
  - "[[OAuth]]"
aliases:
  - "IdP"
  - "Okta"
  - "directory service"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Identity Provider

> [!eli5] Summary
> An identity provider is the central system that holds a company's user accounts. Other applications ask it to confirm who someone is instead of keeping their own passwords.

**In data work:** An identity provider (IdP) stores identities and groups and handles sign-in, including multi-factor authentication. Applications trust it through standards such as SAML and OpenID Connect (built on [[OAuth]]) for [[Single Sign-On|single sign-on]], and SCIM for provisioning users and groups. Common IdPs are Microsoft Entra ID (formerly Azure Active Directory), Okta, Google Workspace, and Ping Identity. A central IdP means disabling one account removes access to every connected application.

**In Databricks:** Databricks accounts use an IdP for [[Single Sign-On]], and [[SCIM Provisioning]] syncs users and groups. On Azure Databricks, automatic identity management lets admins add Entra ID users, groups, and service principals directly, with Entra ID as the source of record; Microsoft recommends it over SCIM, and it is enabled by default for accounts created after 1 August 2025. Do not provision the same identities through both methods. Permissions in Unity Catalog are granted to these groups ([[Users Groups and Service Principals]]).

Seen in: [[Single Sign-On]], [[SCIM Provisioning]], [[Microsoft Entra ID Integration]], [[Users Groups and Service Principals]]

## Recall

What does an identity provider do?::It stores identities and groups and authenticates sign-ins for other applications.
What does Azure Databricks recommend over SCIM for syncing Entra ID identities?::Automatic identity management.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Automatic identity management (Azure)](https://learn.microsoft.com/en-us/azure/databricks/admin/users-groups/automatic-identity-management/)
> - [Automatic Identity Management for Entra ID is generally available (Databricks blog)](https://www.databricks.com/blog/automatic-identity-management-entra-id-now-generally-available-azure-databricks)
