---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Defining infrastructure such as workspaces, networks, and permissions in version-controlled files that a tool applies automatically."
related:
  - "[[Terraform Provider]]"
  - "[[Declarative Automation Bundles]]"
  - "[[CI-CD for Data Pipelines]]"
  - "[[Databricks CLI]]"
  - "[[Databricks SDKs and REST API]]"
  - "[[Accounts and Workspaces]]"
aliases:
  - "IaC"
  - "infrastructure-as-code"
  - "declarative infrastructure"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Infrastructure as Code

> [!eli5] Summary
> Infrastructure as code describes a technical setup in text files instead of creating it by hand. A tool reads the files and builds the same setup every time.

**In data work:** With infrastructure as code (IaC), you declare the desired state in files stored in [[Git]], and a tool compares it with the actual state and applies the differences. Benefits are repeatable environments, review before changes are applied, and an audit trail. Common tools are Terraform, OpenTofu, Pulumi, AWS CloudFormation, and Azure Bicep.

**In Databricks:** The [[Terraform Provider]] manages workspaces and platform resources, including the Unity Catalog metastore, storage credentials, external locations, catalogs, schemas, and grants (`databricks_grants`). [[Declarative Automation Bundles]] (formerly Databricks Asset Bundles) define project resources such as jobs and pipelines in [[YAML]] alongside the code and deploy through the [[Databricks CLI]] in [[CI-CD for Data Pipelines|CI/CD]]. Databricks guidance uses Terraform for cloud-level resources and admin actions, and bundles for workload resources. Both call the [[Databricks SDKs and REST API|REST API]].

Seen in: [[Terraform Provider]], [[Declarative Automation Bundles]], [[CI-CD for Data Pipelines]], [[Path - Platform Admin]]

## Recall

What are the main benefits of infrastructure as code?::Repeatable, reviewable, version-controlled environments.
Which Terraform resource manages Unity Catalog privileges?::databricks_grants.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Phase 7: Plan an infrastructure as code approach (AWS)](https://docs.databricks.com/aws/en/lakehouse-architecture/deployment-guide/iac)
> - [Developer best practices on Databricks (AWS)](https://docs.databricks.com/aws/en/developers/best-practices)
> - [CI/CD on Databricks (AWS)](https://docs.databricks.com/aws/en/dev-tools/ci-cd)
