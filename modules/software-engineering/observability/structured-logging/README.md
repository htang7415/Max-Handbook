# Structured Logging

> Track: `software-engineering` | Topic: `observability`

## Concept

Structured logging stores events as fields that machines and humans can query reliably, instead of hiding meaning inside one free-form message string.

## Key Points

- Logs should carry stable keys like request IDs and service names.
- Sensitive fields should be redacted before emission.
- Required log fields make production debugging more reliable.

## Minimal Code Mental Model

```python
event = make_log_event("payments", "info", "payment created", {"request_id": "req_1", "token": "secret"})
missing = missing_required_log_fields(event, ["service", "level", "message", "request_id"])
redacted = redact_context({"token": "secret", "request_id": "req_1"})
```

## Function

```python
def redact_context(context: dict[str, object], secret_keys: list[str] | None = None) -> dict[str, object]:
def make_log_event(
    service: str,
    level: str,
    message: str,
    context: dict[str, object] | None = None,
) -> dict[str, object]:
def missing_required_log_fields(log_event: dict[str, object], required_fields: list[str]) -> list[str]:
```

## Run tests

```bash
pytest modules/software-engineering/observability/structured-logging/python -q
```
