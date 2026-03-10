import pytest

from transition_indicators import (
    continuation_mask,
    continuing_transition_batch,
    done_fraction,
    end_of_episode_mask,
    episode_end_rate,
    nonterminal_indicator,
    persistent_transition_batch,
    resilient_transition_batch,
    terminal_indicator,
    terminal_mask,
)


def test_masks_zero_out_terminal_positions() -> None:
    done_flags = [False, True, False]

    assert terminal_mask(done_flags) == [1.0, 0.0, 1.0]
    assert continuation_mask(done_flags) == [1.0, 0.0, 1.0]
    assert continuing_transition_batch(done_flags) == [1.0, 0.0, 1.0]
    assert persistent_transition_batch(done_flags) == [1.0, 0.0, 1.0]
    assert resilient_transition_batch(done_flags) == [1.0, 0.0, 1.0]
    assert end_of_episode_mask(done_flags) == [0.0, 1.0, 0.0]


def test_fraction_and_indicators_match_done_state() -> None:
    assert done_fraction([True, False, True, False]) == pytest.approx(0.5)
    assert episode_end_rate([True, False, True, False]) == pytest.approx(0.5)
    assert terminal_indicator(True) == 1.0
    assert terminal_indicator(False) == 0.0
    assert nonterminal_indicator(True) == 0.0
    assert nonterminal_indicator(False) == 1.0


def test_empty_done_flags_have_zero_fraction() -> None:
    assert done_fraction([]) == 0.0
