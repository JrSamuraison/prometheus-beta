import pytest
from src.find_array_minimum import find_minimum

def test_find_minimum_positive_numbers():
    """Test finding minimum in an array of positive numbers."""
    assert find_minimum([1, 2, 3, 4, 5]) == 1
    assert find_minimum([5, 4, 3, 2, 1]) == 1
    assert find_minimum([3, 3, 3, 3]) == 3

def test_find_minimum_mixed_numbers():
    """Test finding minimum in an array with mixed positive and negative numbers."""
    assert find_minimum([-1, 0, 1, 2]) == -1
    assert find_minimum([0, -5, 10, -3]) == -5

def test_find_minimum_floating_point():
    """Test finding minimum with floating-point numbers."""
    assert find_minimum([1.5, 2.3, 0.1, 4.7]) == 0.1
    assert find_minimum([-1.5, 0.0, 1.5]) == -1.5

def test_find_minimum_single_element():
    """Test finding minimum in a single-element array."""
    assert find_minimum([42]) == 42

def test_find_minimum_empty_array():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find minimum of an empty array"):
        find_minimum([])

def test_find_minimum_invalid_input():
    """Test that invalid inputs raise appropriate exceptions."""
    # Non-list input
    with pytest.raises(TypeError, match="Input must be a list"):
        find_minimum("not a list")
    
    # List with non-numeric elements
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_minimum([1, 2, "3", 4])
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_minimum([1, None, 3])