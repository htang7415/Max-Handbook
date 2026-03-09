from problem_392_is_subsequence import Solution


def test_is_subsequence_example():
    assert Solution().isSubsequence("abc", "ahbgdc") is True


def test_is_subsequence_edge_empty_s():
    assert Solution().isSubsequence("", "ahbgdc") is True


def test_is_subsequence_tricky_repeated_need():
    assert Solution().isSubsequence("axc", "ahbgdc") is False
