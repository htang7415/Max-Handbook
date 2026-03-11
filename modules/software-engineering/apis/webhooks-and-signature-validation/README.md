# Webhooks And Signature Validation

> Track: `software-engineering` | Topic: `apis`

## Concept

Webhook receivers should verify sender authenticity before trusting the payload, usually with a signed timestamp and an HMAC over the request body.

## Key Points

- Signature validation should use constant-time comparison.
- Freshness checks reduce replay risk.
- Invalid signatures should fail closed before event routing logic runs.

## Minimal Code Mental Model

```python
signature = webhook_signature("secret", timestamp=1_700_000_000, body='{"event":"paid"}')
valid = webhook_request_valid(
    "secret",
    timestamp=1_700_000_000,
    body='{"event":"paid"}',
    provided_signature=signature,
    now_timestamp=1_700_000_120,
)
decision = webhook_decision(valid, "payment.paid")
```

## Function

```python
def webhook_signature(secret: str, timestamp: int, body: str) -> str:
def webhook_request_valid(
    secret: str,
    timestamp: int,
    body: str,
    provided_signature: str,
    now_timestamp: int,
    max_age_seconds: int = 300,
) -> bool:
def webhook_decision(valid_request: bool, event_type: str) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/apis/webhooks-and-signature-validation/python -q
```
