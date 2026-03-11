# Failure Taxonomy

> Track: `ai-agents` | Topic: `evaluation`

## Concept

Failure taxonomy groups agent failures into a small set of stable categories so runs can be triaged and compared consistently.

## Key Points

- A small taxonomy is easier to use than many one-off error labels.
- Good categories separate model, tool, workflow, and policy failures.
- Counting by category is often enough to find the main bottleneck.

## Minimal Code Mental Model

```python
kind = categorize_failure("tool timeout")
counts = failure_category_counts(["tool timeout", "policy block", "tool timeout"])
top = top_failure_category(["tool timeout", "policy block", "tool timeout"])
```

## Function

```python
def categorize_failure(message: str) -> str:
def failure_category_counts(messages: list[str]) -> dict[str, int]:
def top_failure_category(messages: list[str]) -> str | None:
```

## Run tests

```bash
pytest modules/ai-agents/evaluation/failure-taxonomy/python -q
```
