def remove_duplicates(sorted_list):
    """
    Remove duplicate values from a sorted list of integers without using built-in functions like set() or dict().

    Args:
        sorted_list (list): A sorted list of integers.

    Returns:
        list: A new list with duplicate values removed, maintaining the original order.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is not sorted.
    """
    # Check if input is a list
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not sorted_list:
        return []
    
    # Check if the list is sorted
    if sorted_list != sorted(sorted_list):
        raise ValueError("Input list must be sorted")
    
    # Remove duplicates
    unique_list = []
    for num in sorted_list:
        # Only add the number if it's not already in the unique list
        if not unique_list or num > unique_list[-1]:
            unique_list.append(num)
    
    return unique_list