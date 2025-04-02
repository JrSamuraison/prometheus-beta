def reverse_words(s: str) -> str:
    """
    Reverse the order of words in a given string.
    
    Args:
        s (str): Input string to be processed.
    
    Returns:
        str: String with words in reversed order, 
             preserving original spacing and handling mixed content.
    
    Examples:
        >>> reverse_words("Hello World")
        'World Hello'
        >>> reverse_words("  Hello   World  ")
        '  World   Hello  '
        >>> reverse_words("123 abc 456")
        'abc 123 456'
    """
    # Import regex 
    import re
    
    # First, split the string maintaining original structure
    # This handles words, numbers, and mixed content
    tokens = re.findall(r'\S+|\s+', s)
    
    # Partition tokens into words and spaces
    words = []
    spaces = []
    for token in tokens:
        if token.strip():  # If non-whitespace
            words.append(token)
        else:
            spaces.append(token)
    
    # Reverse only the words
    words.reverse()
    
    # Reconstruct the string, preserving original spacing
    result = []
    max_iterations = max(len(words), len(spaces))
    
    for i in range(max_iterations):
        # Add word if available
        if i < len(words):
            result.append(words[i])
        
        # Add space if available
        if i < len(spaces):
            result.append(spaces[i])
    
    return ''.join(result)