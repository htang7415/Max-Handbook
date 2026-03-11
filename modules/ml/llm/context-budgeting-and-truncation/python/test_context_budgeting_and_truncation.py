from __future__ import annotations

import pytest

from context_budgeting_and_truncation import (
    available_prompt_budget,
    head_tail_keep,
    tokens_to_drop,
    truncation_needed,
)


def test_context_budgeting_helpers_capture_simple_overflow_logic() -> None:
    prompt_budget = available_prompt_budget(8192, 1024)
    assert prompt_budget == 7168
    assert truncation_needed(9600, prompt_budget) is True
    assert tokens_to_drop(9600, prompt_budget) == 2432
    assert head_tail_keep(9600, prompt_budget, 1024) == (1024, 6144)


def test_context_budgeting_validation_rejects_invalid_inputs() -> None:
    with pytest.raises(ValueError):
        available_prompt_budget(100, 100)
    with pytest.raises(ValueError):
        truncation_needed(-1, 10)
    with pytest.raises(ValueError):
        tokens_to_drop(10, 0)
    with pytest.raises(ValueError):
        head_tail_keep(10, 5, -1)
    with pytest.raises(ValueError):
        head_tail_keep(10, 5, 11)
