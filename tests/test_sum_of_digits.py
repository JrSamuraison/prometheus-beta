import pytest
from src.sum_of_digits import sum_of_digits

def test_sum_of_digits_all_digits():
    """Test a string containing only digits."""
    assert sum_of_digits('1234567890') == 45

def test_sum_of_digits_mixed_string():
    """Test a string with letters and digits."""
    assert sum_of_digits('abc123') == 6

def test_sum_of_digits_empty_string():
    """Test an empty string."""
    assert sum_of_digits('') == 0

def test_sum_of_digits_no_digits():
    """Test a string with no digits."""
    assert sum_of_digits('abcdef') == 0

def test_sum_of_digits_leading_zeros():
    """Test a string with leading zeros."""
    assert sum_of_digits('00123') == 6

def test_sum_of_digits_special_characters():
    """Test a string with special characters."""
    assert sum_of_digits('!@#$%123^&*()') == 6

def test_sum_of_digits_large_numbers():
    """Test a string with large digit values."""
    assert sum_of_digits('9999') == 36

def test_sum_of_digits_type_error():
    """Test that the function handles non-string inputs correctly."""
    with pytest.raises(TypeError):
        sum_of_digits(12345)