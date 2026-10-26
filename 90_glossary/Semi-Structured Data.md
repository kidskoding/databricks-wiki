---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Data with some structure, such as JSON or XML, where fields have names but records can vary in shape and nest."
related:
  - "[[VARIANT Data Type]]"
  - "[[CSV and JSON]]"
  - "[[Structured vs Unstructured Data]]"
  - "[[Schema-on-Read]]"
  - "[[Auto Loader]]"
  - "[[NoSQL]]"
aliases:
  - "semistructured data"
  - "nested data"
  - "JSON data"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Semi-Structured Data

> [!eli5] Summary
> Semi-structured data has labels on its values but no fixed table layout. A JSON order record that sometimes has a coupon field and sometimes does not is a typical example.

**In data work:** [[Structured vs Unstructured Data|Structured data]] fits fixed columns; unstructured data (images, PDFs) has no fields at all. Semi-structured data sits between them: JSON, XML, and Avro records carry field names and can nest objects and arrays, but different records can have different fields. It is common in API responses, event streams, web logs, and exports from [[NoSQL]] databases. A shop's e-commerce platform might send webhook payloads where each order holds a nested list of line items.

**In Databricks:** There are three ways to store it.
- **[[VARIANT Data Type|VARIANT]]:** Stores JSON in an efficient binary encoding without a fixed schema. Query fields with path syntax, for example `raw:customer.name`. Databricks recommends VARIANT over JSON strings for performance, and VARIANT is supported in Delta Lake and Apache Iceberg tables.
- **Structs, arrays, and maps:** Use these when the shape is stable and known.
- **JSON strings:** Parse with `from_json` or the `:` operator; this is the slowest option.

```sql
SELECT raw:customer.name::STRING AS customer, raw:total::DECIMAL(10,2) AS total
FROM shop.bronze.orders_raw;
```

[[Auto Loader]] can ingest JSON files directly into VARIANT columns.

Seen in: [[VARIANT Data Type]], [[CSV and JSON]], [[Structured vs Unstructured Data]]

## Recall

Semi-structured data::Data with named fields but no fixed schema, such as JSON or XML, where records can differ and nest.
Which Databricks type stores semi-structured data efficiently without a fixed schema?::VARIANT.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Query variant data (AWS)](https://docs.databricks.com/aws/en/semi-structured/variant)
> - [How is variant different than JSON strings? (AWS)](https://docs.databricks.com/aws/en/semi-structured/variant-json-diff)
> - [Variant type support for Apache Iceberg and Delta Lake (AWS)](https://docs.databricks.com/aws/en/tables/features/variant)
> - [Ingest data as semi-structured variant type (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/ingestion/variant)
