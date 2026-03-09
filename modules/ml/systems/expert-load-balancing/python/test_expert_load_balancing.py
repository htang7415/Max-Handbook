import pytest

from expert_load_balancing import expert_load_balance_loss


def test_expert_load_balance_loss_is_one_for_balanced_assignments() -> None:
    loss = expert_load_balance_loss(
        router_probs=[[0.8, 0.2], [0.7, 0.3], [0.4, 0.6], [0.3, 0.7]],
        assignments=[0, 0, 1, 1],
    )

    assert loss == pytest.approx(1.0)


def test_expert_load_balance_loss_increases_for_collapsed_routing() -> None:
    loss = expert_load_balance_loss(
        router_probs=[[0.9, 0.1], [0.9, 0.1], [0.9, 0.1], [0.9, 0.1]],
        assignments=[0, 0, 0, 0],
    )

    assert loss == pytest.approx(1.8)


def test_expert_load_balance_loss_requires_matching_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        expert_load_balance_loss([[1.0, 0.0]], [])
