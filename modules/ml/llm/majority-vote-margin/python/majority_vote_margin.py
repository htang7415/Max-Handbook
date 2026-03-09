from __future__ import annotations

import re
import string


def _normalize_answer(text: str) -> str:
    text = text.lower()
    text = "".join(character for character in text if character not in string.punctuation)
    text = re.sub(r"\b(a|an|the)\b", " ", text)
    return " ".join(text.split())


def majority_vote_margin(answers: list[str]) -> float:
    if not answers:
        return 0.0

    counts: dict[str, int] = {}
    for answer in answers:
        normalized = _normalize_answer(answer)
        counts[normalized] = counts.get(normalized, 0) + 1

    sorted_counts = sorted(counts.values(), reverse=True)
    top_share = sorted_counts[0] / len(answers)
    runner_up_share = 0.0 if len(sorted_counts) == 1 else sorted_counts[1] / len(answers)
    return top_share - runner_up_share
