# Semantic Cache Invalidation

> Track: `databases` | Topic: `caching`

## Concept

Semantic caches should be invalidated by the data and policy versions that shaped the answer, not just by time.

## Key Points

- A semantically similar answer is stale if the underlying source corpus changed.
- Policy or prompt-version changes can invalidate cached answers even when the source data did not.
- Invalidation should be scoped so one tenant's content refresh does not wipe every cache entry.
- TTL helps, but version-aware invalidation is the safer correctness boundary.
- Similarity thresholds should stay in `0..1`, and max-age windows should not be negative.

## Boundary

Use `semantic-caching-basics` to learn hit eligibility. Use this module when the problem is eviction or bypass after policy, prompt, corpus, or tenant-scope versions change.

## Minimal Code Mental Model

```python
entries = []
store_semantic_entry(entries, "show failed jobs", "2 failed jobs", 7, "policy-v1", "docs-v1", now=100)
hit = lookup_semantic_cache(entries, "failed jobs", 7, "policy-v1", "docs-v1", now=110)
removed = invalidate_scope(entries, 7, current_policy_version="policy-v2", current_source_version="docs-v2")
```

## Function

```python
def store_semantic_entry(
    entries: list[dict[str, object]],
    query: str,
    response: str,
    workspace_id: int,
    policy_version: str,
    source_version: str,
    now: int,
) -> None:
def lookup_semantic_cache(
    entries: list[dict[str, object]],
    query: str,
    workspace_id: int,
    policy_version: str,
    source_version: str,
    now: int,
    similarity_threshold: float = 0.5,
    max_age_seconds: int = 300,
) -> str | None:
def invalidate_scope(
    entries: list[dict[str, object]],
    workspace_id: int,
    current_policy_version: str,
    current_source_version: str,
) -> int:
```

## Run tests

```bash
pytest modules/databases/caching/semantic-cache-invalidation/python -q
```
