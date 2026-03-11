# Test Portfolio In Practice

> Track: `software-engineering` | Topic: `testing`

## Concept

A practical test portfolio chooses the smallest set of test layers that protect the change's real failure modes.

## Key Points

- Every change should not trigger the same test stack.
- Contract, integration, and end-to-end tests should be added because of boundary risk, not habit.
- Regression tests matter more after bug fixes and AI-generated edits.

## Minimal Code Mental Model

```python
layers = recommended_test_layers(["api", "bugfix", "critical-path"])
missing = missing_required_layers(["database", "workflow"], ["unit", "integration"])
ready = merge_ready(["api", "bugfix"], ["unit", "contract", "regression"])
```

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
