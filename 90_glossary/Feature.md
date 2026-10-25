---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A measurable input variable that a machine-learning model uses to make predictions."
related:
  - "[[Feature Engineering and Feature Store]]"
  - "[[Machine Learning Basics]]"
  - "[[Model Serving]]"
  - "[[Training]]"
  - "[[AutoML]]"
  - "[[Label]]"
aliases:
  - "features"
  - "feature engineering"
  - "input variable"
  - "predictor"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Feature

> [!eli5] Summary
> A feature is one piece of information given to a machine-learning model, such as the number of days since a customer's last order. The model learns patterns from many features.

**In data work:** A feature is a property of each example used as model input. Raw data is usually transformed into features through feature engineering, for example "orders in the last 30 days" or "average basket size". The [[Label|label]] is the value the model predicts; features are the inputs. Features must be computed identically during [[Training|training]] and at prediction time; a mismatch (training-serving skew) degrades accuracy. Example: a churn model uses recency, order frequency, and total spend per customer.

**In Databricks:** In [[Unity Catalog]], any Delta table with a primary key constraint can serve as a feature table ([[Feature Engineering and Feature Store]]). Models logged with `FeatureEngineeringClient.log_model` carry feature metadata, so [[Model Serving]] looks up features by entity ID from an online store at inference time. Databricks now recommends Feature Views for most new projects; feature tables remain for cases such as OpenSharing or third-party online stores. Do not change a feature table's primary key or existing feature types, as this breaks downstream pipelines.

Seen in: [[Feature Engineering and Feature Store]], [[Machine Learning Basics]], [[Model Serving]], [[AutoML]]

## Recall

What is the difference between a feature and a label?::A feature is a model input; the label is the value the model predicts.
Which Unity Catalog tables can serve as feature tables?::Any Delta table with a primary key constraint.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Feature tables in Unity Catalog (AWS)](https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/feature-tables-uc)
> - [Model Serving with automatic feature lookup (AWS)](https://docs.databricks.com/aws/en/machine-learning/feature-store/automatic-feature-lookup)
> - [Databricks Feature Store overview and glossary (AWS)](https://docs.databricks.com/aws/en/machine-learning/feature-store/concepts)
