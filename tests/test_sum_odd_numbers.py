import pytest
from src.sum_odd_numbers import sum_odd_numbers

def test_sum_odd_numbers_basic():
    """Test basic functionality with small positive numbers."""
    assert sum_odd_numbers(5) == 9  # 1 + 3 + 5
    assert sum_odd_numbers(10) == 25  # 1 + 3 + 5 + 7 + 9

def test_sum_odd_numbers_zero():
    """Test input of zero."""
    assert sum_odd_numbers(0) == 0

def test_sum_odd_numbers_single_odd():
    """Test input of a single odd number."""
    assert sum_odd_numbers(1) == 1

def test_sum_odd_numbers_single_even():
    """Test input of a single even number."""
    assert sum_odd_numbers(2) == 1

def test_sum_odd_numbers_large_input():
    """Test functionality with a larger input."""
    assert sum_odd_numbers(100) == 2500  # Sum of odd numbers from 1 to 99

def test_sum_odd_numbers_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_odd_numbers(-5)

def test_sum_odd_numbers_invalid_type():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_odd_numbers(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_odd_numbers("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_odd_numbers([1, 2, 3])