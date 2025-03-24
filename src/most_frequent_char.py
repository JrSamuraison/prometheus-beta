def find_most_frequent_char(input_string):
    """
    Find the most frequently occurring character in a given string.

    Args:
        input_string (str): The input string to analyze.

    Returns:
        str: The most frequently occurring character.
             If multiple characters have the same highest frequency, 
             return the first one encountered.
        None: If the input string is empty.

    Raises:
        TypeError: If input is not a string.
    """
    # Check for invalid input
    if input_string is None:
        return None
    
    # Validate input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if len(input_string) == 0:
        return None
    
    # Count character frequencies
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the character with maximum frequency
    max_char = max(char_count, key=char_count.get)
    return max_char