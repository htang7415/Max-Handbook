from problem_654_maximum_binary_tree import Solution, TreeNode


def level_order(root: TreeNode | None) -> list[int | None]:
    if root is None:
        return []
    result: list[int | None] = []
    queue: list[TreeNode | None] = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


def test_maximum_binary_tree_example():
    nums = [3, 2, 1, 6, 0, 5]
    root = Solution().constructMaximumBinaryTree(nums)
    assert level_order(root) == [6, 3, 5, None, 2, 0, None, None, 1]


def test_maximum_binary_tree_edge_empty():
    assert Solution().constructMaximumBinaryTree([]) is None


def test_maximum_binary_tree_tricky_decreasing():
    nums = [5, 4, 3, 2, 1]
    root = Solution().constructMaximumBinaryTree(nums)
    assert level_order(root) == [5, None, 4, None, 3, None, 2, None, 1]


def test_maximum_binary_tree_tricky_increasing():
    nums = [1, 2, 3, 4, 5]
    root = Solution().constructMaximumBinaryTree(nums)
    assert level_order(root) == [5, 4, None, 3, None, 2, None, 1]
