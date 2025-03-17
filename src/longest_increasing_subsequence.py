def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in the given array.
    
    A subsequence is a sequence that can be derived from an array by deleting 
    some or no elements without changing the order of the remaining elements.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: The longest increasing subsequence
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Edge Cases:
    - Returns empty list for None or empty input
    - Works with lists containing duplicate or negative numbers
    """
    # Handle edge cases
    if not arr:
        return []
    
    # Length of the input array
    n = len(arr)
    
    # Dynamic programming array to store lengths of LIS ending at each index
    dp = [1] * n
    
    # Array to track previous indices for reconstructing the subsequence
    prev = [-1] * n
    
    # Maximum length of increasing subsequence
    max_length = 1
    max_index = 0
    
    # Compute longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            # If current element can extend the subsequence
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        
        # Update max length and index
        if dp[i] > max_length:
            max_length = dp[i]
            max_index = i
    
    # Reconstruct the subsequence
    subsequence = []
    while max_index != -1:
        subsequence.insert(0, arr[max_index])
        max_index = prev[max_index]
    
    return subsequence