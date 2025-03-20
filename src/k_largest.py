from typing import List

def k_largest(arr: List[int], k: int) -> List[int]:
    """
    Returns the k largest elements from the input array.
    
    Args:
        arr (List[int]): Input list of integers
        k (int): Number of largest elements to return
    
    Returns:
        List[int]: k largest elements in descending order
    
    Raises:
        ValueError: If k is negative or larger than the array length
        TypeError: If input is not a list or k is not an integer
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    
    # Handle edge cases
    if k < 0:
        raise ValueError("k cannot be negative")
    
    if k == 0:
        return []
    
    if k > len(arr):
        raise ValueError("k cannot be larger than the array length")
    
    # Sort the array in descending order and return k largest elements
    return sorted(arr, reverse=True)[:k]