import pytest
from src.k_largest import k_largest

def test_k_largest_normal_case():
    """Test k_largest with a standard input"""
    assert k_largest([3, 1, 5, 12, 2, 11], 3) == [12, 11, 5]

def test_k_largest_all_elements():
    """Test k_largest when k equals the array length"""
    assert k_largest([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1]

def test_k_largest_single_element():
    """Test k_largest with k=1"""
    assert k_largest([7, 3, 9, 2], 1) == [9]

def test_k_largest_zero_k():
    """Test k_largest when k is zero"""
    assert k_largest([1, 2, 3], 0) == []

def test_k_largest_negative_numbers():
    """Test k_largest with negative numbers"""
    assert k_largest([-1, -5, 10, 3, -3], 2) == [10, 3]

def test_k_largest_duplicate_numbers():
    """Test k_largest with duplicate numbers"""
    assert k_largest([3, 3, 3, 3], 2) == [3, 3]

def test_k_largest_invalid_k_negative():
    """Test raising ValueError when k is negative"""
    with pytest.raises(ValueError, match="k cannot be negative"):
        k_largest([1, 2, 3], -1)

def test_k_largest_invalid_k_too_large():
    """Test raising ValueError when k is larger than array length"""
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        k_largest([1, 2, 3], 4)

def test_k_largest_invalid_input_type():
    """Test raising TypeError with non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        k_largest("not a list", 2)

def test_k_largest_invalid_k_type():
    """Test raising TypeError with non-integer k"""
    with pytest.raises(TypeError, match="k must be an integer"):
        k_largest([1, 2, 3], "2")