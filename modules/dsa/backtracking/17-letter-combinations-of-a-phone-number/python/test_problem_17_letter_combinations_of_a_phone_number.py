from problem_17_letter_combinations_of_a_phone_number import Solution


def test_letter_combinations_example():
    result = Solution().letterCombinations("23")
    assert set(result) == {"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"}


def test_letter_combinations_edge_empty():
    assert Solution().letterCombinations("") == []


def test_letter_combinations_tricky_four_letter_digits():
    result = Solution().letterCombinations("79")
    assert len(result) == 16
