# Review And Merge Discipline

> Track: `software-engineering` | Topic: `tooling`

## Concept

Review and merge discipline keeps changes safe by tying approvals, unresolved threads, and change risk to a clear merge decision.

## Key Points

- Passing checks are necessary but not sufficient for merge.
- Sensitive or wide changes should require stronger review than a small local edit.
- Open review threads should block merge until the disagreement is resolved or explicitly waived.

## Minimal Code Mental Model

```python
requirement = review_requirement(changed_paths=["services/auth/policy.py"], lines_changed=40)
ready = ready_for_merge(open_threads=0, checks_passed=True, approvals=2, required_approvals=1)
decision = merge_decision(
    changed_paths=["services/auth/policy.py"],
    lines_changed=40,
    checks_passed=True,
    open_threads=0,
    approvals=2,
)
```

## Function

```python
def review_requirement(changed_paths: list[str], lines_changed: int) -> str:
def ready_for_merge(
    open_threads: int,
    checks_passed: bool,
    approvals: int,
    required_approvals: int = 1,
) -> bool:
def merge_decision(
    changed_paths: list[str],
    lines_changed: int,
    checks_passed: bool,
    open_threads: int,
    approvals: int,
) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/tooling/review-and-merge-discipline/python -q
```
