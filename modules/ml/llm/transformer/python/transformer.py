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


def attention_weights(x: list[list[float]]) -> list[list[float]]:
    _validate_matrix(x, "x")
    dk = len(x[0])
    scores = _matmul(x, _transpose(x))
    scaled = [[val / math.sqrt(dk) for val in row] for row in scores]
    return [_softmax(row) for row in scaled]


def self_attention_output(x: list[list[float]]) -> list[list[float]]:
    weights = attention_weights(x)
    return _matmul(weights, x)


def _relu_row(row: list[float]) -> list[float]:
    return [max(0.0, x) for x in row]


def transformer_block(x: list[list[float]], w1: list[list[float]], w2: list[list[float]]) -> list[list[float]]:
    """Minimal transformer-style block with single-head self-attention.

    This example keeps the structure small for learning:
    self-attention -> residual -> feed-forward -> residual.
    It does not implement Q/K/V projections, masking, or layer normalization.
    """
    _validate_matrix(x, "x")
    _validate_matrix(w1, "w1")
    _validate_matrix(w2, "w2")

    d_model = len(x[0])
    hidden_dim = len(w1[0])
    if len(w1) != d_model:
        raise ValueError("w1 rows must match the model dimension")
    if len(w2) != hidden_dim:
        raise ValueError("w2 rows must match the hidden dimension")
    if len(w2[0]) != d_model:
        raise ValueError("w2 output dimension must match the model dimension")

    attn = self_attention_output(x)
    res1 = [[x[i][j] + attn[i][j] for j in range(len(x[0]))] for i in range(len(x))]
    ffn_hidden = _matmul(res1, w1)
    ffn_hidden = [_relu_row(row) for row in ffn_hidden]
    ffn = _matmul(ffn_hidden, w2)
    res2 = [[res1[i][j] + ffn[i][j] for j in range(len(ffn[0]))] for i in range(len(ffn))]
    return res2
