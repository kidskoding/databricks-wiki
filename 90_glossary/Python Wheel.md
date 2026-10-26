---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The standard packaged format (a .whl file) for distributing Python code so it installs with pip without a build step."
related:
  - "[[Libraries and Environments]]"
  - "[[Lakeflow Jobs]]"
  - "[[Declarative Automation Bundles]]"
  - "[[Python for Data]]"
  - "[[CI-CD for Data Pipelines]]"
  - "[[Volumes]]"
aliases:
  - "wheel"
  - ".whl"
  - "wheel file"
  - "python_wheel_task"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Python Wheel

> [!eli5] Summary
> A Python wheel is a ready-to-install package of Python code in a single file. It lets you reuse the same tested code across many jobs.

**In data work:** A wheel (`.whl`) is a zip archive with a standard layout and metadata: package name, version, and dependencies. Build tools such as `setuptools` produce it in a `dist/` folder, and `pip install` installs it without running build steps on the target machine. Packaging shared logic as a wheel, instead of copying functions between notebooks, gives you versioning, unit tests, and one place to fix bugs.

**In Databricks:** Wheels are used in two ways.
- **As a library:** Install a wheel on compute or in a serverless environment (see [[Libraries and Environments]]). Databricks recommends storing libraries in workspace files or Unity Catalog [[Volumes|volumes]].
- **As a job task:** A Python wheel task in [[Lakeflow Jobs]] runs an entry point from the wheel. You set the package name and entry point, which must match one defined in the package metadata, and arguments are passed as command-line arguments. On serverless compute, the task requires an `environment_key`.

In [[Declarative Automation Bundles]], the task looks like this:

```yaml
tasks:
  - task_key: nightly_load
    python_wheel_task:
      package_name: my_package
      entry_point: main
    libraries:
      - whl: ./my_package/dist/my_package-*.whl
```

A one-person data team can build the wheel in [[CI-CD for Data Pipelines|CI]], deploy it with the bundle, and reuse it across every job.

Seen in: [[Libraries and Environments]], [[Lakeflow Jobs]], [[Declarative Automation Bundles]]

## Recall

Python wheel::A .whl file: the standard built package format for Python code, installable with pip.
Which two fields define a Python wheel task?::package_name and entry_point.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Use a Python wheel file in Lakeflow Jobs (AWS)](https://docs.databricks.com/aws/en/jobs/how-to/use-python-wheels-in-workflows)
> - [Python wheel task for jobs (AWS)](https://docs.databricks.com/aws/en/jobs/tasks/python-wheel)
> - [Python wheel task for jobs (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/jobs/tasks/python-wheel)
> - [Add tasks to jobs in Declarative Automation Bundles (AWS)](https://docs.databricks.com/aws/en/dev-tools/bundles/job-task-types)
