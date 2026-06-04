# Webhooks And Signature Validation

> Track: `software-engineering` | Topic: `apis`

## Concept

Webhook receivers should verify sender authenticity before trusting the payload, usually with a signed timestamp and an HMAC over the request body.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| External callback | A third-party system sends events into your service | The sender is already authenticated by another trusted channel |
| Replay risk | Attackers could resend an old valid payload | Events have no side effects and no sensitive data |
| Event routing | Invalid requests must stop before business logic | You only need to parse a local fixture |

## First Principles

- Signature validation should use constant-time comparison.
- Freshness checks reduce replay risk.
- Invalid signatures should fail closed before event routing logic runs.

## Workflow

1. Build the signed payload from timestamp and body.
2. Compute the HMAC with the shared secret.
3. Reject timestamps outside the freshness window.
4. Compare signatures with constant-time comparison.
5. Route only valid events; reject everything else.

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

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Blank secret | Signature has no trust anchor | `webhook_signature` rejects empty secrets |
| Stale timestamp | Old event can be replayed | `webhook_request_valid` checks max age |
| Invalid event type | Receiver cannot route safely | `webhook_decision` rejects empty event types |

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
