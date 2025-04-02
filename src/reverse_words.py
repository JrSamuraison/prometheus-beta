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
    
    # Separate alphabetic words and non-alphabetic tokens
    alpha_words = [word for word in words if word.replace('.', '').replace('-', '').isalpha()]
    non_alpha_tokens = [word for word in words if not word.replace('.', '').replace('-', '').isalpha()]
    
    # Reverse only the alphabetic words 
    alpha_words.reverse()
    
    # Reconstruct the tokens, prioritizing original non-alphabetic tokens
    result_tokens = []
    alpha_index = 0
    non_alpha_index = 0
    
    for token in tokens:
        if token.isspace():
            # Always add spaces
            result_tokens.append(token)
        else:
            # Replace with appropriate token based on type
            if token.replace('.', '').replace('-', '').isalpha():
                # Use reversed alphabetic word
                result_tokens.append(alpha_words[alpha_index])
                alpha_index += 1
            else:
                # Preserve original order for non-alphabetic tokens
                result_tokens.append(non_alpha_tokens[non_alpha_index])
                non_alpha_index += 1
    
    return ''.join(result_tokens)