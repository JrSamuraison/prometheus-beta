import pytest
from src.two_sum import two_sum

def test_two_sum_basic_positive():
    """Test basic case where two numbers sum to target"""
    assert two_sum([1, 2, 3, 4], 7) == True

def test_two_sum_basic_negative():
    """Test case where no two numbers sum to target"""
    assert two_sum([1, 2, 3, 4], 10) == False

def test_two_sum_edge_zero():
    """Test case with zero as target"""
    assert two_sum([-1, 1, 2, 3], 0) == True

def test_two_sum_negative_numbers():
    """Test with negative numbers"""
    assert two_sum([-5, -2, 0, 1, 3], -4) == True

def test_two_sum_single_element():
    """Test with single element list"""
    assert two_sum([5], 10) == False

def test_two_sum_empty_list():
    """Test with empty list"""
    assert two_sum([], 5) == False

def test_two_sum_invalid_input_not_list():
    """Test invalid input type"""
    with pytest.raises(TypeError, match="Input must be a list"):
        two_sum("not a list", 5)

def test_two_sum_invalid_target():
    """Test invalid target type"""
    with pytest.raises(TypeError, match="Target must be an integer"):
        two_sum([1, 2, 3], "5")

def test_two_sum_duplicate_numbers():
    """Test duplicate numbers raise an error"""
    with pytest.raises(ValueError, match="Input list must contain unique numbers"):
        two_sum([1, 2, 2, 3], 4)

def test_two_sum_multiple_possibilities():
    """Test multiple ways to sum to target"""
    assert two_sum([1, 4, 3, 2, 5], 6) == True

def test_two_sum_exact_match():
    """Test when a number exactly matches half the target"""
    assert two_sum([1, 2, 3, 6], 12) == False