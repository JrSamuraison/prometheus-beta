import random

def convert_to_random_case(input_string):
    """
    Convert a string to random case, changing the case of each character randomly.
    
    Args:
        input_string (str): The input string to be converted to random case.
    
    Returns:
        str: A new string with each character randomly converted to upper or lower case.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is an empty string, return an empty string
    if not input_string:
        return ""
    
    # Convert each character to random case
    return ''.join(
        char.upper() if random.choice([True, False]) else char.lower() 
        for char in input_string
    )