# Tenant Offboarding Data Flows

> Track: `databases` | Topic: `schema-design`

## Concept

Tenant deletion is usually a workflow, not one SQL statement. A safe offboarding flow tracks request state, completes required export or retention steps, then deletes tenant-owned rows and leaves a tombstone for auditability.

## Key Points

- Offboarding needs ordered steps, not an ad hoc delete.
- Export and retention requirements often block immediate deletion.
- Child rows should disappear with the tenant once deletion is approved.
- A tombstone preserves proof that offboarding happened.

## Minimal Code Mental Model

```python
request_offboarding(conn, "tenant-a", "2026-03-11T09:00:00Z")
mark_export_complete(conn, "tenant-a", "2026-03-11T10:00:00Z")
finalize_offboarding(conn, "tenant-a", "2026-03-11T11:00:00Z")
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_offboarding_schema(conn: sqlite3.Connection) -> None:
def insert_tenant(conn: sqlite3.Connection, tenant_id: str) -> None:
def insert_document(conn: sqlite3.Connection, tenant_id: str, document_id: str) -> None:
def request_offboarding(conn: sqlite3.Connection, tenant_id: str, requested_at: str) -> None:
def mark_export_complete(conn: sqlite3.Connection, tenant_id: str, exported_at: str) -> None:
def finalize_offboarding(conn: sqlite3.Connection, tenant_id: str, deleted_at: str) -> None:
def tenant_row_counts(conn: sqlite3.Connection, tenant_id: str) -> dict[str, int]:
```

## Run tests

```bash
pytest modules/databases/schema-design/tenant-offboarding-data-flows/python -q
```
