import pytest
from src.fibonacci_reverse import fibonacci_reverse

def test_fibonacci_reverse_zero():
    """Test generating 0 Fibonacci numbers."""
    assert fibonacci_reverse(0) == []

def test_fibonacci_reverse_one():
    """Test generating 1 Fibonacci number."""
    assert fibonacci_reverse(1) == [0]

def test_fibonacci_reverse_two():
    """Test generating 2 Fibonacci numbers."""
    assert fibonacci_reverse(2) == [1, 0]

def test_fibonacci_reverse_five():
    """Test generating 5 Fibonacci numbers."""
    assert fibonacci_reverse(5) == [5, 3, 2, 1, 0]

def test_fibonacci_reverse_ten():
    """Test generating 10 Fibonacci numbers."""
    expected = [55, 34, 21, 13, 8, 5, 3, 2, 1, 0]
    assert fibonacci_reverse(10) == expected

def test_fibonacci_reverse_negative_input():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_reverse(-1)

def test_fibonacci_reverse_non_integer_input():
    """Test that a non-integer input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_reverse("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_reverse(5.5)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_reverse(None)