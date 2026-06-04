# Composition Over Inheritance

> Track: `software-engineering` | Topic: `design-patterns`

## Concept

Composition combines a few small behaviors directly instead of building subclass trees for every feature combination.

## Use When

| Situation | Prefer |
| --- | --- |
| Behaviors combine independently | Composition |
| Reviewers need to see each step | Pipeline of small functions |
| Subtype identity matters | Inheritance may fit |

## First Principles

- Orthogonal behaviors combine more cleanly as functions than as subclass matrices.
- Composed steps keep each transformation obvious in code review.
- Use inheritance only when subtype behavior is actually the point.

## Workflow

1. List the behaviors that vary.
2. Keep each behavior small and testable.
3. Compose behaviors in the order the reader should see.
4. Use inheritance only when callers rely on subtype semantics.

## Minimal Code Mental Model

```python
label = compose_label(
    "  critical incident  ",
    [normalize_label, str.title, badge("P1")],
)
assert label == "Critical Incident [P1]"
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Subclass for every combination | Class matrix grows faster than behavior |
| Hidden transformation order | Reviews miss behavior changes |
| Composition with broad functions | The pipeline becomes another large abstraction |

## Function

```python
def normalize_label(value: str) -> str:
def badge(label: str):
def compose_label(value: str, transforms) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/design-patterns/composition-over-inheritance/python -q
```
