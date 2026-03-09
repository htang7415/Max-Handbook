from problem_700_search_in_a_binary_search_tree import Solution, TreeNode


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


def test_search_bst_example():
    root = build_tree([4, 2, 7, 1, 3])
    node = Solution().searchBST(root, 2)
    assert node is not None
    assert node.val == 2


def test_search_bst_edge_empty():
    assert Solution().searchBST(None, 5) is None


def test_search_bst_tricky_missing():
    root = build_tree([4, 2, 7, 1, 3])
    assert Solution().searchBST(root, 5) is None
