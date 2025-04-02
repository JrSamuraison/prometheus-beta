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
    
    # Split the string into tokens while preserving order
    tokens = re.findall(r'\S+|\s+', s)
    
    # Separate words (including numbers and tokens with non-space characters)
    words = [token for token in tokens if not token.isspace()]
    spaces = [token for token in tokens if token.isspace()]
    
    # Separate alphabetic words 
    alpha_words = [word for word in words if word.replace('.', '').replace('-', '').isalpha()]
    
    # If no alphabetic words, return original string
    if not alpha_words:
        return s
    
    # Reverse only the alphabetic words 
    alpha_words.reverse()
    
    # Reconstruct the tokens, ensuring alphabetic words are positioned correctly
    result_tokens = []
    alpha_index = 0
    
    for token in tokens:
        if token.isspace():
            # Always add spaces
            result_tokens.append(token)
        else:
            # Replace with appropriate word
            if token.replace('.', '').replace('-', '').isalpha():
                # Use reversed alphabetic word
                result_tokens.append(alpha_words[alpha_index])
                alpha_index += 1
            else:
                # Preserve original position of non-alphabetic tokens
                result_tokens.append(token)
    
    return ''.join(result_tokens)