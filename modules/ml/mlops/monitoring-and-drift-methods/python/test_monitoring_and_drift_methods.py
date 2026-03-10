from __future__ import annotations

import pytest

from monitoring_and_drift_methods import drift_detected, ks_drift_score, mean_shift, missing_rate, psi, psi_terms


def test_psi_is_zero_for_identical_distributions() -> None:
    assert psi([0.5, 0.5], [0.5, 0.5]) == 0.0
    assert psi_terms([0.5, 0.5], [0.5, 0.5]) == [0.0, 0.0]


def test_psi_validates_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        psi([0.5], [0.2, 0.8])


def test_ks_drift_score_detects_shift() -> None:
    score = ks_drift_score([1.0, 2.0, 3.0], [10.0, 11.0, 12.0])
    assert score == 1.0


def test_drift_detected_uses_threshold() -> None:
    assert drift_detected([1.0, 2.0, 3.0], [10.0, 11.0, 12.0], threshold=0.5) is True


def test_mean_shift_returns_difference_in_means() -> None:
    assert mean_shift([1.0, 2.0], [4.0, 6.0]) == 3.5


def test_mean_shift_requires_non_empty_inputs() -> None:
    with pytest.raises(ValueError, match="non-empty"):
        mean_shift([], [1.0])


def test_missing_rate_counts_nulls() -> None:
    assert missing_rate([1.0, None, 2.0, None]) == 0.5


def test_missing_rate_handles_empty_input() -> None:
    assert missing_rate([]) == 0.0
