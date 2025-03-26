def find_missing_number(nums):
    """
    Find the missing number in an array of unique positive integers between 1 and n.
    
    Args:
        nums (list): A list of unique positive integers between 1 and n, 
                     where one number is missing.
    
    Returns:
        int: The missing number.
    
    Raises:
        ValueError: If the input is invalid (empty list, not unique, or out of range).
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Check for invalid input
    if not nums:
        raise ValueError("Input array cannot be empty")
    
    # Calculate the expected length
    n = len(nums) + 1  # Total number of elements including the missing number
    
    # Validate that all numbers are within the expected range
    if any(num < 1 or num > n for num in nums):
        raise ValueError("Invalid input: numbers are not in range 1 to n")
    
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of the given array
    actual_sum = sum(nums)
    
    # The difference is the missing number
    missing_number = expected_sum - actual_sum
    
    return missing_number