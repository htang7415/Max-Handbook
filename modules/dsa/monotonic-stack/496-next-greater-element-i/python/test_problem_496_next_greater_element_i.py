from problem_496_next_greater_element_i import Solution


def test_next_greater_element_example():
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    assert Solution().nextGreaterElement(nums1, nums2) == [-1, 3, -1]


def test_next_greater_element_edge_single_query():
    assert Solution().nextGreaterElement([4], [1, 2, 3, 4]) == [-1]


def test_next_greater_element_tricky_multiple_queries():
    nums1 = [2, 1, 3]
    nums2 = [2, 3, 1, 4]
    assert Solution().nextGreaterElement(nums1, nums2) == [3, 4, 4]
