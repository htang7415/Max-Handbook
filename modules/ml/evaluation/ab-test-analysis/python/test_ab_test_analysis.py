import math

import pytest

from ab_test_analysis import ab_test_analysis


def test_ab_test_analysis_reports_lift_and_significance() -> None:
    result = ab_test_analysis(
        control_conversions=45,
        control_trials=100,
        treatment_conversions=60,
        treatment_trials=100,
    )

    assert result.control_rate == pytest.approx(0.45)
    assert result.treatment_rate == pytest.approx(0.60)
    assert result.relative_lift == pytest.approx(1.0 / 3.0)
    assert result.z_score == pytest.approx(2.1240, abs=1e-4)
    assert result.p_value == pytest.approx(0.03367, abs=1e-5)


def test_ab_test_analysis_returns_neutral_statistic_for_identical_rates() -> None:
    result = ab_test_analysis(
        control_conversions=50,
        control_trials=100,
        treatment_conversions=25,
        treatment_trials=50,
    )

    assert result.z_score == pytest.approx(0.0)
    assert result.p_value == pytest.approx(1.0)


def test_ab_test_analysis_handles_zero_control_rate() -> None:
    result = ab_test_analysis(
        control_conversions=0,
        control_trials=100,
        treatment_conversions=10,
        treatment_trials=100,
    )

    assert math.isinf(result.relative_lift)
