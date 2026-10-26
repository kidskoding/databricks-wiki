---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The practice of managing cloud and data platform spending through shared accountability between engineering, finance, and business teams."
related:
  - "[[Cost Management Basics]]"
  - "[[Chargeback]]"
  - "[[Budgets and Usage Dashboards]]"
  - "[[Cost Optimization Checklist]]"
  - "[[Tagging for Chargeback]]"
  - "[[Total Cost of Ownership]]"
aliases:
  - "Cloud financial management"
  - "Cloud FinOps"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# FinOps

> [!eli5] Summary
> FinOps is the habit of watching what the cloud costs, deciding together whether it is worth it, and fixing waste. Engineers and the people who pay the bill work from the same numbers.

**In data work:** The FinOps Foundation defines FinOps as an operational framework and cultural practice that maximizes the business value of cloud, enables timely data-driven decisions, and creates financial accountability through collaboration between engineering, finance, and business teams. Its framework runs in three repeating phases: **Inform** (visibility, allocation, budgets), **Optimize** (rightsizing, scheduling, commitments), and **Operate** (policies and continuous improvement). Data platforms bill in their own units, such as [[DBUs]] on Databricks, so a FinOps practice must translate those units into cost per team or product. The FOCUS specification is the Foundation's open format for normalizing billing data across providers.

**In Databricks:** Databricks supplies the raw material: usage in `system.billing.usage` ([[System Tables]]), tags for [[Chargeback|chargeback]], [[Budgets and Usage Dashboards|budgets and usage dashboards]], and [[Compute Policies|compute policies]] that cap cluster size and enforce [[Auto Termination|auto termination]]. See [[Cost Management Basics]] and the [[Cost Optimization Checklist]].

Small-business example: the owner and the one data engineer review a usage dashboard on the first Monday of each month and agree on one change, such as shortening auto termination on an idle cluster.

Seen in: [[Cost Management Basics]], [[Cost Optimization Checklist]], [[Chargeback]]

## Recall

What are the three phases of the FinOps Framework?::Inform, Optimize, Operate.
FinOps::Managing cloud spend through shared accountability between engineering, finance, and business.

> [!sources]- Sources (last verified: 2026-10-26)
> - [What is FinOps? (FinOps Foundation)](https://www.finops.org/introduction/what-is-finops/)
> - [FinOps Framework overview (Microsoft Learn)](https://learn.microsoft.com/en-us/cloud-computing/finops/framework/finops-framework)
> - [FinOps for Data Cloud Platforms (FinOps Foundation)](https://www.finops.org/wg/finops-data-cloud-platforms/)
