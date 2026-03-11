from __future__ import annotations


def make_contract(
    required_fields: dict[str, str],
    optional_fields: dict[str, str] | None = None,
) -> dict[str, dict[str, str]]:
    return {
        "required": {name: field_type.strip() for name, field_type in required_fields.items()},
        "optional": {
            name: field_type.strip()
            for name, field_type in (optional_fields or {}).items()
        },
    }


def _matches_type(value: object, expected_type: str) -> bool:
    if expected_type == "string":
        return isinstance(value, str)
    if expected_type == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected_type == "boolean":
        return isinstance(value, bool)
    if expected_type == "object":
        return isinstance(value, dict)
    if expected_type == "array":
        return isinstance(value, list)
    raise ValueError(f"unsupported contract type: {expected_type}")


def contract_violations(contract: dict[str, dict[str, str]], payload: dict[str, object]) -> list[str]:
    violations: list[str] = []

    for field_name, field_type in contract["required"].items():
        if field_name not in payload:
            violations.append(f"missing required field: {field_name}")
            continue
        if not _matches_type(payload[field_name], field_type):
            violations.append(f"wrong type for field: {field_name}")

    for field_name, field_type in contract["optional"].items():
        if field_name in payload and not _matches_type(payload[field_name], field_type):
            violations.append(f"wrong type for field: {field_name}")

    return violations


def contract_report(
    contract_name: str,
    contract: dict[str, dict[str, str]],
    payload: dict[str, object],
) -> dict[str, object]:
    cleaned_name = contract_name.strip()
    if not cleaned_name:
        raise ValueError("contract_name must be non-empty")

    violations = contract_violations(contract, payload)
    return {
        "contract": cleaned_name,
        "passed": not violations,
        "violations": violations,
    }
