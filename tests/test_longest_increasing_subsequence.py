import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from longest_increasing_subsequence import find_longest_increasing_subsequence

def test_basic_increasing_sequence():
    """Test a basic increasing sequence"""
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    assert find_longest_increasing_subsequence(arr) == [10, 22, 33, 50, 60, 80]

def test_all_same_elements():
    """Test when all elements are the same"""
    arr = [7, 7, 7, 7, 7, 7, 7]
    assert find_longest_increasing_subsequence(arr) == [7]

def test_empty_list():
    """Test empty list input"""
    arr = []
    assert find_longest_increasing_subsequence(arr) == []

def test_already_increasing_sequence():
    """Test an already increasing sequence"""
    arr = [1, 2, 3, 4, 5]
    assert find_longest_increasing_subsequence(arr) == [1, 2, 3, 4, 5]

def test_descending_sequence():
    """Test a descending sequence"""
    arr = [5, 4, 3, 2, 1]
    assert find_longest_increasing_subsequence(arr) == [5]

def test_mixed_sequence():
    """Test a mixed sequence"""
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    assert find_longest_increasing_subsequence(arr) == [0, 2, 6, 9, 13, 15]

def test_invalid_input_type():
    """Test that a non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_longest_increasing_subsequence("not a list")

def test_invalid_element_type():
    """Test that a list with non-integer elements raises a ValueError"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        find_longest_increasing_subsequence([1, 2, "3", 4])

def test_single_element():
    """Test a list with a single element"""
    arr = [42]
    assert find_longest_increasing_subsequence(arr) == [42]