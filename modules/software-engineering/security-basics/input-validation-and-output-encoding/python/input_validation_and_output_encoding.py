from __future__ import annotations

import html


def validate_username(username: str) -> str:
    cleaned = username.strip()
    if not 3 <= len(cleaned) <= 20:
        raise ValueError("username must be between 3 and 20 characters")
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")
    if any(char not in allowed for char in cleaned):
        raise ValueError("username contains invalid characters")
    return cleaned


def html_escape(text: str) -> str:
    return html.escape(text, quote=True)


def render_comment_html(author: str, comment: str) -> str:
    safe_author = validate_username(author)
    safe_comment = html_escape(comment)
    return f"<p><strong>{safe_author}</strong>: {safe_comment}</p>"
