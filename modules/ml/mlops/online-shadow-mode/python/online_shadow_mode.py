from __future__ import annotations


def shadow_disagreement_rate(
    live_predictions: list[object],
    shadow_predictions: list[object],
) -> tuple[int, float]:
    if len(live_predictions) != len(shadow_predictions):
        raise ValueError("live_predictions and shadow_predictions must have the same length")
    if not live_predictions:
        return 0, 0.0

    disagreements = sum(live != shadow for live, shadow in zip(live_predictions, shadow_predictions))
    return disagreements, disagreements / len(live_predictions)
