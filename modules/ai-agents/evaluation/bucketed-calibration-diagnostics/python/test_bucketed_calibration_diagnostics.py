from __future__ import annotations

import pytest

from bucketed_calibration_diagnostics import (
    bucketed_calibration_table,
    calibration_diagnostic_route,
    confidence_bucket_index,
    expected_calibration_error,
)


def test_bucketed_calibration_diagnostics_build_table_and_ece() -> None:
    confidences = [0.1, 0.2, 0.55, 0.6, 0.9, 0.95]
    outcomes = [False, True, True, False, True, False]

    assert confidence_bucket_index(0.95, bucket_count=4) == 3
    table = bucketed_calibration_table(confidences, outcomes, bucket_count=4)
    assert table == [
        {"bucket": 0, "count": 2, "mean_confidence": pytest.approx(0.15), "accuracy": pytest.approx(0.5), "gap": pytest.approx(0.35)},
        {"bucket": 1, "count": 0, "mean_confidence": pytest.approx(0.0), "accuracy": pytest.approx(0.0), "gap": pytest.approx(0.0)},
        {"bucket": 2, "count": 2, "mean_confidence": pytest.approx(0.575), "accuracy": pytest.approx(0.5), "gap": pytest.approx(0.075)},
        {"bucket": 3, "count": 2, "mean_confidence": pytest.approx(0.925), "accuracy": pytest.approx(0.5), "gap": pytest.approx(0.425)},
    ]
    ece = expected_calibration_error(confidences, outcomes, bucket_count=4)
    assert ece == pytest.approx(0.2833333333)
    assert calibration_diagnostic_route(ece, max_ece=0.3) == "pass"


def test_bucketed_calibration_diagnostics_routes_large_ece_to_review() -> None:
    assert calibration_diagnostic_route(0.18, max_ece=0.1) == "review"


def test_bucketed_calibration_diagnostics_validation() -> None:
    with pytest.raises(ValueError):
        confidence_bucket_index(1.2, bucket_count=5)
    with pytest.raises(ValueError):
        bucketed_calibration_table([], [True], bucket_count=5)
    with pytest.raises(ValueError):
        bucketed_calibration_table([0.5], [True, False], bucket_count=5)
    with pytest.raises(ValueError):
        calibration_diagnostic_route(0.1, max_ece=1.2)
