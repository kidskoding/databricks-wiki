---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Software whose source code anyone can read, use, change, and share under a public license."
related:
  - "[[Apache Software Foundation]]"
  - "[[Linux Foundation]]"
  - "[[Apache Spark]]"
  - "[[Delta Lake]]"
  - "[[Open Source vs Databricks - Who Replaced What]]"
  - "[[Open Table Formats]]"
aliases:
  - "OSS"
  - "open-source software"
  - "FOSS"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Open Source

> [!eli5] Summary
> Open-source software has public source code that anyone may use, change, and share under the terms of its license.

**In data work:** Open-source software publishes its code under a license (Apache 2.0, MIT, GPL and others) that lets anyone use, modify, and redistribute it. Large projects are often governed by neutral foundations such as the [[Apache Software Foundation]] and the [[Linux Foundation]]. Software that is free to download is not free to operate: someone still pays for servers, upgrades, security patches, and expertise, which is why companies sell managed versions. A one-person data team can run Apache Spark on a laptop at no license cost, but operating it reliably for a whole business requires ongoing engineering effort.

**In Databricks:** Databricks was founded by the creators of [[Apache Spark]] and builds its platform on open-source projects it started or supports: Spark, [[Delta Lake]], [[MLflow]], and an open-source edition of [[Unity Catalog]]. Databricks adds managed, proprietary pieces on top, such as [[Photon]] and [[Serverless Compute]]. [[Open Source vs Databricks - Who Replaced What]] maps each open-source tool to its Databricks counterpart.

Seen in: [[Open Source vs Databricks - Who Replaced What]], [[The Founding of Databricks]], [[Apache Spark]]

## Recall

Open Source::Software with public code that anyone may use, change, and share under a license; Spark, Delta Lake, and MLflow are open source.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Databricks Open Source](https://www.databricks.com/product/open-source)
