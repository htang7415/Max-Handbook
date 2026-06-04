# AI-Assisted Feature Delivery

> Track: `software-engineering` | Topic: `capstones`

## Concept

This capstone combines spec-first prompting, generated-code review gates, regression strength, and rollout readiness into one compact AI-assisted delivery workflow.

## Use When

| Delivery Stage | Engineer Gate |
| --- | --- |
| Before prompting or generation | Spec covers contracts, tests, and rollback |
| Before review approval | Compatibility, security, and regression blockers are clear |
| Before shipping | Unit, regression, and metamorphic checks match the risk |
| Before promotion | Rollback path is ready |

## First Principles

- AI should not start implementation before the spec covers contracts, tests, and rollback.
- Review needs explicit blockers for compatibility, security, and regression risk.
- Verification should be strong enough to catch plausible but wrong generated code.
- Shipping still depends on rollback readiness, not just passing tests.

## Workflow

1. Write the spec before generating code.
2. Check generated code against explicit review blockers.
3. Run verification that targets plausible wrong behavior.
4. Ship only when rollback readiness matches the change risk.

## Minimal Code Mental Model

```python
decision = delivery_decision(
    ["api", "ai-generated"],
    ["contract", "invariants", "tests", "rollback", "compatibility"],
    {"correctness": True, "tests": True, "compatibility": True, "regression": True},
    unit_passed=True,
    regression_passed=True,
    metamorphic_passed=True,
    rollback_ready=True,
)
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Prompt before spec | Generated code optimizes an unclear target |
| Review without blockers | Compatibility or security risk is missed |
| Tests only cover happy path | Plausible generated mistakes survive |
| No rollback check | Passing tests still ship an unrecoverable change |

## Function

```python
def required_spec_sections(change_tags: list[str]) -> list[str]:
def spec_gaps(change_tags: list[str], present_sections: list[str]) -> list[str]:
def review_blockers(change_tags: list[str], completed_items: dict[str, bool]) -> list[str]:
def verification_strength(
    unit_passed: bool,
    regression_passed: bool,
    metamorphic_passed: bool,
) -> str:
def delivery_decision(
    change_tags: list[str],
    present_sections: list[str],
    completed_items: dict[str, bool],
    unit_passed: bool,
    regression_passed: bool,
    metamorphic_passed: bool,
    rollback_ready: bool,
) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/capstones/ai-assisted-feature-delivery/python -q
```
