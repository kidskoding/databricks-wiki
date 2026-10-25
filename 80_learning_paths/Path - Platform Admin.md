---
type: path
status: written
level: 80
section: Learning Paths
depth: 301
summary: Accounts, identity, Unity Catalog, networking, and cost controls on your cloud.
personas:
  - admin
  - security
chapter: "[[Chapter 80 - Learning Paths]]"
prev: "[[Path - AI App Developer]]"
next: "[[Path - One-Person Data Team]]"
evolved_from: []
evolved_into: []
cloud_equivalent: []
related:
  - "[[Accounts and Workspaces]]"
  - "[[Control Plane and Compute Plane]]"
  - "[[Account Console]]"
  - "[[Admin Roles]]"
  - "[[Users Groups and Service Principals]]"
  - "[[SCIM Provisioning]]"
  - "[[Unity Catalog]]"
  - "[[Privileges and Grants]]"
  - "[[Storage Credentials and External Locations]]"
  - "[[System Tables]]"
  - "[[Network Security Overview]]"
  - "[[Compute Policies]]"
  - "[[Budgets and Usage Dashboards]]"
  - "[[Terraform Provider]]"
  - "[[Path - Azure Deep Dive]]"
  - "[[Path - AWS Deep Dive]]"
  - "[[Path - Google Cloud Deep Dive]]"
aliases:
  - Admin Path
  - Security Path
prereqs:
  - "[[Path - Absolute Beginner]]"
unlocks:
  - "[[Path - Azure Deep Dive]]"
  - "[[Path - AWS Deep Dive]]"
  - "[[Path - Google Cloud Deep Dive]]"
clouds:
  - aws
  - azure
  - gcp
mastery: new
last_verified: 2026-10-25
tags:
  - path
---

# Path - Platform Admin

> [!persona] Who this is for
> **Who:** the platform or cloud admin who sets Databricks up, and the security or compliance lead who has to sign off on it.
> **Goal:** run a Databricks account that is organized, secure, governed, and not wasting money, on whichever cloud you use.
> **Outcome:** you can design the account and workspace layout, wire up identity, set up Unity Catalog and grants, choose network controls, enforce cost guardrails, and manage it all as code.

## Before you start

You should know your cloud's basics: IAM or Entra ID, virtual networks, and object storage. This path is cloud-neutral; each stage points to the cloud-specific notes, and the full per-cloud routes are [[Path - Azure Deep Dive]], [[Path - AWS Deep Dive]], and [[Path - Google Cloud Deep Dive]]. [[Databricks Free Edition and Trials|Free Edition]] has no account console or network settings, so you need a trial or paid account on your cloud where you are an account admin.

## The route

### Stage 1: The shape of an account (101 to 201)

**Goal:** know what you are administering and who can do what.

1. [[Accounts and Workspaces]]: one account, many workspaces.
2. [[Control Plane and Compute Plane]] (201): what Databricks runs versus what runs in your cloud or in serverless.
3. [[Account Console]] (201): the account-level admin site.
4. [[Admin Roles]] (201): account, workspace, and metastore admins.
5. [[Compute Types]]: the compute your users will ask for.
6. [[Serverless Compute]]: the compute you do not have to network or patch.
7. [[Choosing a Cloud for Databricks]]: why the cloud choice shapes every later stage.

> [!check] Checkpoint
> In a trial account, open the account console and list your workspaces and metastores. Write down which region each workspace is in, which metastore it is attached to, and who holds the account admin role. Draw the control plane and compute plane for one workspace on paper.

### Stage 2: Identity (201 to 301)

**Goal:** get the right people and machines in, with groups owning everything.

1. [[Users Groups and Service Principals]] (201): the three identity types, and why groups own objects.
2. [[Single Sign-On]] (201): log in with your company identity provider.
3. [[SCIM Provisioning]] (301): sync users and groups automatically.
4. [[Authentication - Tokens and OAuth]] (301): personal access tokens versus OAuth, and machine-to-machine auth.
5. [[Microsoft Entra ID Integration]] (201): the Azure flavor, read even if you are on another cloud and use Entra ID as your IdP.
6. [[Identity Provider]]: the glossary entry for the system your users come from.

> [!check] Checkpoint
> At the account level, create a group `data-engineers` and a service principal `ci-deployer`, add the principal to the group, and assign the group to one workspace. Create an OAuth secret for the service principal and authenticate the [[Databricks CLI]] with it (a profile with `client_id` and `client_secret`). Run `databricks current-user me` and confirm it returns the service principal.

### Stage 3: Governance with Unity Catalog (201 to 301)

**Goal:** organize data by environment and team, and prove who touched what.

