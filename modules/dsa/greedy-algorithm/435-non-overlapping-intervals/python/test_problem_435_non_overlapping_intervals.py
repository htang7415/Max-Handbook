from problem_435_non_overlapping_intervals import Solution


def test_non_overlapping_example():
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    assert Solution().eraseOverlapIntervals(intervals) == 1


def test_non_overlapping_edge_empty():
    assert Solution().eraseOverlapIntervals([]) == 0


def test_non_overlapping_tricky_all_overlap():
    intervals = [[1, 2], [1, 2], [1, 2]]
    assert Solution().eraseOverlapIntervals(intervals) == 2
