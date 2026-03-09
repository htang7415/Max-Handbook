import pytest

from wilson_interval import wilson_interval


def test_wilson_interval_for_balanced_rate() -> None:
    lower, upper = wilson_interval(successes=50, trials=100)

    assert lower == pytest.approx(0.4038, abs=1e-4)
    assert upper == pytest.approx(0.5962, abs=1e-4)


def test_wilson_interval_handles_zero_successes() -> None:
    lower, upper = wilson_interval(successes=0, trials=10)

    assert lower == pytest.approx(0.0)
    assert upper == pytest.approx(0.2775, abs=1e-4)


def test_wilson_interval_requires_valid_counts() -> None:
    with pytest.raises(ValueError, match="successes"):
        wilson_interval(successes=11, trials=10)
