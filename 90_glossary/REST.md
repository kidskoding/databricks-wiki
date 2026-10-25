---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A common style of web API where programs request and change resources over HTTP with GET, POST, and similar verbs."
related:
  - "[[APIs]]"
  - "[[Databricks SDKs and REST API]]"
  - "[[Databricks CLI]]"
  - "[[Terraform Provider]]"
  - "[[Webhook]]"
  - "[[OAuth]]"
aliases:
  - "REST API"
  - "RESTful API"
  - "HTTP API"
  - "Representational State Transfer"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# REST

> [!eli5] Summary
> REST is a common style of web API. Programs use standard web requests to read, create, update, and delete resources identified by URLs.

**In data work:** REST (Representational State Transfer) is a design style for [[APIs]] over HTTP. Each resource has a URL, and standard verbs act on it: `GET` reads, `POST` creates, `PUT`/`PATCH` updates, `DELETE` removes. Requests and responses are usually JSON, and authentication uses a [[Token|token]] in a header. Any language with an HTTP client can call a REST API. A bookkeeping app might call a REST endpoint like `GET /invoices?status=unpaid` to fetch unpaid invoices every morning.

**In Databricks:** Almost everything in Databricks can be done through its REST API: creating clusters, running [[Lakeflow Jobs]], managing permissions, or querying a [[Model Serving]] endpoint. Most people use it through wrappers: the [[Databricks SDKs and REST API|SDKs]], the [[Databricks CLI]], and the [[Terraform Provider]]. Calls authenticate with [[OAuth]] tokens or personal access tokens (see [[Authentication - Tokens and OAuth]]).

Seen in: [[Databricks SDKs and REST API]], [[APIs]], [[Model Serving]]

## Recall

REST::A web API style where URLs name resources and HTTP verbs (GET, POST, PATCH, DELETE) act on them; Databricks exposes nearly everything this way.
