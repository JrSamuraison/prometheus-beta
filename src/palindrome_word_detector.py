def contains_palindrome_word(input_string: str) -> bool:
    """
    Determine if the input string contains a palindrome word.

    A palindrome word is a word that reads the same backward as forward,
    ignoring case and considering only alphanumeric characters.

    Args:
        input_string (str): A string containing words, numbers, and special characters

    Returns:
        bool: True if the string contains a palindrome word, False otherwise

    Examples:
        >>> contains_palindrome_word("hello level world")
        True
        >>> contains_palindrome_word("python code 121")
        True
        >>> contains_palindrome_word("no palindromes here")
        False
    """
    # Clean the input string by splitting into words
    # Remove special characters and convert to lowercase
    words = ''.join(char.lower() if char.isalnum() else ' ' for char in input_string).split()
    
    # Check each word to see if it's a palindrome
    for word in words:
        # Compare the word with its reverse, ignoring case
        if len(word) > 1 and word == word[::-1]:
            return True
    
    return False