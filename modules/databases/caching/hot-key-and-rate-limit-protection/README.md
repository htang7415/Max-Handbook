# Hot-Key And Rate-Limit Protection

> Track: `databases` | Topic: `caching`

## Concept

Hot keys create thundering herds. Once many clients pile onto the same key, a small rate limiter or guardrail can stop that key from overwhelming the origin.

## Key Points

- A hot key is a cache key that attracts far more requests than its neighbors.
- Detecting hot keys is just counting, but protecting the origin requires a rolling-window policy.
- Rate limits are usually scoped by caller and key so one noisy client cannot stampede the backend.
- Protection should reset as the window moves forward instead of permanently blocking the key.

## Minimal Code Mental Model

```python
requests = ["workspace:7:doc:42", "workspace:7:doc:42", "workspace:7:doc:42"]
state = {}
is_hot = hot_keys(requests, threshold=3)
allowed = allow_request(
    state,
    actor_id="user-1",
    key="workspace:7:doc:42",
    now=10,
    max_requests=2,
    window_seconds=30,
)
```

## Function

```python
def hot_keys(requests: list[str], threshold: int) -> list[str]:
def allow_request(
    state: dict[tuple[str, str], list[int]],
    actor_id: str,
    key: str,
    now: int,
    max_requests: int,
    window_seconds: int,
) -> bool:
def protected_origin_requests(
    requests: list[dict[str, object]],
    hot_threshold: int,
    max_requests: int,
    window_seconds: int,
) -> list[bool]:
```

## Run tests

```bash
pytest modules/databases/caching/hot-key-and-rate-limit-protection/python -q
```
