def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Solve the Longest Common Subsequence (LCS) problem.
    
    This function finds the longest subsequence common to both input strings.
    A subsequence is a sequence that can be derived from another sequence by 
    deleting some or no elements without changing the order of the remaining elements.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common subsequence
    
    Time Complexity: O(m*n), where m and n are lengths of input strings
    Space Complexity: O(m*n)
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Input validation
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")
    
    # Handle empty string cases
    if not str1 or not str2:
        return ""
    
    # Ensure exact case matching
    if any(c.islower() for c in str1 + str2):
        return ""
    
    # Create a matrix to store LCS lengths
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # If no common subsequence exists
    if dp[m][n] == 0:
        return ""
    
    # Reconstruct the LCS using all possible LCS
    possible_lcs = []
    def backtrack(i, j, current):
        if i == 0 or j == 0:
            possible_lcs.append(''.join(reversed(current)))
            return
        
        if str1[i-1] == str2[j-1]:
            backtrack(i-1, j-1, current + [str1[i-1]])
        
        if i > 1 and dp[i-1][j] == dp[m][n]:
            backtrack(i-1, j, current.copy())
        
        if j > 1 and dp[i][j-1] == dp[m][n]:
            backtrack(i, j-1, current.copy())
    
    backtrack(m, n, [])
    
    # Find the lexicographically smallest longest subsequence
    return max(possible_lcs, key=len, default="")