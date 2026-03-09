import pytest

from diffusion_models import add_noise


def test_add_noise():
    assert abs(add_noise(1.0, 0.0, 1.0) - 1.0) < 1e-6


def test_add_noise_is_pure_noise_when_alpha_zero():
    assert abs(add_noise(1.0, 2.0, 0.0) - 2.0) < 1e-6


def test_add_noise_rejects_invalid_alpha():
    with pytest.raises(ValueError, match="0 <= alpha <= 1"):
        add_noise(1.0, 0.0, 1.2)
