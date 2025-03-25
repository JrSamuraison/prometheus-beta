def gravity_sort(arr):
    """
    Implement the Gravity Sort (Bead Sort) algorithm.
    
    Gravity sort works by simulating gravity acting on a set of beads.
    It's most efficient for non-negative integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A sorted list in ascending order.
    
    Raises:
        ValueError: If the input contains negative numbers.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for non-integer or negative elements
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("All elements must be non-negative integers")
    
    # Handle empty or single-element list cases
    if len(arr) <= 1:
        return arr.copy()
    
    # Find the maximum number to determine the number of rows
    max_num = max(arr)
    
    # Create the bead representation
    beads = [[1 if num > j else 0 for j in range(max_num)] for num in arr]
    
    # Apply gravity (drop beads)
    for col in range(max_num):
        # Count beads in each column
        bead_count = sum(row[col] for row in beads)
        
        # Drop beads to the bottom
        for row in range(len(beads)):
            beads[row][col] = 1 if row >= len(beads) - bead_count else 0
    
    # Reconstruct the sorted array
    sorted_arr = [
        sum(row[j] for j in range(max_num)) 
        for row in beads
    ]
    
    return sorted_arr