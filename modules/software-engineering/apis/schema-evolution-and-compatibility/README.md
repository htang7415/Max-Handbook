# Schema Evolution And Compatibility

> Track: `software-engineering` | Topic: `apis`

## Concept

Schema evolution is about changing a payload shape without surprising existing clients or stored data readers.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Payload change | A field is added, removed, renamed, or retyped | The schema is not consumed outside the current function |
| API version review | Existing clients must keep working after deploy | A full breaking version is already planned |
| Stored data reader | Old records must still parse with new code | Data can be migrated atomically before release |

## First Principles

- Adding an optional field is usually safe.
- Removing a field, changing its type, or making an optional field required is usually breaking.
- Compatibility checks should be mechanized instead of being left to review intuition.

## Workflow

1. Represent each field with type and requiredness.
2. Compare old fields against the new schema.
3. Flag removed fields, type changes, and newly required fields.
4. Treat new fields as additive only when old readers can ignore them.
5. Report compatibility and additive fields together.

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

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Removed field | Existing clients lose a value they depend on | `breaking_changes` reports `removed field` |
| Type change | Old parsers accept the field name but reject the value | `breaking_changes` reports `type changed` |
| Optional becomes required | Old payloads no longer satisfy the new schema | `breaking_changes` reports `field became required` |

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
