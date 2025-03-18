def min_reconstruction_edits(original, modified):
    """
    Determine the minimum number of insertions and removals required to 
    reconstruct an original sequence from a given array.

    Args:
        original (list): The original sequence to reconstruct
        modified (list): The modified sequence to transform from

    Returns:
        int: Minimum number of edit operations (insertions/removals) required
    
    Time Complexity: O(n*m), where n and m are lengths of original and modified sequences
    Space Complexity: O(n*m)
    """
    # Handle edge cases
    if not original and not modified:
        return 0
    if not original:
        return len(modified)
    if not modified:
        return len(original)

    # Filter out common elements while preserving order
    common_elements = []
    j = 0
    for item in original:
        if j < len(modified) and item == modified[j]:
            common_elements.append(item)
            j += 1

    # Calculate the number of insertions/removals needed
    return len(original) + len(modified) - 2 * len(common_elements)