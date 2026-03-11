# Schema Design For Products And AI

Schema design is where database modeling meets product behavior.

## Purpose

Use this topic to design tables around access patterns, ownership, auditability, and the data shapes that modern AI products add.

## First Principles

- Model entities, relationships, and lifecycle first. Query syntax comes later.
- Separate current state from append-only history when the system needs both fast reads and reliable audits.
- Design for tenant boundaries, permissions, and deletion rules early. Retrofitting them later is expensive.
- AI systems add document, chunk, embedding, feedback, and eval tables, but they still need normal product modeling around users, workspaces, jobs, and runs.

## Minimal Query Mental Model

```sql
CREATE TABLE documents (
  id BIGSERIAL PRIMARY KEY,
  workspace_id BIGINT NOT NULL,
  title TEXT NOT NULL,
  source_uri TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE chunks (
  id BIGSERIAL PRIMARY KEY,
  document_id BIGINT NOT NULL REFERENCES documents(id),
  chunk_index INT NOT NULL,
  text TEXT NOT NULL,
  UNIQUE (document_id, chunk_index)
);
```

## Canonical Modules

- `entity-vs-event-tables`
- `one-to-many-and-many-to-many`
- `ownership-and-delete-boundaries`
- `metadata-and-lineage-tables`
- `multi-tenant-schema-patterns`
- `audit-soft-delete-and-history`
- `document-chunk-embedding-schema`

## When To Use What

- Start with entities, relationships, and delete boundaries before adding history or AI-specific tables.
- Use entity tables when the product needs the latest state quickly.
- Use append-only event tables when ordering and replay matter.
- Use explicit join tables when relationships are real first-class data.
- Use lineage, audit, and document-chunk-embedding modules once ownership and lifecycle rules are already settled.
