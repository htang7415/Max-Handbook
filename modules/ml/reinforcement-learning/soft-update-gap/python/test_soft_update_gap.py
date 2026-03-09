import pytest

from soft_update_gap import soft_update_gap


def test_soft_update_gap_reports_remaining_lag_after_update() -> None:
    gap = soft_update_gap(
        target_values=[0.0, 2.0],
        online_values=[2.0, 4.0],
        tau=0.25,
    )

    assert gap == pytest.approx(1.5)


def test_soft_update_gap_returns_zero_for_empty_values() -> None:
    assert soft_update_gap([], [], tau=0.5) == pytest.approx(0.0)


def test_soft_update_gap_requires_tau_in_unit_interval() -> None:
    with pytest.raises(ValueError, match="0 <= tau <= 1"):
        soft_update_gap([0.0], [1.0], tau=1.2)
