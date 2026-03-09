from problem_112_path_sum import Solution, TreeNode


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


def test_path_sum_example():
    root = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    assert Solution().hasPathSum(root, 22) is True


def test_path_sum_edge_empty():
    assert Solution().hasPathSum(None, 0) is False


def test_path_sum_tricky_leaf_required():
    root = build_tree([1, 2, 3])
    assert Solution().hasPathSum(root, 1) is False
