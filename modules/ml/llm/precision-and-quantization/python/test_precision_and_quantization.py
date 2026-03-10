from __future__ import annotations

from precision_and_quantization import quantize_fp, quantize_int


def test_quantize_fp_rounds_to_coarser_mantissa() -> None:
    out = quantize_fp(1.2345, mantissa_bits=3)
    assert abs(out - 1.25) < 0.1


def test_quantize_int_respects_integer_range() -> None:
    quantized = quantize_int(1.2, bits=4, scale=0.1)
    assert quantized <= 7
