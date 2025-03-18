def remove_duplicates_over_threshold(input_string: str) -> str:
    """
    Remove characters that appear more than twice in a given string.
    
    Args:
        input_string (str): The input string to process
    
    Returns:
        str: A string with characters appearing more than twice removed
    
    Examples:
        >>> remove_duplicates_over_threshold("aabbcccd")
        'aabbccd'
        >>> remove_duplicates_over_threshold("aaabbbccc")
        ''
        >>> remove_duplicates_over_threshold("abcde")
        'abcde'
    """
    # If input is None or empty, return empty string
    if not input_string:
        return ""
    
    # Count character occurrences
    result_chars = []
    char_counts = {}
    
    for char in input_string:
        # Keep character if its count is less than 3
        if char_counts.get(char, 0) < 2:
            result_chars.append(char)
        
        # Update character count, track each character
        char_counts[char] = char_counts.get(char, 0) + 1
    
    return ''.join(result_chars)