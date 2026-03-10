from __future__ import annotations


def discounted_return(rewards: list[float], gamma: float) -> float:
    if not 0.0 <= gamma <= 1.0:
        raise ValueError("gamma must satisfy 0 <= gamma <= 1")
    total = 0.0
    for step, reward in enumerate(rewards):
        total += (gamma ** step) * reward
    return total


def n_step_return(rewards: list[float], gamma: float, bootstrap_value: float = 0.0) -> float:
    if not 0.0 <= gamma <= 1.0:
        raise ValueError("gamma must satisfy 0 <= gamma <= 1")

    total = discounted_return(rewards, gamma)
    return total + (gamma ** len(rewards)) * bootstrap_value


def n_step_td_target(rewards: list[float], bootstrap_value: float, gamma: float) -> float:
    return n_step_return(rewards=rewards, gamma=gamma, bootstrap_value=bootstrap_value)


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


def first_visit_returns(states: list[str], rewards: list[float], gamma: float) -> dict[str, float]:
    if len(states) != len(rewards):
        raise ValueError("states and rewards must have the same length")
    if not 0.0 <= gamma <= 1.0:
        raise ValueError("gamma must satisfy 0 <= gamma <= 1")

    returns: dict[str, float] = {}
    running_return = 0.0

    for timestep in range(len(states) - 1, -1, -1):
        running_return = rewards[timestep] + gamma * running_return
        if states[timestep] not in states[:timestep]:
            returns[states[timestep]] = running_return

    return returns
