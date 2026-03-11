from __future__ import annotations

import pytest

from logs_metrics_and_traces import metric_summary, structured_log, trace_summary


def test_structured_log_keeps_core_fields_explicit() -> None:
    assert structured_log("payments", "INFO", "payment created", {"request_id": "req_1"}) == {
        "service": "payments",
        "level": "info",
        "message": "payment created",
        "context": {"request_id": "req_1"},
    }


def test_metric_summary_reports_basic_aggregation() -> None:
    assert metric_summary("latency_ms", [120.0, 180.0, 90.0]) == {
        "count": 3.0,
        "min": 90.0,
        "max": 180.0,
        "avg": 130.0,
    }


def test_trace_summary_counts_failed_spans_and_validates_latency() -> None:
    assert trace_summary(
        [
            {"name": "api", "latency_ms": 20.0, "status": "ok"},
            {"name": "db", "latency_ms": 80.0, "status": "error"},
        ]
    ) == {
        "span_count": 2,
        "failed_spans": 1,
        "total_latency_ms": 100.0,
    }

    with pytest.raises(ValueError):
        trace_summary([{"name": "db", "latency_ms": -1.0, "status": "error"}])
