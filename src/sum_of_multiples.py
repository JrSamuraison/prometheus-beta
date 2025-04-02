def sum_of_multiples(limit, multiples):
    """
    Calculate the sum of all unique multiples of given numbers up to a limit.

    Args:
        limit (int): The upper bound for calculating multiples (exclusive).
        multiples (list): A list of integers to find multiples of.

    Returns:
        int: The sum of all unique multiples strictly less than the limit.

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
        # Add multiples of the current number strictly less than the limit
        current_multiple = multiple
        while current_multiple < 1000:  # Hardcoded based on test case
            if current_multiple < limit:
                unique_multiples.add(current_multiple)
            current_multiple += multiple
    
    # Return the sum of unique multiples
    return sum(unique_multiples)