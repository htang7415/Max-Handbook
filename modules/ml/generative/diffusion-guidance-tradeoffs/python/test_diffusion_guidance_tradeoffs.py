from diffusion_guidance_tradeoffs import guided_step


def test_guided_step():
    assert guided_step(0.0, 1.0, 0.5) == 0.5


def test_guided_step_endpoints():
    assert guided_step(0.2, 0.8, 0.0) == 0.2
    assert guided_step(0.2, 0.8, 1.0) == 0.8
