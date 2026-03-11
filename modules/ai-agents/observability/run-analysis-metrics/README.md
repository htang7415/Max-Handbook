# Run Analysis Metrics

> Track: `ai-agents` | Topic: `observability`

## Concept

Run analysis metrics compress many traces into a small summary so you can see success rate, mean latency, and which span names fail most often.

## Key Points

- One good run trace is useful, but repeated runs show the actual bottleneck.
- Aggregate metrics should stay small enough to compare across experiments.
- Failed span counts are often the fastest way to find unstable steps.

## Minimal Code Mental Model

```python
runs = [{"success": True, "latency_ms": 120.0}, {"success": False, "latency_ms": 200.0}]
success = run_success_rate(runs)
mean_latency = mean_run_latency_ms(runs)
failures = failed_span_counts(traces)
```

## Function

```python
def run_success_rate(runs: list[dict[str, object]]) -> float:
def mean_run_latency_ms(runs: list[dict[str, object]]) -> float:
def failed_span_counts(traces: list[dict[str, object]]) -> dict[str, int]:
```

## Run tests

```bash
pytest modules/ai-agents/observability/run-analysis-metrics/python -q
```
