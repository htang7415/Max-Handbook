# Review And Merge Discipline

> Track: `software-engineering` | Topic: `tooling`

## Concept

Review and merge discipline keeps changes safe by tying approvals, unresolved threads, and change risk to a clear merge decision.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Pull request review | Checks, approvals, and threads should produce one decision | The change is not ready for review |
| Sensitive change | Auth, billing, payment, security, or secrets are touched | Risk is already handled by another required gate |
| Large diff | Review depth should rise with size or scope | The diff is generated and separately audited |

## First Principles

- Passing checks are necessary but not sufficient for merge.
- Sensitive or wide changes should require stronger review than a small local edit.
- Open review threads should block merge until the disagreement is resolved or explicitly waived.

## Workflow

1. Classify review requirement from paths and size.
2. Require more approval for security-sensitive changes.
3. Block merge while checks fail.
4. Block merge while review threads remain open.
5. Merge only when approvals meet the requirement.

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

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Sensitive change under-reviewed | One approval ships high-risk behavior | `review_requirement` returns `security-review` |
| Open thread ignored | Known disagreement ships | `ready_for_merge` requires zero open threads |
| Negative review counts | Decision math is invalid | Review helpers validate counts |

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
