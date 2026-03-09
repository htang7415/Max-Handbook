import pytest

from robust_scaling import robust_scale


def test_robust_scale_uses_median_and_iqr() -> None:
    scaled = robust_scale([1.0, 2.0, 3.0, 4.0, 5.0])

    assert scaled == pytest.approx([-1.0, -0.5, 0.0, 0.5, 1.0])


def test_robust_scale_flattens_zero_iqr_values() -> None:
    assert robust_scale([2.0, 2.0, 2.0]) == [0.0, 0.0, 0.0]


def test_robust_scale_handles_empty_input() -> None:
    assert robust_scale([]) == []
