from typing import List, Union
from collections import Counter

def find_mode(numbers: List[Union[int, float]]) -> Union[int, float, List[Union[int, float]]]:
    """
    Find the mode (most frequent value) in a list of numbers.

    Args:
        numbers (List[Union[int, float]]): A list of numbers to find the mode of.

    Returns:
        Union[int, float, List[Union[int, float]]]: 
        - The single mode if there's only one most frequent value
        - A list of modes if multiple values have the same highest frequency
        - Raises ValueError if the input list is empty

    Raises:
        ValueError: If the input list is empty
    """
    # Check for empty list
    if not numbers:
        raise ValueError("Cannot find mode of an empty list")
    
    # Use Counter to count occurrences of each number
    count = Counter(numbers)
    
    # Find the maximum frequency
    max_freq = max(count.values())
    
    # Find all numbers with the maximum frequency
    modes = [num for num, freq in count.items() if freq == max_freq]
    
    # Return single mode or list of modes
    return modes[0] if len(modes) == 1 else modes