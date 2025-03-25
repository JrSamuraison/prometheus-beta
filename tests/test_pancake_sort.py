import pytest
from src.pancake_sort import pancake_sort

def test_pancake_sort_basic():
    """Test basic sorting functionality"""
    assert pancake_sort([3, 2, 1]) == [1, 2, 3]
    assert pancake_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_pancake_sort_already_sorted():
    """Test list that is already sorted"""
    assert pancake_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_pancake_sort_with_duplicates():
    """Test list with duplicate values"""
    assert pancake_sort([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]

def test_pancake_sort_empty_list():
    """Test empty list"""
    assert pancake_sort([]) == []

def test_pancake_sort_single_element():
    """Test list with a single element"""
    assert pancake_sort([42]) == [42]

def test_pancake_sort_with_floats():
    """Test list with floating point numbers"""
    assert pancake_sort([3.14, 2.71, 1.41]) == [1.41, 2.71, 3.14]

def test_pancake_sort_invalid_input_type():
    """Test handling of invalid input type"""
    with pytest.raises(TypeError):
        pancake_sort("not a list")
    with pytest.raises(TypeError):
        pancake_sort(123)

def test_pancake_sort_non_comparable_elements():
    """Test handling of non-comparable elements"""
    with pytest.raises(ValueError):
        # A list with a mix of types that can't be compared
        pancake_sort([1, 'a', None])