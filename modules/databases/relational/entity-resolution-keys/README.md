# Entity Resolution Keys

> Track: `databases` | Topic: `relational`

## Concept

Entity resolution maps many external identifiers onto one canonical row. The relational shape is usually one entity table plus a separate keys table with a uniqueness rule per source system.

## Key Points

- A person or company can have different IDs in CRM, billing, and product systems.
- The canonical entity row should not need one nullable column for every upstream system.
- A dedicated keys table makes identity mapping extensible and enforceable.
- This matters in AI data systems when documents, users, or accounts arrive from multiple tools with different identifiers.

## Minimal Code Mental Model

```python
entity_id = insert_entity(conn, "Acme Labs")
attach_resolution_key(conn, entity_id, "crm", "acct-42", "account-id")
resolved = resolve_entity_id(conn, "crm", "acct-42")
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_entity_resolution_schema(conn: sqlite3.Connection) -> None:
def insert_entity(conn: sqlite3.Connection, canonical_name: str) -> int:
def attach_resolution_key(
    conn: sqlite3.Connection,
    entity_id: int,
    source_system: str,
    source_key: str,
    key_kind: str,
) -> int:
def resolve_entity_id(conn: sqlite3.Connection, source_system: str, source_key: str) -> int | None:
def keys_for_entity(conn: sqlite3.Connection, entity_id: int) -> list[tuple[str, str, str]]:
```

## Run tests

```bash
pytest modules/databases/relational/entity-resolution-keys/python -q
```
