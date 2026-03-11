from __future__ import annotations

import math

import numpy as np


def _validate_matrix(a: list[list[float]], name: str) -> None:
    if not a or not a[0]:
        raise ValueError(f"{name} must be non-empty")
    width = len(a[0])
    if any(len(row) != width for row in a):
        raise ValueError(f"{name} must be rectangular")


def _softmax_row(row: list[float]) -> list[float]:
    maximum = max(row)
    exps = [math.exp(x - maximum) for x in row]
    total = sum(exps)
    return [value / total for value in exps]


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


def scaled_dot_product_scores(q: list[list[float]], k: list[list[float]]) -> list[list[float]]:
    _validate_matrix(q, "q")
    _validate_matrix(k, "k")
    if len(q) != len(k):
        raise ValueError("q and k must have the same sequence length")
    if len(q[0]) != len(k[0]):
        raise ValueError("q and k must have the same feature dimension")

    dk = len(k[0])
    scores = _matmul(q, _transpose(k))
    return [[value / math.sqrt(dk) for value in row] for row in scores]


def attention_weights(q: list[list[float]], k: list[list[float]]) -> list[list[float]]:
    return [_softmax_row(row) for row in scaled_dot_product_scores(q, k)]


def self_attention(q: list[list[float]], k: list[list[float]], v: list[list[float]]) -> list[list[float]]:
    _validate_matrix(v, "v")
    if len(q) != len(v) or len(k) != len(v):
        raise ValueError("q, k, and v must have the same sequence length")
    weights = attention_weights(q, k)
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
    for head in range(heads):
        start = head * head_dim
        stop = (head + 1) * head_dim
        q_head = [row[start:stop] for row in q]
        k_head = [row[start:stop] for row in k]
        v_head = [row[start:stop] for row in v]
        outputs.append(self_attention(q_head, k_head, v_head))

    merged = []
    for index in range(len(q)):
        row = []
        for head in range(heads):
            row.extend(outputs[head][index])
        merged.append(row)
    return merged


def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    if x.size == 0:
        raise ValueError("x must be non-empty")
    x_max = np.max(x, axis=axis, keepdims=True)
    exps = np.exp(x - x_max)
    return exps / np.sum(exps, axis=axis, keepdims=True)


def causal_mask(seq_len: int) -> np.ndarray:
    if seq_len <= 0:
        raise ValueError("seq_len must be positive")
    mask = np.zeros((seq_len, seq_len))
    mask[np.triu_indices(seq_len, k=1)] = -np.inf
    return mask


def causal_self_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray) -> np.ndarray:
    if Q.ndim != 2 or K.ndim != 2 or V.ndim != 2:
        raise ValueError("Q, K, and V must be rank-2 matrices")
    if Q.shape != K.shape:
        raise ValueError("Q and K must have the same shape")
    if Q.shape[0] != V.shape[0]:
        raise ValueError("Q, K, and V must have the same sequence length")
    if Q.shape[1] == 0 or V.shape[1] == 0:
        raise ValueError("Q, K, and V must have non-zero feature dimension")
    seq_len, d_k = Q.shape
    scores = Q @ K.T / np.sqrt(d_k)
    scores = scores + causal_mask(seq_len)
    weights = softmax(scores, axis=-1)
    return weights @ V


def window_mask(seq_len: int, window: int) -> list[list[int]]:
    if seq_len <= 0:
        raise ValueError("seq_len must be positive")
    if window < 0:
        raise ValueError("window must be non-negative")
    mask = [[0 for _ in range(seq_len)] for _ in range(seq_len)]
    for i in range(seq_len):
        for j in range(seq_len):
            if abs(i - j) <= window:
                mask[i][j] = 1
    return mask
