import pytest
from src.most_frequent_char import find_most_frequent_char

def test_find_most_frequent_char_normal_case():
    """Test normal case with a clear most frequent character."""
    assert find_most_frequent_char("hello") == 'l'
    assert find_most_frequent_char("aabbbc") == 'b'
    assert find_most_frequent_char("abracadabra") == 'a'

def test_find_most_frequent_char_first_tie_breaker():
    """Test tie-breaking behavior - first encountered character wins."""
    assert find_most_frequent_char("aabb") == 'a'
    assert find_most_frequent_char("bbaa") == 'b'

def test_find_most_frequent_char_empty_string():
    """Test behavior with empty string."""
    assert find_most_frequent_char("") is None

def test_find_most_frequent_char_single_char():
    """Test string with a single character."""
    assert find_most_frequent_char("x") == 'x'

def test_find_most_frequent_char_different_types():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        find_most_frequent_char(123)
    with pytest.raises(TypeError):
        find_most_frequent_char(None)
    with pytest.raises(TypeError):
        find_most_frequent_char(['a', 'b', 'c'])

def test_find_most_frequent_char_special_characters():
    """Test handling of special characters and spaces."""
    assert find_most_frequent_char("hello world!!") == 'l'
    assert find_most_frequent_char("!!@@##hello") == '!'