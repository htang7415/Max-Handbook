import pytest

from error_budget import error_budget_status


def test_error_budget_status_reports_remaining_fraction_and_burn_rate() -> None:
    remaining_budget, burn_rate = error_budget_status(total_requests=1000, failed_requests=1, slo_target=0.99)

    assert remaining_budget == pytest.approx(0.9)
    assert burn_rate == pytest.approx(0.1)


def test_error_budget_status_clamps_remaining_budget_at_zero_when_over_budget() -> None:
    remaining_budget, burn_rate = error_budget_status(total_requests=1000, failed_requests=20, slo_target=0.99)

    assert remaining_budget == pytest.approx(0.0)
    assert burn_rate == pytest.approx(2.0)


def test_error_budget_status_requires_valid_slo_target() -> None:
    with pytest.raises(ValueError, match="slo_target"):
        error_budget_status(total_requests=100, failed_requests=1, slo_target=1.0)
