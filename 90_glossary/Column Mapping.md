---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A Delta Lake table feature that tracks columns by internal IDs or physical names, so you can rename or drop columns without rewriting data files."
related:
  - "[[Delta Lake]]"
  - "[[Schema Enforcement and Evolution]]"
  - "[[Delta UniForm]]"
  - "[[Delta Transaction Log]]"
  - "[[OPTIMIZE and VACUUM]]"
aliases:
  - "delta.columnMapping.mode"
  - "Delta column mapping"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Column Mapping

> [!eli5] Summary
> Column mapping lets you rename or remove a column in a Delta table as a quick label change. The data stays where it is.

**In data work:** Parquet files identify columns by name, so renaming a column normally means rewriting every file. Column mapping adds a layer of indirection: the table's metadata maps each logical column name to a physical name or ID stored in the files. A rename or drop then changes only metadata.

**In Databricks:** On [[Delta Lake]] tables you enable it with the `delta.columnMapping.mode` table property. Mode `name` can be set on new or existing tables; mode `id` must be set at creation. Enabling it upgrades the table protocol, which older readers may not support.

```sql
ALTER TABLE sales SET TBLPROPERTIES ('delta.columnMapping.mode' = 'name');
ALTER TABLE sales RENAME COLUMN cust_nm TO customer_name;
ALTER TABLE sales DROP COLUMN legacy_flag;
```

Dropping a column does not delete its data from files. Run `REORG TABLE ... APPLY (PURGE)` and then `VACUUM` to remove it physically (see [[OPTIMIZE and VACUUM]]). Renames and drops are non-additive schema changes and can break streaming readers unless they set `schemaTrackingLocation`. Column mapping is also required for [[Delta UniForm]] Iceberg reads.

Small-business example: you fix a badly named column `amt2` to `refund_amount` in a five-year sales table in seconds instead of rewriting it.

Seen in: [[Delta Lake]], [[Schema Enforcement and Evolution]], [[Delta UniForm]]

## Recall

What does Delta column mapping let you do without rewriting files?::Rename and drop columns.
Does DROP COLUMN with column mapping delete the column's data from files?::No. Use REORG TABLE with PURGE, then VACUUM.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Rename and drop columns with Delta Lake column mapping (AWS)](https://docs.databricks.com/aws/en/tables/features/column-mapping)
> - [Rename and drop columns with Delta Lake column mapping (Azure)](https://learn.microsoft.com/en-us/azure/databricks/delta/column-mapping)
