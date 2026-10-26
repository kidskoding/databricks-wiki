---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A network address, usually a URL, where a service accepts requests; on Databricks the word names model serving endpoints, AI Search endpoints, and the connection details of SQL warehouses."
related:
  - "[[Model Serving]]"
  - "[[APIs]]"
  - "[[REST]]"
  - "[[SQL Warehouses]]"
  - "[[AI Search]]"
  - "[[Private Endpoint]]"
aliases:
  - "Serving endpoint"
  - "API endpoint"
  - "Endpoints"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Endpoint

> [!eli5] Summary
> An endpoint is an address that a program sends requests to. Like a phone number for a service, it is where you call to get something done.

**In data work:** In web APIs, an endpoint is a specific URL and HTTP method that performs one operation, for example `POST /orders`. More loosely, an endpoint is any reachable service address that accepts connections. Endpoints are secured with authentication [[Token|tokens]] and, in private networks, by restricting where they can be reached from.

**In Databricks:** The term appears in several places:

| Usage | What it is |
|---|---|
| [[Model Serving]] endpoint | A named, scalable service that hosts models; you query it with `POST https://<workspace>/serving-endpoints/<name>/invocations`. |
| [[AI Search]] endpoint | The compute that hosts one or more vector indexes. |
| [[SQL Warehouses\|SQL warehouse]] | BI tools connect to its server hostname and HTTP path over [[JDBC and ODBC]]. |
| [[Private Endpoint]] | An Azure networking resource that gives a service a private IP address (see [[Azure Private Link]]). |

Requests need a Databricks OAuth token or [[Personal Access Token|personal access token]].

Small-business example: a web shop calls a serving endpoint's `invocations` URL to get product recommendations for each visitor.

Seen in: [[Model Serving]], [[Foundation Model APIs]], [[AI Search]]

## Recall

What URL path do you POST to when querying a Databricks model serving endpoint?::/serving-endpoints/<name>/invocations
Endpoint::A network address where a service accepts requests.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Query serving endpoints for custom models (AWS)](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-custom-model-endpoints)
> - [Manage model serving endpoints (Azure)](https://learn.microsoft.com/en-us/azure/databricks/machine-learning/model-serving/manage-serving-endpoints)
> - [Create AI Search endpoints and indexes (AWS)](https://docs.databricks.com/aws/en/vector-search/create-vector-search)
