def find_palindromic_substrings(s: str) -> list[str]:
    """
    Find all palindromic substrings in a given string.
    
    A palindrome is a string that reads the same backward as forward.
    
    Args:
        s (str): Input string to search for palindromic substrings
    
    Returns:
        list[str]: List of all unique palindromic substrings in a specific order
    
    Examples:
        >>> find_palindromic_substrings("aaa")
        ['a', 'aa', 'aaa']
        >>> find_palindromic_substrings("abc")
        ['a', 'b', 'c']
    """
    # Handle edge cases
    if not s:
        return []
    
    # List to maintain order and uniqueness
    palindromes = []
    
    # Check every possible substring
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Extract substring
            substring = s[i:j+1]
            
            # Check if substring is a palindrome
            if substring == substring[::-1]:
                # Add only if not already in list
                if substring not in palindromes:
                    palindromes.append(substring)
    
    # Custom sort with specific order prioritization
    def custom_sort_key(x):
        # Prioritize characters from the original string's order
        order = [(s.index(c) if c in s else float('inf')) for c in x]
        return (len(x), order)
    
    # Sort palindromes
    return sorted(palindromes, key=custom_sort_key)