# Vector Retrieval, Hybrid Search, And Memory

Vector search is one retrieval layer inside a larger system of metadata, ranking, and product constraints.

## Purpose

Use this topic to learn how embeddings, ANN indexes, metadata filters, reranking, and agent memory fit together in AI products.

## First Principles

- A vector store is rarely enough by itself. Good retrieval also needs document metadata, permissions, freshness rules, and often lexical ranking.
- Chunking and embedding quality often matter more than the database brand.
- Exact search and approximate nearest neighbor search trade recall, latency, and memory differently.
- Postgres plus vector extensions can be the right baseline when transactional data, permissions, and retrieval metadata belong together.
- Dedicated vector databases or ANN libraries matter when recall-latency scale, index operations, or specialized filtering exceed the baseline.
- Agent memory is retrieval over prior state. It still needs schema, scoring, decay, and conflict rules.

## Minimal Query Mental Model

```sql
SELECT chunk_id, document_id, distance
FROM chunk_embeddings
WHERE workspace_id = 42
  AND doc_type = 'spec'
ORDER BY embedding <-> :query_embedding
LIMIT 5;
```

## Canonical Modules

- `embedding-table-design`
- `exact-vs-ann-search`
- `hnsw-graph-search`, `ivf-search`, `faiss-index-families`, `scann-search`
- `metadata-filtering`
- `hybrid-search`
- `reranking-pipelines`
- `hybrid-retrieval-evaluation`
- `agent-memory-retrieval`

## When To Use What

- Start with embedding table design and metadata filters before ANN tuning.
- Use exact search for smaller collections or correctness-first baselines.
- Use ANN when collection size or latency targets make exact search too expensive.
- Use `hnsw-graph-search` when low-latency search and incremental inserts matter.
- Use `ivf-search` when coarse partitioning plus `nprobe` tuning is the main ANN pattern.
- Use hybrid search when lexical terms, metadata filters, and embeddings each capture a different part of relevance.
- Use `faiss-index-families` when choosing which FAISS family fits memory, recall, and update constraints.
- Use `scann-search` when you want to reason about partition-and-reorder search at large scale.
- Add reranking and retrieval evaluation once first-stage retrieval is stable enough to measure.
- Use agent memory only after scoring, freshness, and conflict rules are already explicit.
