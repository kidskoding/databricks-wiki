---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A vector of numbers that represents the meaning of text, images, or other items, so similar items have nearby vectors."
related:
  - "[[AI Search]]"
  - "[[Retrieval-Augmented Generation]]"
  - "[[Generative AI and LLMs]]"
  - "[[Foundation Model APIs]]"
  - "[[Model Serving]]"
  - "[[AI Functions in SQL]]"
aliases:
  - "embeddings"
  - "vector"
  - "vector embedding"
  - "embedding model"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Embedding

> [!eli5] Summary
> An embedding converts text or an image into a list of numbers that captures its meaning. Items with similar meanings get similar numbers, which lets software find related content.

**In data work:** An embedding model maps an input to a fixed-length vector, typically hundreds to a few thousand dimensions. The distance between vectors, often cosine similarity, measures semantic similarity. Embeddings support semantic search, recommendations, clustering, and [[Retrieval-Augmented Generation|RAG]]. Example: embedding product descriptions lets a search for "plants that tolerate shade" return ferns even when the word "shade" is absent.

**In Databricks:** Databricks AI Search ([[AI Search]], renamed in June 2026) can compute embeddings for a Delta Sync index: you choose a text column and an embedding model endpoint (a Databricks-managed model is selected by default), and the index stays in sync with the source table. Unchanged rows reuse existing embeddings on later syncs. You can also supply precomputed embeddings or serve a custom embedding model with [[Model Serving]]. The index is governed by [[Unity Catalog]] and provides the retrieval step for RAG and [[AI Agent|agents]].

Seen in: [[AI Search]], [[Retrieval-Augmented Generation]], [[Generative AI and LLMs]], [[Model Serving]]

## Recall

What does the distance between two embeddings represent?::How similar their meanings are.
What is Databricks Vector Search called since June 2026?::Databricks AI Search.

> [!sources]- Sources (last verified: 2026-10-25)
> - [June 2026 release notes (AWS)](https://docs.databricks.com/aws/en/release-notes/product/2026/june)
> - [Databricks AI Search (AWS)](https://docs.databricks.com/aws/en/ai-search/ai-search)
> - [Create AI Search endpoints and indexes (AWS)](https://docs.databricks.com/aws/en/ai-search/create-ai-search)
