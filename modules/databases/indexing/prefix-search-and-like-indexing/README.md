# Prefix Search And LIKE Indexing

> Track: `databases` | Topic: `indexing`

## Concept

B-tree indexes can help prefix searches like `name LIKE 'ada%'`, but only when the pattern can be turned into a range scan. This module demonstrates that behavior in SQLite with `case_sensitive_like` enabled; in PostgreSQL, `LIKE` and `ILIKE` indexability also depends on collation and operator class choices.

## Key Points

- Prefix patterns can map to a contiguous range in index order.
- Leading wildcards usually force a scan.
- Ordered prefix results can often come straight from the index.
- Text search beyond prefixes usually needs a different access path.

## Minimal Code Mental Model

```python
add_name_index(conn)
plan = like_prefix_plan(conn, "ada")
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_users_table(conn: sqlite3.Connection) -> None:
def seed_names(conn: sqlite3.Connection, names: list[str]) -> None:
def add_name_index(conn: sqlite3.Connection) -> None:
def like_prefix_plan(conn: sqlite3.Connection, prefix: str) -> list[str]:
def matching_names(conn: sqlite3.Connection, prefix: str) -> list[str]:
def plan_flags(plan_details: list[str]) -> dict[str, bool]:
```

## Run tests

```bash
pytest modules/databases/indexing/prefix-search-and-like-indexing/python -q
```
