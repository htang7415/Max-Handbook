from __future__ import annotations

import pytest

from agent_evaluation_basics import (
    failure_breakdown,
    mean_latency_ms,
    task_success_rate,
    tool_call_success_rate,
)


def test_agent_evaluation_basics_metrics() -> None:
    assert task_success_rate([True, False, True]) == pytest.approx(2 / 3)
    assert tool_call_success_rate([True, True, False, True]) == pytest.approx(0.75)
    assert mean_latency_ms([100.0, 140.0, 160.0]) == pytest.approx(133.3333333333)
    assert failure_breakdown(["tool", "model", "tool"]) == {"tool": 2, "model": 1}


def test_agent_evaluation_basics_validation() -> None:
    with pytest.raises(ValueError):
        task_success_rate([])
    with pytest.raises(ValueError):
        tool_call_success_rate([])
    with pytest.raises(ValueError):
        mean_latency_ms([])
    with pytest.raises(ValueError):
        mean_latency_ms([10.0, -1.0])
