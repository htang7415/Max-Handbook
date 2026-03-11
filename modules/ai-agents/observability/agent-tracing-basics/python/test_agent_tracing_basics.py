from __future__ import annotations

import pytest

from agent_tracing_basics import add_span, start_trace, summarize_trace


def test_agent_tracing_basics_records_and_summarizes_trace() -> None:
    trace = start_trace("run_7", "prepare report")
    trace = add_span(trace, "plan", 40.0, "ok")
    trace = add_span(trace, "tool_call", 180.0, "error")
    assert summarize_trace(trace) == {
        "span_count": 2,
        "total_latency_ms": 220.0,
        "failed_spans": 1,
    }


def test_agent_tracing_basics_validation() -> None:
    with pytest.raises(ValueError):
        start_trace("", "goal")
    with pytest.raises(ValueError):
        start_trace("run_1", "")
    trace = start_trace("run_1", "goal")
    with pytest.raises(ValueError):
        add_span(trace, "", 10.0, "ok")
    with pytest.raises(ValueError):
        add_span(trace, "tool", -1.0, "ok")
    with pytest.raises(ValueError):
        add_span(trace, "tool", 10.0, "")
