from __future__ import annotations

import re
import string


def _normalize_answer(text: str) -> str:
    text = text.lower()
    text = "".join(character for character in text if character not in string.punctuation)
    text = re.sub(r"\b(a|an|the)\b", " ", text)
    return " ".join(text.split())


def answer_stability(answers: list[str]) -> float:
    if not answers:
        return 0.0
    if len(answers) == 1:
        return 1.0

    counts: dict[str, int] = {}
    for answer in answers:
        normalized = _normalize_answer(answer)
        counts[normalized] = counts.get(normalized, 0) + 1

    total = len(answers)
    agreeing_pairs = sum(count * (count - 1) for count in counts.values())
    return agreeing_pairs / (total * (total - 1))
