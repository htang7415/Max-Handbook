from __future__ import annotations


def few_shot_block(pairs: list[tuple[str, str]]) -> str:
    blocks: list[str] = []
    for question, answer in pairs:
        q = question.strip()
        a = answer.strip()
        if not q or not a:
            continue
        blocks.append(f"Input: {q}\nOutput: {a}")
    return "\n\n".join(blocks)


def wrap_section(label: str, content: str) -> str:
    clean_label = label.strip()
    clean_content = content.strip()
    if not clean_label:
        raise ValueError("label must be non-empty")
    return f"<<<{clean_label}>>>\n{clean_content}\n<<<END {clean_label}>>>"


def compose_prompt_sections(sections: list[str]) -> str:
    cleaned = [section.strip() for section in sections if section.strip()]
    return "\n\n".join(cleaned)
