---
type: chapter
status: written
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
last_verified: 2026-10-25
tags:
  - chapter
---

# Chapter 14 - Admin Security and Cost

> [!story] Context
> Chapters 11 to 13 covered the cloud-specific parts of a deployment on Azure, AWS, and Google Cloud, ending with [[Customer-Managed Keys on Google Cloud]]. This chapter covers the administration tasks that apply on every cloud: identity, access, network security, encryption, compliance, cost control, automation, and disaster recovery.

**Running Databricks safely and cheaply, covering identity, networking, encryption, compliance, and FinOps.**

## The story of this chapter

### Scope

A working Databricks deployment still needs an owner. Someone must decide who can sign in, what each identity can do, which networks can reach the platform, how data is encrypted, how spend is limited and attributed, and how the platform is rebuilt after a failure. This chapter covers those tasks at the account level, with per-cloud differences in each note.

### Administration surface

Since [[Unity Catalog]] moved governance to the account, most platform-wide settings live in the [[Account Console]]: workspaces, metastores, identities, security settings, and usage. Workspace settings cover the rest. Responsibility is split across [[Admin Roles|admin roles]] (account admin, workspace admin, metastore admin, and narrower roles such as billing admin), and administrators should hold these roles through groups.

### Identity and access

Databricks has three identity types: users, service principals, and groups ([[Users Groups and Service Principals]]). Account groups receive workspace assignments and Unity Catalog grants; legacy workspace-local groups cannot. Identities come from the company identity provider through [[SCIM Provisioning|SCIM or automatic identity management]], and people sign in through [[Single Sign-On]] with SAML 2.0 or OIDC, configured once for the account by unified login. Tools and automation authenticate with OAuth: user-to-machine for people, machine-to-machine for service principals, and token federation, which Databricks recommends because it removes stored secrets. Personal access tokens remain available but are treated as legacy ([[Authentication - Tokens and OAuth]]).

### Guardrails

[[Compute Policies]] (formerly cluster policies) limit how classic compute can be configured: size, runtime, auto-termination, access mode, and required tags. [[Secrets Management]] keeps credentials out of code with secret scopes, Azure Key Vault-backed scopes, and secrets in Unity Catalog.

### Network security

Databricks traffic follows three paths: front-end (users and clients to the workspace), back-end (classic compute to the control plane), and serverless (serverless compute to customer resources) ([[Network Security Overview]]). Front-end access is controlled with [[IP Access Lists]], context-based ingress policies, and inbound private connectivity. Classic compute uses secure cluster connectivity and, optionally, customer-managed networks and private links. Serverless compute is governed by network connectivity configurations and network policies for egress control ([[Serverless Network Security]]).

### Data protection and compliance

Data is encrypted at rest and in transit by default. Customer-managed keys add customer control over control-plane data, workspace storage, and compute disks ([[Encryption]]). For regulated data, the [[Compliance Security Profile]] applies hardened images, enhanced security monitoring, and automatic cluster updates, and is required for standards such as HIPAA, PCI-DSS, and FedRAMP.

### Cost

Usage is metered in DBUs and recorded in `system.billing.usage` ([[Cost Management Basics]]). [[Budgets and Usage Dashboards]] provide alerts and breakdowns. [[Tagging for Chargeback]] attributes spend to teams through compute tags and serverless usage policies (formerly serverless budget policies). The [[Cost Optimization Checklist]] lists the settings that reduce spend, led by auto-termination, serverless compute, and job compute.

### Automation and recovery

The [[Terraform Provider]] manages accounts, workspaces, identities, policies, and permissions as code, alongside Declarative Automation Bundles for project assets. [[Disaster Recovery]] defines [[RPO and RTO]] targets and the strategies to meet them, including managed disaster recovery (Public Preview as of October 2026). Databricks protects its control plane; table data lives in customer storage and is the customer's responsibility to replicate.

### Next

With the platform secured, governed, and cost-controlled, the remaining question is how to move existing data, pipelines, and reports onto it. [[Chapter 15 - Migrating to Databricks]] covers migration strategy and playbooks by source system.

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[Account Console]] | 201 Practitioner | The account-level admin site for workspaces, users, metastores, and billing. |
| 2 | [[Users Groups and Service Principals]] | 201 Practitioner | The three kinds of identity, and why groups should own everything. |
| 3 | [[SCIM Provisioning]] | 301 Advanced | Syncing users and groups automatically from Entra ID, Okta, or another IdP. |
| 4 | [[Single Sign-On]] | 201 Practitioner | Logging in with your company identity provider, configured once for the account and every workspace. |
| 5 | [[Authentication - Tokens and OAuth]] | 301 Advanced | Personal access tokens versus OAuth (U2M, M2M, and token federation) for scripts, tools, and automation. |
| 6 | [[Admin Roles]] | 201 Practitioner | Account admins, workspace admins, metastore admins, and the narrower feature roles, and who can do what. |
| 7 | [[Compute Policies]] | 201 Practitioner | Guardrails on what classic compute people can create, written as JSON rules (formerly cluster policies). |
| 8 | [[Secrets Management]] | 201 Practitioner | Keeping passwords and keys out of notebooks with secret scopes, and the newer secrets in Unity Catalog. |
| 9 | [[Network Security Overview]] | 301 Advanced | The map of front-end, back-end (classic), and serverless network controls on every cloud. |
| 10 | [[IP Access Lists]] | 301 Advanced | Allowing workspace and account console access only from known networks. |
| 11 | [[Serverless Network Security]] | 401 Expert | Network connectivity configurations, private endpoints, and network policies (serverless egress control) for serverless compute. |
| 12 | [[Encryption]] | 301 Advanced | Encryption at rest and in transit on Databricks, and where customer-managed keys apply. |
| 13 | [[Compliance Security Profile]] | 401 Expert | A workspace setting that applies hardened images, monitoring agents, and other controls required for HIPAA, PCI-DSS, FedRAMP, and other standards. |
| 14 | [[Cost Management Basics]] | 101 Beginner | Where Databricks spend comes from, how it is metered, and the first five controls to set. |
| 15 | [[Budgets and Usage Dashboards]] | 201 Practitioner | Budget alerts in the account console and the built-in usage dashboards built on system.billing tables. |
| 16 | [[Tagging for Chargeback]] | 201 Practitioner | Tagging compute, warehouses, pools, and serverless usage so every DBU maps to a team or project. |
| 17 | [[Cost Optimization Checklist]] | 201 Practitioner | A practical checklist covering auto-termination, serverless, spot instances, sizing, Photon, pools, and data layout. |
| 18 | [[Terraform Provider]] | 301 Advanced | Managing Databricks accounts, workspaces, identities, policies, and permissions as code with the databricks/databricks Terraform provider. |
| 19 | [[Disaster Recovery]] | 401 Expert | Backups, multi-region strategies, managed disaster recovery, and what Databricks does and does not protect. |

<!-- GENERATED:reading-order END -->

> [!nextup] Next
> [[Account Console]] covers the account-level administration site where most settings in this chapter are configured.
