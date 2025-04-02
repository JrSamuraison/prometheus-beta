import pytest
from src.list_intersection import find_list_intersection

def test_basic_intersection():
    """Test intersection of two lists with common elements"""
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    assert set(find_list_intersection(list1, list2)) == {4, 5}

def test_no_intersection():
    """Test lists with no common elements"""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    assert find_list_intersection(list1, list2) == []

def test_duplicate_elements():
    """Test lists with duplicate elements"""
    list1 = [1, 2, 2, 3, 3, 4]
    list2 = [2, 2, 3, 4, 4, 5]
    assert set(find_list_intersection(list1, list2)) == {2, 3, 4}

def test_empty_lists():
    """Test intersection with empty lists"""
    list1 = []
    list2 = [1, 2, 3]
    assert find_list_intersection(list1, list2) == []

def test_string_lists():
    """Test intersection with string lists"""
    list1 = ['apple', 'banana', 'cherry']
    list2 = ['banana', 'date', 'cherry']
    assert set(find_list_intersection(list1, list2)) == {'banana', 'cherry'}

def test_mixed_type_lists():
    """Test intersection with mixed type lists"""
    list1 = [1, 'a', 2, 'b']
    list2 = ['a', 1, 'c', 3]
    assert set(find_list_intersection(list1, list2)) == {1, 'a'}

def test_large_lists():
    """Test intersection with larger lists"""
    list1 = list(range(1000)) + [2000, 2001]
    list2 = list(range(500, 1500)) + [2000, 2001]
    result = find_list_intersection(list1, list2)
    assert set(result) == set(list(range(500, 1000)) + [2000, 2001])