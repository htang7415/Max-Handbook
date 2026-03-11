from __future__ import annotations

import hashlib
import hmac


def webhook_signature(secret: str, timestamp: int, body: str) -> str:
    cleaned_secret = secret.strip()
    if not cleaned_secret:
        raise ValueError("secret must be non-empty")
    if timestamp < 0:
        raise ValueError("timestamp must be non-negative")
    payload = f"{timestamp}.{body}".encode("utf-8")
    return hmac.new(cleaned_secret.encode("utf-8"), payload, hashlib.sha256).hexdigest()


def webhook_request_valid(
    secret: str,
    timestamp: int,
    body: str,
    provided_signature: str,
    now_timestamp: int,
    max_age_seconds: int = 300,
) -> bool:
    if now_timestamp < timestamp:
        raise ValueError("now_timestamp must be at least timestamp")
    if max_age_seconds <= 0:
        raise ValueError("max_age_seconds must be positive")

    if now_timestamp - timestamp > max_age_seconds:
        return False
    expected = webhook_signature(secret, timestamp, body)
    return hmac.compare_digest(expected, provided_signature.strip())


def webhook_decision(valid_request: bool, event_type: str) -> str:
    cleaned_event_type = event_type.strip()
    if not cleaned_event_type:
        raise ValueError("event_type must be non-empty")
    if not valid_request:
        return "reject"
    return f"process:{cleaned_event_type}"
