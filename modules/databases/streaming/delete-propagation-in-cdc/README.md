# Delete Propagation In CDC

> Track: `databases` | Topic: `streaming`

## Concept

CDC is not only inserts and updates. If downstream consumers ignore delete events, their materialized state diverges and keeps rows that no longer exist upstream.

## Key Points

- Delete propagation is part of state correctness, not an optional cleanup detail.
- Soft deletes and hard deletes both need clear downstream semantics.
- Sinks that ignore delete events can serve stale or non-compliant data.
- Reinserts after a delete should still work once the delete was applied correctly.

## Minimal Code Mental Model

```python
events = [
    cdc_event(1, "documents", "doc-1", "upsert", {"title": "Guide"}),
    cdc_event(2, "documents", "doc-1", "delete", None),
]
summary = propagation_summary(events)
```

## Function

```python
def cdc_event(
    sequence: int,
    table: str,
    row_id: str,
    op: str,
    after: dict[str, object] | None,
) -> dict[str, object]:
def apply_cdc_ignoring_deletes(events: list[dict[str, object]]) -> dict[tuple[str, str], dict[str, object]]:
def apply_cdc_with_deletes(events: list[dict[str, object]]) -> dict[tuple[str, str], dict[str, object]]:
def propagation_summary(events: list[dict[str, object]]) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/streaming/delete-propagation-in-cdc/python -q
```
