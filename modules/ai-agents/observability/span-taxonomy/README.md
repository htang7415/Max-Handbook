# Span Taxonomy

> Track: `ai-agents` | Topic: `observability`

## Concept

Span taxonomy gives traces a small shared vocabulary so each span is labeled as model, tool, workflow, or guardrail work.

## Key Points

- Consistent span labels make traces easier to compare.
- A small taxonomy is usually enough for a first observability system.
- Unknown spans should stay visible instead of being forced into the wrong bucket.

## Minimal Code Mental Model

```python
kind = span_kind("tool_call")
labels = label_spans(["plan", "tool_call", "guardrail_check"])
counts = span_kind_counts(["plan", "tool_call", "tool_result"])
```

## Function

```python
def span_kind(span_name: str) -> str:
def label_spans(span_names: list[str]) -> dict[str, str]:
def span_kind_counts(span_names: list[str]) -> dict[str, int]:
```

## Run tests

```bash
pytest modules/ai-agents/observability/span-taxonomy/python -q
```
