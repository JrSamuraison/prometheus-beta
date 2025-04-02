import pytest
from src.cycle_sort import cycle_sort

def test_cycle_sort_basic():
    """Test basic sorting of a list of integers"""
    arr = [5, 2, 9, 1, 7, 6, 3]
    assert cycle_sort(arr) == [1, 2, 3, 5, 6, 7, 9]

def test_cycle_sort_already_sorted():
    """Test sorting of an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert cycle_sort(arr) == [1, 2, 3, 4, 5]

def test_cycle_sort_reverse_sorted():
    """Test sorting of a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert cycle_sort(arr) == [1, 2, 3, 4, 5]

def test_cycle_sort_duplicates():
    """Test sorting of a list with duplicate elements"""
    arr = [5, 2, 2, 8, 5, 1, 3]
    assert cycle_sort(arr) == [1, 2, 2, 3, 5, 5, 8]

def test_cycle_sort_empty_list():
    """Test sorting of an empty list"""
    arr = []
    assert cycle_sort(arr) == []

def test_cycle_sort_single_element():
    """Test sorting of a single-element list"""
    arr = [42]
    assert cycle_sort(arr) == [42]

def test_cycle_sort_invalid_input():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        cycle_sort("not a list")

def test_cycle_sort_negative_numbers():
    """Test sorting of a list with negative numbers"""
    arr = [-5, 2, -1, 0, 8, -3]
    assert cycle_sort(arr) == [-5, -3, -1, 0, 2, 8]

def test_cycle_sort_floating_point():
    """Test sorting of a list with floating-point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58]
    assert cycle_sort(arr) == [0.58, 1.41, 2.71, 3.14]