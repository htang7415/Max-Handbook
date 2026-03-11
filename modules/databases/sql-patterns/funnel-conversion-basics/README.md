# Funnel Conversion Basics

> Track: `databases` | Topic: `sql-patterns`

## Concept

Funnel analysis counts how many users reach each stage in a defined order. The important part is not raw event totals, but distinct users who actually progressed through the sequence.

## Key Points

- Each funnel stage has an ordered dependency on the previous one.
- Users who fire a later event without an earlier stage should not count as converted.
- Stage counts are distinct-user counts, not event counts.
- Conversion rates are each stage divided by the previous stage, not by total traffic forever.

## Minimal Code Mental Model

```python
stages = ["visit", "signup", "activate"]
counts = funnel_counts(conn, stages)
rates = conversion_rates(conn, stages)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_funnel_events_table(conn: sqlite3.Connection) -> None:
def insert_funnel_event(conn: sqlite3.Connection, user_id: str, stage: str, occurred_at: str) -> int:
def stage_times_by_user(conn: sqlite3.Connection) -> dict[str, dict[str, str]]:
def funnel_counts(conn: sqlite3.Connection, stages: list[str]) -> list[tuple[str, int]]:
def conversion_rates(conn: sqlite3.Connection, stages: list[str]) -> list[tuple[str, float]]:
```

## Run tests

```bash
pytest modules/databases/sql-patterns/funnel-conversion-basics/python -q
```
