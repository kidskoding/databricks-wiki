---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Low-Rank Adaptation: a fine-tuning method that freezes a model's original weights and trains small added matrices, which cuts the memory and storage needed to customize a large language model."
related:
  - "[[Fine-Tuning]]"
  - "[[LLM]]"
  - "[[GPU]]"
  - "[[AI Runtime]]"
  - "[[Model Serving]]"
  - "[[MosaicML and Open Models]]"
aliases:
  - "Low-Rank Adaptation"
  - "LoRA adapter"
  - "PEFT"
  - "Parameter-efficient fine-tuning"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# LoRA

> [!eli5] Summary
> LoRA is a cheap way to teach a large AI model a new skill. Instead of changing the whole model, it trains a small add-on that adjusts the model's behavior.

**In data work:** Full [[Fine-Tuning|fine-tuning]] updates every weight in a model, which needs large [[GPU|GPUs]] and stores a full copy per task. LoRA keeps the original weights frozen and learns a low-rank update `ΔW = BA` for selected layers, where the rank `r` is much smaller than the layer size. Only `A` and `B` are trained, so the adapter is a small fraction of the model's size. Key settings are rank `r`, scaling `alpha`, and which layers to target. One base model can serve several adapters, one per task. LoRA is the most widely used parameter-efficient fine-tuning (PEFT) method.

**In Databricks:** Databricks recommends starting with LoRA before full fine-tuning. Its [[AI Runtime]] serverless GPU tutorials fine-tune open models such as Llama 3.2 1B with LoRA using the Hugging Face libraries, and the adapters can then be registered in [[Models in Unity Catalog|Unity Catalog]] and deployed with [[Model Serving]]. The older Foundation Model Fine-tuning product is marked end of life in the Databricks docs.

Small-business consideration: try prompt engineering and [[Retrieval-Augmented Generation|RAG]] first. Use LoRA only when you need a consistent output style or format that prompts cannot achieve, and have a few hundred good examples.

Seen in: [[Fine-Tuning]], [[AI Runtime]]

## Recall

What does LoRA train instead of the full model weights?::Small low-rank matrices added to selected layers, with the base weights frozen.
Why can one base model serve many LoRA adapters?::The base weights are unchanged, so adapters are small add-ons swapped per task.

> [!sources]- Sources (last verified: 2026-10-26)
> - [A Practical Guide to LLM Fine Tuning (databricks.com blog)](https://www.databricks.com/blog/llm-fine-tuning)
> - [Fine-tune Llama 3.2 1B with LoRA using Serverless GPU (Azure)](https://learn.microsoft.com/en-us/azure/databricks/machine-learning/ai-runtime/examples/tutorials/sgc-sft-trl-deepspeed-llama-1b)
> - [Fast PEFT Serving at Scale (databricks.com blog)](https://www.databricks.com/blog/fast-peft-serving-scale)
> - [Foundation Model Fine-tuning (EoL) (AWS)](https://docs.databricks.com/aws/en/large-language-models/foundation-model-training/)
