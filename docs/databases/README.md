# Databases

This track is about the data layer for modern products and AI systems.

## Purpose

Use this track to learn databases in the order that matters most in 2026:
- relational source-of-truth design
- schema and query patterns
- indexing, transactions, and query plans
- caching and streaming
- document, key-value, and vector retrieval systems

## First Principles

- Most AI systems still keep core business state in a relational database.
- Schema design, access paths, and consistency rules matter more than vendor labels.
- AI products add new data needs like embeddings, chunk metadata, eval logs, lineage, and freshness, but they do not replace transactional fundamentals.
- Most production systems are hybrid: one operational store, one cache, one stream, one retrieval layer, and one analytics path.

## Recommended Path

Use the track in this order:

1. Relational core
   Start with `tables-and-keys`, `join-shapes`, `constraints-and-integrity`, and `foreign-key-cascades`.
2. Schema design
   Move to `one-to-many-and-many-to-many`, `entity-vs-event-tables`, `document-chunk-embedding-schema`, and `ownership-and-delete-boundaries`.
3. SQL patterns
   Learn `window-functions-basics`, `dedup-and-latest-row`, `upserts-and-merge-patterns`, and `duckdb-parquet-query-patterns`.
4. Indexing
   Add `btree-basics`, `composite-index-order`, `partial-indexes`, and `expression-index-basics`.
5. Transactions and query plans
   Learn `transaction-basics`, `isolation-levels-and-anomalies`, `mvcc-mental-model`, `explain-basics`, and `seq-scan-vs-index-scan`.
6. System patterns
   Only then add `caching`, `streaming`, and `nosql`.
7. AI retrieval
   Finish with `vector-db` once metadata, freshness, and product constraints already make sense.

## Topic Map

- Relational core: `relational/overview.md`
- Schema design: `schema-design/overview.md`
- SQL and analytics patterns: `sql-patterns/overview.md`
- Indexing and access paths: `indexing/overview.md`
- Transactions and concurrency: `transactions/overview.md`
- Query plans and tuning: `query-plans/overview.md`
- Caching and semantic caching: `caching/overview.md`
- NoSQL trade-offs: `nosql/overview.md`
- Streaming and CDC: `streaming/overview.md`
- Vector retrieval and memory: `vector-db/overview.md`

## AI-Time 2026 Priorities

- Keep PostgreSQL-level relational fundamentals, MVCC, and `EXPLAIN` central.
- Treat DuckDB and Parquet as part of the normal analytics toolbox, not a separate specialty.
- Teach CDC and streaming as the bridge between operational systems, analytics, and AI pipelines.
- Teach caching with invalidation first, then semantic caching for repeated model calls.
- Teach vector search as one retrieval component inside a larger metadata and ranking system.

## Scope Rule

- Prefer stable mental models over vendor tours.
- Prefer concise docs and compact labs over exhaustive catalogs.
- Prefer Postgres-first concepts for core database ideas, while keeping examples portable when possible.
- Only add separate modules when they teach a distinct access pattern, failure mode, or system design choice.
