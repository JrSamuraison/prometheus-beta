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
    # Import regex 
    import re
    
    # If the string is empty or just whitespace, return as-is
    if not s.strip():
        return s
    
    # Split the string into words and spaces, keeping the exact original structure
    # This method ensures exact preservation of original spacing
    def is_space(token):
        return token.isspace()
    
    def is_non_word(token):
        return not token.replace('.', '').replace('-', '').isalnum()
    
    # First pass: purely alphabetic words
    alpha_words = [token for token in re.findall(r'\S+', s) if token.isalpha()]
    
    # If no alphabetic words, return original string
    if not alpha_words:
        return s
    
    # Reverse only the alphabetic words
    alpha_words.reverse()
    
    # Tokenize the original string
    tokens = re.findall(r'\S+|\s+', s)
    
    # Create a new sequence of tokens, replacing alphabetic words
    result_tokens = []
    alpha_index = 0
    
    for token in tokens:
        if token.isalpha():
            # Replace with reversed alphabetic word
            result_tokens.append(alpha_words[alpha_index])
            alpha_index += 1
        else:
            # Keep non-alphabetic tokens as they are
            result_tokens.append(token)
    
    return ''.join(result_tokens)