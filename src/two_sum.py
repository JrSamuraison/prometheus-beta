def two_sum(nums, target):
    """
    Determine if any two unique numbers in the input array sum to the target.
    
    Args:
        nums (list): A list of unique integers
        target (int): The target sum to find
    
    Returns:
        bool: True if any two numbers in the array sum to the target, False otherwise
    
    Raises:
        TypeError: If input is not a list or if target is not an integer
        ValueError: If the input list contains duplicate numbers
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Type checking
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Check for unique numbers
    if len(set(nums)) != len(nums):
        raise ValueError("Input list must contain unique numbers")
    
    # Use a set for O(1) lookup
    seen = set()
    
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    
    return False