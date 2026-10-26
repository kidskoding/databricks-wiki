---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "System for Cross-domain Identity Management: a standard API identity providers use to create, update, and remove users and groups in other applications automatically."
related:
  - "[[SCIM Provisioning]]"
  - "[[Identity Provider]]"
  - "[[Users Groups and Service Principals]]"
  - "[[SAML]]"
  - "[[Single Sign-On]]"
  - "[[Microsoft Entra ID Integration]]"
aliases:
  - "System for Cross-domain Identity Management"
  - "SCIM 2.0"
  - "SCIM API"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# SCIM

> [!eli5] Summary
> SCIM keeps the list of people in an app in sync with the company directory. When someone joins, changes teams, or leaves, the app updates automatically.

**In data work:** [[Single Sign-On|SSO]] decides how users sign in; it does not create or remove accounts. SCIM fills that gap. It is a REST API with standard resources for `Users` and `Groups`. The [[Identity Provider|identity provider]] acts as the SCIM client and pushes changes to each application. Offboarding is the main benefit: when an employee is deactivated in the directory, SCIM deactivates them in every connected app, instead of relying on someone to remember each one.

**In Databricks:** Databricks exposes SCIM APIs, and Databricks recommends provisioning at the **account** level; workspace-level SCIM is legacy.
1. Create a SCIM token in the [[Account Console|account console]].
2. Configure the Databricks SCIM connector in your IdP (Okta, Microsoft Entra ID, and others).
3. Assign users and groups to the connector.
4. Assign the synced groups to workspaces and grant them privileges.

On Azure Databricks, automatic identity management can sync users and groups from Microsoft Entra ID without a SCIM connector. For a team of ten, SCIM may be optional at first, but it is worth setting up before the first departure. Setup steps are in [[SCIM Provisioning]].

Seen in: [[SCIM Provisioning]], [[Users Groups and Service Principals]], [[Microsoft Entra ID Integration]]

## Recall

SCIM::A standard REST API that identity providers use to provision and deprovision users and groups in applications.
At what level does Databricks recommend SCIM provisioning?::The account level.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Sync users and groups from your identity provider using SCIM (AWS)](https://docs.databricks.com/aws/en/admin/users-groups/scim/)
> - [Sync users and groups from Microsoft Entra ID using SCIM (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/admin/users-groups/scim/)
> - [Configure SCIM provisioning for Okta (AWS)](https://docs.databricks.com/aws/en/admin/users-groups/scim/okta)
> - [Automatic identity management (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/admin/users-groups/automatic-identity-management/)
> - [Provision identities to a Databricks workspace, legacy (GCP)](https://docs.databricks.com/gcp/en/archive/workspace-level-scim)
