from problem_1_two_sum import two_sum


def test_two_sum_example():
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]


def test_two_sum_edge_duplicates():
    assert sorted(two_sum([3, 3], 6)) == [0, 1]


def test_two_sum_tricky_negative_values():
    assert sorted(two_sum([-3, 4, 3, 90], 0)) == [0, 2]
