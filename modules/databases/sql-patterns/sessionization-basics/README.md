# Sessionization Basics

> Track: `databases` | Topic: `sql-patterns`

## Concept

Sessionization groups a user’s events into bursts separated by inactivity gaps. The common SQL pattern uses `LAG` to compare neighboring events and a running sum to label each new session.

## Key Points

- A session starts on the first event or after a gap larger than the threshold.
- Window functions are the standard way to detect those boundaries.
- Session counts depend on event ordering within each user partition.
- This pattern shows up in product analytics, agent activity analysis, and clickstream modeling.

## Minimal Code Mental Model

```python
rows = sessionized_events(conn, gap_minutes=30)
counts = session_counts(conn, gap_minutes=30)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_event_table(conn: sqlite3.Connection) -> None:
def insert_event(conn: sqlite3.Connection, user_id: str, occurred_minute: int) -> int:
def sessionized_events(conn: sqlite3.Connection, gap_minutes: int) -> list[tuple[str, int, int]]:
def session_counts(conn: sqlite3.Connection, gap_minutes: int) -> list[tuple[str, int]]:
```

## Run tests

```bash
pytest modules/databases/sql-patterns/sessionization-basics/python -q
```
