---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Splitting long documents into smaller passages before embedding them, so a retrieval system can find and return only the relevant parts."
related:
  - "[[Retrieval-Augmented Generation]]"
  - "[[Embedding]]"
  - "[[AI Search]]"
  - "[[Context Window]]"
  - "[[Token]]"
  - "[[Hybrid Search]]"
aliases:
  - "Text chunking"
  - "Document chunking"
  - "Chunk"
  - "Chunk size"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Chunking

> [!eli5] Summary
> Chunking cuts long documents into short pieces. An AI assistant can then search those pieces and read only the few that answer a question.

**In data work:** In a [[Retrieval-Augmented Generation|RAG]] pipeline, documents are parsed, split into chunks, turned into [[Embedding|embeddings]], and stored in a search index. Common strategies split by a fixed number of characters or [[Token|tokens]], by sentence or paragraph, or by document structure such as headings. Chunk size is a trade-off: small chunks are precise but lose surrounding context, while large chunks keep context but bring in irrelevant text and cost more. Many pipelines add a small overlap between neighboring chunks so a fact is not cut in half. Embedding models have their own token limit, and text beyond it is truncated.

**In Databricks:** Databricks documents chunking as a step in the unstructured data pipeline for RAG: parse, chunk, embed, then index in [[AI Search]]. Chunks are usually stored in a [[Delta Lake|Delta]] table so the index can sync from it. Databricks does not publish one recommended chunk size; you tune it against an evaluation set (see [[Agent Evaluation and Tracing]]).

Small-business example: a 40-page employee handbook split into section-sized chunks lets a help bot answer a question about vacation policy from the right paragraph.

Seen in: [[Retrieval-Augmented Generation]], [[AI Search]], [[Agent Evaluation and Tracing]]

## Recall

Why do RAG pipelines chunk documents?::So retrieval can find and return only the relevant passages, within the model's and embedding model's token limits.
What is the trade-off in chunk size?::Small chunks are precise but lose context; large chunks keep context but add noise and cost.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Build an unstructured data pipeline for RAG (AWS)](https://docs.databricks.com/aws/en/generative-ai/tutorials/ai-cookbook/quality-data-pipeline-rag)
> - [Build an unstructured data pipeline for RAG (GCP)](https://docs.databricks.com/gcp/en/agents/tutorials/ai-cookbook/quality-data-pipeline-rag)
