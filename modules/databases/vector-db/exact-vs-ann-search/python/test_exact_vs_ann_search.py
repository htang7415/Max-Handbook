from exact_vs_ann_search import ann_top_k, bucket_key, exact_top_k, recall_at_k
import pytest


DOCUMENTS = [
    {"id": "cross-bucket-best", "vector": [0.82, 0.57]},
    {"id": "mixed-good", "vector": [0.75, 0.65]},
    {"id": "mixed-second", "vector": [0.70, 0.45]},
    {"id": "high-y", "vector": [0.10, 0.95]},
]

QUERY = [0.79, 0.61]


def test_bucket_key_groups_vectors_into_toy_ann_partitions() -> None:
    assert bucket_key(QUERY) == "mixed"
    assert bucket_key([0.82, 0.57]) == "high-x"
    assert bucket_key([0.10, 0.95]) == "high-y"


def test_exact_search_scores_all_documents_and_finds_the_true_best_match() -> None:
    results = exact_top_k(QUERY, DOCUMENTS, k=2)

    assert [doc_id for doc_id, _ in results] == [
        "cross-bucket-best",
        "mixed-good",
    ]
    assert results[0][1] > results[1][1]


def test_ann_search_scores_fewer_candidates_but_can_reduce_recall() -> None:
    ann_results, candidates_scored = ann_top_k(QUERY, DOCUMENTS, k=2)
    exact_results = exact_top_k(QUERY, DOCUMENTS, k=2)

    assert [doc_id for doc_id, _ in ann_results] == [
        "mixed-good",
        "mixed-second",
    ]
    assert candidates_scored == 2
    assert recall_at_k(exact_results, ann_results) == 0.5
    assert ann_results[0][1] < exact_results[0][1]


def test_empty_vectors_and_negative_k_are_rejected() -> None:
    with pytest.raises(ValueError, match="vector"):
        bucket_key([])

    with pytest.raises(ValueError, match="k"):
        exact_top_k(QUERY, DOCUMENTS, k=-1)
