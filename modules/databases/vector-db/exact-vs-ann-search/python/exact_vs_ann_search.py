"""exact_vs_ann_search - exact scoring versus toy ANN candidate pruning."""

from __future__ import annotations

import math


def validate_vector(vector: list[float]) -> None:
    if not vector:
        raise ValueError("vector must be non-empty")


def validate_k(k: int) -> None:
    if k < 0:
        raise ValueError("k must be non-negative")


def cosine_similarity(left: list[float], right: list[float]) -> float:
    validate_vector(left)
    validate_vector(right)
    if len(left) != len(right):
        raise ValueError("vectors must have the same dimensions")
    left_norm = math.sqrt(sum(value * value for value in left))
    right_norm = math.sqrt(sum(value * value for value in right))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    similarity = sum(a * b for a, b in zip(left, right)) / (left_norm * right_norm)
    if abs(similarity - 1.0) < 1e-12:
        return 1.0
    if abs(similarity + 1.0) < 1e-12:
        return -1.0
    return similarity


def bucket_key(vector: list[float], threshold: float = 0.8) -> str:
    validate_vector(vector)
    if vector[0] >= threshold:
        return "high-x"
    if len(vector) > 1 and vector[1] >= threshold:
        return "high-y"
    return "mixed"


def exact_top_k(
    query_vector: list[float],
    documents: list[dict[str, object]],
    k: int,
) -> list[tuple[str, float]]:
    validate_vector(query_vector)
    validate_k(k)
    scored = [
        (
            str(document["id"]),
            cosine_similarity(query_vector, list(document["vector"])),
        )
        for document in documents
    ]
    return sorted(scored, key=lambda item: (-item[1], item[0]))[:k]


def ann_top_k(
    query_vector: list[float],
    documents: list[dict[str, object]],
    k: int,
    threshold: float = 0.8,
) -> tuple[list[tuple[str, float]], int]:
    validate_vector(query_vector)
    validate_k(k)
    query_bucket = bucket_key(query_vector, threshold=threshold)
    candidates = [
        document
        for document in documents
        if bucket_key(list(document["vector"]), threshold=threshold) == query_bucket
    ]
    if not candidates:
        candidates = documents

    scored = [
        (
            str(document["id"]),
            cosine_similarity(query_vector, list(document["vector"])),
        )
        for document in candidates
    ]
    scored.sort(key=lambda item: (-item[1], item[0]))
    return scored[:k], len(candidates)


def recall_at_k(
    exact_results: list[tuple[str, float]],
    ann_results: list[tuple[str, float]],
) -> float:
    if not exact_results:
        return 1.0
    exact_ids = {doc_id for doc_id, _ in exact_results}
    ann_ids = {doc_id for doc_id, _ in ann_results}
    return len(exact_ids & ann_ids) / len(exact_ids)
