from problem_337_house_robber_iii import Solution, TreeNode


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


def test_house_robber_iii_example():
    root = build_tree([3, 2, 3, None, 3, None, 1])
    assert Solution().rob(root) == 7


def test_house_robber_iii_edge_empty():
    assert Solution().rob(None) == 0


def test_house_robber_iii_tricky_skip_root():
    root = build_tree([3, 4, 5, 1, 3, None, 1])
    assert Solution().rob(root) == 9
