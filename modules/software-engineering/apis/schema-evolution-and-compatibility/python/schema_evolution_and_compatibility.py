from __future__ import annotations


def make_field(type_name: str, required: bool = False) -> dict[str, object]:
    cleaned_type = type_name.strip()
    if not cleaned_type:
        raise ValueError("type_name must be non-empty")
    return {"type": cleaned_type, "required": required}


def breaking_changes(
    old_schema: dict[str, dict[str, object]],
    new_schema: dict[str, dict[str, object]],
) -> list[str]:
    issues: list[str] = []

    for field_name, old_field in old_schema.items():
        if field_name not in new_schema:
            issues.append(f"removed field: {field_name}")
            continue

        new_field = new_schema[field_name]
        if old_field["type"] != new_field["type"]:
            issues.append(f"type changed for field: {field_name}")
        if not old_field.get("required", False) and new_field.get("required", False):
            issues.append(f"field became required: {field_name}")

    return issues


def compatibility_summary(
    old_schema: dict[str, dict[str, object]],
    new_schema: dict[str, dict[str, object]],
) -> dict[str, object]:
    breaking = breaking_changes(old_schema, new_schema)
    additive = sorted(name for name in new_schema if name not in old_schema)
    return {
        "backward_compatible": not breaking,
        "breaking_changes": breaking,
        "additive_fields": additive,
    }
