# Regression Tests For AI-Generated Code

> Track: `software-engineering` | Topic: `testing`

## Concept

AI-generated code should trigger targeted regression suites based on touched areas and recent failures, not just generic smoke tests.

## Key Points

- The regression suite should be selected from change scope and failure history.
- Recent bug-fix cases should stay in the required suite.
- Generated-code changes deserve extra drift checks because the output can look plausible while still breaking contracts.

## Minimal Code Mental Model

```python
required = select_regression_cases(
    ["services/auth/policy.py", "src/generated/client.ts"],
    {"auth": ["auth-deny-default"], "generated": ["client-contract-drift"]},
    recent_bugfix_case_ids=["incident-1427"],
    touches_generated_code=True,
)
missing = missing_regression_cases(required, ["smoke", "auth-deny-default"])
ready = release_ready(required, ["smoke", "auth-deny-default", "client-contract-drift", "incident-1427"])
```

## Function

```python
def select_regression_cases(
    changed_paths: list[str],
    historical_case_map: dict[str, list[str]],
    recent_bugfix_case_ids: list[str] | None = None,
    touches_generated_code: bool = False,
) -> list[str]:
def missing_regression_cases(required_case_ids: list[str], executed_case_ids: list[str]) -> list[str]:
def release_ready(required_case_ids: list[str], passed_case_ids: list[str]) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/testing/regression-tests-for-ai-generated-code/python -q
```
