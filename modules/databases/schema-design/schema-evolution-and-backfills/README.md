# Schema Evolution And Backfills

> Track: `databases` | Topic: `schema-design`

## Concept

Safe schema evolution is usually additive first: add a nullable column, let old and new writers coexist, then backfill old rows. That avoids locking the whole rollout to one deploy.

## Key Points

- Additive columns make mixed-version deploys safer.
- Old rows stay incomplete until a backfill runs.
- Backfills should only fill missing values, not overwrite fresh writes.
- Schema rollout and data rollout are separate steps.

## Minimal Code Mental Model

```python
evolve_to_v2_add_priority(conn)
backfill_priority(conn)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_job_table_v1(conn: sqlite3.Connection) -> None:
def evolve_to_v2_add_priority(conn: sqlite3.Connection) -> None:
def insert_job_v1(conn: sqlite3.Connection, job_name: str, job_type: str) -> int:
def insert_job_v2(
    conn: sqlite3.Connection,
    job_name: str,
    job_type: str,
    priority: str,
) -> int:
def backfill_priority(conn: sqlite3.Connection) -> None:
def job_rows(conn: sqlite3.Connection) -> list[tuple[str, str, str | None]]:
```

## Run tests

```bash
pytest modules/databases/schema-design/schema-evolution-and-backfills/python -q
```
