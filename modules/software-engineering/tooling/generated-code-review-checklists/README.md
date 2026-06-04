# Generated Code Review Checklists

> Track: `software-engineering` | Topic: `tooling`

## Concept

Generated code should pass an explicit review checklist so reviewers verify the right risks instead of reacting to whatever the diff happens to highlight.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| AI-generated diff | Reviewers need risk-specific questions | The output is not going to merge |
| API or schema change | Compatibility must be reviewed explicitly | The change is internal-only behavior |
| Security-sensitive change | Auth, secrets, or permissions are touched | The change has no trust boundary |

## First Principles

- Review quality drops when the checklist lives only in reviewer memory.
- Different change types need different blocking questions.
- Merge should depend on completed review items, not reviewer confidence alone.

## Workflow

1. Tag the change by risk area.
2. Build a required review checklist from those tags.
3. Mark each item complete only after evidence exists.
4. Report incomplete review items.
5. Allow merge only when every required item is complete.

## Minimal Code Mental Model

```python
required = review_checklist(["api", "security", "ai-generated"])
blockers = missing_review_items(required, completed)
ready = review_complete(required, completed)
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Checklist in memory | Different reviewers check different risks | `review_checklist` derives required items from tags |
| Incomplete review item | Merge relies on confidence rather than evidence | `missing_review_items` reports open items |
| AI drift unreviewed | Generated code breaks contracts silently | `ai-generated` adds `regression` review |

## Function

```python
def review_checklist(change_tags: list[str]) -> list[str]:
def missing_review_items(required_items: list[str], completed_items: dict[str, bool]) -> list[str]:
def review_complete(required_items: list[str], completed_items: dict[str, bool]) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/tooling/generated-code-review-checklists/python -q
```
