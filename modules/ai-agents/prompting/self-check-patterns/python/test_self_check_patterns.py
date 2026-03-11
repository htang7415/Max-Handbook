from __future__ import annotations

import pytest

from self_check_patterns import self_check_checklist, self_check_notes, self_check_pass


def test_self_check_patterns_build_notes_and_pass_flag() -> None:
    checklist = self_check_checklist(["answer in bullets", "cite sources", ""])
    assert checklist == ["answer in bullets", "cite sources"]
    notes = self_check_notes({"bullets": True, "citations": False})
    assert notes == ["bullets: ok", "citations: fix"]
    assert self_check_pass({"bullets": True, "citations": True}) is True
    assert self_check_pass({"bullets": True, "citations": False}) is False


def test_self_check_patterns_validation() -> None:
    with pytest.raises(ValueError):
        self_check_pass({"": True})
