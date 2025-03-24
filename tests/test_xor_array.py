import pytest
from src.xor_array import xor_array_elements

def test_xor_array_basic():
    """Test basic XOR operation with multiple elements"""
    assert xor_array_elements([1, 2, 3]) == 0  # 1 ^ 2 ^ 3 = 0

def test_xor_array_single_element():
    """Test XOR with a single element"""
    assert xor_array_elements([5]) == 5

def test_xor_array_zero_elements():
    """Test error handling for zero elements"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        xor_array_elements([])

def test_xor_array_invalid_input():
    """Test error handling for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        xor_array_elements(42)

def test_xor_array_non_integer_elements():
    """Test error handling for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        xor_array_elements([1, 2, "3"])

def test_xor_array_large_numbers():
    """Test XOR with larger numbers"""
    assert xor_array_elements([10, 20, 30]) == 0  # 10 ^ 20 ^ 30 = 0

def test_xor_array_repetitive_elements():
    """Test XOR with repetitive elements"""
    assert xor_array_elements([1, 1, 1, 1]) == 0  # Any number XOR with itself is 0

def test_xor_array_negative_numbers():
    """Test XOR with negative numbers"""
    assert xor_array_elements([-1, -2, -3]) == -4  # Actual bitwise XOR result