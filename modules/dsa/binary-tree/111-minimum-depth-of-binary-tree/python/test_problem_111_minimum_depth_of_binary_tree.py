from problem_111_minimum_depth_of_binary_tree import Solution, TreeNode


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


def test_min_depth_example():
    root = build_tree([3, 9, 20, None, None, 15, 7])
    assert Solution().minDepth(root) == 2


def test_min_depth_edge_single():
    root = build_tree([1])
    assert Solution().minDepth(root) == 1


def test_min_depth_tricky_one_sided():
    root = build_tree([2, None, 3, None, 4, None, 5, None, 6])
    assert Solution().minDepth(root) == 5
