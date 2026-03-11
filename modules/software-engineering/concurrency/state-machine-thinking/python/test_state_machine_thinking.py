from __future__ import annotations

import pytest

from state_machine_thinking import apply_transition, is_terminal_state, valid_transition


TRANSITIONS = {
    ("pending", "start"): "running",
    ("running", "complete"): "completed",
    ("running", "fail"): "failed",
}


def test_valid_transition_and_apply_transition_use_explicit_transition_table() -> None:
    assert valid_transition("pending", "start", TRANSITIONS) is True
    assert apply_transition("pending", "start", TRANSITIONS) == "running"


def test_invalid_transition_is_rejected() -> None:
    assert valid_transition("pending", "complete", TRANSITIONS) is False
    with pytest.raises(ValueError):
        apply_transition("pending", "complete", TRANSITIONS)


def test_terminal_states_are_explicit() -> None:
    assert is_terminal_state("completed", {"completed", "failed"}) is True
    assert is_terminal_state("running", {"completed", "failed"}) is False
