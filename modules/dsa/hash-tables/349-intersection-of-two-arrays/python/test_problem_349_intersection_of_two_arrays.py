from problem_349_intersection_of_two_arrays import intersection


def test_intersection_example():
    result = intersection([1, 2, 2, 1], [2, 2])
    assert sorted(result) == [2]


def test_intersection_edge_empty():
    assert intersection([], [1, 2]) == []


def test_intersection_tricky_deduplicates():
    result = intersection([4, 9, 5], [9, 4, 9, 8, 4])
    assert sorted(result) == [4, 9]
