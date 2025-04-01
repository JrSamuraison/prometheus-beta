import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from kth_smallest_element import find_kth_smallest

def test_find_kth_smallest_basic():
    """Test basic functionality of finding kth smallest element."""
    arr = [7, 10, 4, 3, 20, 15]
    assert find_kth_smallest(arr, 3) == 7
    assert find_kth_smallest(arr, 1) == 3
    assert find_kth_smallest(arr, 6) == 20

def test_find_kth_smallest_with_duplicates():
    """Test finding kth smallest with duplicate elements."""
    arr = [3, 3, 1, 4, 4, 2]
    assert find_kth_smallest(arr, 2) == 2
    assert find_kth_smallest(arr, 3) == 3

def test_find_kth_smallest_single_element():
    """Test finding kth smallest in a single-element array."""
    arr = [42]
    assert find_kth_smallest(arr, 1) == 42

def test_find_kth_smallest_sorted_array():
    """Test finding kth smallest in a sorted array."""
    arr = [1, 2, 3, 4, 5]
    assert find_kth_smallest(arr, 4) == 4

def test_find_kth_smallest_reverse_sorted_array():
    """Test finding kth smallest in a reverse-sorted array."""
    arr = [5, 4, 3, 2, 1]
    assert find_kth_smallest(arr, 3) == 3

def test_invalid_k_raises_value_error():
    """Test that invalid k values raise ValueError."""
    arr = [1, 2, 3, 4, 5]
    
    with pytest.raises(ValueError, match="k must be between"):
        find_kth_smallest(arr, 0)
    
    with pytest.raises(ValueError, match="k must be between"):
        find_kth_smallest(arr, 6)

def test_invalid_input_raises_type_error():
    """Test that invalid input types raise TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_kth_smallest("not a list", 2)
    
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_kth_smallest([1, 2, "3", 4], 2)