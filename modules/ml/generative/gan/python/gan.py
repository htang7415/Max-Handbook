import math


def gan_loss(d_real: float, d_fake: float) -> float:
    if not 0.0 < d_real < 1.0:
        raise ValueError("d_real must be strictly between 0 and 1")
    if not 0.0 < d_fake < 1.0:
        raise ValueError("d_fake must be strictly between 0 and 1")

    return -math.log(d_real) - math.log(1 - d_fake)
