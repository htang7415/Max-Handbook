from vae import elbo


def test_elbo():
    assert elbo(2.0, 0.5) == 1.5


def test_elbo_decreases_as_kl_penalty_grows():
    assert elbo(2.0, 0.2) > elbo(2.0, 0.8)
