import pytest
from src.list_difference import find_list_difference

def test_basic_list_difference():
    """Test basic list difference scenario"""
    assert find_list_difference([1, 2, 3], [2, 3, 4]) == [1]

def test_string_list_difference():
    """Test list difference with string elements"""
    assert find_list_difference(['a', 'b', 'c'], ['b', 'c', 'd']) == ['a']

def test_empty_first_list():
    """Test when the first list is empty"""
    assert find_list_difference([], [1, 2, 3]) == []

def test_empty_second_list():
    """Test when the second list is empty"""
    assert find_list_difference([1, 2, 3], []) == [1, 2, 3]

def test_no_difference():
    """Test when lists are identical"""
    assert find_list_difference([1, 2, 3], [1, 2, 3]) == []

def test_duplicate_elements():
    """Test list with duplicate elements"""
    assert find_list_difference([1, 1, 2, 3], [3, 4]) == [1, 2]

def test_mixed_type_lists():
    """Test lists with mixed types"""
    assert find_list_difference([1, 'a', 2], ['a', 3]) == [1, 2]