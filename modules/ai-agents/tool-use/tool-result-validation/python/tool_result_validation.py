from __future__ import annotations


def result_has_fields(result: dict[str, object], required_fields: list[str]) -> bool:
    return all(field in result for field in required_fields)


def result_has_error(result: dict[str, object]) -> bool:
    status = str(result.get("status", "")).strip().lower()
    is_error_flag = bool(result.get("is_error", False))
    return status == "error" or is_error_flag


def validation_report(result: dict[str, object], required_fields: list[str]) -> dict[str, object]:
    has_fields = result_has_fields(result, required_fields)
    has_error = result_has_error(result)
    return {
        "ok": has_fields and not has_error,
        "has_required_fields": has_fields,
        "has_error": has_error,
    }
