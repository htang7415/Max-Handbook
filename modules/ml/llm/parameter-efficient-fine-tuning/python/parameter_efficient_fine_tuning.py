from __future__ import annotations


def _matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    out = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            row.append(sum(a[i][k] * b[k][j] for k in range(len(b))))
        out.append(row)
    return out


def lora_update(w: list[list[float]], a: list[list[float]], b: list[list[float]], alpha: float) -> list[list[float]]:
    rank = len(b)
    delta = _matmul(a, b)
    scale = alpha / rank
    return [[w[i][j] + scale * delta[i][j] for j in range(len(w[0]))] for i in range(len(w))]


def _quantize(w: list[list[float]], scale: float) -> list[list[float]]:
    return [[round(value / scale) * scale for value in row] for row in w]


def qlora_update(w: list[list[float]], a: list[list[float]], b: list[list[float]], alpha: float, scale: float) -> list[list[float]]:
    w_q = _quantize(w, scale)
    rank = len(b)
    delta = _matmul(a, b)
    factor = alpha / rank
    return [[w_q[i][j] + factor * delta[i][j] for j in range(len(w_q[0]))] for i in range(len(w_q))]
