def calculate_min_max_average(numbers):
    """
    Calculate the average of the three smallest and three largest numbers in a given array.
    
    Args:
        numbers (list): A list of six real numbers.
    
    Returns:
        float: The average of the three smallest and three largest numbers.
    
    Raises:
        ValueError: If the input list does not contain exactly six numbers.
    """
    # Validate input
    if len(numbers) != 6:
        raise ValueError("Input must contain exactly six numbers")
    
    # Sort the numbers
    sorted_numbers = sorted(numbers)
    
    # Take the first three (smallest) and last three (largest) numbers
    smallest_three = sorted_numbers[:3]
    largest_three = sorted_numbers[3:]
    
    # Calculate and return the average
    return (sum(smallest_three) / 3 + sum(largest_three) / 3) / 2