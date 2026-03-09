from __future__ import annotations

import re
import string


def _normalize_answer(text: str) -> str:
    text = text.lower()
    text = "".join(character for character in text if character not in string.punctuation)
    text = re.sub(r"\b(a|an|the)\b", " ", text)
    return " ".join(text.split())


def self_consistency_vote(answers: list[str]) -> tuple[str, float]:
    if not answers:
        return "", 0.0

    counts: dict[str, int] = {}
    first_seen: list[str] = []
    for answer in answers:
        normalized = _normalize_answer(answer)
        if normalized not in counts:
            counts[normalized] = 0
            first_seen.append(normalized)
        counts[normalized] += 1

    winner = max(first_seen, key=lambda normalized: (counts[normalized], -first_seen.index(normalized)))
    vote_share = counts[winner] / len(answers)
    return winner, vote_share
