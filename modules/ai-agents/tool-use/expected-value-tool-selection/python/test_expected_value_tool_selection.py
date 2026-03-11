from __future__ import annotations

import pytest

from expected_value_tool_selection import (
    expected_tool_value,
    rank_tools_by_expected_value,
    tool_selection_route,
)


def test_expected_value_tool_selection_ranks_tools_by_expected_value() -> None:
    tool_profiles = {
        "search": {
            "success_probability": 0.8,
            "success_value": 10.0,
            "tool_cost": 1.0,
            "failure_penalty": 2.0,
        },
        "memory": {
            "success_probability": 0.9,
            "success_value": 5.0,
            "tool_cost": 0.5,
            "failure_penalty": 1.0,
        },
        "crm": {
            "success_probability": 0.6,
            "success_value": 12.0,
            "tool_cost": 2.0,
            "failure_penalty": 4.0,
        },
    }

    assert expected_tool_value(0.8, 10.0, 1.0, failure_penalty=2.0) == pytest.approx(6.6)
    assert rank_tools_by_expected_value(tool_profiles) == [
        {"tool": "search", "expected_value": pytest.approx(6.6)},
        {"tool": "memory", "expected_value": pytest.approx(3.9)},
        {"tool": "crm", "expected_value": pytest.approx(3.6)},
    ]
    assert tool_selection_route(tool_profiles, min_expected_value=4.0, min_margin=1.0) == "search"


def test_expected_value_tool_selection_distinguishes_skip_and_review() -> None:
    assert (
        tool_selection_route(
            {
                "tool-a": {"success_probability": 0.4, "success_value": 4.0, "tool_cost": 1.0},
                "tool-b": {"success_probability": 0.3, "success_value": 5.0, "tool_cost": 1.0},
            },
            min_expected_value=1.0,
            min_margin=0.5,
        )
        == "skip"
    )
    assert (
        tool_selection_route(
            {
                "tool-a": {"success_probability": 0.8, "success_value": 10.0, "tool_cost": 2.0},
                "tool-b": {"success_probability": 0.7, "success_value": 11.0, "tool_cost": 1.0},
            },
            min_expected_value=4.0,
            min_margin=0.8,
        )
        == "review"
    )


def test_expected_value_tool_selection_validation() -> None:
    with pytest.raises(ValueError):
        expected_tool_value(1.1, 10.0, 1.0)
    with pytest.raises(ValueError):
        expected_tool_value(0.8, -1.0, 1.0)
    with pytest.raises(ValueError):
        rank_tools_by_expected_value({})
    with pytest.raises(ValueError):
        tool_selection_route({"tool-a": {"success_probability": 0.8, "success_value": 10.0, "tool_cost": 1.0}}, 1.0, min_margin=-0.1)
