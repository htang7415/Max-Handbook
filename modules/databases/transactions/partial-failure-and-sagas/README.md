# Partial Failure And Sagas

> Track: `databases` | Topic: `transactions`

## Concept

Sagas handle workflows that span multiple local writes. If a later step fails after earlier ones already committed, the system runs compensating actions instead of pretending the whole workflow was atomic.

## Key Points

- Local steps can succeed independently and still leave the workflow in a bad intermediate state.
- Compensation is explicit business logic such as refunding a payment or releasing inventory.
- A saga is not a free rollback. It is a forward process plus compensating steps.
- This pattern matters when one transaction cannot cover all side effects or services involved.

## Minimal Code Mental Model

```python
summary = run_order_saga(fail_after_step="charge")
```

## Function

```python
def empty_saga_state() -> dict[str, object]:
def reserve_inventory(state: dict[str, object]) -> None:
def charge_payment(state: dict[str, object]) -> None:
def create_shipment(state: dict[str, object]) -> None:
def release_inventory(state: dict[str, object]) -> None:
def refund_payment(state: dict[str, object]) -> None:
def run_order_saga(fail_after_step: str | None = None) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/transactions/partial-failure-and-sagas/python -q
```
