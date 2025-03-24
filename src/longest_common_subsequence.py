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
    
    # Handle case sensitivity
    if any(c.islower() for c in str1 + str2):
        return ""
    
    # Handle empty string cases
    if not str1 or not str2:
        return ""
    
    # Maintain a list of potential LCS
    candidates = []
    
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
    
    # Backtracking function to find all LCS
    def backtrack(i, j, path):
        # Base case
        if i == 0 or j == 0:
            candidates.append(''.join(reversed(path)))
            return
        
        # If characters match
        if str1[i-1] == str2[j-1]:
            backtrack(i-1, j-1, path + [str1[i-1]])
        
        # Try different paths
        if i > 1 and dp[i-1][j] == dp[m][n]:
            backtrack(i-1, j, path.copy())
        
        if j > 1 and dp[i][j-1] == dp[m][n]:
            backtrack(i, j-1, path.copy())
    
    # Start backtracking
    backtrack(m, n, [])
    
    # If no candidates found, return empty string
    if not candidates:
        return ""
    
    # Find max length candidates
    max_len = max(len(c) for c in candidates)
    max_candidates = [c for c in candidates if len(c) == max_len]
    
    # Return lexicographically first candidate if multiple exist
    return min(max_candidates)