def pancake_sort(arr):
    """
    Implement the Pancake Sort algorithm to sort a list in ascending order.
    
    The Pancake Sort algorithm works by repeatedly flipping the largest unsorted 
    element to the top of the list and then flipping it to its correct position.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains non-comparable elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    sorted_arr = arr.copy()
    
    # Check if all elements are comparable
    try:
        sorted_arr.sort()
    except TypeError:
        raise ValueError("List contains non-comparable elements")
    
    # Main pancake sort algorithm
    def flip(sublist, k):
        """Reverse the first k elements of the list."""
        left = sublist[:k]
        left.reverse()
        return left + sublist[k:]
    
    n = len(sorted_arr)
    for size in range(n, 1, -1):
        # Find the index of the maximum element in the unsorted portion
        max_idx = sorted_arr[:size].index(max(sorted_arr[:size]))
        
        # If the max element is not already at the end, flip it to the top
        if max_idx != 0:
            sorted_arr = flip(sorted_arr, max_idx + 1)
        
        # Flip the max element to its correct position
        sorted_arr = flip(sorted_arr, size)
    
    return sorted_arr