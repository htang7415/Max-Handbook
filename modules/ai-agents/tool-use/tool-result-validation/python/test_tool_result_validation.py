from __future__ import annotations

from tool_result_validation import (
    result_has_error,
    result_has_fields,
    validation_report,
)


def test_tool_result_validation_checks_fields_and_error_state() -> None:
    result = {"status": "ok", "temperature_f": 41}
    assert result_has_fields(result, ["status", "temperature_f"]) is True
    assert result_has_error(result) is False
    assert validation_report(result, ["status", "temperature_f"]) == {
        "ok": True,
        "has_required_fields": True,
        "has_error": False,
    }


def test_tool_result_validation_rejects_bad_results() -> None:
    bad = {"status": "error", "message": "timeout"}
    assert result_has_fields(bad, ["status", "temperature_f"]) is False
    assert result_has_error(bad) is True
    assert validation_report(bad, ["status", "temperature_f"]) == {
        "ok": False,
        "has_required_fields": False,
        "has_error": True,
    }
