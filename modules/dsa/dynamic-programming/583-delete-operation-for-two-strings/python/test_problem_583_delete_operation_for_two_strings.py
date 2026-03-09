from problem_583_delete_operation_for_two_strings import Solution


def test_delete_operation_example():
    assert Solution().minDistance("sea", "eat") == 2


def test_delete_operation_edge_empty():
    assert Solution().minDistance("", "abc") == 3


def test_delete_operation_tricky_longer():
    assert Solution().minDistance("leetcode", "etco") == 4
