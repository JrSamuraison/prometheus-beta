def sum_odd_numbers(n):
    """
    Calculate the sum of all odd numbers between 1 and n (inclusive).
    
    Args:
        n (int): The upper bound of the range to sum odd numbers.
    
    Returns:
        int: The sum of all odd numbers from 1 to n.
    
    Raises:
        ValueError: If n is negative.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Examples:
        >>> sum_odd_numbers(5)
        9  # 1 + 3 + 5
        >>> sum_odd_numbers(10)
        25  # 1 + 3 + 5 + 7 + 9
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Use range to generate odd numbers and sum them
    return sum(range(1, n + 1, 2))