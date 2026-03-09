from __future__ import annotations


def isotonic_calibration(scores: list[float], labels: list[int]) -> list[float]:
    if len(scores) != len(labels):
        raise ValueError("scores and labels must have the same length")
    if any(label not in {0, 1} for label in labels):
        raise ValueError("labels must be binary")
    if not scores:
        return []

    order = sorted(range(len(scores)), key=lambda index: scores[index])
    blocks: list[dict[str, object]] = []
    for index in order:
        blocks.append({"indices": [index], "sum": float(labels[index]), "count": 1})
        while len(blocks) >= 2:
            prev = blocks[-2]
            curr = blocks[-1]
            prev_mean = prev["sum"] / prev["count"]
            curr_mean = curr["sum"] / curr["count"]
            if prev_mean <= curr_mean:
                break
            prev["indices"].extend(curr["indices"])
            prev["sum"] += curr["sum"]
            prev["count"] += curr["count"]
            blocks.pop()

    calibrated = [0.0] * len(scores)
    for block in blocks:
        mean_value = block["sum"] / block["count"]
        for index in block["indices"]:
            calibrated[index] = mean_value
    return calibrated
