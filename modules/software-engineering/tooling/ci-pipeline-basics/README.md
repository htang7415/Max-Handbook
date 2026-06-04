# CI Pipeline Basics

> Track: `software-engineering` | Topic: `tooling`

## Concept

A CI pipeline is a sequence of automated gates that should fail early on cheap checks and reserve heavier checks for boundary-risk changes.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Merge gate | Required checks should block unsafe changes | The repo has no automated checks yet |
| Change-risk routing | API, database, bugfix, or release tags change required stages | Every change truly needs the same checks |
| CI review | Missing or failed stages should be visible | Check results are managed outside CI |

## First Principles

- Not every change needs the same pipeline stages.
- Required stages should be explicit instead of being inferred from habit.
- A merge should be blocked when any required stage is missing or failing.

## Workflow

1. Start with lint and unit stages.
2. Add contract, integration, regression, or build stages from change tags.
3. Compare required stages with actual stage statuses.
4. Report missing or failed stages as blockers.
5. Merge only when every required stage passed.

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

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Missing required check | Merge happens without evidence | `pipeline_blockers` reports missing stages |
| Failed required check | CI failure is ignored | `mergeable` requires blockers to be empty |
| One-size pipeline | Slow or weak checks hide risk | `required_ci_stages` expands by change tags |

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
