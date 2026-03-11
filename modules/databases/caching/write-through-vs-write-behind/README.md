# Write Through Vs Write Behind

> Track: `databases` | Topic: `caching`

## Concept

Both patterns update the cache on writes, but they differ on when the database changes. Write-through updates the database immediately. Write-behind updates the cache first and flushes to the database later.

## Key Points

- Write-through keeps the cache and database aligned after each write.
- Write-behind lowers synchronous write latency but creates a durability gap.
- Buffered writes need a flush path and failure handling.
- The right choice depends on whether freshness and durability matter more than write latency.

## Minimal Code Mental Model

```python
write_behind_update(store, cache, pending, "profile:1", "new-value")
flush_pending_writes(store, pending)
```

## Function

```python
def write_through_update(
    store: dict[str, str],
    cache: dict[str, str],
    key: str,
    value: str,
) -> None:
def write_behind_update(
    store: dict[str, str],
    cache: dict[str, str],
    pending_writes: dict[str, str],
    key: str,
    value: str,
) -> None:
def flush_pending_writes(store: dict[str, str], pending_writes: dict[str, str]) -> None:
def write_view(
    store: dict[str, str],
    cache: dict[str, str],
    pending_writes: dict[str, str],
    key: str,
) -> dict[str, str | bool | None]:
```

## Run tests

```bash
pytest modules/databases/caching/write-through-vs-write-behind/python -q
```
