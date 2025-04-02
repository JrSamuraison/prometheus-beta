import pytest
from src.double_even_numbers import double_even_numbers

def test_double_even_numbers_basic():
    """Test basic functionality of doubling even numbers"""
    input_list = [1, 2, 3, 4, 5, 6]
    expected = [1, 4, 3, 8, 5, 12]
    assert double_even_numbers(input_list) == expected

def test_double_even_numbers_immutability():
    """Test that the original list is not modified"""
    input_list = [1, 2, 3, 4, 5, 6]
    original_copy = input_list.copy()
    double_even_numbers(input_list)
    assert input_list == original_copy, "Original list should not be modified"

# ... (previous tests remain the same)