from __future__ import annotations


def clip_rewards(rewards: list[float], min_reward: float = -1.0, max_reward: float = 1.0) -> list[float]:
    if min_reward > max_reward:
        raise ValueError("min_reward cannot exceed max_reward")

    return [min(max(reward, min_reward), max_reward) for reward in rewards]
