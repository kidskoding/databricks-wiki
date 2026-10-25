---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The process of a machine learning model learning patterns from example data."
related:
  - "[[Machine Learning Basics]]"
  - "[[Experiment Tracking]]"
  - "[[AutoML]]"
  - "[[Fine-Tuning]]"
  - "[[GPU Compute]]"
  - "[[MLflow]]"
aliases:
  - "model training"
  - "train"
  - "fitting"
  - "training run"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Training

> [!eli5] Summary
> Training is the process in which a machine learning model learns patterns from example data by repeatedly adjusting itself to reduce its errors.

**In data work:** Training (or fitting) feeds a [[Model|model]] historical examples, measures how wrong its predictions are against the [[Label|labels]], and adjusts its internal parameters to reduce that error, over and over. The data is split so part of it is held back to test whether the model generalizes or is [[Overfitting|overfitting]]. Training can take seconds for a small model on a laptop or weeks on thousands of [[GPU|GPUs]] for a large language model. Using the trained model on new data is [[Inference|inference]]. A bike shop might train a model on three years of sales to predict demand per model per month.

**In Databricks:** On Databricks you train with libraries such as scikit-learn, XGBoost, or PyTorch in [[Notebooks]], on CPU or [[GPU Compute]], and log each run with [[MLflow]] ([[Experiment Tracking]]). [[AutoML]] runs many training trials for you. For large language models, [[Fine-Tuning]] continues training a pre-trained model on your own data. Trained models are registered in [[Models in Unity Catalog]].

Seen in: [[Machine Learning Basics]], [[Experiment Tracking]], [[AutoML]], [[Fine-Tuning]]

## Recall

Training::Fitting a model by repeatedly adjusting it to reduce errors on labeled examples; on Databricks each run is logged with MLflow.
