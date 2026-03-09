from problem_131_palindrome_partitioning import Solution


def test_partition_example():
    result = Solution().partition("aab")
    assert sorted(result) == [["a", "a", "b"], ["aa", "b"]]


def test_partition_edge_empty():
    assert Solution().partition("") == [[]]


def test_partition_tricky_all_same():
    result = Solution().partition("aaa")
    assert sorted(result) == [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]
