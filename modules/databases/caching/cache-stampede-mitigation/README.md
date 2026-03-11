# Cache Stampede Mitigation

> Track: `databases` | Topic: `caching`

## Concept

Cache stampede mitigation lets one caller refresh a cold or expired key while other callers either wait or temporarily use stale data instead of all hitting the origin.

## Key Points

- A stampede happens when many callers miss the same key at once.
- Single-flight refresh means only one caller becomes the loader for that key.
- Stale-while-revalidate can keep serving a slightly stale value while the loader refreshes it.
- Cold misses without a stale value usually need waiting or request coalescing, not parallel origin calls.
- The stale window should extend beyond expiry, and refresh TTLs should stay positive.

## Minimal Code Mental Model

```python
cache = {"doc:42": cache_entry("old", expires_at=100, stale_until=130)}
inflight = set()
first = request_action(cache, inflight, "doc:42", now=110)
second = request_action(cache, inflight, "doc:42", now=111)
finish_refresh(cache, inflight, "doc:42", "new", now=112, ttl=30, stale_window=60)
```

## Function

```python
def validate_timing(expires_at: int, stale_until: int) -> None:
def cache_entry(value: str, expires_at: int, stale_until: int) -> dict[str, object]:
def request_action(
    cache: dict[str, dict[str, object]],
    inflight: set[str],
    key: str,
    now: int,
) -> str:
def finish_refresh(
    cache: dict[str, dict[str, object]],
    inflight: set[str],
    key: str,
    value: str,
    now: int,
    ttl: int,
    stale_window: int,
) -> None:
```

## Run tests

```bash
pytest modules/databases/caching/cache-stampede-mitigation/python -q
```
