# Logs, Metrics, And Traces

> Track: `software-engineering` | Topic: `observability`

## Concept

Logs describe discrete events, metrics summarize changing quantities, and traces explain where work spent time across a request path.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Incident debugging | Operators need request-level context | A single aggregate threshold is enough |
| Health monitoring | You need trends, rates, or thresholds | You need full causal context for one request |
| Dependency latency | Work crosses service or storage boundaries | The path has only one local step |

## First Principles

- Structured logs are more useful than free-form strings when incidents happen.
- Metrics are good for trends and alert thresholds.
- Traces are good for dependency paths, latency attribution, and failure localization.

## Workflow

1. Emit structured logs for important events.
2. Summarize repeated values as metrics.
3. Record spans when work crosses a boundary.
4. Count failed spans and total latency.
5. Use logs for context, metrics for alerting, and traces for localization.

## Minimal Code Mental Model

```python
log = structured_log("payments", "info", "payment created", {"request_id": "req_1"})
metric = metric_summary("latency_ms", [120.0, 180.0, 90.0])
trace = trace_summary(
    [
        {"name": "api", "latency_ms": 20.0, "status": "ok"},
        {"name": "db", "latency_ms": 80.0, "status": "error"},
    ]
)
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Free-form logs only | Incidents require brittle text search | `structured_log` keeps service, level, message, and context explicit |
| Empty metric series | Aggregates hide missing data | `metric_summary` rejects empty values |
| Negative span latency | Trace math becomes impossible | `trace_summary` rejects negative latency |

## Function

```python
def structured_log(
    service: str,
    level: str,
    message: str,
    context: dict[str, object] | None = None,
) -> dict[str, object]:
def metric_summary(name: str, values: list[float]) -> dict[str, float]:
def trace_summary(spans: list[dict[str, object]]) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/software-engineering/observability/logs-metrics-and-traces/python -q
```
