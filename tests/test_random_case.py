import pytest
import random
from src.random_case import convert_to_random_case

def test_convert_to_random_case_basic():
    """Test basic random case conversion"""
    # Set a fixed seed for reproducibility in testing
    random.seed(42)
    
    # Test a basic string
    result = convert_to_random_case("hello")
    assert isinstance(result, str)
    assert len(result) == 5
    assert result.lower() == "hello"

def test_convert_to_random_case_empty_string():
    """Test conversion of an empty string"""
    assert convert_to_random_case("") == ""

def test_convert_to_random_case_different_runs():
    """Verify that multiple runs can produce different results"""
    # Reset seed to ensure randomness
    random.seed(None)
    
    input_str = "abcdefg"
    result1 = convert_to_random_case(input_str)
    result2 = convert_to_random_case(input_str)
    
    # While possible to be the same, it's highly unlikely
    assert len(result1) == len(input_str)
    assert len(result2) == len(input_str)
    assert result1.lower() == input_str.lower()
    assert result2.lower() == input_str.lower()
    assert result1 != result2  # Very high probability of different case

def test_convert_to_random_case_invalid_input():
    """Test error handling for non-string inputs"""
    with pytest.raises(TypeError):
        convert_to_random_case(123)
    
    with pytest.raises(TypeError):
        convert_to_random_case(None)
    
    with pytest.raises(TypeError):
        convert_to_random_case(["hello"])

def test_convert_to_random_case_special_chars():
    """Test conversion with special characters and mixed case"""
    # Set a fixed seed for reproducibility
    random.seed(42)
    
    input_str = "Hello, World! 123"
    result = convert_to_random_case(input_str)
    
    # Verify length and that only case changes
    assert len(result) == len(input_str)
    assert result.lower() == input_str.lower()
    assert result != input_str