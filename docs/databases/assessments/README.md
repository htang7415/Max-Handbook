# Assessments

Use this page to check whether the database track is improving system design judgment, not just SQL vocabulary.

## Purpose

Use this page to test whether you can:
- choose the right source of truth
- design schemas around ownership, freshness, and deletion
- explain query and index behavior from access paths
- route data between operational state, cache, stream, analytics, and retrieval layers

## First Principles

- Database design starts from product invariants and access patterns.
- A query shape, index, and schema change should be reasoned about together.
- Hybrid AI systems need explicit freshness, lineage, permissions, and retrieval quality checks.
- Operational correctness comes before cache, stream, analytics, or vector-store convenience.

## Section Checks

- Relational Core: Can you name the keys, constraints, joins, and ownership rules?
- Schema Design: Can you separate current state, events, history, chunks, and embeddings?
- SQL and Analytics: Can you choose windows, latest-row logic, DuckDB, Parquet, or materialization intentionally?
- Indexing and Access Paths: Can you explain why an index helps and what it costs on writes?
- Transactions and Concurrency: Can you explain isolation, idempotency, retries, and replica lag?
- Query Plans and Performance: Can you read `EXPLAIN` before guessing?
- Caching: Can you name the invalidation trigger?
- Streaming and CDC: Can you define event ordering, replay, and schema evolution?
- NoSQL and Distributed Data: Can you justify the trade-off against staying in Postgres?
- Vector Retrieval and Memory: Can you enforce metadata filters, permissions, freshness, and retrieval evals?

## Capstone Readiness

You are ready for database capstones when you can do all of these:

- define the source-of-truth table and its constraints
- describe the change stream and replay path
- choose the analytics shape for offline debugging or evals
- design vector retrieval with metadata and permissions
- state the freshness and rollback checks

## Graduation Check

The track is working if you can review a proposed data stack and answer these six questions quickly:

1. What is the source of truth?
2. What invariant does the database enforce?
3. What query or index shape serves the hot path?
4. What downstream systems depend on changes?
5. How fresh must each copy be?
6. How is retrieval quality measured?
