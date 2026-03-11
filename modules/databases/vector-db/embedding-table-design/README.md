# Embedding Table Design

> Track: `databases` | Topic: `vector-db`

## Concept

An embedding table should make chunk identity, model identity, and embedding freshness explicit so the system can tell what is missing, duplicated, or stale.

## Key Points

- Chunks and embeddings should be separate tables linked by a foreign key.
- One chunk can have many embeddings across different models or refresh jobs.
- A uniqueness rule should block duplicate embeddings for the same chunk and model snapshot.
- Good table design makes “which chunks still need embeddings?” an easy query.

## Minimal Code Mental Model

```python
conn = create_connection()
create_embedding_schema(conn)
chunk_id = insert_chunk(conn, 7, "spec", "hello")
insert_embedding(conn, chunk_id, "text-embedding-3-small", "job-1", [0.1, 0.2, 0.3])
missing = chunks_missing_model(conn, "text-embedding-3-large")
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_embedding_schema(conn: sqlite3.Connection) -> None:
def insert_chunk(
    conn: sqlite3.Connection,
    workspace_id: int,
    doc_type: str,
    text: str,
) -> int:
def insert_embedding(
    conn: sqlite3.Connection,
    chunk_id: int,
    model_name: str,
    job_id: str,
    vector: list[float],
) -> int:
def embedding_rows(conn: sqlite3.Connection) -> list[tuple[int, str, str]]:
def chunks_missing_model(conn: sqlite3.Connection, model_name: str) -> list[int]:
```

## Run tests

```bash
pytest modules/databases/vector-db/embedding-table-design/python -q
```
