import pytest

from retrieval_fusion import weighted_retrieval_fusion


def test_weighted_retrieval_fusion_combines_sparse_and_dense_scores() -> None:
    ranking = weighted_retrieval_fusion(
        sparse_scores={"a": 0.8, "b": 0.5},
        dense_scores={"a": 0.2, "c": 0.9},
        alpha=0.6,
    )

    assert [doc_id for doc_id, _ in ranking] == ["a", "c", "b"]
    assert [score for _, score in ranking] == pytest.approx([0.56, 0.36000000000000004, 0.3])


def test_weighted_retrieval_fusion_allows_dense_only_weight() -> None:
    ranking = weighted_retrieval_fusion(
        sparse_scores={"a": 1.0},
        dense_scores={"a": 0.1, "b": 0.9},
        alpha=0.0,
    )

    assert ranking == [("b", 0.9), ("a", 0.1)]


def test_weighted_retrieval_fusion_requires_valid_alpha() -> None:
    with pytest.raises(ValueError, match="0 <= alpha <= 1"):
        weighted_retrieval_fusion({}, {}, alpha=1.5)
