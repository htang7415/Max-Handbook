from remove_element import Solution


def test_remove_element_example():
    nums = [3, 2, 2, 3]
    k = Solution().removeElement(nums, 3)
    assert k == 2
    assert sorted(nums[:k]) == [2, 2]


def test_remove_element_edge_no_match():
    nums = [1, 2, 3]
    k = Solution().removeElement(nums, 4)
    assert k == 3
    assert sorted(nums[:k]) == [1, 2, 3]


def test_remove_element_tricky_all_removed():
    nums = [2, 2, 2]
    k = Solution().removeElement(nums, 2)
    assert k == 0
    assert nums[:k] == []
