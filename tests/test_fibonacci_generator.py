import pytest
from src.fibonacci_generator import generate_fibonacci_sequence

def test_fibonacci_sequence_zero_terms():
    """Test generating 0 terms returns an empty list."""
    assert generate_fibonacci_sequence(0) == []

def test_fibonacci_sequence_one_term():
    """Test generating 1 term returns [0]."""
    assert generate_fibonacci_sequence(1) == [0]

def test_fibonacci_sequence_two_terms():
    """Test generating 2 terms returns [0, 1]."""
    assert generate_fibonacci_sequence(2) == [0, 1]

def test_fibonacci_sequence_multiple_terms():
    """Test generating multiple Fibonacci terms."""
    assert generate_fibonacci_sequence(6) == [0, 1, 1, 2, 3, 5]
    assert generate_fibonacci_sequence(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_sequence_negative_input():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Number of terms must be non-negative"):
        generate_fibonacci_sequence(-1)

def test_fibonacci_sequence_invalid_input():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_sequence(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_sequence("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_sequence(None)