# Idempotency Keys

> Track: `software-engineering` | Topic: `apis`

## Concept

An idempotency key lets a client retry a mutating request without accidentally applying the same change twice.

## Key Points

- The key should bind to the request intent, not just to the endpoint name.
- A repeated request with the same key and same payload should replay the stored result.
- A repeated request with the same key and different payload should be rejected as a conflict.

## Minimal Code Mental Model

```python
fingerprint = request_fingerprint("POST", "/v1/payments", {"amount_cents": 2500, "currency": "USD"})
decision = idempotency_decision("pay_123", fingerprint, stored_record=None)
stored = store_response("pay_123", fingerprint, 201, {"payment_id": "p_1"})
```

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