1. [[Unity Catalog]]: the governance layer for every workspace.
2. [[Metastore]] (201): one per region, and how workspaces attach.
3. [[Catalogs Schemas and Tables]]: a catalog layout for dev, staging, and prod.
4. [[Privileges and Grants]] (201): `GRANT`, inheritance, and ownership.
5. [[Storage Credentials and External Locations]] (301): how Unity Catalog reaches your buckets.
6. [[Managed vs External Tables]] (201): who owns the files.
7. [[Row Filters and Column Masks]] (301): per-user rows and values.
8. [[Attribute-Based Access Control]] (301): tag-driven policies at scale.
9. [[Data Classification]] (301): finding PII automatically.
10. [[Audit Logs]] (301): who did what, when.
11. [[System Tables]] (201): audit, billing, and lineage as SQL tables.
12. [[Hive Metastore Migration to Unity Catalog]] (301): upgrading older workspaces.

> [!check] Checkpoint
> Create catalogs `dev` and `prod`, grant `USE CATALOG`, `USE SCHEMA`, and `SELECT` on `prod` to a reader group, and `ALL PRIVILEGES` on `dev` to `data-engineers`. Add a row filter function to one table so the reader group sees only one region. Then query `system.access.audit` for the grant events you just made.

### Stage 4: Network and encryption (301 to 401)

**Goal:** choose and apply the right network and key controls for your risk level.

1. [[Network Security Overview]] (301): front-end, back-end, and serverless controls on every cloud.
2. [[IP Access Lists]] (301): allow access only from known networks.
3. [[Serverless Network Security]] (401): network connectivity configurations, private endpoints, and egress control.
4. [[Secrets Management]] (201): secret scopes, and keeping keys out of notebooks.
5. [[Encryption]] (301): at rest, in transit, and where customer-managed keys fit.
6. [[Compliance Security Profile]] (401): hardened settings for HIPAA, PCI-DSS, and FedRAMP.
7. Your cloud's network notes: [[VNet Injection]], [[Customer-Managed VPC on AWS]], or [[Customer-Managed VPC on Google Cloud]].

> [!check] Checkpoint
> On a trial workspace on a plan that supports it, add an IP access list that allows only your office or VPN range, and confirm a request from another network is refused. Create a secret scope, store a fake API key, and read it in a notebook with `dbutils.secrets.get(...)`; confirm the notebook output shows `[REDACTED]`. Write a one-page network design for production: which private connectivity option, which egress controls, and why.

### Stage 5: Cost guardrails and automation (201 to 401)

**Goal:** stop waste before it happens, and make the setup reproducible.

1. [[Compute Policies]] (201): limits on what clusters people can create (formerly cluster policies).
2. [[Cost Management Basics]]: where the money goes.
3. [[Budgets and Usage Dashboards]] (201): budget alerts and built-in cost dashboards.
4. [[Tagging for Chargeback]] (201): map every DBU to a team.
5. [[Cost Optimization Checklist]] (201): the practical list.
6. [[Terraform Provider]] (301): accounts, workspaces, and grants as code.
7. [[Disaster Recovery]] (401): what Databricks covers and what you must plan.

> [!check] Checkpoint
> Create a compute policy that fixes auto-termination, caps worker count, and requires a `team` tag, and assign it to `data-engineers`. Create a budget with an alert email. Query `system.billing.usage` grouped by `sku_name` and the `team` tag for the last 30 days. Finally, describe one of your Stage 2 or 3 objects in Terraform and run `terraform plan` against the account.

## Rabbit holes

- **Your cloud, all the way down:** [[Path - Azure Deep Dive]], [[Path - AWS Deep Dive]], [[Path - Google Cloud Deep Dive]], and the side-by-side hub [[Cloud Comparison - Azure vs AWS vs GCP]].
- **Private connectivity:** [[Azure Private Link]], [[AWS PrivateLink]], [[Private Service Connect]].
- **Keys you own:** [[Customer-Managed Keys on Azure]], [[Customer-Managed Keys on AWS]], [[Customer-Managed Keys on Google Cloud]].
- **Sharing and partners:** [[OpenSharing]] and [[Clean Rooms]].
- **AI governance:** [[Unity Gateway]] and [[Models in Unity Catalog]].
- **Automation in CI:** [[Declarative Automation Bundles]], [[Databricks SDKs and REST API]], [[CI-CD for Data Pipelines]].
- **Regulated workloads:** [[Databricks on AWS GovCloud]], [[HIPAA]], [[SOC 2]].

## You are done when

- You can draw your account, workspaces, metastores, and regions from memory.
- Users and groups arrive from your IdP, and service principals run all automation.
- Every catalog has an owner group and a documented grant model.
- You can answer "who read this table last week?" from system tables.
- You have picked network and key controls for production and can defend the choice.
- Compute policies, tags, and budgets are in place, and the setup lives in Terraform.

> [!nextup] Up next
> Small businesses rarely have a separate admin. When one person does every job, use [[Path - One-Person Data Team]].

> [!sources]- Sources (last verified: 2026-10-25)
> - Route assembled on 2026-10-25 from the vault index (`llms.txt`) and the `admin` and `security` persona tags in `_meta/manifest.yaml`. Product facts and official documentation links live in each linked note's `[!sources]` callout; [[Unity Catalog]] is fully sourced.
> - Plan requirements for IP access lists, budgets, and the compliance security profile were not re-checked for this path; see the linked notes before relying on them.
