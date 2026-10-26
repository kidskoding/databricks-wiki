---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A setting chosen before training a machine learning model, such as tree depth or learning rate, as opposed to the parameters the model learns from data."
related:
  - "[[Machine Learning Basics]]"
  - "[[Training]]"
  - "[[AutoML]]"
  - "[[Experiment Tracking]]"
  - "[[MLflow]]"
  - "[[Overfitting]]"
aliases:
  - "Hyperparameters"
  - "Hyperparameter tuning"
  - "HPO"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Hyperparameter

> [!eli5] Summary
> A hyperparameter is a knob you set before a model learns, such as how many questions a decision tree may ask. You try several settings and keep the one that predicts best.

**In data work:** During [[Training|training]], a model learns parameters (for example, regression weights) from data. Hyperparameters control that process and are fixed beforehand: the number of trees, maximum depth, learning rate, regularization strength. Hyperparameter tuning searches over candidate values, trains a model for each, and compares scores on validation data. Grid search, random search, and Bayesian optimization are common methods. Poor choices cause [[Overfitting|overfitting]] or underfitting.

**In Databricks:** Databricks recommends **Optuna** for single-node tuning and **Ray Tune** for distributed tuning. Hyperopt is deprecated: the open-source project is no longer maintained, and it is not included in Databricks Runtime for Machine Learning after 16.4 LTS ML. Log each trial with [[MLflow]] so results appear in [[Experiment Tracking|experiment tracking]]; MLlib `CrossValidator` and `TrainValidationSplit` log automatically. [[AutoML]] runs a tuning search for you.

Small-business example: a bakery's demand forecast improves when tuning tries tree depths of 3 to 10 and keeps depth 6, which scores best on the last eight weeks of sales.

Seen in: [[AutoML]], [[Experiment Tracking]], [[Machine Learning Basics]]

## Recall

What is the difference between a parameter and a hyperparameter?::Parameters are learned from data; hyperparameters are set before training.
Which tuning libraries does Databricks recommend now that Hyperopt is deprecated?::Optuna for single-node and Ray Tune for distributed tuning.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Hyperparameter tuning (AWS)](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/)
> - [Hyperparameter tuning (Azure)](https://learn.microsoft.com/en-us/azure/databricks/machine-learning/automl-hyperparam-tuning/)
