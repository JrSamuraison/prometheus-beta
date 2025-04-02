def double_even_numbers(numbers):
    """
    Takes an array of numbers and returns a new array with all even numbers multiplied by 2.
    
    Args:
        numbers (list): Input list of numbers
    
    Returns:
        list: A new list where even numbers are doubled and odd numbers remain unchanged
    
    Raises:
        TypeError: If the input is not a list or contains non-numeric elements
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are numeric
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements must be numeric")
    
    # Create a new list with even numbers doubled
    return [num * 2 if num % 2 == 0 else num for num in numbers]