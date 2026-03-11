# Query Plans And Tuning

If you cannot read a query plan, you are tuning blind.

## Purpose

Use this topic to learn how the optimizer chooses scans, joins, and sorts, and how to debug slow queries from the plan outward.

## First Principles

- Query performance comes from row counts, access paths, and operator choice.
- `EXPLAIN` is a model of what the optimizer expects. `EXPLAIN ANALYZE` shows what actually happened.
- Bad plans often come from poor cardinality estimates, missing indexes, or query shapes that force too much work.
- Tuning is usually simpler than it looks: reduce scanned rows, improve predicates, and make joins more selective earlier.

## Minimal Query Mental Model

```sql
EXPLAIN ANALYZE
SELECT c.document_id, COUNT(*) AS hits
FROM chunks AS c
WHERE c.workspace_id = 42
  AND c.created_at >= now() - interval '7 days'
GROUP BY c.document_id;
```

## Canonical Modules

- `explain-basics`
- `seq-scan-vs-index-scan`
- `nested-loop-vs-hash-join`
- `cardinality-estimation`
- `sargability-basics`
- `or-predicate-plan-shapes`
- `sort-limit-and-group-by-costs`

## When To Use What

- Start with `explain-basics`, then compare scan and join shapes before debugging edge cases.
- Use `EXPLAIN ANALYZE` when a query is already slow and you need actual timing and row counts.
- Suspect cardinality or sargability issues when a plan shape looks reasonable but still performs badly.
- Recheck the data model when tuning becomes a long chain of special-case indexes and plan workarounds.
