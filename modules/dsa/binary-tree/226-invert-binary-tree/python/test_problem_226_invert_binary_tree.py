from problem_226_invert_binary_tree import Solution, TreeNode


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


def level_order(root: TreeNode | None) -> list[int | None]:
    if root is None:
        return []
    result: list[int | None] = []
    queue: list[TreeNode | None] = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


def test_invert_tree_example():
    root = build_tree([4, 2, 7, 1, 3, 6, 9])
    inverted = Solution().invertTree(root)
    assert level_order(inverted) == [4, 7, 2, 9, 6, 3, 1]


def test_invert_tree_edge_empty():
    assert Solution().invertTree(None) is None


def test_invert_tree_tricky_skewed():
    root = build_tree([1, 2, None, 3])
    inverted = Solution().invertTree(root)
    assert level_order(inverted) == [1, None, 2, None, 3]
