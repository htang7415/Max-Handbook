from __future__ import annotations

from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack: list[TreeNode] = []

        for value in nums:
            current = TreeNode(value)
            while stack and stack[-1].val < value:
                current.left = stack.pop()

            if stack:
                stack[-1].right = current

            stack.append(current)

        return stack[0] if stack else None
