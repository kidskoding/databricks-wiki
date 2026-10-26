---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A retrieval method that combines vector similarity search with keyword search and merges the two ranked result lists."
related:
  - "[[AI Search]]"
  - "[[Embedding]]"
  - "[[Retrieval-Augmented Generation]]"
  - "[[Chunking]]"
  - "[[Index]]"
aliases:
  - "Hybrid retrieval"
  - "query_type HYBRID"
  - "Keyword plus vector search"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Hybrid Search

> [!eli5] Summary
> Hybrid search looks for matches two ways at once: by meaning and by exact words. It then blends the results, so a search for a product code finds that exact code as well as related items.

**In data work:** Vector search compares [[Embedding|embeddings]] and finds passages with similar meaning, but it can miss exact strings such as SKUs, error codes, or names. Keyword search (for example BM25) matches literal terms but misses paraphrases. Hybrid search runs both and fuses the rankings, commonly with Reciprocal Rank Fusion (RRF).

**In Databricks:** [[AI Search]] (previously Mosaic AI Vector Search) supports hybrid queries by setting `query_type="HYBRID"` in the Python SDK, the REST API, or the `vector_search()` SQL function. Keyword and vector results are combined with RRF. By default hybrid search covers all text metadata columns and returns at most 200 results. Databricks recommends it for [[Retrieval-Augmented Generation|RAG]] over data with unique identifiers.

```python
results = index.similarity_search(
    query_text="return policy SKU 44-120",
    columns=["id", "text"],
    num_results=5,
    query_type="HYBRID",
)
```

Small-business example: a parts supplier's support bot finds the right manual page when a customer types an exact part number, which pure vector search often ranks too low.

Seen in: [[AI Search]], [[Retrieval-Augmented Generation]]

## Recall

What two retrieval methods does hybrid search combine?::Vector similarity search and keyword search.
How does Databricks AI Search merge hybrid results?::With Reciprocal Rank Fusion (RRF).

> [!sources]- Sources (last verified: 2026-10-26)
> - [Query an AI Search index (AWS)](https://docs.databricks.com/aws/en/vector-search/query-vector-search)
> - [AI Search retrieval quality guide (AWS)](https://docs.databricks.com/aws/en/vector-search/vector-search-retrieval-quality)
> - [vector_search function (GCP)](https://docs.databricks.com/gcp/en/sql/language-manual/functions/vector_search)
