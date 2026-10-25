---
type: concept
status: written
level: 6
section: Databricks Platform
depth: 201
summary: The tuned Spark plus libraries image every classic cluster boots, and its LTS versions.
personas:
  - engineer
  - scientist
chapter: "[[Chapter 06 - The Databricks Platform]]"
prev: "[[Control Plane and Compute Plane]]"
next: "[[Photon]]"
evolved_from:
  - "[[Apache Spark]]"
evolved_into:
  - "[[Serverless Compute]]"
cloud_equivalent: []
related:
  - "[[Photon]]"
  - "[[Delta Lake]]"
  - "[[Libraries and Environments]]"
  - "[[All-Purpose Compute]]"
  - "[[Jobs Compute]]"
  - "[[MLflow]]"
  - "[[Scala]]"
  - "[[JVM]]"
  - "[[Spark Connect]]"
  - "[[AI Runtime]]"
aliases:
  - DBR
  - Databricks Runtime LTS
  - Databricks Runtime for Machine Learning
  - DBR ML
prereqs:
  - "[[Apache Spark]]"
  - "[[Control Plane and Compute Plane]]"
unlocks:
  - "[[Photon]]"
  - "[[Compute Types]]"
  - "[[Libraries and Environments]]"
clouds:
  - aws
  - azure
  - gcp
mastery: new
last_verified: 2026-10-25
tags:
  - concept
  - flashcards
---

# Databricks Runtime

Mastery: `INPUT[inlineSelect(option(new), option(learning), option(solid)):mastery]`

> [!story] Previously
> In [[Control Plane and Compute Plane]] the control plane launched virtual machines into the compute plane. A bare VM is only an empty computer, though. Something has to turn it into a Spark node with the right Python, the right Delta Lake version, and Databricks' own speed-ups. That something is the Databricks Runtime.

> [!eli5] In one breath
> The Databricks Runtime is the software package that every Databricks computer starts with. It bundles the data engine, the programming languages, and hundreds of popular tools, all tested together. You pick a version number when you create a cluster, a bit like picking which version of an app to install.

> [!analogy] Analogy: a pre-built gaming PC
> - **Open-source [[Apache Spark]]** is a box of parts: you can build a PC from it, but you pick and test every part yourself.
> - **The Databricks Runtime** is a pre-built, tested PC: the same core parts, plus tuned drivers and extras, guaranteed to work together.
> - **The version number** is the model year. A new model has new features. An **LTS** model is the one the maker promises to repair for three years.
> - **The ML runtime** is the "creator edition" with extra software (PyTorch, scikit-learn, [[MLflow]]) already installed.

## Why it exists

When you run Spark yourself, you choose versions of Spark, Scala, Java, Python, Hadoop connectors, Delta Lake, and every Python package, then hope they work together. A small mismatch (say, a library built for the wrong Scala version) breaks a job at 2 a.m.

The Databricks Runtime (DBR) removes that problem:

- Everything in one version is **tested together**.
- It includes **Databricks-only improvements** to Spark and Delta (faster I/O, caching, [[Photon]]).
- It has a **clear support lifecycle**, so you know how long a version gets security fixes.

## What it actually is

A Databricks Runtime version is a machine image plus software stack that classic compute boots. Each version includes:

- **Apache Spark**, with Databricks improvements (Runtime 19 is built on Spark 4.2.0, Runtime 18 LTS on Spark 4.1.0).
- **Delta Lake** and the Databricks I/O layer.
- **Languages:** Python, [[Scala]] (Runtime 17 and later support only Scala 2.13), Java ([[JVM]]), SQL, and R.
- **System libraries** on Ubuntu, and a large set of preinstalled Python, Java, Scala, and R packages.
- **Optional [[Photon]]**, the native query engine, turned on per cluster.

There are two main flavors:

| Flavor | What is added | Use it for |
|---|---|---|
| **Databricks Runtime** | The standard stack | Data engineering, SQL, general Python |
| **Databricks Runtime for Machine Learning** (DBR ML) | ML libraries such as PyTorch, TensorFlow, scikit-learn, XGBoost, plus [[MLflow]]; GPU builds for [[AI Runtime]] | Training and experimentation |

