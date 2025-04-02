def cycle_sort(arr):
    """
    Implement the Cycle Sort algorithm to sort an array in-place.
    
    Cycle sort is an in-place, unstable sorting algorithm that is optimal in terms 
    of the number of memory writes. It works by finding the correct position for 
    each element and moving it to that position.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: The sorted list (modified in-place)
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains elements that cannot be compared
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If list is empty or has only one element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Traverse through all array elements
    for cycle_start in range(len(arr) - 1):
        item = arr[cycle_start]
        
        # Find the correct position for the current element
        pos = cycle_start
        for i in range(cycle_start + 1, len(arr)):
            if arr[i] < item:
                pos += 1
        
        # If the item is already in the correct position
        if pos == cycle_start:
            continue
        
        # Otherwise, put the item in its correct position
        while item == arr[pos]:
            pos += 1
        
        arr[pos], item = item, arr[pos]
        
        # Rotate the rest of the cycle
        while pos != cycle_start:
            # Find the correct position for the current item
            pos = cycle_start
            for i in range(cycle_start + 1, len(arr)):
                if arr[i] < item:
                    pos += 1
            
            # Place the item in its correct position
            while item == arr[pos]:
                pos += 1
            
            arr[pos], item = item, arr[pos]
    
    return arr