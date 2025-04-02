def reverse_string(input_string):
    """
    Reverse a given string, handling single and multi-word inputs with special characters.
    
    Args:
        input_string (str): The string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Reverse the string
    return input_string[::-1]