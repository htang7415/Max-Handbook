# Trace-Driven Debugging

> Track: `software-engineering` | Topic: `observability`

## Concept

Trace-driven debugging uses span latency and failure status to decide where an investigation should start instead of guessing from symptoms alone.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Distributed request | One user action crosses services or dependencies | The issue is a single local function |
| Latency triage | You need the slowest contributing span | No span timings are available |
| Failure localization | Some span status is not `ok` | The trace is incomplete or untrusted |

## First Principles

- Failing spans are the fastest path to the broken dependency or workflow step.
- If nothing failed, the slowest span is usually the first latency suspect.
- Traces are most useful when the route from symptom to next inspection step is explicit.

## Workflow

1. Collect spans for one request or workflow run.
2. Check for failing spans first.
3. If no spans failed, find the slowest span.
4. Compare the slowest span with a latency threshold.
5. Route investigation to failure, latency, or insufficient evidence.

## Minimal Code Mental Model

```python
failed = failing_spans(spans)
slowest = slowest_span(spans)
route = debugging_route(spans, slow_ms_threshold=200.0)
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Failed span ignored | Investigation starts in the wrong service | `failing_spans` lists non-OK spans |
| Slow span hidden | Latency work optimizes the wrong step | `slowest_span` identifies the largest span |
| No trace evidence | Debugging falls back to guessing | `debugging_route` reports insufficient evidence |

## Function

```python
def failing_spans(spans: list[dict[str, object]]) -> list[str]:
def slowest_span(spans: list[dict[str, object]]) -> str | None:
def debugging_route(spans: list[dict[str, object]], slow_ms_threshold: float) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/observability/trace-driven-debugging/python -q
```
