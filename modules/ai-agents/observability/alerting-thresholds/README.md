# Alerting Thresholds

> Track: `ai-agents` | Topic: `observability`

## Concept

Alerting thresholds turn observed metrics into simple raise-or-don't-raise decisions so operators know when the agent needs attention.

## Key Points

- Good alerts focus on a few high-signal metrics.
- Thresholds should be easy to inspect and adjust.
- Alert messages should say which metric crossed which boundary.

## Minimal Code Mental Model

```python
breached = threshold_breached(220.0, 200.0, direction="above")
message = alert_message("latency_ms", 220.0, 200.0, direction="above")
alerts = alert_candidates({"latency_ms": 220.0}, {"latency_ms": (200.0, "above")})
```

## Function

```python
def threshold_breached(value: float, threshold: float, direction: str) -> bool:
def alert_message(metric_name: str, value: float, threshold: float, direction: str) -> str:
def alert_candidates(metrics: dict[str, float], thresholds: dict[str, tuple[float, str]]) -> list[str]:
```

## Run tests

```bash
pytest modules/ai-agents/observability/alerting-thresholds/python -q
```
