---
type: path
status: written
level: 80
section: Learning Paths
depth: 201
summary: Notebooks, Spark, MLflow, the feature store, and serving.
personas:
  - scientist
chapter: "[[Chapter 80 - Learning Paths]]"
prev: "[[Path - Data Engineer]]"
next: "[[Path - AI App Developer]]"
evolved_from: []
evolved_into: []
cloud_equivalent: []
related:
  - "[[Notebooks]]"
  - "[[PySpark]]"
  - "[[Libraries and Environments]]"
  - "[[Machine Learning Basics]]"
  - "[[MLflow]]"
  - "[[Experiment Tracking]]"
  - "[[AutoML]]"
  - "[[Feature Engineering and Feature Store]]"
  - "[[Models in Unity Catalog]]"
  - "[[Model Serving]]"
  - "[[Data Quality Monitoring]]"
  - "[[AI Runtime]]"
  - "[[Path - Data Engineer]]"
  - "[[Path - AI App Developer]]"
  - "[[Path - Certification Prep]]"
aliases:
  - ML Path
  - Data Science Path
  - MLOps Path
prereqs:
  - "[[Path - Absolute Beginner]]"
unlocks:
  - "[[Path - AI App Developer]]"
  - "[[Path - Certification Prep]]"
clouds:
  - aws
  - azure
  - gcp
mastery: new
last_verified: 2026-10-25
tags:
  - path
---

# Path - Data Scientist and ML Engineer

> [!persona] Who this is for
> **Who:** a data scientist used to pandas and Jupyter, or an ML engineer who has to get models into production.
> **Goal:** train models on lakehouse data, track every experiment, govern models like tables, and serve and monitor them.
> **Outcome:** you can take a model from a notebook to a versioned, aliased model in Unity Catalog, serve it or batch-score it on a schedule, and watch it for drift.

## Before you start

You should know Python and pandas and have trained at least one scikit-learn model. Spark experience is not required. [[Databricks Free Edition and Trials|Free Edition]] covers Stages 1 and 2 and most of Stage 3. GPU work in Stage 4 needs a paid or trial workspace on your cloud.

## The route

### Stage 1: Notebooks, Python, and Spark (101 to 201)

**Goal:** be productive in a Databricks notebook with data too big for pandas.

1. [[Python for Data]]: the starting point you already know.
2. [[Notebooks]]: Databricks notebooks versus Jupyter.
3. [[PySpark]]: Spark from Python.
4. [[DataFrames]]: Spark DataFrames versus pandas DataFrames.
5. [[Lazy Evaluation]] (201): why your cell returned instantly and the next one took a minute.
6. [[Libraries and Environments]] (201): `%pip`, environments, and pinning versions.
7. [[Volumes]] (201): where images, CSVs, and other files live.
8. [[Databricks Runtime]] (201): the ML runtime and its preinstalled libraries.
9. [[All-Purpose Compute]] (201): interactive clusters when serverless is not enough.

> [!check] Checkpoint
> In a notebook, `%pip install` a library you like, read a sample table with `spark.table(...)`, aggregate it in Spark, and convert only the small result with `.toPandas()`. Explain in a text cell why you aggregated before converting.

### Stage 2: Classic ML with MLflow (101 to 201)

**Goal:** train, compare, and record models properly.

1. [[Machine Learning Basics]]: training, features, labels, and predictions.
2. [[MLflow]]: the open-source backbone for ML on Databricks.
3. [[Experiment Tracking]] (201): logging parameters, metrics, and artifacts for every run.
4. [[AutoML]]: let Databricks try baselines and hand you the notebook.
5. [[MLlib]] (201): Spark's built-in ML, for when data really is huge.

> [!check] Checkpoint
> Train a scikit-learn regressor on a sample table with `mlflow.autolog()` turned on, three times with different hyperparameters. Open the **Experiments** page, compare the three runs on one chart, and note which parameters produced the best metric.

### Stage 3: Production ML (201 to 301)

**Goal:** make models reproducible, governed, and live.

1. [[Feature Engineering and Feature Store]] (301): reusable features consistent between training and serving.
2. [[Models in Unity Catalog]] (201): versions, aliases, and permissions for models.
3. [[Model Serving]] (201): an autoscaling REST endpoint for a model.
4. [[Lakeflow Jobs]]: scheduled retraining and batch scoring.
5. [[Data Quality Monitoring]] (301): drift and freshness checks on tables and inference logs.
6. [[Declarative Automation Bundles]] (301): ship the training job and endpoint from Git.
7. [[System Tables]] (201): see what your training and serving cost.

> [!check] Checkpoint
> Register your best run to Unity Catalog with `mlflow.set_registry_uri("databricks-uc")` and `mlflow.register_model(..., "<catalog>.<schema>.my_model")`. Give it the alias `champion`, then load it with `mlflow.pyfunc.load_model("models:/<catalog>.<schema>.my_model@champion")` and batch-score a table. Schedule that scoring notebook as a job. If your workspace allows serving endpoints, deploy the model and call it once.

### Stage 4: Deep learning and LLMs (301 to 401)

**Goal:** know when you need GPUs and when a foundation model does the job.

1. [[AI Runtime]] (301): GPU clusters and serverless GPUs.
2. [[Generative AI and LLMs]]: what changes when the model is a language model.
3. [[Foundation Model APIs]] (201): hosted LLMs you call by the token.
4. [[Agent Evaluation and Tracing]] (301): measuring LLM quality with judges and traces in MLflow.
5. [[Fine-Tuning]] (401): further training a foundation model, and when not to bother.
6. [[MosaicML and Open Models]] (201): where Databricks' model work came from.

> [!check] Checkpoint
> Call a hosted foundation model from SQL with `ai_query()` or from Python with the MLflow deployments client, and log the prompt, response, and latency to an MLflow run. Write down one task where this beats training your own model and one where it does not.

## Rabbit holes

- **Spark performance for ML:** [[Partitions]], [[Shuffles]], [[Spark UI]], [[Photon]].
- **Feature pipelines:** [[Lakeflow Spark Declarative Pipelines]] and [[Change Data Feed]].
- **Working from your IDE:** [[Databricks Connect]] and [[Git Folders and Workspace Files]].
- **Governance of AI:** [[Unity Gateway]] and [[Unity Catalog]].
- **Cloud GPUs and node types:** [[EC2 Instance Types and Graviton]], [[Compute on Google Cloud]], and the cloud routes [[Path - Azure Deep Dive]], [[Path - AWS Deep Dive]], [[Path - Google Cloud Deep Dive]].
- **Exams:** the ML Associate and Professional tracks in [[Path - Certification Prep]].

## You are done when

- You can work in a notebook on data larger than pandas can hold.
- Every model you train is tracked in MLflow with its parameters and metrics.
- You can register a model in Unity Catalog, alias it, and load it by alias.
- You can batch-score on a schedule and know how to serve in real time.
- You can set up monitoring for drift on a table or inference log.
- You can choose between a classic model, a hosted LLM, and fine-tuning.

> [!nextup] Up next
> Models become products when they sit inside an app. That is [[Path - AI App Developer]].

> [!sources]- Sources (last verified: 2026-10-25)
> - Route assembled on 2026-10-25 from the vault index (`llms.txt`) and the `scientist` persona tags in `_meta/manifest.yaml`. Product facts and official documentation links live in each linked note's `[!sources]` callout.
> - The MLflow calls in the checkpoints are standard MLflow APIs. Free Edition availability of AutoML, Model Serving, and GPUs was not re-checked for this path; see [[Databricks Free Edition and Trials]].
