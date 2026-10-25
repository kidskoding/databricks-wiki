---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Output from an AI model that is false or unsupported but presented as fact."
related:
  - "[[Generative AI and LLMs]]"
  - "[[Retrieval-Augmented Generation]]"
  - "[[Agent Evaluation and Tracing]]"
  - "[[AI Gateway]]"
  - "[[Vector Search]]"
  - "[[Genie]]"
aliases:
  - "hallucinations"
  - "confabulation"
  - "ungrounded answer"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Hallucination

> [!eli5] Summary
> A hallucination is an AI answer that sounds confident but is wrong or made up.

**In data work:** [[LLM|Large language models]] generate likely text from learned patterns rather than retrieving verified facts, so they can produce fluent but incorrect output: invented figures, nonexistent citations, or fabricated policies. The risk is highest for private or recent information the model was not trained on. Mitigations are grounding answers in retrieved documents, requiring citations, restricting the model to defined tools, and systematic evaluation.

**In Databricks:** [[Retrieval-Augmented Generation]] grounds answers in documents retrieved with Databricks AI Search ([[Vector Search]]). In [[MLflow]] 3, the built-in `RetrievalGroundedness` judge checks whether a response is supported by the retrieved context, and `RetrievalRelevance` checks whether the context fits the request ([[Agent Evaluation and Tracing]]). [[AI Gateway]] guardrails provide safety filtering, PII detection, and topic restrictions on supported endpoints. [[Genie]] answers by generating SQL that can be inspected.

Seen in: [[Generative AI and LLMs]], [[Retrieval-Augmented Generation]], [[Agent Evaluation and Tracing]], [[Genie]]

## Recall

Why do LLMs hallucinate?::They generate likely text from patterns rather than verifying facts.
Which MLflow judge checks whether an answer is supported by retrieved context?::RetrievalGroundedness.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Built-in LLM judges (AWS)](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges)
> - [AI Gateway for serving endpoints (AWS)](https://docs.databricks.com/aws/en/ai-gateway/overview-serving-endpoints)
