from problem_718_maximum_length_of_repeated_subarray import Solution


def test_repeated_subarray_example():
    assert Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3


def test_repeated_subarray_edge_empty():
    assert Solution().findLength([], [1, 2, 3]) == 0


def test_repeated_subarray_tricky_all_equal():
    assert Solution().findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]) == 5
