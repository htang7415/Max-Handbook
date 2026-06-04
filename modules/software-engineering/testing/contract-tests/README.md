# Contract Tests

> Track: `software-engineering` | Topic: `testing`

## Concept

A contract test checks that a provider still satisfies the exact fields and types a consumer depends on.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Service boundary | A consumer depends on provider payload fields | The provider is an internal helper with no stable caller |
| Event or webhook payload | Consumers process data asynchronously | A full end-to-end environment is required for the question |
| Schema review | Required and optional fields must stay explicit | The payload is intentionally free-form |

## First Principles

- Extra provider fields are usually fine.
- Missing required fields or wrong types are the main contract breaks.
- Contract tests protect boundaries without needing a full end-to-end environment.

## Workflow

1. Write the consumer-required fields and types.
2. Add optional fields only when the consumer can handle absence.
3. Validate provider payloads against the contract.
4. Report missing required fields and wrong types.
5. Keep the contract name stable enough to trace failures.

## Minimal Code Mental Model

```python
contract = make_contract({"id": "string", "amount_cents": "integer"}, {"memo": "string"})
violations = contract_violations(contract, {"id": "p_1", "amount_cents": 2500})
report = contract_report("payment-created", contract, {"id": "p_1", "amount_cents": "2500"})
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Missing required field | Consumer crashes or silently drops data | `contract_violations` reports missing fields |
| Wrong field type | Payload shape looks correct but parsing fails | `_matches_type` checks supported contract types |
| Blank contract name | Reports cannot identify the broken boundary | `contract_report` rejects empty names |

## Function

```python
def make_contract(
    required_fields: dict[str, str],
    optional_fields: dict[str, str] | None = None,
) -> dict[str, dict[str, str]]:
def contract_violations(contract: dict[str, dict[str, str]], payload: dict[str, object]) -> list[str]:
def contract_report(
    contract_name: str,
    contract: dict[str, dict[str, str]],
    payload: dict[str, object],
) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/software-engineering/testing/contract-tests/python -q
```
