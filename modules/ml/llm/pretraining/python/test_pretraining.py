import pytest

from pretraining import next_token_loss, token_nlls


def test_next_token_loss():
    logits = [[2.0, 0.0], [0.0, 2.0]]
    loss = next_token_loss(logits, [0, 1])
    assert loss < 0.2


def test_token_nlls_return_one_loss_per_position() -> None:
    losses = token_nlls([[2.0, 0.0], [0.0, 2.0]], [0, 1])
    assert len(losses) == 2
    assert losses[0] == pytest.approx(losses[1])


def test_token_nlls_validate_shape_and_targets() -> None:
    with pytest.raises(ValueError, match="same length"):
        token_nlls([[1.0, 0.0]], [0, 1])
    with pytest.raises(ValueError, match="within the logit row"):
        token_nlls([[1.0, 0.0]], [2])
