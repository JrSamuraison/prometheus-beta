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
    
    # Strictly enforce uppercase
    if not (str1.isupper() and str2.isupper()):
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
    
    # Possible LCS
    candidates = []
    
    # Reconstruct the LCS
    def backtrack(i, j, current_lcs):
        if i == 0 or j == 0:
            candidates.append(''.join(reversed(current_lcs)))
            return
        
        if str1[i-1] == str2[j-1]:
            backtrack(i-1, j-1, current_lcs + [str1[i-1]])
        
        if i > 1 and dp[i-1][j] == dp[m][n]:
            backtrack(i-1, j, current_lcs.copy())
        
        if j > 1 and dp[i][j-1] == dp[m][n]:
            backtrack(i, j-1, current_lcs.copy())
    
    backtrack(m, n, [])
    
    # Filter candidates with max length and return lexicographically first
    max_length = max(len(c) for c in candidates) if candidates else 0
    max_candidates = [c for c in candidates if len(c) == max_length]
    
    return min(max_candidates) if max_candidates else ""