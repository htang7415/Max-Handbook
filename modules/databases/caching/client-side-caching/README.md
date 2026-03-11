# Client Side Caching

> Track: `databases` | Topic: `caching`

## Concept

Client-side caching keeps hot keys in the application process instead of making every read hit the server cache or database. It only works safely when the server can tell clients which cached keys became stale.

## Key Points

- Client-side caches save network hops as well as database work.
- They go stale unless invalidation signals reach the client.
- Reads are cheap when the local copy is valid.
- Missed invalidations are the core failure mode.

## Minimal Code Mental Model

```python
server_update(server, invalidations, "doc:1", "v2")
apply_invalidations(client_cache, invalidations)
```

## Function

```python
def client_read(
    server: dict[str, tuple[str, int]],
    client_cache: dict[str, tuple[str, int]],
    key: str,
) -> str | None:
def server_update(
    server: dict[str, tuple[str, int]],
    invalidations: list[str],
    key: str,
    value: str,
) -> None:
def apply_invalidations(
    client_cache: dict[str, tuple[str, int]],
    invalidations: list[str],
) -> None:
def stale_client_keys(
    server: dict[str, tuple[str, int]],
    client_cache: dict[str, tuple[str, int]],
) -> list[str]:
```

## Run tests

```bash
pytest modules/databases/caching/client-side-caching/python -q
```
