from __future__ import annotations

import math

import pytest

from log_rate_metrics import log_rate, log_rate_table


def test_log_rate_matches_log_of_fraction() -> None:
    assert log_rate(2, 100) == pytest.approx(math.log(0.02))


def test_log_rate_returns_negative_infinity_for_zero_events() -> None:
    assert log_rate(0, 100) == float("-inf")


def test_log_rate_rejects_invalid_counts() -> None:
    with pytest.raises(ValueError):
        log_rate(-1, 100)
    with pytest.raises(ValueError):
        log_rate(101, 100)
    with pytest.raises(ValueError):
        log_rate(1, 0)


def test_log_rate_table_applies_same_formula_to_multiple_events() -> None:
    table = log_rate_table({"drop": 4, "timeout": 1}, total_count=100)
    assert table["drop"] == pytest.approx(math.log(0.04))
    assert table["timeout"] == pytest.approx(math.log(0.01))
