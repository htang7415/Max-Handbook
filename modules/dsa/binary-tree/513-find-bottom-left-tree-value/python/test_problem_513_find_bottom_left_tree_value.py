from problem_513_find_bottom_left_tree_value import Solution, TreeNode


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


def test_bottom_left_example():
    root = build_tree([2, 1, 3])
    assert Solution().findBottomLeftValue(root) == 1


def test_bottom_left_edge_single():
    root = build_tree([1])
    assert Solution().findBottomLeftValue(root) == 1


def test_bottom_left_tricky_deeper():
    root = build_tree([1, 2, 3, 4, None, 5, 6, None, None, 7])
    assert Solution().findBottomLeftValue(root) == 7
