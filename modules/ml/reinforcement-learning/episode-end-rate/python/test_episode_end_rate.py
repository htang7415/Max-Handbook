import pytest

from episode_end_rate import episode_end_rate


def test_episode_end_rate_returns_fraction_of_terminal_transitions() -> None:
    score = episode_end_rate([False, True, False, True])

    assert score == pytest.approx(0.5)


def test_episode_end_rate_returns_zero_for_empty_input() -> None:
    assert episode_end_rate([]) == pytest.approx(0.0)


def test_episode_end_rate_is_one_when_all_transitions_end_episodes() -> None:
    assert episode_end_rate([True, True]) == pytest.approx(1.0)
