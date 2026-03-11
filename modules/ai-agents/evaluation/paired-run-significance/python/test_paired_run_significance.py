from __future__ import annotations

import pytest

from paired_run_significance import (
    mcnemar_statistic,
    paired_outcome_counts,
    paired_significance_route,
)


def test_paired_run_significance_counts_discordant_pairs_and_routes_improvement() -> None:
    counts = paired_outcome_counts(
        [True, True, False, False, False, False, False, False, False, False],
        [True, False, True, True, True, True, True, False, False, False],
    )

    assert counts == {
        "both_success": 1,
        "baseline_only": 1,
        "candidate_only": 5,
        "both_fail": 3,
    }
    assert mcnemar_statistic(counts["baseline_only"], counts["candidate_only"]) == pytest.approx(1.5)
    assert paired_significance_route(counts, threshold=1.0) == "candidate-better"


def test_paired_run_significance_distinguishes_regression_and_inconclusive() -> None:
    regression_counts = {
        "both_success": 2,
        "baseline_only": 5,
        "candidate_only": 1,
        "both_fail": 2,
    }
    assert paired_significance_route(regression_counts, threshold=1.0) == "baseline-better"

    inconclusive_counts = {
        "both_success": 3,
        "baseline_only": 2,
        "candidate_only": 1,
        "both_fail": 4,
    }
    assert paired_significance_route(inconclusive_counts, threshold=3.84) == "inconclusive"


def test_paired_run_significance_validation() -> None:
    with pytest.raises(ValueError):
        paired_outcome_counts([], [True])
    with pytest.raises(ValueError):
        paired_outcome_counts([True], [True, False])
    with pytest.raises(ValueError):
        mcnemar_statistic(-1, 2)
    with pytest.raises(ValueError):
        paired_significance_route({"baseline_only": 1, "candidate_only": 2}, threshold=1.0)
