---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A large language model: an AI trained on huge amounts of text that predicts and generates language."
related:
  - "[[Generative AI and LLMs]]"
  - "[[Foundation Model APIs]]"
  - "[[Retrieval-Augmented Generation]]"
  - "[[Fine-Tuning]]"
  - "[[AI Gateway]]"
  - "[[AI Functions in SQL]]"
aliases:
  - "Large Language Model"
  - "LLMs"
  - "foundation model"
  - "language model"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# LLM

> [!eli5] Summary
> A large language model (LLM) is an AI system trained on very large amounts of text to predict and generate language. It can answer questions, summarize, classify, and draft text.

**In data work:** A large language model is a [[Model|model]] trained on very large text collections to predict the next [[Token|token]]. This capability supports chat, summarizing, classification, extraction, and code writing. LLMs work from a [[Prompt|prompt]] and have no live knowledge of your business unless you supply it, and they can produce fluent but incorrect answers ([[Hallucination|hallucinations]]). A landscaping company might use an LLM to sort incoming emails into quotes, complaints, and scheduling requests, or to draft replies from past job notes.

**In Databricks:** Databricks gives access to hosted LLMs through [[Foundation Model APIs]] and [[Model Serving]], and governs that access with [[AI Gateway]]. You can call an LLM from SQL with [[AI Functions in SQL]], ground it in your data with [[Retrieval-Augmented Generation]] and [[Vector Search]], or adapt it with [[Fine-Tuning]]. The background is in [[Generative AI and LLMs]].

Seen in: [[Generative AI and LLMs]], [[Foundation Model APIs]], [[AI Functions in SQL]], [[Retrieval-Augmented Generation]]

## Recall

LLM::A large language model: AI trained on huge text collections to predict the next token, which lets it chat, summarize, and write.
