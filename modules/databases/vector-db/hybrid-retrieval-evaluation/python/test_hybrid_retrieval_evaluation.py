from hybrid_retrieval_evaluation import (
    best_run_name,
    evaluate_run,
    evaluate_runs,
    precision_at_k,
    reciprocal_rank,
)


def test_basic_metrics_capture_rank_quality():
    assert precision_at_k(["a", "b"], {"a"}, 1) == 1.0
    assert precision_at_k(["a", "b"], {"b"}, 1) == 0.0
    assert reciprocal_rank(["x", "b", "a"], {"b"}) == 0.5


def test_hybrid_run_beats_lexical_and_vector_baselines_on_toy_queries():
    relevant = {"q1": {"a"}, "q2": {"d"}}
    runs = {
        "lexical": {"q1": ["a", "b"], "q2": ["x", "d"]},
        "vector": {"q1": ["b", "a"], "q2": ["d", "x"]},
        "hybrid": {"q1": ["a", "b"], "q2": ["d", "x"]},
    }

    scores = evaluate_runs(runs, relevant, k=1)

    assert scores["hybrid"] == {"precision_at_k": 1.0, "mrr": 1.0}
    assert best_run_name(scores, "precision_at_k") == "hybrid"
    assert best_run_name(scores, "mrr") == "hybrid"


def test_evaluate_run_handles_missing_rankings():
    relevant = {"q1": {"a"}}
    assert evaluate_run({}, relevant, k=2) == {"precision_at_k": 0.0, "mrr": 0.0}


def test_duplicate_results_do_not_get_extra_precision_credit():
    assert precision_at_k(["a", "a"], {"a"}, 2) == 0.5
