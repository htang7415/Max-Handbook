from __future__ import annotations

import pytest

from retrieval_abstention_and_coverage import (
    claim_coverage,
    rag_abstention_route,
    unsupported_claims,
)


def test_retrieval_abstention_and_coverage_measures_supported_claim_share() -> None:
    assert claim_coverage(["c1", "c2", "c3"], ["c1", "c3"]) == pytest.approx(2 / 3)
    assert unsupported_claims(["c1", "c2", "c3"], ["c1", "c3"]) == ["c2"]
    assert rag_abstention_route(coverage=2 / 3, support_count=2, min_coverage=0.6, min_support_count=2) == "answer"


def test_retrieval_abstention_and_coverage_distinguishes_retrieve_more_and_abstain() -> None:
    assert rag_abstention_route(coverage=0.5, support_count=1, min_coverage=0.8, min_support_count=2) == "retrieve-more"
    assert rag_abstention_route(coverage=0.0, support_count=0, min_coverage=0.8, min_support_count=2) == "abstain"


def test_retrieval_abstention_and_coverage_validation() -> None:
    with pytest.raises(ValueError):
        claim_coverage([], ["c1"])
    with pytest.raises(ValueError):
        unsupported_claims([], ["c1"])
    with pytest.raises(ValueError):
        rag_abstention_route(coverage=1.1, support_count=1, min_coverage=0.8, min_support_count=1)
