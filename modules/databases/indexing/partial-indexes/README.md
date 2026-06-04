# Partial Indexes

> Track: `databases` | Topic: `indexing`

## Concept

Partial indexes index only the subset of rows that a hot query actually cares about.

## Key Points

- A partial index is useful when one status or one slice of the table dominates the read path.
- Smaller indexes can be cheaper to maintain than full-table indexes.
- The query predicate has to match the partial condition closely.
- Queries outside the indexed subset still need another access path or a scan.

## Boundary

Use `btree-basics` for ordinary equality, range, and ordering access. Use this module when the useful rows are a stable subset and indexing the whole table would waste write cost and storage.

## Minimal Code Mental Model

```python
conn = create_connection()
create_eval_runs_table(conn)
seed_eval_runs(conn, rows)
add_failed_runs_partial_index(conn)
failed_plan = plan_flags(plan_for_recent_failed_runs(conn, 7))
completed_plan = plan_flags(plan_for_recent_completed_runs(conn, 7))
```

## Function

```python
def add_failed_runs_partial_index(conn: sqlite3.Connection) -> None:
def plan_for_recent_failed_runs(
    conn: sqlite3.Connection,
    workspace_id: int,
    limit: int = 2,
) -> list[str]:
def plan_for_recent_completed_runs(
    conn: sqlite3.Connection,
    workspace_id: int,
    limit: int = 2,
) -> list[str]:
def plan_flags(plan_details: list[str]) -> dict[str, bool]:
```

## Run tests

```bash
pytest modules/databases/indexing/partial-indexes/python -q
```
