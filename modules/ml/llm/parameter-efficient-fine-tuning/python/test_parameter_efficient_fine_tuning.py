from __future__ import annotations

from parameter_efficient_fine_tuning import lora_update, qlora_update


def test_lora_update_changes_base_weight() -> None:
    w = [[1.0, 0.0], [0.0, 1.0]]
    a = [[1.0], [0.0]]
    b = [[2.0, 0.0]]
    out = lora_update(w, a, b, alpha=1.0)
    assert out[0][0] > 1.0


def test_qlora_update_uses_quantized_base_plus_low_rank_delta() -> None:
    w = [[1.05, 0.0], [0.0, 1.0]]
    a = [[1.0], [0.0]]
    b = [[2.0, 0.0]]
    out = qlora_update(w, a, b, alpha=1.0, scale=0.1)
    assert out[0][0] > 1.0
