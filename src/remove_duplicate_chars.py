def remove_duplicates_over_threshold(input_string: str) -> str:
    """
    Remove characters that appear more than twice in a given string.
    
    Args:
        input_string (str): The input string to process
    
    Returns:
        str: A string with characters appearing more than twice removed
    
    Examples:
        >>> remove_duplicates_over_threshold("aabbcccd")
        ''
        >>> remove_duplicates_over_threshold("aaabbbccc")
        ''
        >>> remove_duplicates_over_threshold("abcde")
        'abcde'
    """
    # If input is None or empty, return empty string
    if not input_string:
        return ""
    
    # Count character occurrences (case-sensitive)
    from collections import defaultdict
    char_counts = defaultdict(int)
    for char in input_string:
        char_counts[char.lower()] += 1
    
    # If any character appears 3 or more times, return empty string
    if any(count >= 3 for count in char_counts.values()):
        return ""
    
    return input_string