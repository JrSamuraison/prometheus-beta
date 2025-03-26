import pytest
from src.odd_even_sum import calculate_odd_even_sums

def test_mixed_numbers():
    """Test with a mix of odd and even numbers"""
    result = calculate_odd_even_sums([1, 2, 3, 4, 5, 6])
    assert result == (9, 12)

def test_only_odd_numbers():
    """Test with only odd numbers"""
    result = calculate_odd_even_sums([1, 3, 5, 7])
    assert result == (16, 0)

def test_only_even_numbers():
    """Test with only even numbers"""
    result = calculate_odd_even_sums([2, 4, 6, 8])
    assert result == (0, 20)

def test_empty_list():
    """Test with an empty list"""
    result = calculate_odd_even_sums([])
    assert result == (0, 0)

def test_negative_numbers():
    """Test with mixed positive and negative numbers"""
    result = calculate_odd_even_sums([-1, -2, 3, 4, -5, 6])
    assert result == (-3, 8)

def test_invalid_input_not_list():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        calculate_odd_even_sums("not a list")

def test_invalid_input_non_integers():
    """Test that TypeError is raised for list with non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        calculate_odd_even_sums([1, 2, "3", 4])