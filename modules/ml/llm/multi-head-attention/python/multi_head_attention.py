from __future__ import annotations

import math


def _validate_matrix(a: list[list[float]], name: str) -> None:
    if not a or not a[0]:
        raise ValueError(f"{name} must be non-empty")
    width = len(a[0])
    if any(len(row) != width for row in a):
        raise ValueError(f"{name} must be rectangular")


def _softmax(row: list[float]) -> list[float]:
    m = max(row)
    exps = [math.exp(x - m) for x in row]
    s = sum(exps)
    return [e / s for e in exps]


def _matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    out = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            row.append(sum(a[i][k] * b[k][j] for k in range(len(b))))
        out.append(row)
    return out


def _transpose(a: list[list[float]]) -> list[list[float]]:
    return [list(col) for col in zip(*a)]


def _attention(q: list[list[float]], k: list[list[float]], v: list[list[float]]) -> list[list[float]]:
    dk = len(k[0])
    scores = _matmul(q, _transpose(k))
    scaled = [[val / math.sqrt(dk) for val in row] for row in scores]
    weights = [_softmax(row) for row in scaled]
    return _matmul(weights, v)


def multi_head_attention(q: list[list[float]], k: list[list[float]], v: list[list[float]], heads: int) -> list[list[float]]:
    _validate_matrix(q, "q")
    _validate_matrix(k, "k")
    _validate_matrix(v, "v")
    if heads <= 0:
        raise ValueError("heads must be positive")
    if len(q) != len(k) or len(k) != len(v):
        raise ValueError("q, k, and v must have the same sequence length")
    if len(q[0]) != len(k[0]) or len(k[0]) != len(v[0]):
        raise ValueError("q, k, and v must share the same model dimension")

    d_model = len(q[0])
    if d_model % heads != 0:
        raise ValueError("model dimension must be divisible by heads")

    head_dim = d_model // heads
    outputs = []
    for h in range(heads):
        q_h = [row[h * head_dim:(h + 1) * head_dim] for row in q]
        k_h = [row[h * head_dim:(h + 1) * head_dim] for row in k]
        v_h = [row[h * head_dim:(h + 1) * head_dim] for row in v]
        outputs.append(_attention(q_h, k_h, v_h))
    merged = []
    for i in range(len(q)):
        merged_row = []
        for h in range(heads):
            merged_row.extend(outputs[h][i])
        merged.append(merged_row)
    return merged
