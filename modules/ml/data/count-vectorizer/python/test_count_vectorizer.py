import pytest

from count_vectorizer import count_vector


def test_count_vector_counts_tokens_in_vocabulary_order() -> None:
    vector = count_vector(tokens=["cat", "dog", "cat", "bird"], vocabulary=["bird", "cat", "dog"])

    assert vector == [1, 2, 1]


def test_count_vector_ignores_out_of_vocabulary_tokens() -> None:
    vector = count_vector(tokens=["cat", "fox"], vocabulary=["cat"])

    assert vector == [1]


def test_count_vector_requires_unique_vocabulary_terms() -> None:
    with pytest.raises(ValueError, match="unique"):
        count_vector(tokens=["cat"], vocabulary=["cat", "cat"])
