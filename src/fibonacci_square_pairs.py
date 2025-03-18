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
    
    # Initialize sequence with first two elements
    sequence = [1, 3]
    
    # Generate subsequent elements
    while len(sequence) < n:
        # Potential next element
        next_num = sequence[-1] + sequence[-2]
        
        # Ensure the sum of the last two consecutive pairs is a perfect square
        if is_perfect_square(sequence[-2] + sequence[-1]):
            sequence.append(next_num)
        else:
            # If no suitable next number is found, break to prevent infinite loop
            break
    
    # Truncate or pad the sequence to exactly n elements
    return sequence[:n]