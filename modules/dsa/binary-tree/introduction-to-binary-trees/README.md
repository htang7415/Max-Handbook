# Introduction to Binary Trees

> Track: `dsa` | Topic: `binary-tree`

## What This Module Covers

Binary trees store values through left and right child pointers and support recursive reasoning over subtrees.

## Recognition Cues

- Each node has up to two children.
- The problem naturally splits into left-subtree and right-subtree cases.
- Traversal order changes what information is available when.

## Core Ideas

- A subtree is a full smaller instance of the original problem.
- Recursive definitions are natural because tree structure is recursive.
- Traversal order matters: preorder, inorder, postorder, and level order answer different questions.

## Common Mistakes

- Forgetting the base case for an empty node.
- Mixing node values with subtree structure.
- Writing tree code without deciding what each recursive call should return.

## Connections

- BSTs add ordering constraints on top of the same tree structure.
- DFS and BFS are both tree traversal styles.
- Many tree problems are really subtree-aggregation problems.

## Self-Check

- What does an empty subtree contribute?
- What should one recursive call mean?
- Which traversal order matches the information you need?
