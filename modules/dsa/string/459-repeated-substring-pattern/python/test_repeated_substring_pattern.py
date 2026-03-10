from repeated_substring_pattern import Solution


def test_repeat_example():
    assert Solution().repeatedSubstringPattern("abab") is True


def test_repeat_edge_single_character():
    assert Solution().repeatedSubstringPattern("a") is False


def test_repeat_tricky_uniform_string():
    assert Solution().repeatedSubstringPattern("aaaa") is True


def test_repeat_tricky_prefix_suffix_without_full_period():
    assert Solution().repeatedSubstringPattern("abcabcab") is False
