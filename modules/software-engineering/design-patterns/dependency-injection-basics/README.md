# Dependency Injection Basics

> Track: `software-engineering` | Topic: `design-patterns`

## Concept

Dependency injection keeps side effects at the boundary by passing behavior in, which makes domain logic easier to test with fakes.

## Use When

| Situation | Dependency Injection Value |
| --- | --- |
| Logic calls a gateway, database, or clock | Replace side effects in tests |
| Domain decision should stay pure | Pass behavior in from the boundary |
| Framework wiring is optional | Use explicit parameters first |

## First Principles

- Pure decision logic should stay separate from network, database, and email calls.
- Injected callables let tests replace expensive or risky side effects.
- The value is not a framework; the value is explicit control of dependencies.

## Workflow

1. Keep the decision function independent of side effects.
2. Pass external behavior into the function or service.
3. Use fakes in tests for slow or risky dependencies.
4. Add a container only when manual wiring becomes real complexity.

## Minimal Code Mental Model

```python
events: list[str] = []

receipt = issue_refund(
    "ord_1",
    900,
    False,
    gateway=lambda order_id, amount: f"refund:{order_id}:{amount}",
    audit_log=events.append,
)
assert receipt == "refund:ord_1:900"
assert events == ["refund ord_1 900 refund:ord_1:900"]
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Hidden global dependency | Unit tests become brittle or slow |
| Injecting everything | Function signatures lose meaning |
| Framework first | The pattern becomes ceremony instead of control |

## Function

```python
def refund_ready(amount_cents: int, duplicate_request: bool) -> bool:
def audit_entry(order_id: str, amount_cents: int, receipt: str) -> str:
def issue_refund(
    order_id: str,
    amount_cents: int,
    duplicate_request: bool,
    gateway,
    audit_log,
) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/design-patterns/dependency-injection-basics/python -q
```
