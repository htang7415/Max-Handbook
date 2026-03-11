from __future__ import annotations

import pytest

from golden_and_snapshot_test_tradeoffs import (
    recommended_output_test,
    snapshot_noise_risk,
    snapshot_update_allowed,
)


def test_recommended_output_test_depends_on_output_stability_and_size() -> None:
    assert recommended_output_test(stable_output=True, large_structured_output=True) == "snapshot"
    assert recommended_output_test(stable_output=True, large_structured_output=False) == "golden"
    assert recommended_output_test(stable_output=False, large_structured_output=True) == "assert-specific-fields"


def test_snapshot_noise_risk_rises_with_large_or_nondeterministic_diffs() -> None:
    assert snapshot_noise_risk(changed_lines=8, has_nondeterministic_values=False) == "low"
    assert snapshot_noise_risk(changed_lines=40, has_nondeterministic_values=False) == "medium"
    assert snapshot_noise_risk(changed_lines=2, has_nondeterministic_values=True) == "high"


def test_snapshot_update_allowed_requires_review_and_blocks_high_noise() -> None:
    assert snapshot_update_allowed(8, has_nondeterministic_values=False, reviewer_signed_off=True) is True
    assert snapshot_update_allowed(40, has_nondeterministic_values=False, reviewer_signed_off=False) is False
    assert snapshot_update_allowed(2, has_nondeterministic_values=True, reviewer_signed_off=True) is False

    with pytest.raises(ValueError):
        snapshot_noise_risk(-1, False)
