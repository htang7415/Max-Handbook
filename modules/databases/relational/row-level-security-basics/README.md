# Row Level Security Basics

> Track: `databases` | Topic: `relational`

## Concept

Row-level security limits which rows a session can read or write based on policy, often tenant identity or user role. The core idea is that access control is attached to the data path, not left to every caller to remember a filter.

## Key Points

- Tenant-scoped systems should not rely on every query author remembering `WHERE tenant_id = ?`.
- Admin sessions may need broader access than ordinary tenant sessions.
- Write policies matter too; otherwise a session can insert or modify another tenant’s rows.
- Real database RLS is engine-enforced, but the mental model is still “automatic per-row policy.”

## Minimal Code Mental Model

```python
rows = visible_documents(conn, session_tenant_id=1)
insert_document_as_session(conn, session_tenant_id=1, row_tenant_id=1, title="Safe")
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_document_table(conn: sqlite3.Connection) -> None:
def insert_document(conn: sqlite3.Connection, tenant_id: int, title: str) -> int:
def can_access_tenant_row(session_tenant_id: int, row_tenant_id: int, is_admin: bool = False) -> bool:
def visible_documents(
    conn: sqlite3.Connection,
    session_tenant_id: int,
    is_admin: bool = False,
) -> list[tuple[int, str]]:
def insert_document_as_session(
    conn: sqlite3.Connection,
    session_tenant_id: int,
    row_tenant_id: int,
    title: str,
    is_admin: bool = False,
) -> int:
```

## Run tests

```bash
pytest modules/databases/relational/row-level-security-basics/python -q
```
