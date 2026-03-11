# Negative Caching Patterns

> Track: `databases` | Topic: `caching`

## Concept

Negative caching stores “not found” results for a short time so repeated misses do not keep hammering the origin.

## Key Points

- Missing keys can be hot too.
- A short negative TTL reduces repeated misses without hiding newly-created data forever.
- Negative entries should expire and be refreshed.
- This pattern is for stable misses, not for caching arbitrary transient errors forever.
- The negative TTL should stay positive; `0` does not create a meaningful cache window.

## Minimal Code Mental Model

```python
cache = {}
value, origin = read_with_negative_cache(store, cache, "doc:404", now=100, negative_ttl=30)
value2, origin2 = read_with_negative_cache(store, cache, "doc:404", now=110, negative_ttl=30)
```

## Function

```python
def validate_negative_ttl(ttl: int) -> None:
def negative_entry(now: int, ttl: int) -> dict[str, object]:
def read_with_negative_cache(
    store: dict[str, str],
    cache: dict[str, object],
    key: str,
    now: int,
    negative_ttl: int,
) -> tuple[str | None, bool]:
def expired_negative_keys(cache: dict[str, object], now: int) -> list[str]:
def purge_expired_negative(cache: dict[str, object], now: int) -> None:
```

## Run tests

```bash
pytest modules/databases/caching/negative-caching-patterns/python -q
```
