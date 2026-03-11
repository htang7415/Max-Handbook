# Logs, Metrics, And Traces

> Track: `software-engineering` | Topic: `observability`

## Concept

Logs describe discrete events, metrics summarize changing quantities, and traces explain where work spent time across a request path.

## Key Points

- Structured logs are more useful than free-form strings when incidents happen.
- Metrics are good for trends and alert thresholds.
- Traces are good for dependency paths, latency attribution, and failure localization.

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
