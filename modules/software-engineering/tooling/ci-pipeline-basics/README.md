# CI Pipeline Basics

> Track: `software-engineering` | Topic: `tooling`

## Concept

A CI pipeline is a sequence of automated gates that should fail early on cheap checks and reserve heavier checks for boundary-risk changes.

## Key Points

- Not every change needs the same pipeline stages.
- Required stages should be explicit instead of being inferred from habit.
- A merge should be blocked when any required stage is missing or failing.

## Minimal Code Mental Model

```python
stages = required_ci_stages(["api", "bugfix"])
blockers = pipeline_blockers(
    {"lint": "passed", "unit": "passed", "contract": "failed", "regression": "passed"},
    stages,
)
ready = mergeable(
    {"lint": "passed", "unit": "passed", "contract": "passed", "regression": "passed"},
    stages,
)
```

## Function

```python
def required_ci_stages(change_tags: list[str]) -> list[str]:
def pipeline_blockers(stage_statuses: dict[str, str], required_stages: list[str]) -> list[str]:
def mergeable(stage_statuses: dict[str, str], required_stages: list[str]) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/tooling/ci-pipeline-basics/python -q
```
