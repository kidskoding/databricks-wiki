---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Continuous integration and continuous delivery: automatically testing every code change and deploying it through a repeatable process."
related:
  - "[[CI-CD for Data Pipelines]]"
  - "[[Declarative Automation Bundles]]"
  - "[[Git Folders and Workspace Files]]"
  - "[[Testing Data Pipelines]]"
  - "[[Databricks CLI]]"
  - "[[Terraform Provider]]"
aliases:
  - "CI/CD"
  - "CI"
  - "CD"
  - "continuous integration"
  - "continuous delivery"
  - "continuous deployment"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# CI-CD

> [!eli5] Summary
> CI/CD automatically checks each change to code and, if the checks pass, deploys it the same way every time. It replaces manual copying and editing of production code.

**In data work:** Continuous integration (CI) runs automated tests on every change pushed to [[Git]]. Continuous delivery or deployment (CD) promotes passing changes to staging and production with a script rather than by hand. Common CI systems are GitHub Actions, Azure DevOps Pipelines, GitLab CI, and Jenkins. For data teams, CI/CD prevents untested edits to production pipelines.

**In Databricks:** Databricks recommends [[Declarative Automation Bundles]] (formerly Databricks Asset Bundles) for CI/CD. A bundle defines jobs, pipelines, and other resources as source-controlled files. A CI system runs the [[Databricks CLI]] to validate and deploy the bundle to dev, staging, and prod workspaces, authenticating as a [[Users Groups and Service Principals|service principal]]; Databricks suggests workload identity federation so no long-lived secret is stored in the CI system. Developers work in [[Git Folders and Workspace Files|Git folders]]. See [[CI-CD for Data Pipelines]] and [[Testing Data Pipelines]].

Seen in: [[CI-CD for Data Pipelines]], [[Declarative Automation Bundles]], [[Testing Data Pipelines]], [[Path - Data Engineer]]

## Recall

What is the difference between CI and CD?::CI tests every change automatically; CD deploys passing changes to environments automatically.
What does Databricks recommend for CI/CD of jobs and pipelines?::Declarative Automation Bundles, deployed with the Databricks CLI.

> [!sources]- Sources (last verified: 2026-10-25)
> - [CI/CD on Databricks (AWS)](https://docs.databricks.com/aws/en/dev-tools/ci-cd)
> - [Developer best practices on Databricks (AWS)](https://docs.databricks.com/aws/en/developers/best-practices)
