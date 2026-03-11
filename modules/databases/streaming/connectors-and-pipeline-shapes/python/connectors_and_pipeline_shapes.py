"""connectors_and_pipeline_shapes - validate simple streaming pipeline topologies."""

from __future__ import annotations


def validate_pipeline(
    stages: dict[str, str],
    edges: list[tuple[str, str]],
) -> bool:
    inbound = {name: 0 for name in stages}
    outbound = {name: 0 for name in stages}

    for left, right in edges:
        if left not in stages or right not in stages:
            return False
        inbound[right] += 1
        outbound[left] += 1

    for name, kind in stages.items():
        if kind == "source" and inbound[name] != 0:
            return False
        if kind == "sink" and outbound[name] != 0:
            return False
    return True


def classify_pipeline_shape(
    stages: dict[str, str],
    edges: list[tuple[str, str]],
) -> str:
    if not validate_pipeline(stages, edges):
        return "invalid"

    inbound = {name: 0 for name in stages}
    outbound = {name: 0 for name in stages}
    for left, right in edges:
        outbound[left] += 1
        inbound[right] += 1

    if any(outbound[name] > 1 for name, kind in stages.items() if kind == "source"):
        return "fan-out"
    if any(inbound[name] > 1 for name, kind in stages.items() if kind == "sink"):
        return "fan-in"
    if any(kind == "transform" for kind in stages.values()):
        return "source-transform-sink"
    return "source-to-sink"


def reachable_sinks(
    stages: dict[str, str],
    edges: list[tuple[str, str]],
    source_name: str,
) -> list[str]:
    graph: dict[str, list[str]] = {name: [] for name in stages}
    for left, right in edges:
        graph.setdefault(left, []).append(right)

    seen = {source_name}
    queue = [source_name]
    sinks: set[str] = set()
    while queue:
        current = queue.pop(0)
        if stages.get(current) == "sink":
            sinks.add(current)
        for nxt in graph.get(current, []):
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return sorted(sinks)
