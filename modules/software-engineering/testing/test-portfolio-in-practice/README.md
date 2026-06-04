# Test Portfolio In Practice

> Track: `software-engineering` | Topic: `testing`

## Concept

A practical test portfolio chooses the smallest set of test layers that protect the change's real failure modes.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Change planning | You need to decide which tests belong in the merge gate | You are only editing comments or docs |
| Risk review | Tags like `api`, `database`, `bugfix`, or `critical-path` describe the change | The risk cannot be named yet |
| AI-generated edit | Plausible code needs regression protection before merge | The generated output is not executable code |

## First Principles

- Every change should not trigger the same test stack.
- Contract, integration, and end-to-end tests should be added because of boundary risk, not habit.
- Regression tests matter more after bug fixes and AI-generated edits.

## Workflow

1. Tag the change by boundary and risk.
2. Start with unit tests as the default local proof.
3. Add contract, integration, regression, or end-to-end layers only when the tag requires them.
4. Compare required layers with present layers.
5. Block merge until the missing layer list is empty.

## Minimal Code Mental Model

```python
layers = recommended_test_layers(["api", "bugfix", "critical-path"])
missing = missing_required_layers(["database", "workflow"], ["unit", "integration"])
ready = merge_ready(["api", "bugfix"], ["unit", "contract", "regression"])
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Same test stack for every change | Slow checks hide the important signal | `recommended_test_layers` maps tags to focused layers |
| Boundary change with only unit tests | Provider and consumer drift | `missing_required_layers` catches absent contract or integration coverage |
| Bugfix without regression test | The same bug can return silently | `bugfix` and `ai-generated` tags require `regression` |

## Function

```python
def recommended_test_layers(change_tags: list[str]) -> list[str]:
def missing_required_layers(change_tags: list[str], present_layers: list[str]) -> list[str]:
def merge_ready(change_tags: list[str], present_layers: list[str]) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/testing/test-portfolio-in-practice/python -q
```
