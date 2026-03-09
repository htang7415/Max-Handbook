from __future__ import annotations

import re
import string


def _normalize_answer(text: str) -> str:
    text = text.lower()
    text = "".join(character for character in text if character not in string.punctuation)
    text = re.sub(r"\b(a|an|the)\b", " ", text)
    return " ".join(text.split())


def answer_uniqueness_rate(answers: list[str]) -> float:
    if not answers:
        return 0.0
    normalized = {_normalize_answer(answer) for answer in answers}
    return len(normalized) / len(answers)
