# Ownership And Delete Boundaries

> Track: `databases` | Topic: `schema-design`

## Concept

Deletion behavior should follow ownership, not accident. Some child rows are owned and should cascade away with the parent; others are shared references and should block deletion or be detached explicitly.

## Key Points

- Ownership is a schema decision, not just a foreign key detail.
- Cascading deletes fit truly owned child data.
- Shared references often need blocking or reassignment instead of cascading.
- Good delete boundaries make offboarding and retention flows predictable.

## Minimal Code Mental Model

```python
plan = delete_plan(
    "workspace",
    [relation("documents", "cascade"), relation("billing-account", "block")],
)
```

## Function

```python
def relation(name: str, policy: str) -> dict[str, str]:
def delete_plan(parent: str, relations: list[dict[str, str]]) -> dict[str, object]:
def can_delete(plan: dict[str, object]) -> bool:
```

## Run tests

```bash
pytest modules/databases/schema-design/ownership-and-delete-boundaries/python -q
```
