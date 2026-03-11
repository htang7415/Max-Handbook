from __future__ import annotations

import pytest

from retrieval_quality_and_citations import (
    citation_coverage,
    cited_source_counts,
    uncited_claims,
)


def test_retrieval_quality_and_citations_measures_grounding() -> None:
    claim_ids = ["c1", "c2", "c3"]
    citations = {
        "c1": ["doc1"],
        "c2": ["doc1", "doc2"],
        "c3": [],
    }
    assert citation_coverage(claim_ids, citations) == pytest.approx(2 / 3)
    assert uncited_claims(claim_ids, citations) == ["c3"]
    assert cited_source_counts(citations) == {"doc1": 2, "doc2": 1}


def test_retrieval_quality_and_citations_validation() -> None:
    with pytest.raises(ValueError):
        citation_coverage([], {})
    with pytest.raises(ValueError):
        citation_coverage(["", "   "], {})
