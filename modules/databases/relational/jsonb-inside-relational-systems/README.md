# JSONB Inside Relational Systems

> Track: `databases` | Topic: `relational`

## Concept

Keep source-of-truth columns relational, then attach flexible JSON-like metadata for the fields that change faster than the main schema.

## Key Points

- Stable identity, tenancy, and status columns should stay as normal relational fields.
- Flexible metadata is useful, but filtering should usually go through extracted index terms instead of raw JSON blobs.
- A mixed design keeps joins, constraints, and audits simple while still allowing product-specific attributes.
- Metadata updates need to refresh the extracted terms or indexed queries drift out of sync.

## Minimal Code Mental Model

```python
conn = create_connection()
create_ticket_schema(conn)
ticket_id = insert_ticket(
    conn,
    workspace_id=7,
    status="open",
    title="Broken retrieval",
    metadata={"priority": "high", "tags": ["rag", "prod"]},
)
matches = filter_ticket_ids(
    conn,
    workspace_id=7,
    status="open",
    required_terms=["priority=high", "tag=rag"],
)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_ticket_schema(conn: sqlite3.Connection) -> None:
def insert_ticket(
    conn: sqlite3.Connection,
    workspace_id: int,
    status: str,
    title: str,
    metadata: dict[str, object],
) -> int:
def update_ticket_metadata(
    conn: sqlite3.Connection,
    ticket_id: int,
    metadata: dict[str, object],
) -> None:
def filter_ticket_ids(
    conn: sqlite3.Connection,
    workspace_id: int,
    status: str | None = None,
    required_terms: list[str] | None = None,
) -> list[int]:
def ticket_metadata(conn: sqlite3.Connection, ticket_id: int) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/relational/jsonb-inside-relational-systems/python -q
```
