def find_list_intersection(list1, list2):
    """
    Find the intersection of two lists, returning a list of common elements.

    Args:
        list1 (list): The first input list
        list2 (list): The second input list

    Returns:
        list: A list containing elements that are present in both input lists

    Note:
        - The order of elements in the result is not guaranteed
        - Duplicate elements are handled correctly
        - Works with lists of any hashable type
    """
    # Convert lists to sets for efficient intersection
    # This handles duplicates and provides efficient lookup
    return list(set(list1) & set(list2))