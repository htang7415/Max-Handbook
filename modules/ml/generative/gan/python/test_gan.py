import pytest

from gan import gan_loss


def test_gan_loss():
    assert gan_loss(0.9, 0.1) < gan_loss(0.6, 0.4)


def test_gan_loss_rejects_invalid_probabilities():
    with pytest.raises(ValueError, match="strictly between 0 and 1"):
        gan_loss(1.0, 0.1)
