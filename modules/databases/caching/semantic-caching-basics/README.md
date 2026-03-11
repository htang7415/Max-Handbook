# Semantic Caching Basics

> Track: `databases` | Topic: `caching`

## Concept

Semantic caching reuses prior model answers when a new request is similar enough and still matches the same scope and freshness rules.

## Key Points

- Semantic similarity alone is not enough; scope guards like workspace and policy version matter too.
- A semantic cache is a latency and cost optimization, not a correctness layer.
- Cache hits should still respect freshness rules.
- Similar query, same scope, and fresh answer is the minimum safe pattern.

## Minimal Code Mental Model

```python
entries = []
store_semantic_entry(entries, "find failed runs", "3 failed runs", workspace_id=7, version="v1", now=100)
hit = lookup_semantic_cache(entries, "show failed runs", workspace_id=7, version="v1", now=120)
```

## Function

```python
def token_overlap_score(left: str, right: str) -> float:
def store_semantic_entry(
    entries: list[dict[str, object]],
    query: str,
    response: str,
    workspace_id: int,
    version: str,
    now: int,
) -> None:
def lookup_semantic_cache(
    entries: list[dict[str, object]],
    query: str,
    workspace_id: int,
    version: str,
    now: int,
    similarity_threshold: float = 0.5,
    max_age_seconds: int = 300,
) -> str | None:
```

## Run tests

```bash
pytest modules/databases/caching/semantic-caching-basics/python -q
```
