import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_basic_increasing_sequence():
    """Test a basic increasing sequence"""
    arr = [10, 22, 33, 44, 55]
    assert find_longest_increasing_subsequence(arr) == [10, 22, 33, 44, 55]

def test_non_consecutive_increasing_sequence():
    """Test a non-consecutive increasing subsequence"""
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    assert find_longest_increasing_subsequence(arr) == [2, 5, 7, 101]

def test_empty_input():
    """Test empty input returns empty list"""
    assert find_longest_increasing_subsequence([]) == []

def test_none_input():
    """Test None input returns empty list"""
    assert find_longest_increasing_subsequence(None) == []

def test_single_element():
    """Test input with single element"""
    arr = [42]
    assert find_longest_increasing_subsequence(arr) == [42]

def test_all_same_elements():
    """Test input with all same elements"""
    arr = [5, 5, 5, 5]
    assert find_longest_increasing_subsequence(arr) == [5]

def test_negative_numbers():
    """Test input with negative numbers"""
    arr = [-7, -3, 0, -2, 5, 3, 6, 8]
    assert find_longest_increasing_subsequence(arr) == [-7, -3, 0, 5, 6, 8]

def test_mixed_numbers():
    """Test input with mixed positive and negative numbers"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert find_longest_increasing_subsequence(arr) == [1, 4, 5, 6]

def test_multiple_possible_subsequences():
    """Test case with multiple possible longest increasing subsequences"""
    arr = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    result = find_longest_increasing_subsequence(arr)
    assert result == [1, 3, 6, 7, 9, 10]