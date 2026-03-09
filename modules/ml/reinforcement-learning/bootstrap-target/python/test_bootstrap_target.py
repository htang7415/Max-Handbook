import pytest

from bootstrap_target import bootstrap_target


def test_bootstrap_target_adds_discounted_next_value_for_non_terminal_step() -> None:
    target = bootstrap_target(reward=1.0, gamma=0.9, next_value=4.0, done=False)

    assert target == pytest.approx(4.6)


def test_bootstrap_target_drops_bootstrap_term_for_terminal_step() -> None:
    assert bootstrap_target(reward=1.5, gamma=0.9, next_value=4.0, done=True) == pytest.approx(1.5)


def test_bootstrap_target_requires_gamma_in_unit_interval() -> None:
    with pytest.raises(ValueError, match="0 <= gamma <= 1"):
        bootstrap_target(reward=1.0, gamma=1.2, next_value=2.0, done=False)
