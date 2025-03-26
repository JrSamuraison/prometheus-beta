import pytest
from src.min_max_average import calculate_min_max_average

def test_standard_case():
    """Test a standard case with six different numbers."""
    numbers = [1, 2, 3, 4, 5, 6]
    assert calculate_min_max_average(numbers) == 10.5

def test_negative_numbers():
    """Test with negative numbers."""
    numbers = [-6, -5, -4, -3, -2, -1]
    assert calculate_min_max_average(numbers) == -10.5

def test_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    numbers = [-3, 0, 2, 4, 6, 8]
    assert calculate_min_max_average(numbers) == 8.5

def test_duplicate_numbers():
    """Test with duplicate numbers."""
    numbers = [1, 1, 2, 2, 3, 3]
    assert calculate_min_max_average(numbers) == 6.0

def test_float_numbers():
    """Test with floating point numbers."""
    numbers = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
    assert calculate_min_max_average(numbers) == 12.0

def test_invalid_input_length():
    """Test that an error is raised for incorrect number of inputs."""
    with pytest.raises(ValueError, match="Input must contain exactly six numbers"):
        calculate_min_max_average([1, 2, 3, 4, 5])
    
    with pytest.raises(ValueError, match="Input must contain exactly six numbers"):
        calculate_min_max_average([1, 2, 3, 4, 5, 6, 7])