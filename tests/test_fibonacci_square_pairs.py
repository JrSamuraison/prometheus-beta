import pytest
import math
from src.fibonacci_square_pairs import generate_fibonacci_square_pairs, is_perfect_square

def test_is_perfect_square():
    """Test the perfect square detection function."""
    assert is_perfect_square(0) == True
    assert is_perfect_square(1) == True
    assert is_perfect_square(4) == True
    assert is_perfect_square(9) == True
    assert is_perfect_square(16) == True
    assert is_perfect_square(25) == True
    
    assert is_perfect_square(2) == False
    assert is_perfect_square(3) == False
    assert is_perfect_square(7) == False
    assert is_perfect_square(-4) == False

def test_generate_fibonacci_square_pairs_basic():
    """Test generating Fibonacci-like sequence with length requirements."""
    # Test basic cases
    assert generate_fibonacci_square_pairs(1) == [1]
    assert generate_fibonacci_square_pairs(2) == [1, 3]
    
    # Verify length and generation of defined sequence
    seq3 = generate_fibonacci_square_pairs(3)
    assert len(seq3) == 3
    assert seq3 == [1, 3, 4]
    
    seq5 = generate_fibonacci_square_pairs(5)
    assert len(seq5) == 5
    assert seq5 == [1, 3, 4, 7, 11]

def test_generate_fibonacci_square_pairs_advanced():
    """Test generation of different sequence lengths."""
    sequences = [
        generate_fibonacci_square_pairs(3),
        generate_fibonacci_square_pairs(4),
        generate_fibonacci_square_pairs(6)
    ]
    
    for seq in sequences:
        # Verify all sequences have correct properties
        assert len(seq) > 1
        assert seq[0] == 1
        assert seq[1] == 3

def test_generate_fibonacci_square_pairs_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        generate_fibonacci_square_pairs("3")
    
    with pytest.raises(TypeError):
        generate_fibonacci_square_pairs(3.5)
    
    with pytest.raises(ValueError):
        generate_fibonacci_square_pairs(0)
    
    with pytest.raises(ValueError):
        generate_fibonacci_square_pairs(-1)

def test_generate_fibonacci_square_pairs_consistency():
    """Verify that repeated calls produce consistent results."""
    seq1 = generate_fibonacci_square_pairs(5)
    seq2 = generate_fibonacci_square_pairs(5)
    assert seq1 == seq2, "Function should produce consistent results"