"""hybrid_retrieval_evaluation - compare lexical, vector, and hybrid retrieval runs."""

from __future__ import annotations


def unique_hits_within_k(ranked_ids: list[str], relevant_ids: set[str], k: int) -> int:
    seen: set[str] = set()
    hits = 0
    for doc_id in ranked_ids[:k]:
        if doc_id in relevant_ids and doc_id not in seen:
            hits += 1
        seen.add(doc_id)
    return hits


def precision_at_k(
    ranked_ids: list[str],
    relevant_ids: set[str],
    k: int,
) -> float:
    if k <= 0:
        return 0.0
    top_k = ranked_ids[:k]
    if not top_k:
        return 0.0
    hits = unique_hits_within_k(ranked_ids, relevant_ids, k)
    return hits / k


def reciprocal_rank(
    ranked_ids: list[str],
    relevant_ids: set[str],
) -> float:
    for index, doc_id in enumerate(ranked_ids, start=1):
        if doc_id in relevant_ids:
            return 1.0 / index
    return 0.0


def evaluate_run(
    ranked_by_query: dict[str, list[str]],
    relevant_by_query: dict[str, set[str]],
    k: int,
) -> dict[str, float]:
    if not relevant_by_query:
        return {"precision_at_k": 0.0, "mrr": 0.0}
    precisions: list[float] = []
    reciprocal_ranks: list[float] = []
    for query_id, relevant_ids in relevant_by_query.items():
        ranked_ids = ranked_by_query.get(query_id, [])
        precisions.append(precision_at_k(ranked_ids, relevant_ids, k))
        reciprocal_ranks.append(reciprocal_rank(ranked_ids, relevant_ids))
    query_count = len(relevant_by_query)
    return {
        "precision_at_k": sum(precisions) / query_count,
        "mrr": sum(reciprocal_ranks) / query_count,
    }


def evaluate_runs(
    runs: dict[str, dict[str, list[str]]],
    relevant_by_query: dict[str, set[str]],
    k: int,
) -> dict[str, dict[str, float]]:
    return {
        run_name: evaluate_run(ranked_by_query, relevant_by_query, k)
        for run_name, ranked_by_query in runs.items()
    }


def best_run_name(
    scores: dict[str, dict[str, float]],
    metric: str,
) -> str:
    return max(scores, key=lambda run_name: (scores[run_name][metric], run_name))
