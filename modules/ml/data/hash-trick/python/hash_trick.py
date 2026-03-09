from __future__ import annotations

import hashlib


def _stable_bucket(token: str, num_buckets: int) -> int:
    digest = hashlib.md5(token.encode("utf-8")).digest()
    return int.from_bytes(digest[:8], byteorder="big") % num_buckets


def hashed_feature_counts(tokens: list[str], num_buckets: int) -> list[int]:
    if num_buckets <= 0:
        raise ValueError("num_buckets must be positive")

    counts = [0] * num_buckets
    for token in tokens:
        counts[_stable_bucket(token, num_buckets)] += 1
    return counts
