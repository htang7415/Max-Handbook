from __future__ import annotations


def bucketize(values: list[float], boundaries: list[float]) -> list[int]:
    if any(boundaries[index] > boundaries[index + 1] for index in range(len(boundaries) - 1)):
        raise ValueError("boundaries must be sorted in nondecreasing order")

    bucket_indices: list[int] = []
    for value in values:
        bucket = len(boundaries)
        for index, boundary in enumerate(boundaries):
            if value < boundary:
                bucket = index
                break
        bucket_indices.append(bucket)
    return bucket_indices
