from __future__ import annotations


def prune_rare_tokens(tokens: list[str], min_count: int, unk_token: str = "__UNK__") -> list[str]:
    if min_count <= 0:
        raise ValueError("min_count must be positive")

    counts: dict[str, int] = {}
    for token in tokens:
        counts[token] = counts.get(token, 0) + 1

    return [token if counts[token] >= min_count else unk_token for token in tokens]
