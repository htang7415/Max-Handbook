from __future__ import annotations

import pytest

from root_cause_attribution import (
    attribution_route,
    attributed_failure_counts,
    dominant_failure_source,
)


def test_root_cause_attribution_groups_failures_by_source() -> None:
    spans = [
        {"kind": "tool", "status": "failed"},
        {"kind": "tool", "status": "timeout"},
        {"kind": "model", "status": "failed"},
        {"kind": "workflow", "status": "ok"},
    ]

    counts = attributed_failure_counts(spans)
    assert counts == {"model": 1, "tool": 2}
    assert dominant_failure_source(counts) == "tool"
    assert attribution_route(counts, min_share=0.6) == "targeted-fix"


def test_root_cause_attribution_distinguishes_broad_review_and_no_failures() -> None:
    assert attribution_route({"tool": 2, "model": 2}, min_share=0.6) == "broad-review"
    assert attribution_route({}, min_share=0.6) == "no-failures"


def test_root_cause_attribution_validation() -> None:
    with pytest.raises(ValueError):
        attributed_failure_counts([])
    with pytest.raises(ValueError):
        attribution_route({"tool": 1}, min_share=1.1)
