from typing import List, Dict, Set, Tuple
from collections import deque

class AhoCorasick:
    def __init__(self, patterns: List[str]):
        """
        Initialize the Aho-Corasick algorithm with a list of patterns to match.
        
        Args:
            patterns (List[str]): List of strings to search for in the text
        """
        # Trie root node
        self.trie = {}
        # Output mapping for found patterns
        self.output = {}
        # Failure links for efficient matching
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
        # Initialize root's failure link to root
        self.failure_links = {}
        queue = deque()
        
        # Process first level characters
        for char, subtrie in self.trie.items():
            if char != '$':
                queue.append((char, subtrie, self.trie))
                self.failure_links[subtrie] = self.trie
        
        # BFS to construct failure links
        while queue:
            prev_char, current_node, parent = queue.popleft()
            
            # Process child nodes of current node
            for char, child_node in current_node.items():
                if char == '$':
                    continue
                
                # Add to queue for further processing
                queue.append((char, child_node, current_node))
                
                # Find failure link for this node
                failure_state = parent
                while True:
                    if char in failure_state and failure_state is not self.trie:
                        failure_state = failure_state[char]
                        break
                    elif failure_state is self.trie:
                        failure_state = self.trie
                        break
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
        
        # Iterate through the text
        for i, char in enumerate(text):
            # Transition through the trie
            while char not in current and current is not self.trie:
                current = self.failure_links.get(current, self.trie)
            
            # Move to next state if possible
            if char in current:
                current = current[char]
            else:
                current = self.trie
            
            # Check for matches
            state = current
            while state is not self.trie:
                if '$' in state:
                    pattern = state['$']
                    # Find start index by subtracting pattern length
                    start_index = i - len(pattern) + 1
                    matches.append((start_index, pattern))
                
                # Follow failure link
                state = self.failure_links.get(state, self.trie)
        
        return matches