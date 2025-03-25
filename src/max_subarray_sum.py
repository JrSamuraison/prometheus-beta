def max_subarray_sum(arr):
    """
    Calculate the maximum sum of a contiguous subarray using Kadane's algorithm.
    
    This function finds the contiguous subarray within the given array 
    that has the largest sum, handling both positive and negative numbers.
    
    Args:
        arr (list): A list of integers to find the maximum subarray sum from.
    
    Returns:
        int: The maximum sum of any contiguous subarray.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    
    Examples:
        >>> max_subarray_sum([1, -2, 3, 4, -1, 5])
        11
        >>> max_subarray_sum([-1, -2, -3, -4])
        -1
    """
    # Check input validity
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm implementation
    max_so_far = current_max = arr[0]
    
    for num in arr[1:]:
        # Choose between extending the current subarray or starting a new one
        current_max = max(num, current_max + num)
        
        # Update the overall maximum if necessary
        max_so_far = max(max_so_far, current_max)
    
    return max_so_far