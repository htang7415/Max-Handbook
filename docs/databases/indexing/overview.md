# Indexing And Access Paths

Indexes are physical shortcuts for specific query shapes.

## Purpose

Use this topic to learn how access paths speed up reads, what they cost on writes, and how to choose indexes from actual predicates and sort order.

## First Principles

- An index is not free. It adds storage, write amplification, and maintenance cost.
- Good indexing starts from the query shape: filters, joins, ordering, and limits.
- Composite index order matters because databases use left-prefix access patterns.
- The fastest query is often a combination of better schema, smaller scans, and the right index, not "add indexes everywhere".

## Minimal Query Mental Model

```sql
EXPLAIN
SELECT id, created_at
FROM eval_runs
WHERE workspace_id = 42
  AND status = 'completed'
ORDER BY created_at DESC
LIMIT 20;
```

## Canonical Modules

- `btree-basics`
- `composite-index-order`
- `expression-index-basics`
- `covering-index-concepts`
- `partial-indexes`
- `index-write-amplification`
- `jsonb-and-gin-indexing`

## Supporting Modules

- `partition-pruning-basics`
- `partitioning-vs-secondary-indexes`
- `index-merge-vs-composite-indexes`
- `point-lookups-vs-range-scans`
- `sparse-index-selectivity`

## Boundary Notes

- `btree-basics` teaches the default ordered access path.
- `composite-index-order` teaches column order inside one index.
- `partial-indexes` teaches narrowing an index to rows that match a stable predicate.
- `partition-pruning-basics` removes whole partitions before normal access paths run; it is not a replacement for secondary indexes.
- `index-merge-vs-composite-indexes` is the fallback comparison when a query could use several single-column indexes or one purpose-built composite index.

## When To Use What

- Start with `btree-basics`, then learn `composite-index-order` and `covering-index-concepts`.
- Use expression and partial indexes only when the predicate shape is already stable.
- Reach for JSONB, GIN, prefix search, or partitioning only after a plain B-tree design is clearly insufficient.
- Recheck `index-write-amplification` and low-selectivity trade-offs before adding another index to a hot write path.
