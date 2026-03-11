# Schema Evolution And Compatibility

> Track: `software-engineering` | Topic: `apis`

## Concept

Schema evolution is about changing a payload shape without surprising existing clients or stored data readers.

## Key Points

- Adding an optional field is usually safe.
- Removing a field, changing its type, or making an optional field required is usually breaking.
- Compatibility checks should be mechanized instead of being left to review intuition.

## Minimal Code Mental Model

```python
old_schema = {
    "id": make_field("string", required=True),
    "title": make_field("string", required=True),
}
new_schema = {
    "id": make_field("string", required=True),
    "title": make_field("string", required=True),
    "summary": make_field("string"),
}
report = compatibility_summary(old_schema, new_schema)
```

## Function

```python
def make_field(type_name: str, required: bool = False) -> dict[str, object]:
def breaking_changes(
    old_schema: dict[str, dict[str, object]],
    new_schema: dict[str, dict[str, object]],
) -> list[str]:
def compatibility_summary(
    old_schema: dict[str, dict[str, object]],
    new_schema: dict[str, dict[str, object]],
) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/software-engineering/apis/schema-evolution-and-compatibility/python -q
```
