# Semantic Cache Hit-Rate Analysis

> Track: `databases` | Topic: `caching`

## Concept

Semantic caching only matters if it actually hits often enough to save time or cost. Hit-rate analysis turns cache performance into a measurable signal instead of a guess.

## Key Points

- Overall hit rate shows whether the cache is helping at all.
- Scoped hit rates can reveal one workspace or version doing much worse than another.
- Savings estimates connect hit rate to latency or cost impact.
- A low hit rate may point to key design, similarity thresholds, or version churn.
- Event records should store `hit` as a real boolean, not a truthy string.

## Minimal Code Mental Model

```python
events = [
    {"workspace_id": 7, "hit": True},
    {"workspace_id": 7, "hit": False},
    {"workspace_id": 8, "hit": True},
]
overall = hit_rate(events)
by_workspace = scoped_hit_rates(events, "workspace_id")
summary = savings_summary(events, hit_latency_ms=20, miss_latency_ms=200)
```

## Function

```python
def validate_event(event: dict[str, object]) -> None:
def hit_rate(events: list[dict[str, object]]) -> float:
def scoped_hit_rates(
    events: list[dict[str, object]],
    scope_field: str,
) -> dict[object, float]:
def latency_saved_ms(
    events: list[dict[str, object]],
    hit_latency_ms: int,
    miss_latency_ms: int,
) -> int:
def savings_summary(
    events: list[dict[str, object]],
    hit_latency_ms: int,
    miss_latency_ms: int,
) -> dict[str, float | int]:
```

## Run tests

```bash
pytest modules/databases/caching/semantic-cache-hit-rate-analysis/python -q
```
