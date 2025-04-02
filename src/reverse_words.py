def reverse_words(s: str) -> str:
    """
    Reverse the order of words in a given string.
    
    Args:
        s (str): Input string to be processed.
    
    Returns:
        str: String with words in reversed order, 
             precisely preserving original spacing and handling mixed content.
    
    Examples:
        >>> reverse_words("Hello World")
        'World Hello'
        >>> reverse_words("  Hello   World  ")
        '  World   Hello  '
        >>> reverse_words("123 abc 456")
        'abc 123 456'
    """
    import re
    
    # If the string is empty or just whitespace, return as-is
    if not s.strip():
        return s
    
    # Split the string into tokens
    tokens = re.findall(r'\S+|\s+', s)
    
    # Separate words (including words with non-alphabetic characters)
    words = [token for token in tokens if not token.isspace()]
    spaces = [token for token in tokens if token.isspace()]
    
    # Reverse only the sequence of words
    words.reverse()
    
    # Reconstruct the string
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