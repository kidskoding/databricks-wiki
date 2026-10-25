---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A plain-text format for configuration files that uses indentation instead of brackets."
related:
  - "[[Declarative Automation Bundles]]"
  - "[[CI-CD for Data Pipelines]]"
  - "[[Infrastructure as Code]]"
  - "[[Lakeflow Jobs]]"
  - "[[Metric Views]]"
  - "[[Git Folders and Workspace Files]]"
aliases:
  - "YAML Ain't Markup Language"
  - ".yml"
  - ".yaml"
  - "databricks.yml"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# YAML

> [!eli5] Summary
> YAML is a plain-text format for configuration files that uses indentation to show structure. Both people and programs can read it.

**In data work:** YAML is a human-readable data format for configuration. It uses `key: value` pairs, indentation for nesting, and dashes for lists. Indentation must be spaces, not tabs, and a wrong indent changes the meaning, which is the most common YAML mistake. It is common in DevOps and data tooling, and this vault's own note frontmatter is YAML. Example: `schedule:` on one line, then `cron: "0 6 * * *"` indented under it, meaning run every day at 6 a.m.

**In Databricks:** YAML is how you describe Databricks projects as code. [[Declarative Automation Bundles]] (formerly Databricks Asset Bundles) use a `databricks.yml` file plus resource files to define jobs, pipelines, and other resources, which the [[Databricks CLI]] deploys from [[Git]] in [[CI-CD for Data Pipelines|CI/CD]]. Existing [[Lakeflow Jobs]] can be viewed and edited as YAML from the job's menu, and [[Metric Views]] are defined in YAML. See [[Infrastructure as Code]] for the bigger idea.

Seen in: [[Declarative Automation Bundles]], [[CI-CD for Data Pipelines]], [[Metric Views]]

## Recall

YAML::An indentation-based text format for configuration; Declarative Automation Bundles define Databricks jobs and pipelines in databricks.yml.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Declarative Automation Bundles configuration (AWS)](https://docs.databricks.com/aws/en/dev-tools/bundles/settings)
> - [Declarative Automation Bundles configuration (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/bundles/settings)
> - [Configure and edit Lakeflow Jobs (AWS)](https://docs.databricks.com/aws/en/jobs/configure-job)
> - [Metric view YAML syntax reference (AWS)](https://docs.databricks.com/aws/en/uc-semantics/metric-views/yaml-reference)
