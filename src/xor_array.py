def xor_array_elements(arr):
    """
    Calculate the XOR of all elements in the given array.

    Args:
        arr (list): A list of integers to perform XOR operation on.

    Returns:
        int: The result of XORing all elements in the array.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list is empty.
    """
    # Validate input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for empty list
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Initial result is the first element
    result = arr[0]
    
    # XOR with subsequent elements
    for num in arr[1:]:
        # Ensure each element is an integer
        if not isinstance(num, int):
            raise TypeError("All elements must be integers")
        
        result ^= num
    
    return result