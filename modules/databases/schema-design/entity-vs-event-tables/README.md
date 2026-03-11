# Entity Vs Event Tables

> Track: `databases` | Topic: `schema-design`

## Concept

Entity tables store current state, while event tables store the history of changes that produced that state.

## Key Points

- Entity tables answer “what is true now?”
- Event tables answer “what happened, and in what order?”
- Some systems need both: a fast current-state table plus an append-only audit log.
- Reconstructing current state from events is possible, but it is usually more expensive than reading an entity table directly.

## Minimal Code Mental Model

```python
conn = create_connection()
create_entity_event_schema(conn)
upsert_job_state(conn, "run-1", "running")
append_job_event(conn, "run-1", "running", "2026-03-11T10:00:00Z")
current = current_state_from_entity_table(conn)
rebuilt = current_state_from_event_table(conn)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_entity_event_schema(conn: sqlite3.Connection) -> None:
def upsert_job_state(conn: sqlite3.Connection, run_id: str, status: str) -> None:
def append_job_event(
    conn: sqlite3.Connection,
    run_id: str,
    status: str,
    occurred_at: str,
) -> None:
def current_state_from_entity_table(conn: sqlite3.Connection) -> dict[str, str]:
def current_state_from_event_table(conn: sqlite3.Connection) -> dict[str, str]:
```

## Run tests

```bash
pytest modules/databases/schema-design/entity-vs-event-tables/python -q
```
