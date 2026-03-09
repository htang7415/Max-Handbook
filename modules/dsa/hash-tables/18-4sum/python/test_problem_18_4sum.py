from problem_18_4sum import four_sum


def test_four_sum_example():
    result = four_sum([1, 0, -1, 0, -2, 2], 0)
    assert sorted([sorted(quad) for quad in result]) == [
        [-2, -1, 1, 2],
        [-2, 0, 0, 2],
        [-1, 0, 0, 1],
    ]


def test_four_sum_edge_no_solution():
    assert four_sum([2, 2, 2, 2, 2], 9) == []


def test_four_sum_tricky_deduplicates_quadruplets():
    assert four_sum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]
