import pytest
from src.zigzag_level_order_traversal import TreeNode, zigzag_level_order

def test_empty_tree():
    """Test zigzag traversal of an empty tree."""
    assert zigzag_level_order(None) == []

def test_single_node_tree():
    """Test zigzag traversal of a tree with a single node."""
    root = TreeNode(1)
    assert zigzag_level_order(root) == [[1]]

def test_simple_balanced_tree():
    """Test zigzag traversal of a simple balanced tree."""
    # Tree:
    #     3
    #    / \
    #   9  20
    #      / \
    #     15  7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    assert zigzag_level_order(root) == [[3], [20, 9], [15, 7]]

def test_unbalanced_tree():
    """Test zigzag traversal of an unbalanced tree."""
    # Tree:
    #     1
    #    / \
    #   2   3
    #  /     \
    # 4       5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    
    assert zigzag_level_order(root) == [[1], [3, 2], [4, 5]]

def test_deep_tree():
    """Test zigzag traversal of a deep tree."""
    # Tree:
    #         1
    #       /   \
    #      2     3
    #     / \   / \
    #    4   5 6   7
    #   /
    #  8
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    
    assert zigzag_level_order(root) == [[1], [3, 2], [4, 5, 6, 7], [8]]