from typing import List, Any

def find_list_difference(list1: List[Any], list2: List[Any]) -> List[Any]:
    """
    Find the elements that are in list1 but not in list2.

    Args:
        list1 (List[Any]): The first input list
        list2 (List[Any]): The second input list to compare against

    Returns:
        List[Any]: A list of elements that are in list1 but not in list2

    Examples:
        >>> find_list_difference([1, 2, 3], [2, 3, 4])
        [1]
        >>> find_list_difference(['a', 'b', 'c'], ['b', 'c', 'd'])
        ['a']
        >>> find_list_difference([], [1, 2, 3])
        []
    """
    # Convert lists to sets for efficient difference operation
    # Use list() to convert back to list to preserve order of first appearance
    return list(set(list1) - set(list2))