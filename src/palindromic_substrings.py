def find_palindromic_substrings(s: str) -> list[str]:
    """
    Find all palindromic substrings in a given string.
    
    A palindrome is a string that reads the same backward as forward.
    
    Args:
        s (str): Input string to search for palindromic substrings
    
    Returns:
        list[str]: List of all unique palindromic substrings, sorted
    
    Examples:
        >>> find_palindromic_substrings("aaa")
        ['a', 'aa', 'aaa']
        >>> find_palindromic_substrings("abc")
        ['a', 'b', 'c']
    """
    # Handle edge cases
    if not s:
        return []
    
    # Set to store unique palindromes 
    palindromes = set()
    
    # Check every possible substring
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Extract substring
            substring = s[i:j+1]
            
            # Check if substring is a palindrome
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    # Return sorted list of unique palindromes
    return sorted(list(palindromes), key=len)