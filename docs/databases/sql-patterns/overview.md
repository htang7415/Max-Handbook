# SQL And Analytics Patterns

Most day-to-day database work is repeated query shapes, not obscure syntax.

## Purpose

Use this topic to learn the SQL patterns that matter across OLTP, analytics, and AI data workflows.

## First Principles

- Most useful queries are combinations of filter, join, aggregate, rank, dedupe, and update.
- Common table expressions help readability, but they do not replace understanding the actual plan.
- Window functions are often the cleanest way to compute latest-row, rank, running total, and cohort-style questions.
- In 2026, local analytics with DuckDB plus Parquet is part of the normal workflow for experiments, offline evaluation, and data debugging.

## Minimal Query Mental Model

```sql
WITH ranked AS (
  SELECT
    run_id,
    model_name,
    score,
    ROW_NUMBER() OVER (
      PARTITION BY model_name
      ORDER BY score DESC, run_id DESC
    ) AS rn
  FROM eval_results
)
SELECT model_name, run_id, score
FROM ranked
WHERE rn = 1;
```

## Canonical Modules

- `window-functions-basics`
- `dedup-and-latest-row`
- `as-of-joins`
- `upserts-and-merge-patterns`
- `time-bucket-aggregations`
- `duckdb-parquet-query-patterns`

## When To Use What

- Start here after the basic join shapes in `relational`.
- Use window functions when you need row context without collapsing the result set.
- Use as-of joins and latest-row patterns when time and freshness matter.
- Use upserts when writes must be idempotent and conflict-safe.
- Use time-bucket aggregations for dashboards and periodic rollups.
- Use DuckDB and Parquet when the question is analytical and does not need transactional writes.
