---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A directed acyclic graph: a set of steps connected by one-way dependencies with no loops, used to order pipeline and query work."
related:
  - "[[Apache Airflow]]"
  - "[[Lakeflow Jobs]]"
  - "[[Tasks Triggers and Schedules]]"
  - "[[Jobs Stages and Tasks]]"
  - "[[Lazy Evaluation]]"
  - "[[Lakeflow Spark Declarative Pipelines]]"
aliases:
  - "directed acyclic graph"
  - "DAGs"
  - "task graph"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# DAG

> [!eli5] Summary
> A DAG is a diagram of steps and the order they must run in. Arrows show which step depends on which, and the steps never loop back.

**In data work:** In a directed acyclic graph, each edge points from a step to a step that depends on it (directed), and no path returns to an earlier step (acyclic), so execution always terminates. Schedulers use the graph to determine which steps can run in parallel and which must wait. Example: load orders and load customers run in parallel, then a daily sales table is built, then a dashboard refreshes. [[Apache Airflow]] defines pipelines as DAGs written in Python.

**In Databricks:** In [[Lakeflow Jobs]], tasks and their **Depends on** settings form a DAG that the job UI displays; upstream tasks run first, and independent tasks run in parallel ([[Tasks Triggers and Schedules]]). [[Lakeflow Spark Declarative Pipelines]] infer dependencies between datasets from your code and show them in the **Pipeline graph**. In [[Apache Spark]], each query becomes a DAG of stages, visible in the [[Spark UI]] job details page.

Seen in: [[Apache Airflow]], [[Lakeflow Jobs]], [[Tasks Triggers and Schedules]], [[Jobs Stages and Tasks]]

## Recall

What does acyclic mean in DAG?::No path through the graph returns to a step already visited.
Where does a Lakeflow job's DAG come from?::Each task's Depends on settings.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Configure task dependencies (AWS)](https://docs.databricks.com/aws/en/jobs/run-if)
> - [What are pipelines? (AWS)](https://docs.databricks.com/aws/en/ldp/concepts/pipelines)
> - [Debugging with the Spark UI (AWS)](https://docs.databricks.com/aws/en/compute/troubleshooting/debugging-spark-ui)
