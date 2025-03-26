def fibonacci_reverse(n):
    """
    Generate a reversed Fibonacci sequence up to the nth element.
    
    Args:
        n (int): The number of Fibonacci elements to generate.
    
    Returns:
        list: A list of Fibonacci numbers in reverse order.
    
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle special cases
    if n == 0:
        return []
    if n == 1:
        return [0]
    
    # Generate Fibonacci sequence
    a, b = 0, 1
    fib_sequence = [0, 1]
    
    # Continue generating Fibonacci numbers
    while len(fib_sequence) < n:
        a, b = b, a + b
        fib_sequence.append(b)
    
    # Return sequence up to nth element in reverse order
    return list(reversed(fib_sequence[:n]))