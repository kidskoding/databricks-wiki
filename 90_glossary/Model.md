---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A trained program that turns inputs into a prediction or generated output."
related:
  - "[[Machine Learning Basics]]"
  - "[[MLflow]]"
  - "[[Models in Unity Catalog]]"
  - "[[Model Serving]]"
  - "[[Training]]"
  - "[[Inference]]"
aliases:
  - "ML model"
  - "machine learning model"
  - "trained model"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Model

> [!eli5] Summary
> A model is a program produced by learning from examples. Given new inputs, it returns a prediction or generated output.

**In data work:** A machine learning model is the result of [[Training|training]]: a learned set of rules or numbers that maps inputs ([[Feature|features]]) to outputs, such as a price, a yes or no, or text. Using it on new data is called [[Inference|inference]]. Models range from a simple linear formula to an [[LLM]] with billions of parameters. A hardware store could train a model on past sales, weather, and holidays to forecast how many bags of salt to order each week. Note: data model also refers to table design (see [[Data Modeling Basics]]), not ML.

**In Databricks:** Databricks tracks training runs with [[MLflow]], registers the resulting models in [[Models in Unity Catalog]] with versions and permissions, and puts them behind an API with [[Model Serving]]. [[AutoML]] can train a baseline model for you, and [[Foundation Model APIs]] give you large pre-trained models without training anything.

Seen in: [[Machine Learning Basics]], [[MLflow]], [[Models in Unity Catalog]], [[Model Serving]]

## Recall

Model::A program learned from examples that maps inputs to a prediction or output; in Databricks it is tracked with MLflow and registered in Unity Catalog.
