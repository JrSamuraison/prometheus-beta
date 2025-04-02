import pytest
from src.reverse_words import reverse_words

def test_basic_reverse():
    """Test basic word reversal."""
    assert reverse_words("Hello World") == "World Hello"

def test_multiple_words():
    """Test reversal of multiple words."""
    assert reverse_words("Python is awesome") == "awesome is Python"

def test_preserve_spacing():
    """Test that original spacing is preserved."""
    input_str = "  Hello   World  "
    assert reverse_words(input_str) == "  World   Hello  "

def test_single_word():
    """Test a single word input."""
    assert reverse_words("Python") == "Python"

def test_empty_string():
    """Test empty string input."""
    assert reverse_words("") == ""

def test_numbers_and_words():
    """Test input with numbers and words."""
    assert reverse_words("123 abc 456") == "abc 123 456"

def test_mixed_characters():
    """Test input with mixed characters."""
    assert reverse_words("hello! world@") == "world@ hello!"

def test_only_whitespace():
    """Test input with only whitespace."""
    assert reverse_words("   ") == "   "

def test_multiple_consecutive_spaces():
    """Test multiple consecutive spaces."""
    input_str = "word1    word2   word3"
    expected = "word3   word2    word1"
    assert reverse_words(input_str) == expected