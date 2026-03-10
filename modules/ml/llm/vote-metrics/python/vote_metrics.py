from __future__ import annotations

import math
import re
import string


def normalize_answer(text: str) -> str:
    text = text.lower()
    text = "".join(character for character in text if character not in string.punctuation)
    text = re.sub(r"\b(a|an|the)\b", " ", text)
    return " ".join(text.split())


def normalized_vote_counts(answers: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for answer in answers:
        normalized = normalize_answer(answer)
        counts[normalized] = counts.get(normalized, 0) + 1
    return counts


def _sorted_vote_counts(answers: list[str]) -> list[int]:
    return sorted(normalized_vote_counts(answers).values(), reverse=True)


def answer_stability(answers: list[str]) -> float:
    if not answers:
        return 0.0
    if len(answers) == 1:
        return 1.0

    counts = normalized_vote_counts(answers)
    total = len(answers)
    agreeing_pairs = sum(count * (count - 1) for count in counts.values())
    return agreeing_pairs / (total * (total - 1))


def majority_vote_margin(answers: list[str]) -> float:
    counts = _sorted_vote_counts(answers)
    if not counts:
        return 0.0

    top_share = counts[0] / len(answers)
    runner_up_share = 0.0 if len(counts) == 1 else counts[1] / len(answers)
    return top_share - runner_up_share


def vote_entropy(answers: list[str]) -> float:
    if not answers:
        return 0.0

    counts = normalized_vote_counts(answers)
    total = len(answers)
    return -sum((count / total) * math.log(count / total) for count in counts.values())


def answer_uniqueness_rate(answers: list[str]) -> float:
    if not answers:
        return 0.0
    return len(normalized_vote_counts(answers)) / len(answers)


def candidate_diversity(answers: list[str]) -> float:
    return answer_uniqueness_rate(answers)


def top_vote_share(answers: list[str]) -> float:
    counts = _sorted_vote_counts(answers)
    if not counts:
        return 0.0
    return counts[0] / len(answers)


def consensus_disagreement_rate(answers: list[str]) -> float:
    return 1.0 - top_vote_share(answers)


def minority_cluster_entropy(answers: list[str]) -> float:
    counts = _sorted_vote_counts(answers)
    if len(counts) <= 1:
        return 0.0

    minority_sizes = counts[1:]
    minority_total = sum(minority_sizes)
    return -sum((size / minority_total) * math.log(size / minority_total) for size in minority_sizes)
