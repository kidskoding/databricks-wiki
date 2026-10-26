---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Long-term support: a Databricks Runtime version that receives stability and security fixes for three years from its release, recommended for production jobs."
related:
  - "[[Databricks Runtime]]"
  - "[[Jobs Compute]]"
  - "[[Compute Policies]]"
  - "[[Lakeflow Jobs]]"
  - "[[Serverless Compute]]"
aliases:
  - "Long-term support"
  - "LTS release"
  - "Databricks Runtime LTS"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# LTS

> [!eli5] Summary
> LTS marks a software version that will be maintained for a long time. Pick an LTS version for jobs that must keep running without surprise changes.

**In data work:** Software vendors label some releases long-term support. LTS versions receive bug and security fixes for an extended, published period, while other releases are replaced quickly. Teams standardize on LTS to reduce upgrade frequency and risk.

**In Databricks:** Each [[Databricks Runtime]] version first goes through about six months of feature development after GA and then moves to LTS. Databricks backports major stability and security fixes, and the end-of-support date is three years after the GA release date. For example, Databricks lists Runtime 17.3 LTS as released October 22, 2025 with end of support on October 22, 2028. Databricks aims to set end of life about six months after end of support. LTS versions have `LTS` in their name (for example `16.4 LTS`), and the support lifecycle page lists the current dates. [[Serverless Compute|Serverless compute]] manages versions for you, so LTS selection applies to classic compute.

Small-business example: pin production [[Jobs Compute|job clusters]] to the newest LTS in a [[Compute Policies|compute policy]], and plan one upgrade test per year rather than chasing every release.

Seen in: [[Databricks Runtime]], [[Compute Policies]]

## Recall

How long is a Databricks Runtime LTS version supported?::Three years from its GA release date.
LTS::Long-term support: a runtime version that receives fixes for an extended published period.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Databricks support lifecycles (AWS)](https://docs.databricks.com/aws/en/release-notes/runtime/databricks-runtime-ver)
> - [Databricks support lifecycles (Azure)](https://learn.microsoft.com/en-us/azure/databricks/release-notes/runtime/databricks-runtime-ver)
