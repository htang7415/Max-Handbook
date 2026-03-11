# Isolation Levels And Anomalies

> Track: `databases` | Topic: `transactions`

## Concept

Isolation levels are best understood by the anomalies they permit or prevent. The goal is not “use the strongest level always,” but “use the weakest level that still blocks the bug you care about.”

## Key Points

- Lower isolation allows more concurrency but more anomalies.
- Read committed blocks dirty reads but still allows some race conditions.
- Repeatable read blocks more read instability but can still allow write skew in some systems.
- Serializable aims to reject executions that would break serial correctness.

## Minimal Code Mental Model

```python
level = minimum_isolation_for(["nonrepeatable-read", "phantom-read"])
```

## Function

```python
def allowed_anomalies(level: str) -> set[str]:
def prevents(level: str, anomaly: str) -> bool:
def minimum_isolation_for(required_preventions: list[str]) -> str:
```

## Run tests

```bash
pytest modules/databases/transactions/isolation-levels-and-anomalies/python -q
```
