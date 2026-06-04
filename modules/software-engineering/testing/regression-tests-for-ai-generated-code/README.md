# Regression Tests For AI-Generated Code

> Track: `software-engineering` | Topic: `testing`

## Concept

AI-generated code should trigger targeted regression suites based on touched areas and recent failures, not just generic smoke tests.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| AI-generated code change | A model edited logic, schemas, tests, or generated outputs | The model only summarized code |
| Recent bugfix | A known failure should stay covered | The case is unrelated to this change path |
| Generated output drift | Generated clients or artifacts changed | The generator output is not part of the repo |

## First Principles

- The regression suite should be selected from change scope and failure history.
- Recent bug-fix cases should stay in the required suite.
- Generated-code changes deserve extra drift checks because the output can look plausible while still breaking contracts.

## Workflow

1. Map changed paths to historical regression cases.
2. Always include a smoke case.
3. Add recent bugfix cases.
4. Add generated-output drift checks when generated code is touched.
5. Block release until required cases pass.

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

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Generic smoke tests only | Known failure mode is not exercised | `select_regression_cases` maps paths to historical cases |
| Recent incident forgotten | Fixed bug returns | Recent bugfix IDs are included in required cases |
| Required case not executed | Release proceeds without evidence | `missing_regression_cases` reports gaps |

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
