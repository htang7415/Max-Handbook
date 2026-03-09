import pytest

from value_normalization import normalize_value_targets


def test_normalize_value_targets_returns_normalized_values_and_stats() -> None:
    normalized, mean, std = normalize_value_targets([1.0, 2.0, 3.0])

    assert normalized == pytest.approx([-1.22474486, 0.0, 1.22474486], abs=1e-7)
    assert mean == pytest.approx(2.0)
    assert std == pytest.approx(0.81649658, abs=1e-7)


def test_normalize_value_targets_returns_zero_variance_for_constant_batch() -> None:
    normalized, mean, std = normalize_value_targets([2.0, 2.0, 2.0])

    assert normalized == pytest.approx([0.0, 0.0, 0.0])
    assert mean == pytest.approx(2.0)
    assert std == pytest.approx(0.0)


def test_normalize_value_targets_rejects_negative_eps() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        normalize_value_targets([1.0], eps=-1.0)
