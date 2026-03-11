# Root Cause Attribution

> Track: `ai-agents` | Topic: `observability`

## Concept

Root cause attribution groups failing spans by source so the system can tell whether a run is mostly breaking in the model layer, tool layer, or workflow layer.

## Key Points

- Failure counts are more useful when they roll up to stable sources.
- A dominant failure source can drive a focused fix instead of a broad review.
- If failures are spread across sources, the system should review broadly rather than overfit one cause.

## Minimal Code Mental Model

```python
counts = attributed_failure_counts(spans)
source = dominant_failure_source(counts)
route = attribution_route(counts, min_share=0.6)
```

## Function

```python
def attributed_failure_counts(spans: list[dict[str, object]]) -> dict[str, int]:
def dominant_failure_source(counts: dict[str, int]) -> str | None:
def attribution_route(counts: dict[str, int], min_share: float) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/observability/root-cause-attribution/python -q
```
