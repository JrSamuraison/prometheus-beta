import pytest
from src.find_missing_number import find_missing_number

def test_basic_missing_number():
    """Test finding a missing number in a standard case."""
    assert find_missing_number([1, 3, 4, 5]) == 2

def test_missing_first_number():
    """Test when the first number is missing."""
    assert find_missing_number([2, 3, 4, 5]) == 1

def test_missing_last_number():
    """Test when the last number is missing."""
    assert find_missing_number([1, 2, 3, 4]) == 5

def test_larger_range():
    """Test with a larger range of numbers."""
    assert find_missing_number([3, 7, 1, 2, 8, 4, 5]) == 6

def test_invalid_input_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_missing_number([])

def test_invalid_input_out_of_range():
    """Test that numbers outside the valid range raise a ValueError."""
    with pytest.raises(ValueError, match="Invalid input: numbers are not in range 1 to n"):
        find_missing_number([1, 2, 4, 6])  # These numbers don't form a valid sequence

def test_single_number_missing():
    """Test with just one number missing from a small sequence."""
    assert find_missing_number([1]) == 2

def test_larger_missing_number():
    """Test with a larger missing number."""
    nums = list(range(1, 11))
    nums.remove(7)
    assert find_missing_number(nums) == 7