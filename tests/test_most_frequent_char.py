import pytest
from src.most_frequent_char import find_most_frequent_char

def test_find_most_frequent_char_normal_case():
    """Test finding most frequent character in a typical string."""
    assert find_most_frequent_char("hello") == 'l'
    assert find_most_frequent_char("programming") == 'r'

def test_find_most_frequent_char_multiple_same_frequency():
    """Test case where multiple characters have same frequency."""
    assert find_most_frequent_char("aabbc") in ['a', 'b']

def test_find_most_frequent_char_empty_string():
    """Test handling of empty string."""
    assert find_most_frequent_char("") is None

def test_find_most_frequent_char_none_input():
    """Test handling of None input."""
    assert find_most_frequent_char(None) is None

def test_find_most_frequent_char_single_char():
    """Test string with a single character."""
    assert find_most_frequent_char("x") == 'x'

def test_find_most_frequent_char_all_unique():
    """Test string where all characters are unique."""
    assert find_most_frequent_char("abcde") in "abcde"

def test_find_most_frequent_char_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError):
        find_most_frequent_char(123)
    with pytest.raises(TypeError):
        find_most_frequent_char(["a", "b", "c"])

def test_find_most_frequent_char_case_sensitive():
    """Test that the function is case-sensitive."""
    assert find_most_frequent_char("HelLo") == 'l'
    assert find_most_frequent_char("HeLLo") == 'l'