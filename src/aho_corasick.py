from typing import List, Dict, Set, Tuple, Union
from collections import deque
import json

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
        
        # Failure links using serialized dict as key
        self.failure_links = {}
        
        # Build the trie with the given patterns
        self._build_trie(patterns)
        
        # Construct failure links using BFS
        self._construct_failure_links()
    
    def _dict_to_key(self, d: dict) -> str:
        """
        Convert a dictionary to a consistent unique string key.
        
        Args:
            d (dict): Dictionary to convert
        
        Returns:
            str: Unique string representation of the dictionary
        """
        # Handle non-dict and empty case
        if not isinstance(d, dict):
            return str(d)
        
        # Sort the keys to ensure consistent serialization
        return json.dumps(
            {k: self._dict_to_key(v) for k, v in sorted(d.items())}, 
            sort_keys=True
        )
    
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
        
        # Initialize first level nodes
        for char, subtrie in self.trie.items():
            if char != '$':
                # Use json-serialized keys
                subtrie_key = self._dict_to_key(subtrie)
                trie_key = self._dict_to_key(self.trie)
                
                queue.append((subtrie, self.trie))
                self.failure_links[subtrie_key] = trie_key
        
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
                    # Try to find a matching path
                    if char in failure_state and failure_state is not self.trie:
                        failure_state = failure_state[char]
                        break
                    # If root is reached, stay at root
                    elif failure_state is self.trie:
                        failure_state = self.trie
                        break
                    # Try parent's failure link
                    parent_key = self._dict_to_key(parent)
                    failure_state = self._get_dict_from_key(
                        self.failure_links.get(parent_key, self._dict_to_key(self.trie))
                    )
                
                # Set failure link
                child_key = self._dict_to_key(child_node)
                failure_key = self._dict_to_key(failure_state)
                self.failure_links[child_key] = failure_key
    
    def _get_dict_from_key(self, key: str) -> dict:
        """
        Retrieve the dictionary corresponding to a key.
        This is the reverse of _dict_to_key.
        
        Args:
            key (str): Serialized dictionary key
        
        Returns:
            dict: Corresponding dictionary
        """
        # To find the correct dictionary, search through all 
        # candidates that match the key
        for d, k in list(map(lambda x: (x[0], self._dict_to_key(x[0])), [
            (self.trie, self._dict_to_key(self.trie)),
            *[(node, k) for char, node in self.trie.items() 
              if char != '$' for k in [self._dict_to_key(node)]]
        ]):
            if k == key:
                return d
        
        return self.trie
    
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
            current_key = self._dict_to_key(current)
            while char not in current and current is not self.trie:
                # Move through failure links
                current_key = self.failure_links.get(current_key, self._dict_to_key(self.trie))
                current = self._get_dict_from_key(current_key)
            
            # Move to next state if possible
            if char in current:
                current = current[char]
            else:
                current = self.trie
            
            # Check for matches
            state = current
            state_key = self._dict_to_key(state)
            while state is not self.trie:
                if '$' in state:
                    pattern = state['$']
                    # Find start index by subtracting pattern length
                    start_index = i - len(pattern) + 1
                    matches.append((start_index, pattern))
                
                # Follow failure link
                state_key = self.failure_links.get(state_key, self._dict_to_key(self.trie))
                state = self._get_dict_from_key(state_key)
        
        return matches