import pytest
from src.array_intersection import find_array_intersection

def test_basic_intersection():
    """Test basic intersection of two arrays"""
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [4, 5, 6, 7, 8]
    assert find_array_intersection(arr1, arr2) == [4, 5]

def test_no_intersection():
    """Test when there are no common elements"""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert find_array_intersection(arr1, arr2) == []

def test_duplicate_elements():
    """Test with duplicate elements in input arrays"""
    arr1 = [1, 2, 2, 3, 4]
    arr2 = [2, 2, 4, 5, 6]
    assert find_array_intersection(arr1, arr2) == [2, 4]

def test_empty_arrays():
    """Test with empty input arrays"""
    arr1 = []
    arr2 = [1, 2, 3]
    assert find_array_intersection(arr1, arr2) == []

def test_invalid_input_type():
    """Test error handling for non-list inputs"""
    with pytest.raises(TypeError):
        find_array_intersection("not a list", [1, 2, 3])

def test_non_integer_elements():
    """Test error handling for non-integer elements"""
    with pytest.raises(ValueError):
        find_array_intersection([1, 2, 'a'], [1, 2, 3])

def test_sorting_of_result():
    """Test that the result is always sorted"""
    arr1 = [5, 2, 1, 4, 3]
    arr2 = [3, 1, 6, 5]
    assert find_array_intersection(arr1, arr2) == [1, 3, 5]