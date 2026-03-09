import pytest

from positive_rate import positive_rate


def test_positive_rate_returns_fraction_of_positive_labels() -> None:
    assert positive_rate([1, 0, 1, 1, 0]) == pytest.approx(0.6)


def test_positive_rate_returns_zero_for_empty_labels() -> None:
    assert positive_rate([]) == pytest.approx(0.0)


def test_positive_rate_requires_binary_labels() -> None:
    with pytest.raises(ValueError, match="0 or 1"):
        positive_rate([1, 2, 0])
