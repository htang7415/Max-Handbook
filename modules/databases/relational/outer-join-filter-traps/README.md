# Outer Join Filter Traps

> Track: `databases` | Topic: `relational`

## Concept

`LEFT JOIN` only preserves unmatched rows until a `WHERE` clause filters on the right-side table. Moving the filter into the `ON` clause is often the difference between keeping outer-join semantics and accidentally turning the query into an inner join.

## Key Points

- Right-side filters in `WHERE` can remove `NULL`-extended rows.
- Putting the filter in `ON` preserves unmatched left rows.
- This matters when asking for “all parents, plus matching children if present.”
- Many subtle reporting bugs come from this one mistake.

## Minimal Code Mental Model

```python
rows = open_tasks_filter_in_on(conn)
missing = projects_without_open_tasks(conn)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_demo_tables(conn: sqlite3.Connection) -> None:
def seed_projects(conn: sqlite3.Connection, rows: list[tuple[int, str]]) -> None:
def seed_tasks(conn: sqlite3.Connection, rows: list[tuple[int, str, str]]) -> None:
def open_tasks_filter_in_where(conn: sqlite3.Connection) -> list[str]:
def open_tasks_filter_in_on(conn: sqlite3.Connection) -> list[tuple[str, str | None]]:
def projects_without_open_tasks(conn: sqlite3.Connection) -> list[str]:
```

## Run tests

```bash
pytest modules/databases/relational/outer-join-filter-traps/python -q
```
