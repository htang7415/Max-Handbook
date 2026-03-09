from __future__ import annotations


def td_lambda_returns(
    rewards: list[float],
    next_state_values: list[float],
    gamma: float,
    lam: float,
    terminal_value: float = 0.0,
) -> list[float]:
    if len(rewards) != len(next_state_values):
        raise ValueError("rewards and next_state_values must have the same length")
    if not 0.0 <= gamma <= 1.0:
        raise ValueError("gamma must satisfy 0 <= gamma <= 1")
    if not 0.0 <= lam <= 1.0:
        raise ValueError("lam must satisfy 0 <= lam <= 1")

    lambda_returns = [0.0] * len(rewards)
    future_return = terminal_value

    for index in range(len(rewards) - 1, -1, -1):
        bootstrap = next_state_values[index]
        future_return = rewards[index] + gamma * ((1.0 - lam) * bootstrap + lam * future_return)
        lambda_returns[index] = future_return

    return lambda_returns
