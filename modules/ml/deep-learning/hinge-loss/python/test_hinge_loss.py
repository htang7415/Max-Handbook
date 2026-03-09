import pytest

from hinge_loss import hinge_loss


def test_hinge_loss():
    assert hinge_loss(2.0, 1) == 0.0
    assert hinge_loss(0.2, 1) == 0.8


def test_hinge_loss_penalizes_wrong_sign():
    assert hinge_loss(-0.5, 1) == 1.5


def test_hinge_loss_rejects_invalid_label():
    with pytest.raises(ValueError, match="either -1 or 1"):
        hinge_loss(1.0, 0)
