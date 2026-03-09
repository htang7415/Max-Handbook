# Binary Tree Summary

> Track: `dsa` | Topic: `binary-tree`

## What This Module Covers

This summary reviews traversal patterns, subtree recursion, tree construction, and BST-specific operations.

## Recognition Cues

- The problem can be decomposed into left and right subtree work.
- Traversal order affects correctness.
- BST problems gain extra power from ordering.

## Core Ideas

- Decide whether the node is processed before, between, or after its children.
- Tree recursion is usually about what one call returns for one subtree.
- BSTs support pruning, ordered search, and inorder-sorted reasoning.

## Common Mistakes

- Solving a tree problem without defining the subtree contract.
- Using the wrong traversal order for the needed information.
- Ignoring BST ordering when it could simplify the search.

## Connections

- Linked lists train pointer identity; trees add branching.
- Stack/queue structures support iterative DFS and BFS.
- Dynamic programming on trees is still subtree-state aggregation.

## Self-Check

- What does one recursive call return?
- Which traversal order matches the task?
- When can BST ordering prune work?
