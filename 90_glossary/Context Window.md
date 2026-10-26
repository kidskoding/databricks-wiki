---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The maximum amount of text, measured in tokens, that a large language model can read and write in a single request."
related:
  - "[[Token]]"
  - "[[LLM]]"
  - "[[Generative AI and LLMs]]"
  - "[[Retrieval-Augmented Generation]]"
  - "[[Chunking]]"
  - "[[Foundation Model APIs]]"
aliases:
  - "Context length"
  - "Context size"
  - "Token limit"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Context Window

> [!eli5] Summary
> The context window is how much an AI model can keep in view at once. Your question, any documents you include, and the model's answer all have to fit in it.

**In data work:** A [[LLM|large language model]] processes text as [[Token|tokens]]. The context window is the limit on input plus output tokens per request. Content outside the window is not seen at all. Larger windows let you include more documents or longer conversations, but cost and [[Latency|latency]] grow with every token sent. Separate limits often apply to output tokens alone.

**In Databricks:** Each model on [[Foundation Model APIs]] has its own context length, listed on the supported-models page. For example, Databricks lists 128K-token windows for Llama 3.3 70B Instruct and GPT OSS 120B, and defers to the provider's published limits for OpenAI, Google, and Anthropic models. Pay-per-token endpoints also enforce per-model maximum output tokens and rate limits. The `error_behavior` request parameter controls whether an over-long request returns an error or is truncated.

Small-business example: rather than pasting a full 300-page supplier catalog into every prompt, a shop uses [[Retrieval-Augmented Generation|RAG]] to send only the five most relevant [[Chunking|chunks]], which fits easily in the window and costs less.

Seen in: [[Foundation Model APIs]], [[Retrieval-Augmented Generation]], [[Generative AI and LLMs]]

## Recall

What counts against a model's context window?::All input tokens (prompt, documents, history) plus the output tokens.
Where do you find context lengths for Databricks-hosted models?::The Foundation Model APIs supported-models page.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Supported models for Foundation Model APIs (AWS)](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models)
> - [Foundation Model APIs limits and quotas (AWS)](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/limits)
> - [Foundation model REST API reference (Azure)](https://learn.microsoft.com/en-us/azure/databricks/machine-learning/foundation-model-apis/api-reference)
