import pytest
from src.find_mode import find_mode

def test_single_mode():
    """Test finding a single mode in a list of numbers."""
    assert find_mode([1, 2, 2, 3, 4]) == 2

def test_multiple_modes():
    """Test finding multiple modes when frequencies are equal."""
    assert set(find_mode([1, 2, 2, 3, 3, 4])) == {2, 3}

def test_all_unique_numbers():
    """Test when all numbers have the same frequency."""
    result = find_mode([1, 2, 3, 4, 5])
    assert result == 1  # First occurrence when all are unique

def test_with_floats():
    """Test mode finding with floating point numbers."""
    assert find_mode([1.5, 2.3, 1.5, 3.7, 2.3]) == 1.5

def test_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find mode of an empty list"):
        find_mode([])

def test_large_list():
    """Test mode finding in a larger list with multiple occurrences."""
    test_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
    assert find_mode(test_list) == 4

def test_negative_numbers():
    """Test mode finding with negative numbers."""
    assert find_mode([-1, -1, 0, 1, 1]) == -1