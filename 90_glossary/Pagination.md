---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Returning a large result in pages, with a token or offset the client sends back to fetch the next page."
related:
  - "[[REST]]"
  - "[[APIs]]"
  - "[[Databricks SDKs and REST API]]"
  - "[[Databricks CLI]]"
  - "[[Rate Limit]]"
  - "[[Lakeflow Jobs]]"
aliases:
  - "paging"
  - "page token"
  - "next_page_token"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Pagination

> [!eli5] Summary
> Pagination means an API hands back a long list a page at a time instead of all at once. You ask for the next page until there are no more.

**In data work:** List endpoints in [[REST]] [[APIs]] rarely return everything in one response, because large responses are slow and fragile. Two schemes are common. **Offset pagination** (`limit` and `offset`) asks for "50 rows starting at row 100", which can skip or repeat items when the list changes between calls. **Token pagination** returns an opaque cursor that marks where the next page starts, which stays correct as data changes. A script that lists every job in a workspace must loop through all pages or it silently misses items.

**In Databricks:** Most Databricks REST list endpoints use token pagination.
1. Send the first request without `page_token`.
2. Read the results and the `next_page_token` field from the response.
3. Send the next request with `page_token` set to that value.
4. Stop when the response contains no `next_page_token`.

A page can be empty and still carry a token, so test for the token, not for an empty page. In Jobs API 2.2, the `has_more` field was removed from List jobs and List job runs; the presence of `next_page_token` is the only signal. The cluster events API is moving from offset pagination to `page_token`, `next_page_token`, and `prev_page_token`. Heavy paging can hit a [[Rate Limit|rate limit]], so retry HTTP 429 responses with backoff.

```python
params, items = {}, []
while True:
    r = session.get(f"{host}/api/2.2/jobs/list", params=params).json()
    items += r.get("jobs", [])
    if "next_page_token" not in r:
        break
    params["page_token"] = r["next_page_token"]
```

Seen in: [[Databricks SDKs and REST API]], [[Lakeflow Jobs]]

## Recall

Pagination::Returning results in pages; the client passes a token or offset to fetch each next page.
How do you know a Databricks list API has no more pages?::The response has no next_page_token.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Databricks REST API (AWS)](https://docs.databricks.com/aws/en/dev-tools/rest-api)
> - [Updating from Jobs API 2.1 to 2.2 (AWS)](https://docs.databricks.com/aws/en/reference/jobs-api-2-2-updates)
> - [Cluster events API pagination changes (AWS)](https://docs.databricks.com/aws/en/compute/events-api-updates)
> - [Table (Unity Catalog API reference)](https://docs.databricks.com/api/uc-tables/v1/table)
