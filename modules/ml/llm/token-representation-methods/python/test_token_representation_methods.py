from __future__ import annotations

import pytest

from token_representation_methods import (
    add_position_embedding,
    build_vocab,
    compare_token_counts,
    embed,
    sinusoidal_position,
    tokenize,
)


def test_tokenize_basic() -> None:
    vocab = build_vocab(["hello world", "hello there"])
    ids = tokenize("hello world", vocab)
    assert ids == [vocab["hello"], vocab["world"]]


def test_compare_token_counts_shows_subword_split() -> None:
    counts = compare_token_counts("playing now", {"play", "ing", "now"})
    assert counts == (2, 3)


def test_compare_token_counts_handles_empty_text() -> None:
    assert compare_token_counts("", {"a"}) == (0, 0)


def test_embed_lookup() -> None:
    table = [[0.0, 0.1], [1.0, 1.1], [2.0, 2.1]]
    out = embed([2, 0], table)
    assert out == [[2.0, 2.1], [0.0, 0.1]]


def test_positional_encoding_shape() -> None:
    vec = sinusoidal_position(3, 6)
    assert len(vec) == 6
    assert vec[0] != vec[1]


def test_add_position_embedding_combines_token_and_position_vectors() -> None:
    out = add_position_embedding([1.0, 2.0], [0.1, -0.2])
    assert out == [1.1, 1.8]


def test_add_position_embedding_requires_same_length() -> None:
    with pytest.raises(ValueError, match="same length"):
        add_position_embedding([1.0], [0.1, 0.2])
