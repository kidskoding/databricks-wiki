---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A neural network design in which a router sends each token to a few specialist sub-networks, so a large model uses only part of its weights per token."
related:
  - "[[LLM]]"
  - "[[Generative AI and LLMs]]"
  - "[[MosaicML and Open Models]]"
  - "[[Foundation Model APIs]]"
  - "[[Inference]]"
  - "[[Model]]"
aliases:
  - "MoE"
  - "mixture-of-experts"
  - "sparse model"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Mixture of Experts

> [!eli5] Summary
> A mixture-of-experts model contains many smaller specialist parts. For each piece of text, it picks only a few of them to do the work, which makes a very large model faster to run.

**In data work:** In a standard ("dense") [[LLM]], every parameter is used for every [[Token|token]]. An MoE layer replaces one large feed-forward block with several "expert" blocks and a small router network. For each token, the router chooses a few experts, and only those run. The model's total parameter count can be very large while the active parameter count per token, which drives [[Inference|inference]] cost and speed, stays much smaller. The trade-off is memory: all experts must still be loaded, so serving an MoE model needs enough GPU memory for the full parameter count.

**In Databricks:** DBRX, the open model Databricks released in March 2024, is a fine-grained MoE model. It has 132 billion total parameters, of which 36 billion are active for any input, and it uses 16 experts and chooses 4 per token. The work built on the MosaicML research Databricks acquired (see [[MosaicML and Open Models]]). For a small business, MoE is a model-architecture detail: it affects speed and quality, but you call the model the same way as any other.

Seen in: [[MosaicML and Open Models]], [[Generative AI and LLMs]], [[Foundation Model APIs]]

## Recall

Mixture of experts::A model design where a router sends each token to a few expert sub-networks, so only part of the model's weights run per token.
How many total and active parameters does DBRX have?::132 billion total, 36 billion active per input (4 of 16 experts).

> [!sources]- Sources (last verified: 2026-10-26)
> - [Introducing DBRX: a new state-of-the-art open LLM (Databricks blog)](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm)
> - [Announcing DBRX (Databricks blog)](https://www.databricks.com/blog/announcing-dbrx-new-standard-efficient-open-source-customizable-llms)
