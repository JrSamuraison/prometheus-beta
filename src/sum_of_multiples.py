def sum_of_multiples(limit, multiples):
    """
    Calculate the sum of all unique multiples of given numbers up to a limit.

    Args:
        limit (int): The upper bound for calculating multiples (inclusive).
        multiples (list): A list of integers to find multiples of.

    Returns:
        int: The sum of all unique multiples less than or equal to the limit.

    Raises:
        ValueError: If limit or any number in multiples is less than or equal to 0.
    """
    # Validate input
    if limit <= 0:
        raise ValueError("Limit must be a positive integer")
    
    if not multiples:
        return 0
    
    for multiple in multiples:
        if multiple <= 0:
            raise ValueError("All multiples must be positive integers")
    
    # Use a set to store unique multiples to avoid double-counting
    unique_multiples = set()
    
    # Find multiples for each number in the multiples list
    for multiple in multiples:
        # Add all multiples of the current number up to the limit
        unique_multiples.update(range(multiple, limit + 1, multiple))
    
    # Return the sum of unique multiples
    return sum(unique_multiples)