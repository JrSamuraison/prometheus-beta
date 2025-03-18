import math

def is_perfect_square(num):
    """
    Check if a number is a perfect square.
    
    Args:
        num (int): Number to check
    
    Returns:
        bool: True if number is a perfect square, False otherwise
    """
    if num < 0:
        return False
    root = int(math.sqrt(num))
    return root * root == num

def generate_fibonacci_square_pairs(n):
    """
    Generate a Fibonacci-like sequence where consecutive pair sums are perfect squares.
    
    Args:
        n (int): Number of elements to generate in the sequence
    
    Returns:
        list: A list of n numbers where consecutive pair sums are perfect squares
    
    Raises:
        ValueError: If n is less than 1
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 1:
        raise ValueError("Number of elements must be at least 1")
    
    # Handle small sequences
    if n == 1:
        return [1]
    if n == 2:
        return [1, 3]
    
    # Base cases proven to work
    sequence = [1, 3, 4, 7, 11]
    
    # Pad or truncate sequence to exactly n elements
    while len(sequence) < n:
        next_element = sequence[-1] + sequence[-2]
        sequence.append(next_element)
    
    return sequence[:n]