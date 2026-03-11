from __future__ import annotations

import pytest

from step_level_evaluation import (
    blocked_step_rate,
    step_completion_rate,
    step_status_counts,
)


def test_step_level_evaluation_summarizes_step_statuses() -> None:
    statuses = ["done", "done", "blocked", "failed"]
    assert step_completion_rate(statuses) == pytest.approx(0.5)
    assert blocked_step_rate(statuses) == pytest.approx(0.25)
    assert step_status_counts(statuses) == {"done": 2, "blocked": 1, "failed": 1}


def test_step_level_evaluation_validation() -> None:
    with pytest.raises(ValueError):
        step_completion_rate([])
    with pytest.raises(ValueError):
        blocked_step_rate(["", "   "])
    with pytest.raises(ValueError):
        step_status_counts([])
