"""reranking_vs_retrieval_budgeting - choose whether reranking quality is worth the extra budget."""

from __future__ import annotations


def validate_pipeline_inputs(
    budget_ms: int,
    retrieve_k: int,
    rerank_candidates: int,
    retrieval_cost_per_doc: int,
    rerank_cost_per_doc: int,
    expected_retrieval_mrr: float,
    expected_rerank_mrr: float,
) -> None:
    if budget_ms < 0:
        raise ValueError("budget_ms must be non-negative")
    if retrieve_k < 0:
        raise ValueError("retrieve_k must be non-negative")
    if rerank_candidates < 0:
        raise ValueError("rerank_candidates must be non-negative")
    if rerank_candidates > retrieve_k:
        raise ValueError("rerank_candidates cannot exceed retrieve_k")
    if retrieval_cost_per_doc < 0:
        raise ValueError("retrieval_cost_per_doc must be non-negative")
    if rerank_cost_per_doc < 0:
        raise ValueError("rerank_cost_per_doc must be non-negative")
    if not 0.0 <= expected_retrieval_mrr <= 1.0:
        raise ValueError("expected_retrieval_mrr must be between 0 and 1")
    if not 0.0 <= expected_rerank_mrr <= 1.0:
        raise ValueError("expected_rerank_mrr must be between 0 and 1")


def retrieval_only_cost(retrieve_k: int, retrieval_cost_per_doc: int) -> int:
    if retrieve_k < 0:
        raise ValueError("retrieve_k must be non-negative")
    if retrieval_cost_per_doc < 0:
        raise ValueError("retrieval_cost_per_doc must be non-negative")
    return retrieve_k * retrieval_cost_per_doc


def rerank_pipeline_cost(
    retrieve_k: int,
    rerank_candidates: int,
    retrieval_cost_per_doc: int,
    rerank_cost_per_doc: int,
) -> int:
    if rerank_candidates < 0:
        raise ValueError("rerank_candidates must be non-negative")
    if rerank_candidates > retrieve_k:
        raise ValueError("rerank_candidates cannot exceed retrieve_k")
    if rerank_cost_per_doc < 0:
        raise ValueError("rerank_cost_per_doc must be non-negative")
    return retrieval_only_cost(retrieve_k, retrieval_cost_per_doc) + rerank_candidates * rerank_cost_per_doc


def fits_budget(cost: int, budget_ms: int) -> bool:
    if cost < 0:
        raise ValueError("cost must be non-negative")
    if budget_ms < 0:
        raise ValueError("budget_ms must be non-negative")
    return cost <= budget_ms


def choose_pipeline(
    budget_ms: int,
    retrieve_k: int,
    rerank_candidates: int,
    retrieval_cost_per_doc: int,
    rerank_cost_per_doc: int,
    expected_retrieval_mrr: float,
    expected_rerank_mrr: float,
) -> str:
    validate_pipeline_inputs(
        budget_ms,
        retrieve_k,
        rerank_candidates,
        retrieval_cost_per_doc,
        rerank_cost_per_doc,
        expected_retrieval_mrr,
        expected_rerank_mrr,
    )
    rerank_cost = rerank_pipeline_cost(
        retrieve_k,
        rerank_candidates,
        retrieval_cost_per_doc,
        rerank_cost_per_doc,
    )
    if fits_budget(rerank_cost, budget_ms) and expected_rerank_mrr > expected_retrieval_mrr:
        return "retrieval-plus-rerank"
    return "retrieval-only"


def pipeline_summary(
    budget_ms: int,
    retrieve_k: int,
    rerank_candidates: int,
    retrieval_cost_per_doc: int,
    rerank_cost_per_doc: int,
    expected_retrieval_mrr: float,
    expected_rerank_mrr: float,
) -> dict[str, int | float | str | bool]:
    validate_pipeline_inputs(
        budget_ms,
        retrieve_k,
        rerank_candidates,
        retrieval_cost_per_doc,
        rerank_cost_per_doc,
        expected_retrieval_mrr,
        expected_rerank_mrr,
    )
    retrieval_cost = retrieval_only_cost(retrieve_k, retrieval_cost_per_doc)
    rerank_cost = rerank_pipeline_cost(
        retrieve_k,
        rerank_candidates,
        retrieval_cost_per_doc,
        rerank_cost_per_doc,
    )
    return {
        "retrieval_cost": retrieval_cost,
        "rerank_cost": rerank_cost,
        "rerank_fits_budget": fits_budget(rerank_cost, budget_ms),
        "choice": choose_pipeline(
            budget_ms,
            retrieve_k,
            rerank_candidates,
            retrieval_cost_per_doc,
            rerank_cost_per_doc,
            expected_retrieval_mrr,
            expected_rerank_mrr,
        ),
        "mrr_gain": expected_rerank_mrr - expected_retrieval_mrr,
    }
