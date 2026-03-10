from __future__ import annotations


def bootstrap_target(reward: float, gamma: float, next_value: float, done: bool = False) -> float:
    if not 0.0 <= gamma <= 1.0:
        raise ValueError("gamma must satisfy 0 <= gamma <= 1")
    if done:
        return reward
    return reward + gamma * next_value


def q_learning_target(reward: float, gamma: float, next_q_values: list[float], done: bool = False) -> float:
    if done:
        return bootstrap_target(reward, gamma, next_value=0.0, done=True)
    if not next_q_values:
        raise ValueError("next_q_values must be non-empty")
    return bootstrap_target(reward, gamma, next_value=max(next_q_values))


def sarsa_target(reward: float, gamma: float, next_q: float, done: bool = False) -> float:
    return bootstrap_target(reward, gamma, next_value=next_q, done=done)


def expected_sarsa_target(
    reward: float,
    gamma: float,
    next_action_probs: list[float],
    next_q_values: list[float],
    done: bool = False,
) -> float:
    if done:
        return bootstrap_target(reward, gamma, next_value=0.0, done=True)
    if len(next_action_probs) != len(next_q_values):
        raise ValueError("next_action_probs and next_q_values must have the same length")
    if not next_action_probs:
        raise ValueError("next_action_probs and next_q_values must be non-empty")
    if any(probability < 0.0 for probability in next_action_probs):
        raise ValueError("next_action_probs must be non-negative")
    if abs(sum(next_action_probs) - 1.0) > 1e-9:
        raise ValueError("next_action_probs must sum to 1")

    expected_next_value = sum(probability * q_value for probability, q_value in zip(next_action_probs, next_q_values))
    return bootstrap_target(reward, gamma, next_value=expected_next_value)


def double_q_target(
    reward: float,
    gamma: float,
    selector_values: list[float],
    evaluator_values: list[float],
    done: bool = False,
) -> float:
    if done:
        return bootstrap_target(reward, gamma, next_value=0.0, done=True)
    if len(selector_values) != len(evaluator_values):
        raise ValueError("selector_values and evaluator_values must have the same length")
    if not selector_values:
        raise ValueError("selector_values and evaluator_values must be non-empty")

    best_action = max(range(len(selector_values)), key=selector_values.__getitem__)
    return bootstrap_target(reward, gamma, next_value=evaluator_values[best_action])


def td_error(value: float, target: float) -> float:
    return target - value


def td_update(value: float, target: float, alpha: float) -> float:
    if not 0.0 <= alpha <= 1.0:
        raise ValueError("alpha must satisfy 0 <= alpha <= 1")
    return value + alpha * td_error(value=value, target=target)


def soft_target_update(target_values: list[float], online_values: list[float], tau: float) -> list[float]:
    if len(target_values) != len(online_values):
        raise ValueError("target_values and online_values must have the same length")
    if not 0.0 <= tau <= 1.0:
        raise ValueError("tau must satisfy 0 <= tau <= 1")

    return [
        (1.0 - tau) * target_value + tau * online_value
        for target_value, online_value in zip(target_values, online_values)
    ]


def soft_update_gap(target_values: list[float], online_values: list[float], tau: float) -> float:
    if len(target_values) != len(online_values):
        raise ValueError("target_values and online_values must have the same length")
    if not 0.0 <= tau <= 1.0:
        raise ValueError("tau must satisfy 0 <= tau <= 1")
    if not target_values:
        return 0.0

    updated = soft_target_update(target_values, online_values, tau)
    gaps = [abs(online_value - updated_value) for online_value, updated_value in zip(online_values, updated)]
    return sum(gaps) / len(gaps)
