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
    
    # Enhancement: track all potential last elements for max length
    candidates = [(0, arr[0])]
    
    # Enhanced DP to find LIS
    for i in range(1, n):
        for j in range(i):
            # Conditions for extending subsequence
            if arr[i] > arr[j] and (dp[i] < dp[j] + 1):
                dp[i] = dp[j] + 1
                prev[i] = j
        
        # Update max length with more nuanced conditions
        if dp[i] > max_length:
            max_length = dp[i]
            candidates = [(i, arr[i])]
        elif dp[i] == max_length:
            candidates.append((i, arr[i]))
    
    # Find the candidate with the smallest terminating element
    max_index = min(candidates, key=lambda x: x[1])[0]
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_index
    
    while current != -1:
        subsequence.insert(0, arr[current])
        current = prev[current]
    
    return subsequence