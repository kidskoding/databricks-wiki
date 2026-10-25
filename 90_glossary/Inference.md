---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Using a trained model to produce predictions or generated output for new inputs."
related:
  - "[[Model Serving]]"
  - "[[Machine Learning Basics]]"
  - "[[AI Functions in SQL]]"
  - "[[Foundation Model APIs]]"
  - "[[Models in Unity Catalog]]"
  - "[[Feature Engineering and Feature Store]]"
aliases:
  - "prediction"
  - "scoring"
  - "model inference"
  - "batch inference"
  - "real-time inference"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Inference

> [!eli5] Summary
> Inference is when a trained model is put to use: it receives new data and returns a prediction or an answer.

**In data work:** After [[Training|training]], a [[Model|model]] performs inference on new inputs. Batch inference scores many records on a schedule, such as churn risk for every customer each night. Real-time inference answers individual requests within milliseconds, such as a fraud check at checkout. For an [[LLM]], inference is generating a response to a [[Prompt|prompt]], metered in [[Token|tokens]].

**In Databricks:** For real-time inference, [[Model Serving]] exposes models registered in [[Models in Unity Catalog]] as REST endpoints, and [[Foundation Model APIs]] provide hosted LLM endpoints. For batch inference, the `ai_query` SQL function ([[AI Functions in SQL]]) invokes a serving endpoint over a table and can run in Lakeflow pipelines, jobs, and Structured Streaming; Databricks recommends Databricks-hosted foundation models (prefixed `databricks-`) for batch use. Batch usage appears in `system.billing.usage` under the `BATCH_INFERENCE` offering type. AI Gateway inference tables log endpoint requests and responses to Delta tables.

Seen in: [[Model Serving]], [[Machine Learning Basics]], [[AI Functions in SQL]], [[Foundation Model APIs]]

## Recall

What is the difference between training and inference?::Training fits the model to data; inference applies the trained model to new inputs.
Which SQL function runs batch inference against a serving endpoint?::ai_query.

> [!sources]- Sources (last verified: 2026-10-25)
> - [ai_query function (AWS)](https://docs.databricks.com/aws/en/sql/language-manual/functions/ai_query)
> - [Transform unstructured data using AI Functions (AWS)](https://docs.databricks.com/aws/en/large-language-models/ai-functions)
> - [Log requests and responses to inference tables (Azure)](https://learn.microsoft.com/en-us/azure/databricks/ai-gateway/inference-tables)
