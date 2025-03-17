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
    
    # DP arrays to track subsequence length and previous indices
    dp = [1] * n
    prev = [-1] * n
    
    # Track max length and last index
    max_length = 1
    max_index = 0
    
    # Enhanced DP to find LIS
    for i in range(1, n):
        for j in range(i):
            # Specific conditions to prefer lower values with same length
            # and longer/less limited subsequences
            if arr[i] > arr[j] and (dp[i] < dp[j] + 1 or 
                (dp[i] == dp[j] + 1 and arr[i] < arr[max_index])):
                dp[i] = dp[j] + 1
                prev[i] = j
        
        # Update max length with more nuanced conditions
        if (dp[i] > max_length or 
            (dp[i] == max_length and arr[i] < arr[max_index])):
            max_length = dp[i]
            max_index = i
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_index
    
    while current != -1:
        subsequence.insert(0, arr[current])
        current = prev[current]
    
    return subsequence