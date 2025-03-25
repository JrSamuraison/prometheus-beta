import re

def find_longest_word(sentence):
    """
    Find the longest word in a given sentence.

    Args:
        sentence (str): The input sentence to search for the longest word.

    Returns:
        str: The longest word in the sentence. If multiple words have the same 
             maximum length, returns the first occurrence.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty or contains only whitespace.
    """
    # Check for invalid input
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    # Split the sentence into words, preserving original forms 
    # including words with punctuation and Unicode
    words = re.findall(r'\b\S+\b', sentence)
    
    # Check for empty input after splitting
    if not words:
        raise ValueError("Input sentence must contain at least one word")
    
    # Find the first longest word (by preserving original order)
    max_length = len(max(words, key=len))
    for word in words:
        if len(word) == max_length:
            return word