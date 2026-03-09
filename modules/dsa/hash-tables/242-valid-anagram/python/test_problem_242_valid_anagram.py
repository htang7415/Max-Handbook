from problem_242_valid_anagram import is_anagram


def test_is_anagram_example():
    assert is_anagram("anagram", "nagaram") is True


def test_is_anagram_edge_empty_strings():
    assert is_anagram("", "") is True


def test_is_anagram_tricky_repeated_counts():
    assert is_anagram("rat", "car") is False
