from typing import List, Dict, Set, Tuple
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
        # Unique node identifiers
        self.node_ids = {}
        self.next_node_id = 0
        
        # Output mapping for found patterns
        self.output = {}
        # Failure links for efficient matching
        self.failure_links = {}
        
        # Build the trie with the given patterns
        self._build_trie(patterns)
        # Construct failure links using BFS
        self._construct_failure_links()
    
    def _get_node_id(self, node):
        """
        Get or create a unique identifier for a trie node.
        
        Args:
            node (dict): Trie node dictionary
        
        Returns:
            int: Unique node identifier
        """
        if node not in self.node_ids:
            self.node_ids[node] = self.next_node_id
            self.next_node_id += 1
        return self.node_ids[node]
    
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
        # Root's failure link is to itself
        queue = deque()
        
        # Process first level characters
        for char, subtrie in self.trie.items():
            if char != '$':
                queue.append((subtrie, self.trie))
                # Use node identifiers
                node_id = self._get_node_id(subtrie)
                self.failure_links[node_id] = self._get_node_id(self.trie)
        
        # BFS to construct failure links
        while queue:
            current_node, parent = queue.popleft()
            
            # Process child nodes of current node
            for char, child_node in current_node.items():
                if char == '$':
                    continue
                
                # Add to queue for further processing
                queue.append((child_node, current_node))
                
                # Find failure link for this node
                failure_state = parent
                while True:
                    if char in failure_state and failure_state is not self.trie:
                        failure_state = failure_state[char]
                        break
                    elif failure_state is self.trie:
                        failure_state = self.trie
                        break
                    # Translate parent state to node ID
                    failure_state = self.failure_links.get(
                        self._get_node_id(failure_state), 
                        self._get_node_id(self.trie)
                    )
                
                # Set failure link using node identifiers
                current_node_id = self._get_node_id(current_node[char])
                failure_node_id = self._get_node_id(failure_state)
                self.failure_links[current_node_id] = failure_node_id
    
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
        current_node_id = self._get_node_id(current)
        
        # Iterate through the text
        for i, char in enumerate(text):
            # Transition through the trie
            while char not in current and current is not self.trie:
                # Use failure links to jump states
                current_node_id = self.failure_links.get(current_node_id, self._get_node_id(self.trie))
                current = [key for key, value in self.node_ids.items() if value == current_node_id][0]
            
            # Move to next state if possible
            if char in current:
                current = current[char]
                current_node_id = self._get_node_id(current)
            else:
                current = self.trie
                current_node_id = self._get_node_id(current)
            
            # Check for matches
            state = current
            state_node_id = current_node_id
            while state is not self.trie:
                if '$' in state:
                    pattern = state['$']
                    # Find start index by subtracting pattern length
                    start_index = i - len(pattern) + 1
                    matches.append((start_index, pattern))
                
                # Follow failure link
                state_node_id = self.failure_links.get(state_node_id, self._get_node_id(self.trie))
                state = [key for key, value in self.node_ids.items() if value == state_node_id][0]
        
        return matches