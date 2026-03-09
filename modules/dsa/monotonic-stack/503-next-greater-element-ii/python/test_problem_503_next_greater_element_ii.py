from problem_503_next_greater_element_ii import Solution


def test_next_greater_elements_example():
    nums = [1, 2, 1]
    assert Solution().nextGreaterElements(nums) == [2, -1, 2]


def test_next_greater_elements_edge_single():
    assert Solution().nextGreaterElements([5]) == [-1]


def test_next_greater_elements_tricky_wrap():
    nums = [1, 2, 3, 4, 3]
    assert Solution().nextGreaterElements(nums) == [2, 3, 4, -1, 4]
