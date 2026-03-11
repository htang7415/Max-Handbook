from __future__ import annotations

import pytest

from regression_checks import metric_drop, regression_failed, regression_report


def test_regression_checks_detects_excess_drop() -> None:
    assert metric_drop(0.84, 0.79) == pytest.approx(0.05)
    assert regression_failed(0.84, 0.79, max_drop=0.03) is True
    assert regression_report("success", 0.84, 0.79, max_drop=0.03) == {
        "metric": "success",
        "baseline": 0.84,
        "candidate": 0.79,
        "drop": pytest.approx(0.05),
        "failed": True,
    }


def test_regression_checks_validation_and_non_failure_case() -> None:
    assert regression_failed(0.84, 0.82, max_drop=0.03) is False
    with pytest.raises(ValueError):
        regression_failed(0.84, 0.82, max_drop=-0.01)
    with pytest.raises(ValueError):
        regression_report("", 0.84, 0.82, max_drop=0.03)
