from __future__ import annotations


def silhouette_score(a: float, b: float) -> float:
    if max(a, b) == 0:
        return 0.0
    return (b - a) / max(a, b)


def davies_bouldin_score(s_i: float, s_j: float, d_ij: float) -> float:
    return (s_i + s_j) / d_ij if d_ij > 0 else 0.0


def calinski_harabasz_score(
    between_dispersion: float, within_dispersion: float, clusters: int, samples: int
) -> float:
    if clusters <= 1:
        raise ValueError("clusters must be greater than 1")
    if samples <= clusters:
        raise ValueError("samples must be greater than clusters")
    if within_dispersion == 0:
        return 0.0
    return (between_dispersion / (clusters - 1)) / (within_dispersion / (samples - clusters))
