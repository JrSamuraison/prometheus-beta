def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in a given array of integers.
    
    A subsequence is a sequence that can be derived from another sequence by 
    deleting some or no elements without changing the order of the remaining elements.
    
    Args:
        arr (list): A list of integers to find the longest increasing subsequence in.
    
    Returns:
        list: The longest increasing subsequence found in the input array.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list contains non-integer elements.
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Examples:
        >>> find_longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])
        [10, 22, 33, 50, 60, 80]
        >>> find_longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7])
        [7]
        >>> find_longest_increasing_subsequence([])
        []
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return []
    
    # Validate that all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Length of the input array
    n = len(arr)
    
    # Dynamic programming approach to find LIS
    # dp[i] stores the length of LIS ending at index i
    dp = [1] * n
    
    # Previous index tracking for reconstructing the subsequence
    prev = [-1] * n
    
    # Find the longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    # Find the index of the maximum LIS length
    max_length_index = dp.index(max(dp))
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_length_index
    while current != -1:
        subsequence.insert(0, arr[current])
        current = prev[current]
    
    return subsequence