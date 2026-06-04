# Capstones

Use database capstones to combine relational state, analytics, streaming, caching, and retrieval into one product-shaped data system.

## Purpose

Capstones are for practicing the full data-stack decision path:
- source-of-truth schema
- operational access paths
- CDC and replay
- analytics and evaluation data
- vector retrieval with metadata, permissions, and freshness

## First Principles

- A capstone should make every copy of data explainable: why it exists, how it updates, and when it can be trusted.
- Retrieval is not separate from database design when permissions, lineage, freshness, and eval logs matter.
- Release gates should fail when the source of truth, CDC lag, analytics backfill, or retrieval checks are unclear.

## Canonical Modules

- `hybrid-ai-data-stack`

## When To Use What

- Use `hybrid-ai-data-stack` after relational, schema-design, streaming, SQL analytics, and vector-db basics are clear.
- Add more database capstones only when they combine several data layers into one operational workflow.
