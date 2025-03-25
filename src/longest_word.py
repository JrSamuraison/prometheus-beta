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
    
    # Remove leading/trailing whitespace and split the sentence
    # Use regex to split on whitespace and remove punctuation
    words = re.findall(r'\b\w+\b', sentence)
    
    # Check for empty input after splitting
    if not words:
        raise ValueError("Input sentence must contain at least one word")
    
    # Find the longest word maintaining the original order
    return max(words, key=len)