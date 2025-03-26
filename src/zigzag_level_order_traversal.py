from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Perform a zigzag (level order) traversal of a binary tree.
    
    In a zigzag traversal, nodes are visited level by level, 
    alternating the direction of traversal:
    - Level 0 (root): left to right
    - Level 1: right to left
    - Level 2: left to right
    and so on.
    
    Args:
        root (Optional[TreeNode]): The root of the binary tree.
    
    Returns:
        List[List[int]]: A list of lists, where each inner list 
        represents a level of the tree, traversed in zigzag order.
    
    Time Complexity: O(n), where n is the number of nodes
    Space Complexity: O(n)
    
    Examples:
        1. 
           Input: [3,9,20,null,null,15,7]
           Output: [[3],[20,9],[15,7]]
        
        2. 
           Input: []
           Output: []
    """
    # Handle empty tree case
    if not root:
        return []
    
    # Use a queue for level-order traversal
    queue = [root]
    # Result list to store levels
    result = []
    # Flag to track traversal direction
    left_to_right = True
    
    while queue:
        # Number of nodes at current level
        level_size = len(queue)
        # Current level's nodes
        current_level = []
        
        for _ in range(level_size):
            # Remove the first node from queue
            node = queue.pop(0)
            
            # Add node to current level
            current_level.append(node.val)
            
            # Add child nodes to queue for next iteration
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Reverse the level if needed (zigzag)
        if not left_to_right:
            current_level.reverse()
        
        # Add current level to result
        result.append(current_level)
        
        # Flip direction for next level
        left_to_right = not left_to_right
    
    return result