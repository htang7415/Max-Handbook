# Self Referential Relationships

> Track: `databases` | Topic: `relational`

## Concept

Some relational models point back to the same table, like employee-manager trees or category hierarchies. These self-referential relationships are common and need the same integrity rules as any other foreign key.

## Key Points

- A self-reference is still just a foreign key.
- Root rows have `NULL` parents; child rows point to another row in the same table.
- Adjacency lists are simple and flexible for moderate-depth hierarchies.
- Recursive traversal logic belongs on top of a clean base schema.

## Minimal Code Mental Model

```python
lead_id = insert_employee(conn, "lead", ceo_id)
chain = management_chain(conn, engineer_id)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_employee_table(conn: sqlite3.Connection) -> None:
def insert_employee(
    conn: sqlite3.Connection,
    name: str,
    manager_id: int | None = None,
) -> int:
def direct_reports(conn: sqlite3.Connection, manager_id: int) -> list[str]:
def management_chain(conn: sqlite3.Connection, employee_id: int) -> list[str]:
```

## Run tests

```bash
pytest modules/databases/relational/self-referential-relationships/python -q
```
