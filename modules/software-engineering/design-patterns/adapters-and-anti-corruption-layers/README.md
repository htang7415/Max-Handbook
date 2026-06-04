# Adapters And Anti-Corruption Layers

> Track: `software-engineering` | Topic: `design-patterns`

## Concept

Adapters translate externally owned data into a smaller internal contract so vendor naming and status quirks do not leak through the codebase.

## Use When

| Situation | Adapter Role |
| --- | --- |
| Vendor schema uses different names | Translate to internal terms |
| External statuses do not match domain states | Normalize meanings at the boundary |
| Payload contains unused fields | Drop them before internal code sees them |

## First Principles

- External schemas change for reasons your system does not control.
- Internal contracts should keep stable names and meanings.
- A boundary translator should drop fields that are not part of the internal model.

## Workflow

1. Define the internal event shape first.
2. Map vendor fields and statuses into that shape.
3. Reject or ignore fields outside the internal contract.
4. Keep vendor-specific logic out of domain services.

## Minimal Code Mental Model

```python
translated = translate_billing_event(
    {"event_id": "evt_1", "state": "paid", "amount": 4200, "currency": "usd"}
)
assert translated["status"] == "settled"
assert preserves_internal_contract(translated) is True
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Leaking vendor names internally | One external change spreads through the codebase |
| Preserving every field | Internal model becomes a vendor mirror |
| Mapping statuses inline | Business logic becomes inconsistent |

## Function

```python
def vendor_status_to_internal(status: str) -> str:
def translate_billing_event(event: dict[str, object]) -> dict[str, object]:
def preserves_internal_contract(event: dict[str, object]) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/design-patterns/adapters-and-anti-corruption-layers/python -q
```
