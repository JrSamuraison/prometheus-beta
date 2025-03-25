def product_of_left_elements(arr):
    """
    Calculate an array where each element is the product of numbers to its left.
    
    Args:
        arr (list): Input list of numbers
    
    Returns:
        list: Array where each element is the product of numbers to its left
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric elements
    
    Examples:
        >>> product_of_left_elements([1, 2, 3, 4])
        [1, 1, 2, 6]
        >>> product_of_left_elements([])
        []
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return []
    
    # Validate numeric elements
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All list elements must be numeric")
    
    # Initialize result list with the same length as input
    result = [1] * len(arr)
    
    # Calculate left product for each element
    for i in range(1, len(arr)):
        result[i] = result[i-1] * arr[i-1]
    
    return result