### Versions and support (as of October 2026)

Databricks' release lifecycle runs from **Beta**, to **GA** for roughly six months of feature development, to **LTS** (long-term support) with **three years** of stability and security fixes.

| Version | Spark | Status | End of support |
|---|---|---|---|
| **19** | 4.2.0 | GA since July 23, 2026 (Beta from June 15, 2026) | Not yet set |
| **18 LTS** | 4.1.0 | LTS (listed June 10, 2026) | June 10, 2029 |
| **17.3 LTS** | 4.0 | LTS | October 22, 2028 |
| **16.4 LTS** | 3.5 | LTS | May 9, 2028 |
| **15.4 LTS** | 3.5 | LTS | August 19, 2027 |
| **14.3 LTS** | 3.5 | LTS | February 1, 2027 |

Two recent changes are worth knowing:

- **One release line per major version.** From Runtime 18 onward, Databricks documents a major version on one page that collects all features shipped during its release cycle, instead of a separate page per minor version.
- **Java 21.** Runtime 18 defaults to JDK 21 instead of JDK 17, with a fallback to JDK 17 for compatibility problems.

## How it works

```mermaid
flowchart TB
  CP[Control plane] -->|"launch VMs with<br/>spark_version = DBR"| VM[Cloud VMs]
  VM --> IMG["Databricks Runtime image"]
  IMG --> SP["Spark + Databricks improvements"]
  IMG --> DL["Delta Lake + I/O layer"]
  IMG --> LANG["Python, Scala 2.13, Java, R, SQL"]
  IMG --> LIBS["Preinstalled libraries<br/>(ML flavor adds PyTorch, MLflow...)"]
  IMG -.optional.-> PH[Photon engine]
```

You choose the runtime with the `spark_version` field when you create compute. The value is a version key such as `17.3.x-scala2.13`. List the keys your workspace offers with the [[Databricks CLI]]:

```bash
# Which runtime versions can this workspace use?
databricks clusters spark-versions -o json | jq -r '.versions[] | "\(.key)\t\(.name)"' | grep LTS
```

A cluster definition for a jobs cluster, pinned to an LTS runtime with Photon (cloud node types differ, see below):

```json
{
  "cluster_name": "nightly-etl",
  "spark_version": "17.3.x-scala2.13",
  "runtime_engine": "PHOTON",
  "node_type_id": "i3.xlarge",
  "num_workers": 2,
  "data_security_mode": "USER_ISOLATION"
}
```

`data_security_mode: USER_ISOLATION` is the API name for *standard* access mode (see [[Compute Types]]).

Inside a running cluster you can check the version from Python:

```python
spark.version                                    # Spark version, e.g. '4.0.0'
spark.conf.get("spark.databricks.clusterUsageTags.sparkVersion")  # DBR key
```

### Which version should I pick?

- **Production jobs:** the newest **LTS** that your libraries support. You get three years of fixes without surprise behavior changes.
- **Exploration and new features:** the newest GA version.
- **Upgrades:** read the "behavioral changes" section of the release notes. For example, Runtime 19 makes Python UDFs use Arrow-based serialization by default, which can change type handling in some UDFs.

> [!smallbiz] For a small business
> You may barely touch the runtime. [[Serverless Compute]] and [[SQL Warehouses]] pick and upgrade the software for you, and that is the simplest choice for a small team. If you do run classic clusters, follow one rule: **pin your scheduled jobs to an LTS version** and put a reminder in your calendar a few months before it reaches end of support.

## On each cloud

> [!azure]- Azure Databricks
> Runtime versions and support dates are the same as on the other clouds. Node types are Azure VM sizes, for example `Standard_D4ds_v5`. Release notes are mirrored on Microsoft Learn.

> [!aws]- Databricks on AWS
> Same versions. Node types are EC2 instance types, for example `i3.xlarge` or Graviton types (see [[EC2 Instance Types and Graviton]]). Graviton support depends on the runtime version and features, so check the docs.

