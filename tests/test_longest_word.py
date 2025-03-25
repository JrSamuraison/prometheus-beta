import pytest
from src.longest_word import find_longest_word

def test_basic_sentence():
    """Test finding the longest word in a basic sentence."""
    assert find_longest_word("The quick brown fox jumps") == "quick"

def test_multiple_longest_words():
    """Test when multiple words have the same maximum length."""
    result = find_longest_word("cat dog bird mouse")
    assert result in ["cat", "dog", "bird", "mouse"]

def test_single_word():
    """Test with a single word."""
    assert find_longest_word("hello") == "hello"

def test_sentence_with_punctuation():
    """Test a sentence with punctuation."""
    assert find_longest_word("Hello, world! How are you?") == "Hello"

def test_empty_string_raises_error():
    """Test that empty string raises a ValueError."""
    with pytest.raises(ValueError):
        find_longest_word("")
    
    with pytest.raises(ValueError):
        find_longest_word("   ")

def test_non_string_input_raises_error():
    """Test that non-string input raises a TypeError."""
    with pytest.raises(TypeError):
        find_longest_word(123)
    
    with pytest.raises(TypeError):
        find_longest_word(["hello", "world"])

def test_sentence_with_numbers():
    """Test a sentence that includes numbers."""
    assert find_longest_word("Python 3.9 is awesome") == "awesome"

def test_unicode_words():
    """Test finding the longest word with unicode characters."""
    result = find_longest_word("Hello áéíóú world")
    assert result in ["Hello", "áéíóú"]