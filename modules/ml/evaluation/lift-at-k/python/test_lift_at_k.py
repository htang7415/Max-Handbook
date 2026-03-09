import pytest

from lift_at_k import lift_at_k


def test_lift_at_k_compares_top_prefix_to_base_rate() -> None:
    score = lift_at_k([1, 1, 0, 0, 0], k=2)

    assert score == pytest.approx(2.5)


def test_lift_at_k_returns_zero_when_no_positive_examples_exist() -> None:
    assert lift_at_k([0, 0, 0], k=2) == pytest.approx(0.0)


def test_lift_at_k_requires_binary_labels() -> None:
    with pytest.raises(ValueError, match="0 or 1"):
        lift_at_k([1, 2, 0], k=2)


def test_lift_at_k_requires_valid_k() -> None:
    with pytest.raises(ValueError, match="must not exceed"):
        lift_at_k([1, 0], k=3)
