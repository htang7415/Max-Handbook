from __future__ import annotations

import math


def _softmax(row: list[float]) -> list[float]:
    maximum = max(row)
    exps = [math.exp(value - maximum) for value in row]
    total = sum(exps)
    return [value / total for value in exps]


def sft_loss(logits: list[list[float]], targets: list[int], mask: list[int]) -> float:
    total = 0.0
    count = 0
    for row, target, keep in zip(logits, targets, mask):
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
    return beta * (delta_logp - delta_logp_ref)


def dpo_loss(delta_logp: float, delta_logp_ref: float, beta: float = 0.1) -> float:
    diff = dpo_logit(delta_logp, delta_logp_ref, beta=beta)
    return -math.log(1 / (1 + math.exp(-diff)))


def reward_model_loss(chosen: float, rejected: float) -> float:
    diff = chosen - rejected
    return -math.log(1 / (1 + math.exp(-diff)))


def kl_penalty(p: list[float], q: list[float], beta: float) -> float:
    kl = 0.0
    for p_i, q_i in zip(p, q):
        if p_i > 0.0 and q_i > 0.0:
            kl += p_i * math.log(p_i / q_i)
    return beta * kl


def anchored_loss(align_loss: float, ptx_loss: float, alpha: float) -> float:
    return (1 - alpha) * align_loss + alpha * ptx_loss
