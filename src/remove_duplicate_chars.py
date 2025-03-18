def remove_duplicates_over_threshold(input_string: str) -> str:
    """
    Remove characters that appear more than twice in a given string.
    
    Args:
        input_string (str): The input string to process
    
    Returns:
        str: A string with characters appearing more than twice removed
    
    Examples:
        >>> remove_duplicates_over_threshold("aabbcccd")
        'aabbcd'
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
    seen_indices = {}
    
    for i, char in enumerate(input_string):
        current_count = char_counts.get(char, 0)
        
        if current_count < 2:
            result_chars.append(char)
            seen_indices[char] = i
        
        char_counts[char] = current_count + 1
    
    return ''.join(result_chars)