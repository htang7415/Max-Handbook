from __future__ import annotations


def normalize_arguments(
    arguments: dict[str, object],
    aliases: dict[str, str],
    defaults: dict[str, object],
) -> dict[str, object]:
    normalized: dict[str, object] = {}
    for key, value in arguments.items():
        target_key = aliases.get(key, key).strip()
        if not target_key:
            continue
        if isinstance(value, str):
            cleaned_value = value.strip()
            if cleaned_value:
                normalized[target_key] = cleaned_value
        else:
            normalized[target_key] = value

    for key, value in defaults.items():
        normalized.setdefault(key, value)
    return normalized


def missing_required_arguments(arguments: dict[str, object], required: list[str]) -> list[str]:
    missing: list[str] = []
    for key in required:
        cleaned_key = key.strip()
        if not cleaned_key:
            continue
        value = arguments.get(cleaned_key)
        if value is None or (isinstance(value, str) and not value.strip()):
            missing.append(cleaned_key)
    return missing


def arguments_ready(arguments: dict[str, object], required: list[str]) -> bool:
    return len(missing_required_arguments(arguments, required)) == 0
