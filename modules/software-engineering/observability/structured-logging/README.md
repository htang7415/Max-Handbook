# Structured Logging

> Track: `software-engineering` | Topic: `observability`

## Concept

Structured logging stores events as fields that machines and humans can query reliably, instead of hiding meaning inside one free-form message string.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Production debugging | Events need request ID, service, level, and context | A local print statement is enough |
| Incident search | Operators need stable fields to query | The message is never stored or searched |
| Sensitive context | Logs might include tokens or secrets | There is no untrusted or secret data |

## First Principles

- Logs should carry stable keys like request IDs and service names.
- Sensitive fields should be redacted before emission.
- Required log fields make production debugging more reliable.

## Workflow

1. Normalize service, level, and message.
2. Redact secret-looking context fields before emission.
3. Emit context as structured keys.
4. Check required fields for operational queries.
5. Treat missing required fields as logging defects.

## Minimal Code Mental Model

```python
event = make_log_event("payments", "info", "payment created", {"request_id": "req_1", "token": "secret"})
missing = missing_required_log_fields(event, ["service", "level", "message", "request_id"])
redacted = redact_context({"token": "secret", "request_id": "req_1"})
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Secret in logs | Credential leaks into durable storage | `redact_context` redacts secret keys |
| Missing request ID | Incident search cannot join events | `missing_required_log_fields` reports absent fields |
| Invalid level or message | Log stream becomes inconsistent | `make_log_event` validates core fields |

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
