from typing import List, Dict, Set, Tuple, Union
from collections import deque

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
        
        # Trie root node
        self.trie = {}
        
        # Failure links
        self.failure_links = {}
        
        # Build the trie with the given patterns
        self._build_trie(patterns)
        
        # Construct failure links using BFS
        self._construct_failure_links()
    
    def _build_trie(self, patterns: List[str]):
        """
        Build the trie data structure for the given patterns.
        
        Args:
            patterns (List[str]): Patterns to add to the trie
        """
        for pattern in patterns:
            # Start at the root of the trie
            current = self.trie
            
            # Add each character to the trie
            for char in pattern:
                if char not in current:
                    current[char] = {}
                current = current[char]
            
            # Mark the end of a pattern
            current['$'] = pattern
    
    def _construct_failure_links(self):
        """
        Construct failure links using Breadth-First Search.
        Failure links help efficiently skip unnecessary comparisons.
        """
        # Use a queue for BFS
        queue = deque()
        
        # First level nodes have failure link to root
        for char, subtrie in self.trie.items():
            if char != '$':
                queue.append((subtrie, self.trie))
                self.failure_links[subtrie] = self.trie
        
        # BFS to construct failure links
        while queue:
            current_node, parent = queue.popleft()
            
            # Process each character's node 
            for char, child_node in current_node.items():
                if char == '$':
                    continue
                
                # Add to queue for further processing
                queue.append((child_node, current_node))
                
                # Find failure link for this node
                failure_state = parent
                while True:
                    # Try to find a matching path
                    if char in failure_state and failure_state is not self.trie:
                        failure_state = failure_state[char]
                        break
                    # If root is reached, stay at root
                    elif failure_state is self.trie:
                        failure_state = self.trie
                        break
                    # Follow parent's failure link
                    failure_state = self.failure_links.get(failure_state, self.trie)
                
                # Set failure link
                self.failure_links[child_node] = failure_state
    
    def find_matches(self, text: str) -> List[Tuple[int, str]]:
        """
        Find all pattern matches in the given text.
        
        Args:
            text (str): Text to search for patterns
        
        Returns:
            List[Tuple[int, str]]: List of (start_index, matched_pattern) tuples
        """
        matches = []
        current = self.trie
        
        # Iterate through each character in the text
        for i, char in enumerate(text):
            # Move through valid states
            while char not in current and current is not self.trie:
                # Follow failure link
                current = self.failure_links.get(current, self.trie)
            
            # Transition to next state
            if char in current:
                current = current[char]
            else:
                current = self.trie
            
            # Track all patterns found in this state
            state = current
            while state is not self.trie:
                # Check for complete patterns
                if '$' in state:
                    pattern = state['$']
                    # Calculate precise start index 
                    # Subtract pattern length - 1 to get correct start point 
                    start_index = i - len(pattern) + 1
                    matches.append((start_index, pattern))
                
                # Follow failure link to find additional patterns
                state = self.failure_links.get(state, self.trie)
        
        return matches