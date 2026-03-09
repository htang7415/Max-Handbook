from elbo import elbo


def test_elbo():
    assert elbo(2.0, 0.5) == 1.5


def test_elbo_increases_with_better_reconstruction():
    assert elbo(3.0, 0.5) > elbo(2.0, 0.5)
