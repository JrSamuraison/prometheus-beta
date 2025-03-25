import pytest
from src.substring_reversal import reverse_substring

def test_reverse_substring_basic():
    """Test basic substring reversal."""
    assert reverse_substring("hello world", 0, 5) == "olleh world"
    assert reverse_substring("hello world", 6, 11) == "hello dlrow"

def test_reverse_substring_middle():
    """Test reversing a substring in the middle of the string."""
    assert reverse_substring("python programming", 7, 12) == "python gnimargor"

def test_reverse_substring_full_string():
    """Test reversing the entire string."""
    assert reverse_substring("python", 0, 6) == "nohtyp"

def test_reverse_substring_empty_string():
    """Test reversing substring in an empty string."""
    assert reverse_substring("", 0, 0) == ""

def test_reverse_substring_same_start_end():
    """Test when start and end indices are the same."""
    assert reverse_substring("hello", 2, 2) == "hello"

def test_reverse_substring_invalid_type():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_substring(123, 0, 3)

def test_reverse_substring_start_out_of_bounds():
    """Test that a ValueError is raised for invalid start index."""
    with pytest.raises(ValueError, match="Start index .* is out of bounds"):
        reverse_substring("hello", -1, 3)
    with pytest.raises(ValueError, match="Start index .* is out of bounds"):
        reverse_substring("hello", 6, 3)

def test_reverse_substring_end_out_of_bounds():
    """Test that a ValueError is raised for invalid end index."""
    with pytest.raises(ValueError, match="End index .* is out of bounds"):
        reverse_substring("hello", 0, 6)
    with pytest.raises(ValueError, match="End index .* is out of bounds"):
        reverse_substring("hello", 0, -1)

def test_reverse_substring_invalid_start_end():
    """Test that a ValueError is raised when start > end."""
    with pytest.raises(ValueError, match="Start index .* cannot be greater than end index"):
        reverse_substring("hello", 3, 2)