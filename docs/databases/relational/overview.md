# Relational Core

Most AI products still keep their source-of-truth state in relational tables.

## Purpose

Use this topic to learn how tables, keys, joins, and constraints turn raw rows into a reliable product data model.

## First Principles

- A relational database is best treated as the system of record for users, orgs, permissions, jobs, eval runs, and other durable state.
- Normalization reduces duplication in source-of-truth tables. Denormalization creates faster read paths when the access pattern is already clear.
- Constraints are part of the design, not optional cleanup. A foreign key or uniqueness rule is often better than application-only conventions.
- AI-specific data like prompts, documents, chunks, and embeddings still need relational metadata around ownership, timestamps, lineage, and permissions.

## Minimal Query Mental Model

```sql
SELECT d.id, d.title, COUNT(c.id) AS chunk_count
FROM documents AS d
LEFT JOIN chunks AS c ON c.document_id = d.id
WHERE d.workspace_id = 42
GROUP BY d.id, d.title
ORDER BY d.created_at DESC;
```

## Canonical Modules

- `tables-and-keys`
- `join-shapes`
- `constraints-and-integrity`
- `foreign-key-cascades`
- `null-semantics-in-joins`
- `jsonb-inside-relational-systems`

## When To Use What

- Start here before `nosql` or `vector-db`.
- Learn keys, joins, and constraints before moving to JSONB or denormalization decisions.
- Use cascades and nullable join patterns when ownership and optional relationships are part of the real schema.
- Use flexible columns like JSONB for metadata at the edge, not as an excuse to skip relational structure.
