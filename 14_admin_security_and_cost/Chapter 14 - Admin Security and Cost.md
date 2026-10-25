---
type: chapter
status: stub
part: 2
level: 14
section: Admin, Security & Cost
summary: Running Databricks safely and cheaply, covering identity, networking, encryption, compliance, and FinOps.
prev: "[[Customer-Managed Keys on Google Cloud]]"
next: "[[Account Console]]"
notes:
  - "[[Account Console]]"
  - "[[Users Groups and Service Principals]]"
  - "[[SCIM Provisioning]]"
  - "[[Single Sign-On]]"
  - "[[Authentication - Tokens and OAuth]]"
  - "[[Admin Roles]]"
  - "[[Compute Policies]]"
  - "[[Secrets Management]]"
  - "[[Network Security Overview]]"
  - "[[IP Access Lists]]"
  - "[[Serverless Network Security]]"
  - "[[Encryption]]"
  - "[[Compliance Security Profile]]"
  - "[[Cost Management Basics]]"
  - "[[Budgets and Usage Dashboards]]"
  - "[[Tagging for Chargeback]]"
  - "[[Cost Optimization Checklist]]"
  - "[[Terraform Provider]]"
  - "[[Disaster Recovery]]"
last_verified:
tags:
  - chapter
---

# Chapter 14 - Admin Security and Cost

> [!story] Previously
> (to write)

**Running Databricks safely and cheaply, covering identity, networking, encryption, compliance, and FinOps.**

## The story of this chapter

(to write)

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[Account Console]] | 201 Practitioner | The account-level admin site for workspaces, users, metastores, and billing. |
| 2 | [[Users Groups and Service Principals]] | 201 Practitioner | The three kinds of identity, and why groups should own everything. |
| 3 | [[SCIM Provisioning]] | 301 Advanced | Syncing users and groups automatically from Entra ID, Okta, or another IdP. |
| 4 | [[Single Sign-On]] | 201 Practitioner | Logging in with your company identity provider. |
| 5 | [[Authentication - Tokens and OAuth]] | 301 Advanced | Personal access tokens versus OAuth, and machine-to-machine authentication. |
| 6 | [[Admin Roles]] | 201 Practitioner | Account admins, workspace admins, and metastore admins, and who can do what. |
| 7 | [[Compute Policies]] | 201 Practitioner | Guardrails on what clusters people can create (formerly cluster policies). |
| 8 | [[Secrets Management]] | 201 Practitioner | Keeping passwords and keys out of notebooks with secret scopes. |
| 9 | [[Network Security Overview]] | 301 Advanced | The map of front-end, back-end, and serverless network controls on every cloud. |
| 10 | [[IP Access Lists]] | 301 Advanced | Allowing workspace access only from known networks. |
| 11 | [[Serverless Network Security]] | 401 Expert | Network connectivity configurations, private endpoints, and egress control for serverless. |
| 12 | [[Encryption]] | 301 Advanced | Encryption at rest and in transit, and where customer-managed keys fit. |
| 13 | [[Compliance Security Profile]] | 401 Expert | Hardened settings for HIPAA, PCI-DSS, FedRAMP, and other standards. |
| 14 | [[Cost Management Basics]] | 101 Beginner | Where Databricks money goes, and the first five things to check. |
| 15 | [[Budgets and Usage Dashboards]] | 201 Practitioner | Budget alerts and built-in cost dashboards from system tables. |
| 16 | [[Tagging for Chargeback]] | 201 Practitioner | Tagging compute and jobs so every dollar maps to a team or project. |
| 17 | [[Cost Optimization Checklist]] | 201 Practitioner | A practical list covering auto-termination, serverless, spot, sizing, Photon, and more. |
| 18 | [[Terraform Provider]] | 301 Advanced | Managing accounts, workspaces, and permissions as code. |
| 19 | [[Disaster Recovery]] | 401 Expert | Backups, multi-region strategies, and what Databricks does and does not cover. |

<!-- GENERATED:reading-order END -->

> [!nextup] Up next
> [[Account Console]]
