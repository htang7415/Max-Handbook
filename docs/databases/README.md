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

## Frontier Lab Lessons

| Source | Engineering habit | Handbook implication |
| --- | --- | --- |
| OpenAI | Retrieval systems need attributes, chunking, filtering, expiration, and consistency rules. | Teach vector search as an index with metadata and lifecycle constraints. |
| Anthropic | MCP-style integrations expose external systems through clear tool and resource boundaries. | Database interfaces should make metadata, permissions, and ownership explicit. |
| DeepMind | Optimization agents increase the value of telemetry, lineage, and reproducible experiments. | Treat eval logs and analytics stores as first-class data products. |
| Hugging Face | RAG practice ties retrieval to eval datasets, reranking, and answer-quality feedback. | Teach embeddings as one component inside a measured retrieval workflow. |

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

## Handbook Subsections

1. Relational core: tables, keys, joins, constraints, cascades, and null semantics.
2. Schema design: entity/event tables, many-to-many shapes, grain, history, and tenancy.
3. SQL and analytics: windows, latest-row patterns, as-of joins, upserts, DuckDB, and Parquet.
4. Indexing and access paths: B-trees, composite order, partial/expression indexes, and pruning.
5. Transactions and concurrency: isolation, MVCC, retries, sagas, outbox, and replica behavior.
6. Query plans and performance: `EXPLAIN`, selectivity, joins, sorts, scans, and regressions.
7. Caching: cache-aside, invalidation, stampedes, hot keys, semantic caching, and TTL jitter.
8. Streaming and CDC: events, connectors, offsets, watermarks, schema evolution, and replay.
9. NoSQL and distributed data: document/key-value/wide-row trade-offs, quorum, repair, and compaction.
10. Vector retrieval and memory: embeddings, ANN, metadata filters, hybrid search, reranking, agent memory, and data-stack capstones.

## Handbook Map Style

Each subsection should expose at most 20 curated subsubsections. Use this order:
- Frame the data responsibility and correctness boundary.
- Explain the storage or query model.
- Build the schema, query, index, cache, stream, or retrieval path.
- Measure correctness, performance, freshness, and quality.
- Operate migrations, lag, repair, invalidation, or permissions.
- Finish with practice that combines source-of-truth data and AI retrieval.

## AI-Time 2026 Priorities

- Keep PostgreSQL-level relational fundamentals, MVCC, and `EXPLAIN` central.
- Treat recent PostgreSQL releases, including asynchronous I/O, skip scans, and retained optimizer statistics on upgrade, as a reason to teach better operational fundamentals, not as a vendor-feature catalog.
- Treat DuckDB and Parquet as part of the normal analytics toolbox for offline evals, data debugging, and local experimentation.
- Teach CDC and streaming as the bridge between operational systems, analytics, and AI pipelines.
- Teach caching with invalidation first, then semantic caching for repeated model calls.
- Teach vector search as one retrieval component inside a larger metadata, permissions, lexical ranking, and reranking system.
- Add assessments and capstones only after source-of-truth, analytics, CDC, and retrieval responsibilities are separated.

## When To Use What

- Use relational and schema modules before choosing NoSQL or vector infrastructure.
- Use query-plan modules when the schema is reasonable but the runtime behavior is wrong.
- Use caching only after the correctness boundary and invalidation trigger are known.
- Use streaming and CDC when downstream systems need ordered change propagation.
- Use vector retrieval only after metadata, permissions, freshness, and eval data are explicit.
- Use assessments and capstones to verify that the whole data stack can survive product changes, stale data, and AI retrieval failures.

## Neighbor Tracks

- Use `docs/ai-agents/rag` and `docs/ai-agents/memory` when retrieval becomes part of an agent loop.
- Use `docs/ml/llm/evaluation` when retrieval quality is judged by model or answer behavior.
- Use `docs/software-engineering/reliability` when CDC, cache, or retrieval lag becomes an operational SLO.

## References

- [OpenAI Retrieval](https://developers.openai.com/api/docs/guides/retrieval)
- [OpenAI File Search](https://platform.openai.com/docs/guides/tools-file-search/)
- [Anthropic Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
- [Google DeepMind AlphaEvolve](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)
- [Hugging Face RAG Evaluation](https://huggingface.co/learn/cookbook/rag_evaluation)
- [Hugging Face Agentic RAG](https://huggingface.co/learn/agents-course/en/unit2/smolagents/retrieval_agents)

## Scope Rule

- Prefer stable mental models over vendor tours.
- Prefer concise docs and compact labs over exhaustive catalogs.
- Prefer Postgres-first concepts for core database ideas, while keeping examples portable when possible.
- Only add separate modules when they teach a distinct access pattern, failure mode, or system design choice.
