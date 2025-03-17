def sum_digits(number):
    """
    Calculate the sum of digits for a given integer.

    Args:
        number (int): The input number whose digits will be summed.

    Returns:
        int: The sum of all digits in the number.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is negative.

    Examples:
        >>> sum_digits(123)
        6
        >>> sum_digits(0)
        0
        >>> sum_digits(9999)
        36
    """
    # Validate input
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for 0
    if number == 0:
        return 0
    
    # Sum the digits
    total = 0
    while number > 0:
        total += number % 10  # Get the rightmost digit
        number //= 10  # Remove the rightmost digit
    
    return total