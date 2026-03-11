# Contract Tests

> Track: `software-engineering` | Topic: `testing`

## Concept

A contract test checks that a provider still satisfies the exact fields and types a consumer depends on.

## Key Points

- Extra provider fields are usually fine.
- Missing required fields or wrong types are the main contract breaks.
- Contract tests protect boundaries without needing a full end-to-end environment.

## Minimal Code Mental Model

```python
contract = make_contract({"id": "string", "amount_cents": "integer"}, {"memo": "string"})
violations = contract_violations(contract, {"id": "p_1", "amount_cents": 2500})
report = contract_report("payment-created", contract, {"id": "p_1", "amount_cents": "2500"})
```

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
