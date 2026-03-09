import pytest

from advantage_normalization import normalize_advantages


def test_normalize_advantages_centers_and_scales_batch() -> None:
    normalized = normalize_advantages([1.0, 2.0, 3.0])

    assert normalized == pytest.approx([-1.22474486, 0.0, 1.22474486], abs=1e-7)


def test_normalize_advantages_returns_zeros_for_constant_batch() -> None:
    normalized = normalize_advantages([2.0, 2.0, 2.0])

    assert normalized == pytest.approx([0.0, 0.0, 0.0])


def test_normalize_advantages_rejects_negative_eps() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        normalize_advantages([1.0], eps=-1.0)
