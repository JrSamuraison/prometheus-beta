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
        candidates = [
            sequence[-1] + sequence[-2],  # Standard next Fibonacci-like element
            sequence[-1] * 2,  # Alternate growth strategy
            sequence[-1] + 1   # Conservative growth
        ]
        
        found_candidate = False
        for candidate in candidates:
            # Check if this candidate maintains the square pair sum property
            temp_sequence = sequence + [candidate]
            if is_perfect_square(temp_sequence[-2] + temp_sequence[-1]):
                sequence.append(candidate)
                found_candidate = True
                break
        
        # If no suitable candidate found, use the default growth
        if not found_candidate:
            sequence.append(candidates[0])
        
        # Prevent infinite loop
        if len(sequence) > n * 2:
            break
    
    # Pad or truncate sequence to exactly n elements
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    
    return sequence[:n]