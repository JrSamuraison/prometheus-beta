import pytest
from src.product_of_left_elements import product_of_left_elements

def test_standard_case():
    """Test a standard list of numbers"""
    assert product_of_left_elements([1, 2, 3, 4]) == [1, 1, 2, 6]

def test_empty_list():
    """Test empty list returns empty list"""
    assert product_of_left_elements([]) == []

def test_single_element():
    """Test list with single element"""
    assert product_of_left_elements([5]) == [1]

def test_list_with_zero():
    """Test list containing zero"""
    assert product_of_left_elements([1, 0, 2, 3]) == [1, 0, 0, 0]

def test_negative_numbers():
    """Test list with negative numbers"""
    assert product_of_left_elements([-1, 2, -3, 4]) == [1, -1, -2, -6]

def test_float_numbers():
    """Test list with float numbers"""
    assert product_of_left_elements([1.5, 2.0, 3.5]) == [1, 1.5, 3.0]

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        product_of_left_elements("not a list")

def test_non_numeric_elements():
    """Test that ValueError is raised for non-numeric elements"""
    with pytest.raises(ValueError, match="All list elements must be numeric"):
        product_of_left_elements([1, 2, "three", 4])