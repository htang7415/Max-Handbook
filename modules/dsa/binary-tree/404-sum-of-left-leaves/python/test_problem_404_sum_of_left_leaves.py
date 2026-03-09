from problem_404_sum_of_left_leaves import Solution, TreeNode


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


def test_sum_left_leaves_example():
    root = build_tree([3, 9, 20, None, None, 15, 7])
    assert Solution().sumOfLeftLeaves(root) == 24


def test_sum_left_leaves_edge_single():
    root = build_tree([1])
    assert Solution().sumOfLeftLeaves(root) == 0


def test_sum_left_leaves_tricky_right_only():
    root = build_tree([1, None, 2, None, 3])
    assert Solution().sumOfLeftLeaves(root) == 0
