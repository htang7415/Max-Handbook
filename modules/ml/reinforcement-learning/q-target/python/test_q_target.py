import pytest

from q_target import q_target


def test_q_target_uses_max_next_state_action_value() -> None:
    target = q_target(reward=1.0, gamma=0.9, next_q_values=[2.0, 5.0, 4.0])

    assert target == pytest.approx(5.5)


def test_q_target_requires_non_empty_next_values() -> None:
    with pytest.raises(ValueError, match="non-empty"):
        q_target(reward=1.0, gamma=0.9, next_q_values=[])


def test_q_target_requires_valid_gamma() -> None:
    with pytest.raises(ValueError, match="gamma"):
        q_target(reward=1.0, gamma=1.5, next_q_values=[1.0])
