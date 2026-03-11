from __future__ import annotations

import math


def _softmax(row: list[float]) -> list[float]:
    if not row:
        raise ValueError("logit rows must be non-empty")
    maximum = max(row)
    exps = [math.exp(value - maximum) for value in row]
    total = sum(exps)
    return [value / total for value in exps]


def sft_loss(logits: list[list[float]], targets: list[int], mask: list[int]) -> float:
    if len(logits) != len(targets) or len(targets) != len(mask):
        raise ValueError("logits, targets, and mask must have the same length")
    total = 0.0
    count = 0
    for row, target, keep in zip(logits, targets, mask):
        if target < 0 or target >= len(row):
            raise ValueError("target index must stay within the logit row")
        if not keep:
            continue
        probs = _softmax(row)
        total += -math.log(probs[target])
        count += 1
    return total / max(count, 1)


def preference_margin(score_chosen: float, score_rejected: float) -> float:
    return score_chosen - score_rejected


def preference_loss(score_chosen: float, score_rejected: float) -> float:
    return math.log1p(math.exp(-preference_margin(score_chosen, score_rejected)))


def dpo_logit(delta_logp: float, delta_logp_ref: float, beta: float = 0.1) -> float:
    if beta < 0.0:
        raise ValueError("beta must be non-negative")
    return beta * (delta_logp - delta_logp_ref)


def dpo_loss(delta_logp: float, delta_logp_ref: float, beta: float = 0.1) -> float:
    diff = dpo_logit(delta_logp, delta_logp_ref, beta=beta)
    return -math.log(1 / (1 + math.exp(-diff)))


def reward_model_loss(chosen: float, rejected: float) -> float:
    diff = chosen - rejected
    return -math.log(1 / (1 + math.exp(-diff)))


def kl_penalty(p: list[float], q: list[float], beta: float) -> float:
    if len(p) != len(q):
        raise ValueError("p and q must have the same length")
    if beta < 0.0:
        raise ValueError("beta must be non-negative")
    kl = 0.0
    for p_i, q_i in zip(p, q):
        if p_i > 0.0 and q_i > 0.0:
            kl += p_i * math.log(p_i / q_i)
    return beta * kl


def anchored_loss(align_loss: float, ptx_loss: float, alpha: float) -> float:
    if not 0.0 <= alpha <= 1.0:
        raise ValueError("alpha must satisfy 0 <= alpha <= 1")
    return (1 - alpha) * align_loss + alpha * ptx_loss
