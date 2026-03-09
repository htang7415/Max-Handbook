from problem_235_lowest_common_ancestor_of_a_bst import Solution, TreeNode


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


def find_node(root: TreeNode | None, val: int) -> TreeNode | None:
    current = root
    while current and current.val != val:
        current = current.left if val < current.val else current.right
    return current


def test_lca_bst_example():
    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = find_node(root, 2)
    q = find_node(root, 8)
    assert Solution().lowestCommonAncestor(root, p, q).val == 6


def test_lca_bst_edge_same_subtree():
    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = find_node(root, 2)
    q = find_node(root, 4)
    assert Solution().lowestCommonAncestor(root, p, q).val == 2


def test_lca_bst_tricky_one_node_is_ancestor():
    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = find_node(root, 2)
    q = find_node(root, 3)
    assert Solution().lowestCommonAncestor(root, p, q).val == 2
