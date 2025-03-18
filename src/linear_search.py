def linear_search(arr, target):
    """
    Perform a linear search to find the index of a target element in a list.

    Args:
        arr (list): The input list to search through.
        target: The element to search for.

    Returns:
        int: The index of the target element if found, -1 otherwise.

    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    # Iterate through the list
    for index, element in enumerate(arr):
        # Check if current element matches the target
        if element == target:
            return index

    # Return -1 if target is not found
    return -1