import pytest
import random
from src.random_integer_generator import generate_random_integer

def test_generate_random_integer_basic_range():
    """Test generating random integer in a basic positive range."""
    result = generate_random_integer(1, 10)
    assert 1 <= result <= 10, f"Result {result} not in range [1, 10]"

def test_generate_random_integer_zero_range():
    """Test generating random integer when min and max are the same."""
    result = generate_random_integer(5, 5)
    assert result == 5, f"Result {result} should be 5"

def test_generate_random_integer_negative_range():
    """Test generating random integer in a negative range."""
    result = generate_random_integer(-10, -1)
    assert -10 <= result <= -1, f"Result {result} not in range [-10, -1]"

def test_generate_random_integer_mixed_range():
    """Test generating random integer in a mixed range."""
    result = generate_random_integer(-5, 5)
    assert -5 <= result <= 5, f"Result {result} not in range [-5, 5]"

def test_generate_random_integer_invalid_range():
    """Test that ValueError is raised when min > max."""
    with pytest.raises(ValueError, match="min_value must be less than or equal to max_value"):
        generate_random_integer(10, 5)

def test_generate_random_integer_invalid_type():
    """Test that TypeError is raised for non-integer inputs."""
    with pytest.raises(TypeError, match="Both min_value and max_value must be integers"):
        generate_random_integer(1.5, 10)
    with pytest.raises(TypeError, match="Both min_value and max_value must be integers"):
        generate_random_integer(1, "10")

def test_random_distribution():
    """Test that multiple calls generate different results."""
    # Set a seed for reproducibility
    random.seed(42)
    
    # Generate multiple random numbers
    results = set()
    for _ in range(100):
        results.add(generate_random_integer(1, 10))
    
    # Ensure we get multiple different values
    assert len(results) > 1, "Random generator not producing varied results"