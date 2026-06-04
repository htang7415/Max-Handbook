# Idempotency Keys

> Track: `software-engineering` | Topic: `apis`

## Concept

An idempotency key lets a client retry a mutating request without accidentally applying the same change twice.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Retried write | A client may repeat a POST after timeout or network failure | The operation is read-only |
| Payment or job creation | Duplicate side effects are costly | Duplicate execution is harmless and expected |
| External client API | Callers need deterministic retry behavior | The caller cannot provide a stable key |

## First Principles

- The key should bind to the request intent, not just to the endpoint name.
- A repeated request with the same key and same payload should replay the stored result.
- A repeated request with the same key and different payload should be rejected as a conflict.

## Workflow

1. Normalize method, path, and request body into a fingerprint.
2. Require a non-empty idempotency key.
3. Execute when no stored record exists.
4. Replay when key and fingerprint match a stored record.
5. Return conflict when the same key has a different fingerprint.

## Minimal Code Mental Model

```python
fingerprint = request_fingerprint("POST", "/v1/payments", {"amount_cents": 2500, "currency": "USD"})
decision = idempotency_decision("pay_123", fingerprint, stored_record=None)
stored = store_response("pay_123", fingerprint, 201, {"payment_id": "p_1"})
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Blank key | Retries cannot be tied to one request | `idempotency_decision` rejects empty keys |
| Same key, different payload | One retry could apply a different mutation | Returns `conflict` |
| Invalid stored response status | Stored outcome cannot represent an HTTP response | `store_response` enforces status `200..599` |

## Function

```python
def request_fingerprint(
    method: str,
    path: str,
    body: dict[str, object],
) -> tuple[str, str, tuple[tuple[str, str], ...]]:
def idempotency_decision(
    idempotency_key: str,
    fingerprint: tuple[str, str, tuple[tuple[str, str], ...]],
    stored_record: dict[str, object] | None,
) -> str:
def store_response(
    idempotency_key: str,
    fingerprint: tuple[str, str, tuple[tuple[str, str], ...]],
    status_code: int,
    response_body: dict[str, object],
) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/software-engineering/apis/idempotency-keys/python -q
```
