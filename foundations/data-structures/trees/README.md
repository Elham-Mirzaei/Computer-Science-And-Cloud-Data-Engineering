# Trees and Hierarchical Data Structures

## 1. What Is a Tree?

A tree is a hierarchical data structure consisting of nodes connected by edges.

Key concepts:
- **Root:** The top node.
- **Parent:** A node that has children.
- **Child:** A node connected below a parent.
- **Leaf:** A node without children.
- **Subtree:** A node and all its descendants.
- **Depth:** Number of edges from the root to a node.
- **Height:** Length of the longest path from a node to a leaf.

## 2. Binary Trees

A binary tree is a tree in which each node has at most two children:
- Left child
- Right child

## 3. Binary Search Trees (BST)

A Binary Search Tree follows an ordering rule:

- Values in the left subtree are smaller than the node.
- Values in the right subtree are greater than the node.

This allows efficient searching when the tree is balanced.

| Operation | Balanced BST | Skewed BST