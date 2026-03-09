from implement_strstr import Solution


def test_strstr_example():
    assert Solution().strStr("hello", "ll") == 2


def test_strstr_edge_empty_needle():
    assert Solution().strStr("", "") == 0


def test_strstr_tricky_overlapping_match():
    assert Solution().strStr("mississippi", "issi") == 1
