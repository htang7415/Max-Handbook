from __future__ import annotations

import json


Fingerprint = tuple[str, str, tuple[tuple[str, str], ...]]


def request_fingerprint(
    method: str,
    path: str,
    body: dict[str, object],
) -> Fingerprint:
    normalized_method = method.strip().upper()
    normalized_path = path.strip()
    if not normalized_method:
        raise ValueError("method must be non-empty")
    if not normalized_path.startswith("/"):
        raise ValueError("path must start with '/'")

    serialized_items = tuple(
        (key, json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True))
        for key, value in sorted(body.items())
    )
    return (normalized_method, normalized_path, serialized_items)


def idempotency_decision(
    idempotency_key: str,
    fingerprint: Fingerprint,
    stored_record: dict[str, object] | None,
) -> str:
    cleaned_key = idempotency_key.strip()
    if not cleaned_key:
        raise ValueError("idempotency_key must be non-empty")

    if stored_record is None:
        return "execute"
    if stored_record.get("key") != cleaned_key:
        raise ValueError("stored_record key does not match idempotency_key")
    if stored_record.get("fingerprint") == fingerprint:
        return "replay"
    return "conflict"


def store_response(
    idempotency_key: str,
    fingerprint: Fingerprint,
    status_code: int,
    response_body: dict[str, object],
) -> dict[str, object]:
    if not 200 <= status_code < 600:
        raise ValueError("status_code must be between 200 and 599")

    decision = idempotency_decision(idempotency_key, fingerprint, stored_record=None)
    if decision != "execute":
        raise ValueError("new idempotency record must be executable")

    return {
        "key": idempotency_key.strip(),
        "fingerprint": fingerprint,
        "status_code": status_code,
        "response_body": dict(response_body),
    }
