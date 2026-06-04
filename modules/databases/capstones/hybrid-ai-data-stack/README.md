# Hybrid AI Data Stack

> Track: `databases` | Topic: `capstones`

## Concept

A hybrid AI data stack keeps durable product state in a source-of-truth database, propagates changes through CDC, uses analytics for debugging and evals, and uses retrieval only with metadata, permissions, and freshness checks.

## Key Points

- Postgres-style relational state remains the default source of truth for product invariants.
- CDC connects operational state to analytics, caches, and retrieval updates.
- DuckDB/Parquet-style analytics are useful for offline evals and data debugging without replacing the operational store.
- Vector retrieval should fail closed when permissions, freshness, or eval quality are missing.

## Minimal Code Mental Model

```python
route = route_data_request(needs_transaction=True, needs_similarity=False, needs_large_scan=False)
readiness = stack_readiness(
    {
        "source_constraints": True,
        "cdc_watermark_fresh": True,
        "analytics_backfill_ready": True,
        "retrieval_permissions_filtered": True,
        "retrieval_eval_passed": True,
    }
)
gate = release_gate(readiness, max_cdc_lag_seconds=120, observed_cdc_lag_seconds=45)
```

## Function

```python
def route_data_request(
    needs_transaction: bool,
    needs_similarity: bool,
    needs_large_scan: bool,
    needs_fresh_read: bool = False,
) -> str:
def stack_readiness(checks: dict[str, bool]) -> dict[str, object]:
def release_gate(
    readiness: dict[str, object],
    max_cdc_lag_seconds: int,
    observed_cdc_lag_seconds: int,
) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/capstones/hybrid-ai-data-stack/python -q
```
