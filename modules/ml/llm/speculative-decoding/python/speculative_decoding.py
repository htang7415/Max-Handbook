def speculative_decode_step(
    draft_tokens: list[int],
    target_tokens: list[int],
) -> list[int]:
    if not target_tokens:
        raise ValueError("target_tokens must be non-empty")
    if any(token < 0 for token in draft_tokens + target_tokens):
        raise ValueError("token ids must be non-negative")

    accepted = 0
    while (
        accepted < len(draft_tokens)
        and accepted < len(target_tokens)
        and draft_tokens[accepted] == target_tokens[accepted]
    ):
        accepted += 1

    if accepted < len(target_tokens):
        return target_tokens[: accepted + 1]
    return target_tokens[:]
