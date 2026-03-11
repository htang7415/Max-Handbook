# One To Many And Many To Many

> Track: `databases` | Topic: `schema-design`

## Concept

One-to-many relationships put the foreign key on the child row, while many-to-many relationships use a join table to connect both sides explicitly.

## Key Points

- `documents -> chunks` is a classic one-to-many shape.
- `documents <-> tags` is a many-to-many shape because each side can connect to many rows on the other side.
- Join tables should usually have a composite uniqueness rule to block duplicate links.
- Good schema design makes relationship shape visible in the tables instead of hiding it in serialized blobs.

## Minimal Code Mental Model

```python
conn = create_connection()
create_relationship_schema(conn)
document_id = insert_document(conn, "spec")
insert_chunk(conn, document_id, 0, "chunk a")
tag_id = insert_tag(conn, "rag")
link_document_tag(conn, document_id, tag_id)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_relationship_schema(conn: sqlite3.Connection) -> None:
def insert_document(conn: sqlite3.Connection, title: str) -> int:
def insert_chunk(
    conn: sqlite3.Connection,
    document_id: int,
    chunk_index: int,
    text: str,
) -> int:
def insert_tag(conn: sqlite3.Connection, name: str) -> int:
def link_document_tag(conn: sqlite3.Connection, document_id: int, tag_id: int) -> None:
def document_chunk_counts(conn: sqlite3.Connection) -> list[tuple[str, int]]:
def document_tag_names(conn: sqlite3.Connection, title: str) -> list[str]:
```

## Run tests

```bash
pytest modules/databases/schema-design/one-to-many-and-many-to-many/python -q
```
