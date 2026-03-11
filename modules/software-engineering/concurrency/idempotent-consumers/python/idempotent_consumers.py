from __future__ import annotations


def dedupe_key(message_id: str, consumer_name: str) -> str:
    cleaned_message_id = message_id.strip()
    cleaned_consumer_name = consumer_name.strip()
    if not cleaned_message_id or not cleaned_consumer_name:
        raise ValueError("message_id and consumer_name must be non-empty")
    return f"{cleaned_consumer_name}:{cleaned_message_id}"


def should_process_message(message_id: str, seen_keys: set[str], consumer_name: str) -> bool:
    return dedupe_key(message_id, consumer_name) not in seen_keys


def mark_processed(message_id: str, seen_keys: set[str], consumer_name: str) -> set[str]:
    updated = set(seen_keys)
    updated.add(dedupe_key(message_id, consumer_name))
    return updated
