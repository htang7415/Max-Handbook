from __future__ import annotations


def reward_scale(rewards: list[float]) -> float:
    if not rewards:
        return 0.0
    return sum(abs(reward) for reward in rewards) / len(rewards)
