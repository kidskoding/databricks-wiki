---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A graphics processing unit: a processor with thousands of parallel cores, used to train and run deep-learning models and LLMs."
related:
  - "[[AI Runtime]]"
  - "[[Fine-Tuning]]"
  - "[[Model Serving]]"
  - "[[Generative AI and LLMs]]"
  - "[[Machine Learning Basics]]"
  - "[[Foundation Model APIs]]"
aliases:
  - "GPUs"
  - "graphics processing unit"
  - "accelerator"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# GPU

> [!eli5] Summary
> A GPU is a processor that performs many small calculations at the same time. That makes it much faster than a regular processor for training and running AI models.

**In data work:** GPUs were designed for graphics, which applies the same arithmetic to many pixels at once. Neural networks consist mostly of the same kind of operation (large matrix multiplications), so GPUs train and run them far faster than CPUs. GPUs are scarce and comparatively expensive. SQL, ETL, and classic machine learning on tabular data usually run efficiently on CPUs; deep learning and [[LLM]] fine-tuning or hosting usually require GPUs.

**In Databricks:** Classic compute offers GPU instance types with GPU-enabled Databricks Runtime ML. **AI Runtime** is serverless GPU compute for deep learning, with A10 and H100 GPUs and PyTorch and CUDA preinstalled; it is in Public Preview as of October 2026 ([[AI Runtime]]). [[Model Serving]] offers GPU workload types for custom models, with availability that varies by cloud and region. For large LLMs, Databricks recommends [[Foundation Model APIs]] over custom GPU serving. See [[Fine-Tuning]].

Seen in: [[AI Runtime]], [[Fine-Tuning]], [[Model Serving]], [[Generative AI and LLMs]]

## Recall

Why are GPUs suited to deep learning?::They run thousands of calculations in parallel, matching the matrix operations in neural networks.
What is the Databricks serverless GPU offering called?::AI Runtime (Public Preview as of October 2026).

> [!sources]- Sources (last verified: 2026-10-25)
> - [AI Runtime (AWS)](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/)
> - [Create custom model serving endpoints (AWS)](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints)
> - [Serve custom LLMs with Custom Model Serving (AWS)](https://docs.databricks.com/aws/en/machine-learning/model-serving/serve-custom-llms)
