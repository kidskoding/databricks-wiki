---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A nonprofit that hosts and governs major open-source projects, including Delta Lake, MLflow, and Unity Catalog OSS."
related:
  - "[[Open Source]]"
  - "[[Apache Software Foundation]]"
  - "[[Delta Lake]]"
  - "[[MLflow]]"
  - "[[Unity Catalog]]"
  - "[[Open Table Formats]]"
aliases:
  - "LF"
  - "LF AI & Data"
  - "LF Projects"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Linux Foundation

> [!eli5] Summary
> The Linux Foundation is a nonprofit that provides neutral ownership and governance for shared open-source software. Delta Lake, MLflow, and open-source Unity Catalog are hosted there.

**In data work:** The Linux Foundation is a nonprofit that provides a neutral home, legal structure, and governance for [[Open Source|open-source]] projects, beyond Linux itself. One of its sub-foundations is LF AI & Data, which hosts AI and data projects. When a company donates a project to a foundation, the trademark and decisions move to a neutral body, which makes other companies more willing to adopt and contribute. It plays a role similar to the [[Apache Software Foundation]], which hosts [[Apache Spark]].

**In Databricks:** Several projects that started at Databricks now live at the Linux Foundation: [[Delta Lake]] (announced October 2019), [[MLflow]] (June 2020), and the open-source version of [[Unity Catalog]] (June 2024, hosted by LF AI & Data as a Sandbox project). [[Apache Spark]] lives at the Apache Software Foundation instead. This matters for [[Vendor Lock-In|lock-in]]: your tables and models use formats governed outside Databricks.

Seen in: [[Delta Lake]], [[MLflow]], [[Open Table Formats]]

## Recall

Linux Foundation::A nonprofit that neutrally governs open-source projects; it hosts Delta Lake, MLflow, and open-source Unity Catalog.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Delta Lake Now Hosted by the Linux Foundation (Databricks blog, 2019)](https://www.databricks.com/blog/2019/10/16/delta-lake-now-hosted-by-the-linux-foundation-to-become-the-open-standard-for-data-lakes.html)
> - [MLflow is joining the Linux Foundation (Databricks blog, 2020)](https://databricks.com/fr/blog/2020/06/25/mlflow-joins-the-linux-foundation-to-become-the-open-standard-for-machine-learning-platforms.html)
> - [Databricks Open Sources Unity Catalog (press release, 2024)](https://www.databricks.com/company/newsroom/press-releases/databricks-open-sources-unity-catalog-creating-industrys-only-open)
> - [Databricks Open Source](https://www.databricks.com/product/open-source)
