from typing import List, Dict, Set, Tuple, Union
from collections import deque

class TrieNode:
    def __init__(self, char: str = None, parent: 'TrieNode' = None):
        """
        Initialize a trie node.
        
        Args:
            char (str, optional): Character represented by this node
            parent (TrieNode, optional): Parent node in the trie
        """
        self.char = char
        self.parent = parent
        self.children = {}
        self.pattern = None
        self.failure_link = None
    
    def add_child(self, char: str) -> 'TrieNode':
        """
        Add a child node to the current node.
        
        Args:
            char (str): Character for the child node
        
        Returns:
            TrieNode: The newly created or existing child node
        """
        if char not in self.children:
            new_node = TrieNode(char, self)
            self.children[char] = new_node
        return self.children[char]

class AhoCorasick:
    def __init__(self, patterns: List[str]):
        """
        Initialize the Aho-Corasick algorithm with a list of patterns to match.
        
        Args:
            patterns (List[str]): List of strings to search for in the text
        """
        # Validate input
        if not patterns or not all(isinstance(p, str) for p in patterns):
            raise ValueError("Patterns must be a non-empty list of strings")
        
        # Root of the trie
        self.root = TrieNode()
        
        # Build the trie with the given patterns
        self._build_trie(patterns)
        
        # Construct failure links
        self._construct_failure_links()
    
    def _build_trie(self, patterns: List[str]):
        """
        Build the trie data structure for the given patterns.
        
        Args:
            patterns (List[str]): Patterns to add to the trie
        """
        for pattern in patterns:
            # Start at the root
            current = self.root
            
            # Add each character to the trie
            for char in pattern:
                current = current.add_child(char)
            
            # Mark end of pattern 
            current.pattern = pattern
    
    def _construct_failure_links(self):
        """
        Construct failure links using Breadth-First Search.
        Failure links help efficiently skip unnecessary comparisons.
        """
        # Queue for BFS
        queue = deque()
        
        # First level nodes have failure link to root
        for node in self.root.children.values():
            node.failure_link = self.root
            queue.append(node)
        
        # BFS to construct failure links
        while queue:
            current = queue.popleft()
            
            # Process each child of current node
            for char, child in current.children.items():
                queue.append(child)
                
                # Start with the node's parent's failure link
                failure_state = current.failure_link
                
                # Find the longest proper suffix
                while True:
                    # Check if failure state has a valid transition
                    if char in failure_state.children and failure_state.children[char] is not child:
                        child.failure_link = failure_state.children[char]
                        break
                    # If we reach the root, link to root
                    elif failure_state is self.root:
                        child.failure_link = self.root
                        break
                    # Go to failure state's failure link
                    failure_state = failure_state.failure_link
    
    def find_matches(self, text: str) -> List[Tuple[int, str]]:
        """
        Find all pattern matches in the given text.
        
        Args:
            text (str): Text to search for patterns
        
        Returns:
            List[Tuple[int, str]]: List of (start_index, matched_pattern) tuples
        """
        matches = []
        current = self.root
        
        # Iterate through the text
        for i, char in enumerate(text):
            # Find appropriate state
            while char not in current.children and current is not self.root:
                current = current.failure_link
            
            # Try to move to next state
            if char in current.children:
                current = current.children[char]
            else:
                current = self.root
            
            # Check for matches from this state and its ancestors
            state = current
            state_depth = 0
            
            # Count how deep we are in the current state
            temp_state = state
            while temp_state.parent is not None:
                state_depth += 1
                temp_state = temp_state.parent
            
            # Check for matches
            while state is not self.root:
                # Check if this node represents end of a pattern
                if state.pattern:
                    # Calculate precise start index 
                    # Subtract the correct depth to get exact start
                    start_index = i - state_depth
                    matches.append((start_index, state.pattern))
                
                # Follow failure link
                state = state.failure_link
                state_depth = 0
                temp_state = state
                while temp_state.parent is not None:
                    state_depth += 1
                    temp_state = temp_state.parent
        
        return matches