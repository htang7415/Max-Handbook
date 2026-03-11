# Soft Delete And Tombstone Patterns

> Track: `databases` | Topic: `relational`

## Concept

Soft deletes keep the row and mark it deleted. Tombstones remove the row but record a separate delete marker. They solve related problems, but they are not the same pattern.

## Key Points

- Soft deletes are convenient when you may restore the row or still need joins against its old data.
- Tombstones are useful when the base row must disappear but downstream systems still need a delete fact.
- Queries for “live” rows must explicitly filter soft-deleted records.
- Replication, CDC, privacy deletes, and sync systems often need tombstones even if the primary store does not expose soft deletes.

## Minimal Code Mental Model

```python
soft_delete_document(conn, document_id, "2026-03-01T10:00:00")
hard_delete_with_tombstone(conn, document_id, "2026-03-01T11:00:00", "privacy-request")
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_delete_demo_schema(conn: sqlite3.Connection) -> None:
def insert_document(conn: sqlite3.Connection, title: str) -> int:
def soft_delete_document(conn: sqlite3.Connection, document_id: int, deleted_at: str) -> None:
def hard_delete_with_tombstone(
    conn: sqlite3.Connection,
    document_id: int,
    deleted_at: str,
    reason: str,
) -> None:
def live_documents(conn: sqlite3.Connection) -> list[tuple[int, str]]:
def tombstone_rows(conn: sqlite3.Connection) -> list[tuple[int, str, str]]:
```

## Run tests

```bash
pytest modules/databases/relational/soft-delete-and-tombstone-patterns/python -q
```
