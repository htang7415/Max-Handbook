import pytest

from answer_verification import verify_answer


def test_verify_answer_accepts_normalized_text_match() -> None:
    assert verify_answer("The Eiffel Tower!", ["eiffel tower"])


def test_verify_answer_accepts_numeric_match_with_tolerance() -> None:
    assert verify_answer("3.14159", ["3.1416"], numeric_tolerance=1.0e-4)


def test_verify_answer_checks_multiple_references() -> None:
    assert verify_answer("nyc", ["new york", "nyc"])


def test_verify_answer_rejects_mismatch() -> None:
    assert not verify_answer("paris", ["london"])
