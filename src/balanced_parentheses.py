def is_balanced_parentheses(s: str) -> bool:
    """
    Check if all parentheses in the given string are balanced.
    
    Args:
        s (str): Input string to check for balanced parentheses.
    
    Returns:
        bool: True if all parentheses are balanced, False otherwise.
    
    Examples:
        >>> is_balanced_parentheses("()")  # Simple balanced case
        True
        >>> is_balanced_parentheses("(())")  # Nested balanced case
        True
        >>> is_balanced_parentheses("()()")  # Multiple sets of parentheses
        True
        >>> is_balanced_parentheses("(()")  # Unbalanced case
        False
        >>> is_balanced_parentheses(")("  # Unbalanced case
        False
        >>> is_balanced_parentheses("")  # Empty string
        True
    """
    # Stack to keep track of opening parentheses
    stack = []
    
    # Mapping of closing to opening parentheses
    parentheses_map = {')': '('}
    
    for char in s:
        # If it's a closing parenthesis
        if char in parentheses_map:
            # If stack is empty or top doesn't match corresponding opening parenthesis
            if not stack or stack[-1] != parentheses_map[char]:
                return False
            # Remove the matching opening parenthesis from stack
            stack.pop()
        
        # If it's an opening parenthesis, add to stack
        elif char == '(':
            stack.append(char)
        
        # Ignore other characters
    
    # Balanced only if stack is empty
    return len(stack) == 0