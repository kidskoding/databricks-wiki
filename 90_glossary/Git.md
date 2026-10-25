---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A distributed version-control system that records every change to code and supports parallel work through branches."
related:
  - "[[Git Folders and Workspace Files]]"
  - "[[CI-CD for Data Pipelines]]"
  - "[[Declarative Automation Bundles]]"
  - "[[dbt]]"
  - "[[Notebooks]]"
  - "[[CI-CD]]"
aliases:
  - "version control"
  - "GitHub"
  - "GitLab"
  - "Azure DevOps"
  - "Bitbucket"
  - "repository"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Git

> [!eli5] Summary
> Git keeps a full history of changes to code. It shows who changed what and why, allows any change to be undone, and lets several people work on copies that are later combined.

**In data work:** Git stores code in a repository. Changes are recorded as commits on branches and merged into the main branch, usually after review in a pull request on a host such as GitHub, GitLab, Bitbucket, or Azure DevOps. Git is the foundation of [[CI-CD]]. Version control replaces file-naming conventions such as `report_final_v3.sql` and makes any past version recoverable.

**In Databricks:** [[Git Folders and Workspace Files|Git folders]] (formerly Repos) are a Git client in the workspace: you clone a remote repository, create branches, commit, and pull while editing [[Notebooks|notebooks]] and files. Git folders require a remote repository URL, can exist outside the `/Repos` directory, and can contain assets such as Databricks SQL objects and MLflow experiments. Existing `/Repos` paths continue to work. For deployment, [[Declarative Automation Bundles]] keep job and pipeline definitions in the same repository ([[CI-CD for Data Pipelines]]).

Seen in: [[Git Folders and Workspace Files]], [[CI-CD for Data Pipelines]], [[Declarative Automation Bundles]], [[dbt]]

## Recall

What is a Git commit?::A recorded snapshot of changes, with a message, in the repository history.
What were Databricks Git folders formerly called?::Repos.

> [!sources]- Sources (last verified: 2026-10-25)
> - [What happened to Databricks Repos? (AWS)](https://docs.databricks.com/aws/en/repos/what-happened-repos)
> - [Databricks Git folders (AWS)](https://docs.databricks.com/aws/en/repos/)
