from __future__ import annotations

import pytest

from alerting_thresholds import alert_candidates, alert_message, threshold_breached


def test_alerting_thresholds_detects_breaches_and_formats_message() -> None:
    assert threshold_breached(220.0, 200.0, direction="above") is True
    assert threshold_breached(0.92, 0.95, direction="below") is True
    assert alert_message("latency_ms", 220.0, 200.0, direction="above") == (
        "ALERT: latency_ms=220.00 vs above 200.00"
    )
    assert alert_candidates(
        {"latency_ms": 220.0, "success_rate": 0.92},
        {"latency_ms": (200.0, "above"), "success_rate": (0.95, "below")},
    ) == ["latency_ms", "success_rate"]


def test_alerting_thresholds_validation() -> None:
    with pytest.raises(ValueError):
        threshold_breached(1.0, 0.0, direction="sideways")
    with pytest.raises(ValueError):
        alert_message("", 1.0, 0.0, direction="above")
