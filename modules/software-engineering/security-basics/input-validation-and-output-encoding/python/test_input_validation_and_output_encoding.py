from __future__ import annotations

import pytest

from input_validation_and_output_encoding import (
    html_escape,
    render_comment_html,
    validate_username,
)


def test_validate_username_accepts_simple_safe_identifiers() -> None:
    assert validate_username("alice_1") == "alice_1"


def test_html_escape_and_render_comment_html_encode_untrusted_text() -> None:
    assert html_escape('<script>alert("x")</script>') == "&lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt;"
    assert render_comment_html("alice_1", "<b>Hello</b>") == (
        "<p><strong>alice_1</strong>: &lt;b&gt;Hello&lt;/b&gt;</p>"
    )


def test_validate_username_rejects_invalid_characters_or_length() -> None:
    with pytest.raises(ValueError):
        validate_username("ab")
    with pytest.raises(ValueError):
        validate_username("alice@example.com")
