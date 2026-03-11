from __future__ import annotations

import pytest

from examples_and_delimiters import compose_prompt_sections, few_shot_block, wrap_section


def test_examples_and_delimiters_formats_examples_and_sections() -> None:
    block = few_shot_block([("Q1", "A1"), ("Q2", "A2")])
    assert block == "Input: Q1\nOutput: A1\n\nInput: Q2\nOutput: A2"
    section = wrap_section("INPUT", "Summarize this note.")
    assert section == "<<<INPUT>>>\nSummarize this note.\n<<<END INPUT>>>"
    prompt = compose_prompt_sections([block, section])
    assert prompt == (
        "Input: Q1\nOutput: A1\n\nInput: Q2\nOutput: A2\n\n"
        "<<<INPUT>>>\nSummarize this note.\n<<<END INPUT>>>"
    )


def test_examples_and_delimiters_validation() -> None:
    assert few_shot_block([("", "A1"), ("Q2", "")]) == ""
    with pytest.raises(ValueError):
        wrap_section("", "content")
