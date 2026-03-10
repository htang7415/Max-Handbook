from __future__ import annotations

import math


def build_vocab(texts: list[str]) -> dict[str, int]:
    vocab: dict[str, int] = {}
    for text in texts:
        for token in text.lower().split():
            if token not in vocab:
                vocab[token] = len(vocab)
    return vocab


def tokenize(text: str, vocab: dict[str, int]) -> list[int]:
    return [vocab[token] for token in text.lower().split() if token in vocab]


def _greedy_subword_count(word: str, subword_vocab: set[str]) -> int:
    count = 0
    position = 0
    while position < len(word):
        longest = ""
        for token in subword_vocab:
            if word.startswith(token, position) and len(token) > len(longest):
                longest = token
        if longest:
            position += len(longest)
        else:
            position += 1
        count += 1
    return count


def compare_token_counts(text: str, subword_vocab: set[str]) -> tuple[int, int]:
    words = text.lower().split()
    word_count = len(words)
    subword_count = sum(_greedy_subword_count(word, subword_vocab) for word in words)
    return word_count, subword_count


def embed(tokens: list[int], embeddings: list[list[float]]) -> list[list[float]]:
    return [embeddings[index] for index in tokens]


def sinusoidal_position(pos: int, d_model: int) -> list[float]:
    values = []
    for i in range(d_model):
        angle = pos / (10000 ** (2 * (i // 2) / d_model))
        if i % 2 == 0:
            values.append(math.sin(angle))
        else:
            values.append(math.cos(angle))
    return values


def add_position_embedding(token_embedding: list[float], position_encoding: list[float]) -> list[float]:
    if len(token_embedding) != len(position_encoding):
        raise ValueError("token_embedding and position_encoding must have the same length")
    return [token_value + position_value for token_value, position_value in zip(token_embedding, position_encoding)]
