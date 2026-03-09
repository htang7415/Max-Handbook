from problem_56_merge_intervals import Solution


def test_merge_intervals_example():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    assert Solution().merge(intervals) == [[1, 6], [8, 10], [15, 18]]


def test_merge_intervals_edge_empty():
    assert Solution().merge([]) == []


def test_merge_intervals_tricky_touching():
    intervals = [[1, 4], [4, 5]]
    assert Solution().merge(intervals) == [[1, 5]]
