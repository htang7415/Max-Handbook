import pytest

from overload_duration_share import overload_duration_share


def test_overload_duration_share_returns_fraction_above_threshold() -> None:
    share = overload_duration_share([0.8, 1.0, 1.3, 0.9, 1.5], threshold=1.0)

    assert share == pytest.approx(2 / 5)


def test_overload_duration_share_returns_zero_for_empty_input() -> None:
    assert overload_duration_share([], threshold=1.0) == pytest.approx(0.0)


def test_overload_duration_share_requires_non_negative_observations() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        overload_duration_share([1.0, -0.1], threshold=1.0)
