from __future__ import annotations

from tool_argument_normalization import (
    arguments_ready,
    missing_required_arguments,
    normalize_arguments,
)


def test_tool_argument_normalization_cleans_aliases_and_defaults() -> None:
    normalized = normalize_arguments(
        {"city": " Madison ", "units": ""},
        {"city": "location"},
        {"units": "metric"},
    )
    assert normalized == {"location": "Madison", "units": "metric"}
    assert missing_required_arguments(normalized, ["location", "units"]) == []
    assert arguments_ready(normalized, ["location", "units"]) is True


def test_tool_argument_normalization_detects_missing_required_fields() -> None:
    normalized = normalize_arguments({}, {}, {})
    assert missing_required_arguments(normalized, ["location", "units"]) == ["location", "units"]
    assert arguments_ready(normalized, ["location"]) is False
