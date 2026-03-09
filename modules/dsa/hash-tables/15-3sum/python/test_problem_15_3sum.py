from problem_15_3sum import three_sum


def test_three_sum_example():
    result = three_sum([-1, 0, 1, 2, -1, -4])
    assert sorted([sorted(triplet) for triplet in result]) == [
        [-1, -1, 2],
        [-1, 0, 1],
    ]


def test_three_sum_edge_no_solution():
    assert three_sum([1, 2, -2, -1]) == []


def test_three_sum_tricky_deduplicates_triplets():
    assert three_sum([0, 0, 0, 0]) == [[0, 0, 0]]
