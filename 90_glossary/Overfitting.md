---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "When a model memorizes its training data and then does badly on new data."
related:
  - "[[Machine Learning Basics]]"
  - "[[Training]]"
  - "[[Experiment Tracking]]"
  - "[[AutoML]]"
  - "[[MLflow]]"
aliases:
  - "overfit"
  - "overtraining"
  - "high variance"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Overfitting

> [!eli5] Summary
> Overfitting is when a model memorizes its training data instead of learning the general pattern. It scores well on known data and poorly on new data.

**In data work:** A model overfits when it learns noise and quirks of its training data instead of the real pattern. The tell-tale sign is a big gap between scores on training data and on held-out validation or test data. Causes include too little data, too many [[Feature|features]], or a model that is too complex. Fixes include more data, simpler models, regularization, and cross-validation. A pet store forecasting weekly sales from one unusual year might build a model that expects a pandemic spike every spring. Underfitting is the opposite: the model is too simple to capture the pattern at all.

**In Databricks:** On Databricks you catch overfitting by logging both training and validation metrics to [[MLflow]] and comparing runs in [[Experiment Tracking]]. [[AutoML]] splits data into training, validation, and test sets for you and reports metrics on each. See [[Machine Learning Basics]] for how the split works.

Seen in: [[Machine Learning Basics]], [[Experiment Tracking]], [[AutoML]]

## Recall

Overfitting::A model that memorizes training data and fails on new data; spot it by comparing training and validation metrics.
