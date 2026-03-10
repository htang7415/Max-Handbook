from __future__ import annotations

import math


def _softmax(row: list[float]) -> list[float]:
    if not row:
        raise ValueError("logit rows must be non-empty")
    m = max(row)
    exps = [math.exp(x - m) for x in row]
    s = sum(exps)
    return [e / s for e in exps]


def token_nlls(logits: list[list[float]], targets: list[int]) -> list[float]:
    if len(logits) != len(targets):
        raise ValueError("logits and targets must have the same length")
    if not logits:
        raise ValueError("logits must be non-empty")

    losses: list[float] = []
    for row, tgt in zip(logits, targets):
        if tgt < 0 or tgt >= len(row):
            raise ValueError("target index must stay within the logit row")
        probs = _softmax(row)
        losses.append(-math.log(probs[tgt]))
    return losses


def next_token_loss(logits: list[list[float]], targets: list[int]) -> float:
    losses = token_nlls(logits, targets)
    return sum(losses) / len(losses)
