from __future__ import annotations

import re
import string


def _normalize_answer(text: str) -> str:
    text = text.lower()
    text = "".join(character for character in text if character not in string.punctuation)
    text = re.sub(r"\b(a|an|the)\b", " ", text)
    return " ".join(text.split())


def _parse_number(text: str) -> float | None:
    normalized = text.strip().replace(",", "")
    try:
        return float(normalized)
    except ValueError:
        return None


def verify_answer(prediction: str, references: list[str], numeric_tolerance: float = 1.0e-6) -> bool:
    if numeric_tolerance < 0.0:
        raise ValueError("numeric_tolerance must be non-negative")
    if not references:
        return False

    normalized_prediction = _normalize_answer(prediction)
    numeric_prediction = _parse_number(prediction)

    for reference in references:
        if normalized_prediction == _normalize_answer(reference):
            return True

        numeric_reference = _parse_number(reference)
        if numeric_prediction is not None and numeric_reference is not None:
            if abs(numeric_prediction - numeric_reference) <= numeric_tolerance:
                return True

    return False
