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
    # Remove special characters but keep spaces, convert to lowercase
    clean_string = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in input_string)
    
    # Remove extra whitespaces and split into words
    words = clean_string.split()
    
    # Check each word to see if it's a palindrome
    for word in words:
        # Compare the word with its reverse, only keeping alphanumeric characters
        alphanumeric_word = ''.join(char for char in word if char.isalnum())
        
        # Check if word is a true palindrome (length > 1)
        if len(alphanumeric_word) > 1 and alphanumeric_word == alphanumeric_word[::-1]:
            return True
    
    return False