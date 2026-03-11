# Audit Soft Delete And History

> Track: `databases` | Topic: `schema-design`

## Concept

Some systems need more than a `deleted_at` column. They need a current-state row for product behavior and a separate audit history for who changed what and when, even after soft deletes and restores.

## Key Points

- Current-state tables and audit history serve different purposes.
- Soft delete hides a row from normal product reads without losing it.
- Audit rows preserve lifecycle transitions like create, delete, and restore.
- This pattern is useful when compliance or debugging needs a full record of state changes.

## Minimal Code Mental Model

```python
soft_delete_document(conn, document_id, "2026-03-11T10:00:00Z")
restore_document(conn, document_id, "2026-03-11T11:00:00Z")
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_audit_schema(conn: sqlite3.Connection) -> None:
def insert_document(conn: sqlite3.Connection, title: str, occurred_at: str) -> int:
def soft_delete_document(conn: sqlite3.Connection, document_id: int, deleted_at: str) -> None:
def restore_document(conn: sqlite3.Connection, document_id: int, restored_at: str) -> None:
def live_documents(conn: sqlite3.Connection) -> list[tuple[int, str]]:
def audit_history(conn: sqlite3.Connection, document_id: int) -> list[tuple[str, str, str | None]]:
```

## Run tests

```bash
pytest modules/databases/schema-design/audit-soft-delete-and-history/python -q
```
