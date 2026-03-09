from problem_98_validate_binary_search_tree import Solution, TreeNode


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


def test_valid_bst_example():
    root = build_tree([2, 1, 3])
    assert Solution().isValidBST(root) is True


def test_valid_bst_edge_empty():
    assert Solution().isValidBST(None) is True


def test_valid_bst_tricky_global_violation():
    root = build_tree([5, 1, 4, None, None, 3, 6])
    assert Solution().isValidBST(root) is False
