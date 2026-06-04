# Contract To Production API Service

> Track: `software-engineering` | Topic: `capstones`

## Concept

This capstone combines contract validation, idempotency, retry policy, observability, and rollout decisions into one compact service-delivery flow.

## Use When

| Service Stage | Engineer Gate |
| --- | --- |
| Request entry | Validate contract before side effects |
| Duplicate-sensitive operation | Apply idempotency before dependency calls |
| Unreliable dependency | Separate retryable and terminal failures |
| Release promotion | Use canary signals and rollback readiness |

## First Principles

- Validate the request contract before any side effects start.
- Apply idempotency before calling an unreliable dependency.
- Retries need explicit retryable vs terminal failure handling.
- Promotion should depend on canary signals and rollback readiness, not optimism.

## Workflow

1. Parse and validate the request.
2. Check idempotency before external side effects.
3. Call dependencies with bounded retry behavior.
4. Emit structured events and SLI snapshots.
5. Promote only when health and rollback gates pass.

## Minimal Code Mental Model

```python
response = handle_payment_request(request, seen_keys, ["timeout", "ok"])
event = structured_event("/payments", response)
snapshot = sli_snapshot(["accepted", "accepted", "failed"])
decision = release_decision(snapshot["success_rate"], 180, rollback_ready=True)
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Side effects before validation | Bad requests mutate state |
| Idempotency after gateway call | Retries can duplicate charges |
| Retry policy without terminal failure | Unrecoverable errors keep cycling |
| Promotion without rollback | Canary failure becomes harder to recover |

## Function

```python
def validate_payment_request(request: dict[str, object]) -> list[str]:
def handle_payment_request(
    request: dict[str, object],
    seen_idempotency_keys: set[str],
    gateway_attempts: list[str],
) -> dict[str, object]:
def structured_event(route: str, outcome: dict[str, object]) -> dict[str, object]:
def sli_snapshot(outcomes: list[str]) -> dict[str, float]:
def release_decision(success_rate: float, p95_latency_ms: int, rollback_ready: bool) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/capstones/contract-to-production-api-service/python -q
```
