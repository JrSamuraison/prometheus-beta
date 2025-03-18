def min_reconstruction_edits(original, modified):
    """
    Determine the minimum number of insertions and removals required to 
    reconstruct an original sequence from a given array.

    Args:
        original (list): The original sequence to reconstruct
        modified (list): The modified sequence to transform from

    Returns:
        int: Minimum number of edit operations (insertions/removals) required
    
    Time Complexity: O(n*m), where n and m are lengths of original and modified sequences
    Space Complexity: O(n*m)
    """
    # Handle edge cases
    if not original and not modified:
        return 0
    if not original:
        return len(modified)
    if not modified:
        return len(original)

    # Create a dynamic programming matrix
    n, m = len(original), len(modified)
    # dp[i][j] represents min edits to transform original[:i] to modified[:j]
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    # Initialize base cases
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # Fill the dp matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if original[i-1] == modified[j-1]:
                # If elements match, no edit needed
                dp[i][j] = dp[i-1][j-1]
            else:
                # Minimum of insert, remove, or replace
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # removal
                    dp[i][j-1],    # insertion
                    dp[i-1][j-1]   # replacement
                )

    # Return the minimum number of edits
    return dp[n][m]