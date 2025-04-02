def reverse_words(s: str) -> str:
    """
    Reverse the order of words in a given string.
    
    Args:
        s (str): Input string to be processed.
    
    Returns:
        str: String with words in reversed order, 
             preserving original spacing and ignoring non-alphabetic characters.
    
    Examples:
        >>> reverse_words("Hello World")
        'World Hello'
        >>> reverse_words("  Hello   World  ")
        '  World   Hello  '
        >>> reverse_words("123 abc 456")
        'abc 123 456'
    """
    # Split the string into words, preserving whitespace
    # Use regex to split while keeping delimiters
    import re
    
    # Use regex to split string into words and separators
    tokens = re.findall(r'\S+|\s+', s)
    
    # Separate words and whitespace
    words = [token for token in tokens if not token.isspace()]
    spaces = [token for token in tokens if token.isspace()]
    
    # Reverse only the words
    words.reverse()
    
    # Reconstruct the string
    # If there are more spaces than words, distribute them
    result = []
    for i in range(max(len(words), len(spaces))):
        # Add a word if available
        if i < len(words):
            result.append(words[i])
        
        # Add a space if available
        if i < len(spaces):
            result.append(spaces[i])
    
    return ''.join(result)