---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A packaged application with its dependencies that runs the same way on any host; in Azure Storage, also the top-level folder of a storage account."
related:
  - "[[Kubernetes]]"
  - "[[Azure Data Lake Storage]]"
  - "[[Libraries and Environments]]"
  - "[[Databricks Runtime]]"
  - "[[ADLS and Access Connectors]]"
  - "[[Virtual Machine]]"
aliases:
  - "containers"
  - "Docker"
  - "Docker image"
  - "container image"
  - "blob container"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Container

> [!eli5] Summary
> A software container packages a program together with everything it needs, so it behaves the same on any computer. In Azure storage, "container" also means a top-level storage folder.

**In data work:** The term has two meanings. In software, a container (usually built with Docker) bundles an application, its libraries, and its configuration into an image that runs consistently on any host. Containers are lighter than a full [[Virtual Machine]] and are often orchestrated by [[Kubernetes]]. In Azure Storage, a container is the top-level grouping of files within a storage account, comparable to an [[Amazon S3|S3]] bucket.

**In Databricks:** Classic compute normally boots a Databricks-provided [[Databricks Runtime]] image, and packages are added as described in [[Libraries and Environments]]. **Databricks Container Services** runs compute from a custom Docker image pulled from a registry such as Docker Hub, Azure Container Registry, or Amazon ECR. It is generally available for dedicated compute and in Beta for standard compute (Runtime 18 LTS and above) as of October 2026. Databricks ignores the Dockerfile `CMD` and `ENTRYPOINT`. On Azure, Unity Catalog external locations reference storage containers in paths such as `abfss://<container>@<account>.dfs.core.windows.net/`.

Seen in: [[Kubernetes]], [[Azure Data Lake Storage]], [[Libraries and Environments]], [[ADLS and Access Connectors]]

## Recall

What is a software container?::A packaged application plus its dependencies that runs the same way on any host.
What Databricks feature runs compute from a custom Docker image?::Databricks Container Services.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Databricks Container Services for dedicated compute (AWS)](https://docs.databricks.com/aws/en/compute/custom-containers)
> - [Databricks Container Services for standard compute (AWS)](https://docs.databricks.com/aws/en/compute/custom-containers-standard)
