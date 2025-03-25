def find_array_intersection(arr1, arr2):
    """
    Find the intersection of two integer arrays.

    Args:
        arr1 (list): First input array of integers
        arr2 (list): Second input array of integers

    Returns:
        list: A sorted list of unique elements that are common to both input arrays

    Raises:
        TypeError: If inputs are not lists
        ValueError: If inputs contain non-integer elements
    """
    # Validate input types
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        raise TypeError("Inputs must be lists")
    
    # Validate that all elements are integers
    if not all(isinstance(x, int) for x in arr1 + arr2):
        raise ValueError("All array elements must be integers")
    
    # Convert to sets for efficient intersection
    # Then convert back to sorted list to ensure consistent output
    return sorted(list(set(arr1) & set(arr2)))