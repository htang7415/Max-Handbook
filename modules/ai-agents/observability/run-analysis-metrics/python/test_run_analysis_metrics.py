from __future__ import annotations

import pytest

from run_analysis_metrics import failed_span_counts, mean_run_latency_ms, run_success_rate


def test_run_analysis_metrics_summarize_runs_and_failures() -> None:
    runs = [
        {"success": True, "latency_ms": 120.0},
        {"success": False, "latency_ms": 180.0},
        {"success": True, "latency_ms": 150.0},
    ]
    traces = [
        {"spans": [{"name": "tool_call", "status": "error"}]},
        {"spans": [{"name": "tool_call", "status": "ok"}, {"name": "plan", "status": "error"}]},
    ]
    assert run_success_rate(runs) == pytest.approx(2 / 3)
    assert mean_run_latency_ms(runs) == pytest.approx(150.0)
    assert failed_span_counts(traces) == {"tool_call": 1, "plan": 1}


def test_run_analysis_metrics_validation() -> None:
    with pytest.raises(ValueError):
        run_success_rate([])
    with pytest.raises(ValueError):
        mean_run_latency_ms([])
    with pytest.raises(ValueError):
        mean_run_latency_ms([{"latency_ms": -1.0}])
