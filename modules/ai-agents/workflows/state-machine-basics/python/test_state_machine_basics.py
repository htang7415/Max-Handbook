from __future__ import annotations

import pytest

from state_machine_basics import next_state, transition_trace, valid_transition


def test_state_machine_basics_validates_and_advances_states() -> None:
    transitions = {
        "planned": ["running"],
        "running": ["done", "blocked"],
        "blocked": ["running"],
    }
    assert valid_transition("planned", "running", transitions) is True
    assert valid_transition("running", "planned", transitions) is False
    assert next_state("planned", "start") == "running"
    assert next_state("running", "complete") == "done"
    assert transition_trace(["planned", "running", "done"]) == "planned -> running -> done"


def test_state_machine_basics_invalid_transition_raises() -> None:
    with pytest.raises(ValueError):
        next_state("done", "restart")
