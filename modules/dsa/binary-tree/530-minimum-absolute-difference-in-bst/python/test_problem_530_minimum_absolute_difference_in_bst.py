from problem_530_minimum_absolute_difference_in_bst import Solution, TreeNode


def build_tree(values: list[int | None]) -> TreeNode | None:
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def test_min_diff_example():
    root = build_tree([4, 2, 6, 1, 3])
    assert Solution().getMinimumDifference(root) == 1


def test_min_diff_edge_two_nodes():
    root = build_tree([1, None, 3])
    assert Solution().getMinimumDifference(root) == 2


def test_min_diff_tricky_internal_gap():
    root = build_tree([1, 0, 48, None, None, 12, 49])
    assert Solution().getMinimumDifference(root) == 1
