import pytest

from sequential_testing import sequential_test_decision


def test_sequential_testing_uses_tighter_threshold_at_early_looks() -> None:
    threshold, significant = sequential_test_decision(p_value=0.02, alpha=0.05, look_index=1, total_looks=5)

    assert threshold == pytest.approx(0.01)
    assert not significant


def test_sequential_testing_can_accept_same_p_value_later_in_experiment() -> None:
    threshold, significant = sequential_test_decision(p_value=0.02, alpha=0.05, look_index=3, total_looks=5)

    assert threshold == pytest.approx(0.03)
    assert significant


def test_sequential_testing_requires_valid_look_index() -> None:
    with pytest.raises(ValueError, match="look_index"):
        sequential_test_decision(p_value=0.01, alpha=0.05, look_index=0, total_looks=5)