> [!gcp]- Databricks on Google Cloud
> Same versions. Node types are Compute Engine machine types, for example `n2-highmem-4`. See [[Compute on Google Cloud]].

## Going deeper

> [!deepdive]- Expert notes (301–401)
> - **Maintenance updates.** Within a version, Databricks ships maintenance updates (security patches and bug fixes) automatically when a cluster restarts. Long-running clusters do not pick them up until they restart.
> - **Serverless uses runtime versions managed by Databricks.** Serverless compute tracks recent runtime code (serverless releases in August–September 2026 included updates from Runtime 19). You pin a client-side *environment version* instead of a runtime. See [[Serverless Compute]] and [[Libraries and Environments]].
> - **Databricks Connect matches the runtime.** The [[Databricks Connect]] package version should match the runtime major/minor version of the cluster it talks to.
> - **Scala 2.13 only from 17.** JARs compiled for Scala 2.12 must be rebuilt for Runtime 17 and later.
> - **Standard access mode restrictions.** In Runtime 19, several Spark configuration properties are restricted on standard access mode clusters, and creating a cluster that sets them fails.
> - **End of support.** After end of support, a version gets no fixes and is eventually removed from the version list. Jobs pinned to it must be upgraded.
> - **Custom images.** Databricks Container Services lets you boot a custom Docker image on classic compute. It is rarely needed now that environments and init scripts in volumes cover most cases.

## Common confusions

> [!confusion] DBR version is not the Spark version
> Runtime 18 LTS runs Spark 4.1.0. The DBR number tracks Databricks' release, and each one maps to a Spark version listed in its release notes.

> [!confusion] "LTS" does not mean "newest"
> LTS means "supported longest". The newest version may not be LTS yet. Pick LTS for stability and the newest GA for features.

## Recall

What is the Databricks Runtime?::The tested software image (Spark, Delta Lake, languages, libraries, optional Photon) that classic Databricks compute boots.
How long is an LTS runtime supported?::Three years.
Which Spark version does Databricks Runtime 18 LTS use?::Apache Spark 4.1.0.
Which Spark version does Databricks Runtime 19 use?::Apache Spark 4.2.0.
Which Scala version do Runtime 17 and later support?::Scala 2.13 only.
What does DBR ML add?::Machine learning libraries such as PyTorch, TensorFlow, scikit-learn, XGBoost, and MLflow, with GPU builds.
Which cluster field selects the runtime?::`spark_version`, for example `17.3.x-scala2.13`.
Which runtime should production jobs use?::The newest LTS version your libraries support.
Which JDK does Runtime 18 use by default?::JDK 21.

## Where next

> [!path] Learning path
> **Needs first:** [[Apache Spark]], [[Control Plane and Compute Plane]]
> **Unlocks next:** [[Photon]], [[Compute Types]], [[Libraries and Environments]]

> [!nextup] Up next in the story
> The runtime is still Spark on the [[JVM]] at heart. Databricks' biggest speed-up came from rewriting the engine itself in C++. Meet [[Photon]].

> [!sources]- Sources (last verified: 2026-10-25)
> - [Databricks Runtime release notes versions and compatibility (AWS)](https://docs.databricks.com/aws/en/release-notes/runtime/)
> - [Databricks Runtime 19 (AWS)](https://docs.databricks.com/aws/en/release-notes/runtime/19)
> - [Databricks Runtime 19 (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/release-notes/runtime/19)
> - [Databricks Runtime 18 LTS (AWS)](https://docs.databricks.com/aws/en/release-notes/runtime/18)
> - [Databricks Runtime 18 LTS (Google Cloud)](https://docs.databricks.com/gcp/en/release-notes/runtime/18)
> - [Databricks Runtime 16.4 LTS (AWS)](https://docs.databricks.com/aws/en/release-notes/runtime/16.4lts)
> - [Serverless compute release notes (AWS)](https://docs.databricks.com/aws/en/release-notes/serverless)
> - [Databricks platform release notes (AWS)](https://docs.databricks.com/aws/en/release-notes/product)
> - [Compute configuration reference (AWS)](https://docs.databricks.com/aws/en/compute/configure)
