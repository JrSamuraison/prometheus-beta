import pytest
import sys
sys.path.append('src')
from bucket_sort import bucket_sort

def test_basic_integer_sort():
    """Test sorting a list of integers"""
    assert bucket_sort([5, 2, 9, 1, 7, 6, 3]) == [1, 2, 3, 5, 6, 7, 9]

def test_floating_point_numbers():
    """Test sorting a list of floating point numbers"""
    result = bucket_sort([3.14, 2.71, 1.41, 0.58, 2.23])
    assert result == [0.58, 1.41, 2.23, 2.71, 3.14]

def test_negative_numbers():
    """Test sorting a list with negative numbers"""
    assert bucket_sort([-5, -2, -9, -1, -7, -6, -3]) == [-9, -7, -6, -5, -3, -2, -1]

def test_mixed_numbers():
    """Test sorting a list with mixed positive and negative numbers"""
    assert bucket_sort([-5, 2, 9, -1, 7, 6, 3]) == [-5, -1, 2, 3, 6, 7, 9]

def test_single_element():
    """Test sorting a single-element list"""
    assert bucket_sort([42]) == [42]

def test_all_same_numbers():
    """Test sorting a list with all same numbers"""
    assert bucket_sort([5, 5, 5, 5]) == [5, 5, 5, 5]

def test_custom_bucket_count():
    """Test sorting with a custom number of buckets"""
    result = bucket_sort([5, 2, 9, 1, 7, 6, 3], bucket_count=5)
    assert result == [1, 2, 3, 5, 6, 7, 9]

def test_invalid_type_raises_error():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError):
        bucket_sort("not a list")

def test_empty_list_raises_error():
    """Test that empty list raises ValueError"""
    with pytest.raises(ValueError):
        bucket_sort([])

def test_non_numeric_elements_raises_error():
    """Test that non-numeric elements raise TypeError"""
    with pytest.raises(TypeError):
        bucket_sort([1, 2, 'three', 4])

def test_large_range_of_numbers():
    """Test sorting a list with a large range of numbers"""
    large_list = [1000, -1000, 500, -500, 0, 250, -250]
    assert bucket_sort(large_list) == [-1000, -500, -250, 0, 250, 500, 1000]