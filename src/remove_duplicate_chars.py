def remove_duplicates_over_threshold(input_string: str) -> str:
    """
    Remove characters that appear more than twice in a given string.
    
    Args:
        input_string (str): The input string to process
    
    Returns:
        str: A string with characters appearing more than twice removed
    
    Examples:
        >>> remove_duplicates_over_threshold("aabbcccd")
        'abcd'
        >>> remove_duplicates_over_threshold("aaabbbccc")
        ''
        >>> remove_duplicates_over_threshold("abcde")
        'abcde'
    """
    # If input is None or empty, return empty string
    if not input_string:
        return ""
    
    # Count character occurrences
    char_counts = {}
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Build result string using an ordered dict to preserve order of first occurrence
    result_chars = []
    seen_chars = set()
    for char in input_string:
        if char_counts[char] <= 2 and char not in seen_chars:
            result_chars.append(char)
            seen_chars.add(char)
    
    return ''.join(result_chars)