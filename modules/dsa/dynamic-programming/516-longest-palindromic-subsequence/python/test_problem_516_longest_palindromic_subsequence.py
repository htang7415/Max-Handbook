from problem_516_longest_palindromic_subsequence import Solution


def test_lps_example():
    assert Solution().longestPalindromeSubseq("bbbab") == 4


def test_lps_edge_empty():
    assert Solution().longestPalindromeSubseq("") == 0


def test_lps_tricky_mixed_characters():
    assert Solution().longestPalindromeSubseq("agbdba") == 5
