from __future__ import annotations

from test_portfolio_in_practice import (
    merge_ready,
    missing_required_layers,
    recommended_test_layers,
)


def test_recommended_test_layers_match_change_risk() -> None:
    assert recommended_test_layers(["api", "bugfix", "critical-path"]) == [
        "unit",
        "contract",
        "regression",
        "end-to-end",
    ]


def test_missing_required_layers_detects_absent_boundary_coverage() -> None:
    assert missing_required_layers(["database", "workflow"], ["unit"]) == ["integration"]
    assert missing_required_layers(["api", "bugfix"], ["unit", "contract", "regression"]) == []


def test_merge_ready_requires_all_recommended_layers() -> None:
    assert merge_ready(["api", "bugfix"], ["unit", "contract", "regression"]) is True
    assert merge_ready(["critical-path"], ["unit"]) is False
