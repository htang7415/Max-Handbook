"""ownership_and_delete_boundaries - deletion rules should follow ownership semantics."""

from __future__ import annotations


def relation(name: str, policy: str) -> dict[str, str]:
    normalized = policy.strip().lower()
    if normalized not in {"cascade", "block", "detach"}:
        raise ValueError(f"unsupported delete policy: {policy}")
    return {"name": name, "policy": normalized}


def delete_plan(parent: str, relations: list[dict[str, str]]) -> dict[str, object]:
    cascades: list[str] = []
    blocks: list[str] = []
    detaches: list[str] = []
    for item in relations:
        policy = str(item["policy"])
        name = str(item["name"])
        if policy == "cascade":
            cascades.append(name)
        elif policy == "block":
            blocks.append(name)
        elif policy == "detach":
            detaches.append(name)
    return {
        "parent": parent,
        "cascade": sorted(cascades),
        "block": sorted(blocks),
        "detach": sorted(detaches),
    }


def can_delete(plan: dict[str, object]) -> bool:
    blocks = plan.get("block", [])
    assert isinstance(blocks, list)
    return len(blocks) == 0
