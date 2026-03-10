from __future__ import annotations

import math


def quantize_fp(x: float, mantissa_bits: int) -> float:
    if x == 0.0:
        return 0.0
    exponent = int(math.floor(math.log2(abs(x))))
    scale = 2 ** (mantissa_bits - exponent)
    return round(x * scale) / scale


def quantize_int(x: float, bits: int, scale: float) -> int:
    qmax = 2 ** (bits - 1) - 1
    quantized = int(round(x / scale))
    return max(-qmax, min(qmax, quantized))
