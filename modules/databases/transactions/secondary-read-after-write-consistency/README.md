# Secondary Read After Write Consistency

> Track: `databases` | Topic: `transactions`

## Concept

A secondary replica may lag behind the latest committed write. If a session writes on the primary and then reads from a lagging secondary, it can observe stale state instead of its own update.

## Key Points

- Replica freshness is an LSN or applied-log position problem.
- A secondary is safe only after it has applied at least the session’s last write.
- Without that check, read scaling can break read-after-write consistency.
- This is why some systems route recent reads back to the primary until the replica catches up.

## Minimal Code Mental Model

```python
summary = read_after_write_summary(versions, last_write_lsn=120, secondary_applied_lsn=100)
```

## Function

```python
def version(lsn: int, value: str) -> dict[str, object]:
def visible_value(versions: list[dict[str, object]], applied_lsn: int) -> str | None:
def can_secondary_serve(last_write_lsn: int, secondary_applied_lsn: int) -> bool:
def read_after_write_summary(
    versions: list[dict[str, object]],
    last_write_lsn: int,
    secondary_applied_lsn: int,
) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/transactions/secondary-read-after-write-consistency/python -q
```
