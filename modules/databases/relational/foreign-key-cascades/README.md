# Foreign Key Cascades

> Track: `databases` | Topic: `relational`

## Concept

Foreign keys do more than block bad references. With cascade rules, they can also clean up dependent rows automatically when a parent row is deleted, which keeps ownership trees consistent.

## Key Points

- Foreign keys protect referential integrity between parent and child tables.
- `ON DELETE CASCADE` removes dependent rows automatically.
- Cascades are useful for true ownership hierarchies.
- They are dangerous when child rows should outlive the parent.

## Minimal Code Mental Model

```python
delete_workspace(conn, workspace_id)
counts = row_counts(conn)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_cascade_schema(conn: sqlite3.Connection) -> None:
def insert_workspace(conn: sqlite3.Connection, name: str) -> int:
def insert_document(conn: sqlite3.Connection, workspace_id: int, title: str) -> int:
def insert_chunk(conn: sqlite3.Connection, document_id: int, body: str) -> int:
def delete_document(conn: sqlite3.Connection, document_id: int) -> None:
def delete_workspace(conn: sqlite3.Connection, workspace_id: int) -> None:
def row_counts(conn: sqlite3.Connection) -> dict[str, int]:
```

## Run tests

```bash
pytest modules/databases/relational/foreign-key-cascades/python -q
```
