import pytest
from src.linear_search import linear_search

def test_linear_search_found():
    """Test finding an element that exists in the list."""
    arr = [1, 2, 3, 4, 5]
    assert linear_search(arr, 3) == 2
    assert linear_search(arr, 1) == 0
    assert linear_search(arr, 5) == 4

def test_linear_search_not_found():
    """Test searching for an element not in the list."""
    arr = [1, 2, 3, 4, 5]
    assert linear_search(arr, 6) == -1
    assert linear_search(arr, 0) == -1

def test_linear_search_empty_list():
    """Test searching in an empty list."""
    arr = []
    assert linear_search(arr, 1) == -1

def test_linear_search_multiple_occurrences():
    """Test when multiple occurrences of the target exist."""
    arr = [1, 2, 3, 2, 4, 2, 5]
    assert linear_search(arr, 2) == 1

def test_linear_search_different_types():
    """Test searching with different types of elements."""
    arr = [1, 'a', True, 3.14, None]
    assert linear_search(arr, 'a') == 1
    assert linear_search(arr, True) == 2
    assert linear_search(arr, None) == 4

def test_linear_search_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        linear_search("not a list", 1)
    with pytest.raises(TypeError):
        linear_search(123, 1)
    with pytest.raises(TypeError):
        linear_search(None, 1)